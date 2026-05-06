"""Descarga todos los datasets de https://datos.lujandecuyo.gob.ar/.

Uso:
    python descargar_datos.py             # los 83 datasets
    python descargar_datos.py --limit 1   # solo el primero (smoke test)

Salida: ./data/  (catalogo/, datasets/, descarga.log)
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import logging
import re
import sys
import time
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import unquote, urljoin, urlparse

import requests
from bs4 import BeautifulSoup

BASE = "https://datos.lujandecuyo.gob.ar"
RECURSO_PREFIX = f"{BASE}/recursos/dataset/"
OUT = Path("data")
HEADERS = {
    "User-Agent": "Mozilla/5.0 (downloader; +contacto: dantedeagostino@gmail.com)",
    "Accept": "*/*",
}
TIMEOUT = 60
MAX_RETRIES = 3
SLEEP_BETWEEN = 0.5
CHUNK = 64 * 1024

INVALID_FS_CHARS = re.compile(r'[<>:"/\\|?*\x00-\x1f]')
LEADING_TIMESTAMP = re.compile(r"^\d{10,}-")

log = logging.getLogger("descargar")


def setup_logging() -> None:
    OUT.mkdir(exist_ok=True)
    log.setLevel(logging.INFO)
    fmt = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    fh = logging.FileHandler(OUT / "descarga.log", encoding="utf-8")
    fh.setFormatter(fmt)
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(fmt)
    log.addHandler(fh)
    log.addHandler(sh)


def session() -> requests.Session:
    s = requests.Session()
    s.headers.update(HEADERS)
    return s


def get_json(s: requests.Session, url: str) -> Any:
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            r = s.get(url, timeout=TIMEOUT)
            r.raise_for_status()
            return r.json()
        except (requests.RequestException, ValueError) as e:
            log.warning("get_json fallo %s intento %d: %s", url, attempt, e)
            if attempt == MAX_RETRIES:
                raise
            time.sleep(2 ** attempt)


def fetch_catalogo(s: requests.Session) -> list[dict]:
    cat_dir = OUT / "catalogo"
    cat_dir.mkdir(parents=True, exist_ok=True)

    datasets = get_json(s, f"{BASE}/api/datasets")
    (cat_dir / "datasets.json").write_text(
        json.dumps(datasets, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    categories = get_json(s, f"{BASE}/api/categories")
    (cat_dir / "categories.json").write_text(
        json.dumps(categories, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    formats = get_json(s, f"{BASE}/api/formats")
    (cat_dir / "formats.json").write_text(
        json.dumps(formats, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    data = datasets.get("data") if isinstance(datasets, dict) else datasets
    log.info(
        "Catalogo: %d datasets, %d categorias, %d formatos",
        len(data),
        len(categories.get("data", [])),
        len(formats.get("data", [])),
    )
    return data


def fetch_dataset_detalle(s: requests.Session, slug: str) -> dict | None:
    try:
        resp = get_json(s, f"{BASE}/api/datasets?slug={slug}")
        data = resp.get("data") if isinstance(resp, dict) else None
        if data:
            return data[0]
    except Exception as e:
        log.warning("detalle %s fallo: %s", slug, e)
    return None


def extraer_recursos_html(s: requests.Session, slug: str, dataset_id: int) -> list[dict]:
    """Scrapea /dataset/{slug} y extrae <a> que apunten a /recursos/dataset/{id}/...

    Ignora cualquier otro href (cubre los enlaces tipo WEB externos: decisión del usuario).
    """
    url = f"{BASE}/dataset/{slug}"
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            r = s.get(url, timeout=TIMEOUT)
            r.raise_for_status()
            html = r.text
            break
        except requests.RequestException as e:
            log.warning("HTML %s intento %d: %s", slug, attempt, e)
            if attempt == MAX_RETRIES:
                return []
            time.sleep(2 ** attempt)

    soup = BeautifulSoup(html, "html.parser")
    prefix_path = f"/recursos/dataset/{dataset_id}/"
    recursos: list[dict] = []
    for a in soup.find_all("a", href=True):
        raw_href = a["href"]
        absolute = urljoin(BASE + "/", raw_href)
        path = urlparse(absolute).path
        if not path.startswith(prefix_path):
            continue
        href = absolute

        # nombre y formato del recurso: están en la "card" padre.
        card = a
        for _ in range(6):
            card = card.parent
            if card is None:
                break
            text = card.get_text(" ", strip=True)
            if text and len(text) < 400:
                break
        nombre, formato = "", ""
        if card is not None:
            spans = card.find_all(["span", "div"])
            # Heurística: el formato es un span con texto corto en mayúsculas.
            for sp in spans:
                t = sp.get_text(strip=True)
                if t and len(t) <= 10 and t.upper() == t and t.isascii() and t.replace("/", "").isalnum():
                    formato = t
                    break
            # Nombre: primer texto largo dentro de la card que no sea el botón.
            for el in card.find_all(["h3", "h2", "h4", "p", "a", "span", "div"]):
                t = el.get_text(strip=True)
                if t and t not in ("Descargar", "Abrir enlace", formato) and len(t) > 3:
                    nombre = t
                    break

        path = urlparse(href).path
        filename_servidor = unquote(path.rsplit("/", 1)[-1])
        recursos.append(
            {
                "nombre": nombre or filename_servidor,
                "formato": formato,
                "url": href,
                "filename_servidor": filename_servidor,
            }
        )

    # de-dup por url
    seen = set()
    unique: list[dict] = []
    for r in recursos:
        if r["url"] in seen:
            continue
        seen.add(r["url"])
        unique.append(r)
    return unique


def limpiar_filename(s: str) -> str:
    s = unquote(s)
    s = LEADING_TIMESTAMP.sub("", s)
    s = INVALID_FS_CHARS.sub("_", s)
    s = s.strip().strip(".")
    if not s:
        s = "archivo"
    if len(s) > 200:
        # conserva extensión si la hay
        if "." in s[-15:]:
            base, ext = s.rsplit(".", 1)
            s = base[: 200 - len(ext) - 1] + "." + ext
        else:
            s = s[:200]
    return s


def descargar_archivo(
    s: requests.Session, url: str, destino: Path
) -> tuple[int, int, str]:
    """Devuelve (http_status, bytes_escritos, sha256_hex). Idempotente por tamaño."""
    if destino.exists() and destino.stat().st_size > 0:
        # comprobamos tamaño remoto para reuso
        try:
            head = s.head(url, timeout=TIMEOUT, allow_redirects=True)
            remote_len = int(head.headers.get("Content-Length", "0"))
            if remote_len > 0 and remote_len == destino.stat().st_size:
                sha = sha256_of(destino)
                log.info("skip (ya existe igual tamaño): %s", destino.name)
                return head.status_code, remote_len, sha
        except requests.RequestException:
            pass

    last_err: Exception | None = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            with s.get(url, stream=True, timeout=TIMEOUT) as r:
                if r.status_code >= 400:
                    log.warning("HTTP %d en %s", r.status_code, url)
                    return r.status_code, 0, ""
                hasher = hashlib.sha256()
                tmp = destino.with_suffix(destino.suffix + ".part")
                tmp.parent.mkdir(parents=True, exist_ok=True)
                size = 0
                with open(tmp, "wb") as f:
                    for chunk in r.iter_content(chunk_size=CHUNK):
                        if not chunk:
                            continue
                        f.write(chunk)
                        hasher.update(chunk)
                        size += len(chunk)
                tmp.replace(destino)
                return r.status_code, size, hasher.hexdigest()
        except requests.RequestException as e:
            last_err = e
            log.warning("descarga %s intento %d: %s", url, attempt, e)
            if attempt < MAX_RETRIES:
                time.sleep(2 ** attempt)
    log.error("falló descarga: %s (%s)", url, last_err)
    return 0, 0, ""


def sha256_of(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for ch in iter(lambda: f.read(CHUNK), b""):
            h.update(ch)
    return h.hexdigest()


def slug_safe(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "-", s).strip("-")[:80] or "dataset"


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=0, help="Procesa solo los primeros N datasets")
    parser.add_argument("--start", type=int, default=0, help="Saltea los primeros N")
    args = parser.parse_args(argv)

    setup_logging()
    OUT.mkdir(exist_ok=True)
    (OUT / "datasets").mkdir(exist_ok=True)

    s = session()
    datasets = fetch_catalogo(s)

    if args.start:
        datasets = datasets[args.start :]
    if args.limit:
        datasets = datasets[: args.limit]

    manifest_path = OUT / "catalogo" / "manifest.csv"
    nuevo = not manifest_path.exists()
    f_manifest = open(manifest_path, "a", newline="", encoding="utf-8")
    writer = csv.writer(f_manifest)
    if nuevo:
        writer.writerow(
            [
                "dataset_id",
                "slug",
                "titulo",
                "categoria",
                "organizacion",
                "recurso_nombre",
                "formato",
                "url_origen",
                "ruta_local",
                "bytes",
                "http_status",
                "sha256",
            ]
        )

    total_recursos = 0
    total_ok = 0
    total_bytes = 0
    errores: list[str] = []

    try:
        for i, ds in enumerate(datasets, 1):
            ds_id = ds.get("id")
            slug = ds.get("slug") or f"id-{ds_id}"
            titulo = ds.get("title", "")
            categoria = ds.get("category") or ""
            org = ds.get("organization_name") or ""
            log.info("[%d/%d] %s (id=%s)", i, len(datasets), titulo, ds_id)

            ds_dir = OUT / "datasets" / f"{ds_id}-{slug_safe(slug)}"
            archivos_dir = ds_dir / "archivos"
            archivos_dir.mkdir(parents=True, exist_ok=True)

            detalle = fetch_dataset_detalle(s, slug) or ds
            (ds_dir / "_dataset.json").write_text(
                json.dumps(detalle, ensure_ascii=False, indent=2), encoding="utf-8"
            )

            recursos = extraer_recursos_html(s, slug, ds_id)
            (ds_dir / "_recursos.json").write_text(
                json.dumps(recursos, ensure_ascii=False, indent=2), encoding="utf-8"
            )
            log.info("  %d recursos descargables encontrados", len(recursos))

            for rec in recursos:
                total_recursos += 1
                fname = limpiar_filename(rec["filename_servidor"])
                destino = archivos_dir / fname
                # evitar colisiones
                if destino.exists() and destino.stat().st_size == 0:
                    destino.unlink()
                if destino.exists():
                    base = destino.stem
                    ext = destino.suffix
                    n = 2
                    while destino.exists():
                        cand = archivos_dir / f"{base}__{n}{ext}"
                        if not cand.exists():
                            destino = cand
                            break
                        n += 1

                status, size, sha = descargar_archivo(s, rec["url"], destino)
                rel = destino.relative_to(OUT).as_posix() if size else ""
                writer.writerow(
                    [
                        ds_id,
                        slug,
                        titulo,
                        categoria,
                        org,
                        rec["nombre"],
                        rec["formato"],
                        rec["url"],
                        rel,
                        size,
                        status,
                        sha,
                    ]
                )
                f_manifest.flush()
                if 200 <= status < 300 and size > 0:
                    total_ok += 1
                    total_bytes += size
                else:
                    errores.append(f"{slug} -> {rec['url']} (status={status})")

            time.sleep(SLEEP_BETWEEN)

    finally:
        f_manifest.close()

    mb = total_bytes / (1024 * 1024)
    log.info(
        "RESUMEN: %d datasets procesados, %d/%d recursos descargados, %.1f MB total, %d errores",
        len(datasets),
        total_ok,
        total_recursos,
        mb,
        len(errores),
    )
    if errores:
        log.info("Errores (primeros 20):")
        for e in errores[:20]:
            log.info("  - %s", e)

    return 0 if not errores else 1


if __name__ == "__main__":
    raise SystemExit(main())
