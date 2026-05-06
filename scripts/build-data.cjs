/**
 * build-data.cjs
 *
 * Pipeline único que toma los 83 datasets descargados en `../data/`
 * (por descargar_datos.py) y genera todos los JSON/MD que consume el dashboard.
 *
 * Lee:
 *   ../data/catalogo/datasets.json
 *   ../data/catalogo/categories.json
 *   ../data/catalogo/manifest.csv
 *   ../data/datasets/{id}-{slug}/archivos/* (CSVs/XLSX para preview)
 *
 * Genera:
 *   public/data/manifest-summary.json
 *   public/data/explorer/index.json
 *   public/data/explorer/{id}.json
 *   public/data/informes/{categoriaSlug}.json
 *   public/reports/{categoriaSlug}.md     (no sobrescribe si ya existe, salvo --force)
 *
 * Uso:
 *   node scripts/build-data.cjs           # build incremental (preserva .md editados)
 *   node scripts/build-data.cjs --force   # regenera todos los .md
 */

const fs = require('fs');
const path = require('path');
const Papa = require('papaparse');
const XLSX = require('xlsx');

// ─── Config ───
const FORCE = process.argv.includes('--force');
const ROOT = path.resolve(__dirname, '..');
const DATA_DIR = path.resolve(ROOT, 'data');
const PUBLIC_DIR = path.join(ROOT, 'public');
const MAX_PREVIEW_ROWS = 5000;

// Categorías → slugs (deben matchear con app/src/data/reportRegistry.ts)
const CATEGORY_REGISTRY = [
  { slug: 'gobierto-y-sector-publico', title: 'Gobierno Municipal' },
  { slug: 'medio-ambiente-y-desarrollo-sustentable', title: 'Medio Ambiente y Desarrollo Sustentable' },
  { slug: 'economia', title: 'Economía' },
  { slug: 'urbanismo-y-territorio', title: 'Urbanismo y Territorio' },
  { slug: 'deporte-educacion-y-salud', title: 'Deporte, Educación y Salud' },
  { slug: 'honorable-consejo-deliberante-lujan-de-cuyo', title: 'Honorable Concejo Deliberante' },
  { slug: 'cultura-y-turismo', title: 'Turismo y Cultura' },
  { slug: 'desarrollo-humano', title: 'Desarrollo Humano' },
  { slug: 'movilidad', title: 'Movilidad' },
  { slug: 'elecciones', title: 'Elecciones' },
  { slug: 'genero', title: 'Género y Diversidad' },
  { slug: 'gestion_de_datos', title: 'Gestión de Datos' },
  { slug: 'seguridad', title: 'Seguridad' },
  { slug: 'covid-19', title: 'COVID-19' },
];
const CATEGORY_TITLE_TO_SLUG = Object.fromEntries(
  CATEGORY_REGISTRY.map(c => [c.title, c.slug])
);

// ─── Utils ───
function ensureDir(p) {
  fs.mkdirSync(p, { recursive: true });
}

function writeJSON(p, obj) {
  ensureDir(path.dirname(p));
  fs.writeFileSync(p, JSON.stringify(obj, null, 2), 'utf-8');
}

function slugSafe(s) {
  return String(s || '').replace(/[^A-Za-z0-9._-]+/g, '-').replace(/(^-|-$)/g, '').slice(0, 80);
}

function inferType(values) {
  let nums = 0, total = 0;
  for (const v of values) {
    if (v === null || v === undefined || v === '') continue;
    total++;
    const n = Number(String(v).replace(',', '.'));
    if (Number.isFinite(n)) nums++;
  }
  if (total === 0) return 'string';
  return (nums / total) >= 0.8 ? 'number' : 'string';
}

function toNumberMaybe(v) {
  if (v === null || v === undefined || v === '') return v;
  const n = Number(String(v).replace(',', '.'));
  return Number.isFinite(n) ? n : v;
}

function readManifestCSV() {
  const p = path.join(DATA_DIR, 'catalogo', 'manifest.csv');
  if (!fs.existsSync(p)) {
    console.warn(`  ! manifest.csv no encontrado en ${p}`);
    return [];
  }
  const text = fs.readFileSync(p, 'utf-8');
  const parsed = Papa.parse(text, { header: true, skipEmptyLines: true });
  return parsed.data;
}

// ─── Preview tabular ───

function tryReadCSV(filePath) {
  try {
    const text = fs.readFileSync(filePath, 'utf-8');
    const parsed = Papa.parse(text, { header: true, skipEmptyLines: true, dynamicTyping: false });
    if (!parsed.data || parsed.data.length === 0) return null;
    return parsed.data;
  } catch (e) {
    return null;
  }
}

function tryReadXLSX(filePath) {
  try {
    const wb = XLSX.readFile(filePath, { cellDates: false });
    const sheetName = wb.SheetNames[0];
    if (!sheetName) return null;
    const ws = wb.Sheets[sheetName];
    const rows = XLSX.utils.sheet_to_json(ws, { defval: '', raw: true });
    if (rows.length === 0) return null;
    return rows;
  } catch (e) {
    return null;
  }
}

function tryReadJSON(filePath) {
  try {
    const text = fs.readFileSync(filePath, 'utf-8');
    const data = JSON.parse(text);
    if (Array.isArray(data) && data.length > 0 && typeof data[0] === 'object') return data;
    if (data && Array.isArray(data.data)) return data.data;
    if (data && Array.isArray(data.features)) {
      // GeoJSON: aplanar properties
      return data.features.map(f => f.properties || {});
    }
    return null;
  } catch {
    return null;
  }
}

function buildPreview(archivosDir) {
  if (!fs.existsSync(archivosDir)) return null;
  const files = fs.readdirSync(archivosDir).filter(f => !f.startsWith('.'));

  // Prioridad: CSV → XLSX → XLS → JSON/GeoJSON
  const ext = (f) => path.extname(f).toLowerCase();
  const order = ['.csv', '.xlsx', '.xls', '.json', '.geojson'];
  const candidates = files
    .filter(f => order.includes(ext(f)))
    .sort((a, b) => order.indexOf(ext(a)) - order.indexOf(ext(b)));

  for (const f of candidates) {
    const fp = path.join(archivosDir, f);
    let rows = null;
    if (ext(f) === '.csv') rows = tryReadCSV(fp);
    else if (ext(f) === '.xlsx' || ext(f) === '.xls') rows = tryReadXLSX(fp);
    else if (ext(f) === '.json' || ext(f) === '.geojson') rows = tryReadJSON(fp);

    if (!rows || rows.length === 0) continue;

    // Sanitizar y tipar columnas
    const colNames = Object.keys(rows[0] || {});
    if (colNames.length === 0) continue;

    const totalRows = rows.length;
    const limited = rows.slice(0, MAX_PREVIEW_ROWS);

    const columns = colNames.map(name => {
      const values = limited.map(r => r[name]);
      const type = inferType(values);
      return { name, type, label: name };
    });

    // Aplicar tipado a las filas
    const typedRows = limited.map(r => {
      const out = {};
      for (const col of columns) {
        out[col.name] = col.type === 'number' ? toNumberMaybe(r[col.name]) : (r[col.name] === undefined ? null : r[col.name]);
      }
      return out;
    });

    return {
      previewSourceFile: f,
      columns,
      rows: typedRows,
      totalRows,
    };
  }

  return null;
}

// ─── Generación de informes (data + markdown) ───

function buildReportData(catTitle, catSlug, datasets, manifestRows) {
  const today = new Date().toISOString().slice(0, 10);

  // Recursos descargables de los datasets de esta categoría
  const dsIds = new Set(datasets.map(d => String(d.id)));
  const recursos = manifestRows.filter(r => dsIds.has(r.dataset_id) && r.http_status === '200');
  const totalArchivos = recursos.length;
  const totalBytes = recursos.reduce((s, r) => s + (Number(r.bytes) || 0), 0);
  const orgs = Array.from(new Set(datasets.map(d => d.organization_name).filter(Boolean)));

  // KPIs
  const kpis = [
    {
      id: 'kpi-datasets',
      label: 'Datasets',
      value: datasets.length,
      formatted: String(datasets.length),
    },
    {
      id: 'kpi-archivos',
      label: 'Archivos descargables',
      value: totalArchivos,
      formatted: totalArchivos.toLocaleString('es-AR'),
    },
    {
      id: 'kpi-mb',
      label: 'MB publicados',
      value: Math.round(totalBytes / (1024 * 1024)),
      formatted: (totalBytes / (1024 * 1024)).toFixed(1) + ' MB',
    },
    {
      id: 'kpi-orgs',
      label: 'Áreas que publican',
      value: orgs.length,
      formatted: String(orgs.length),
    },
  ];

  // Charts
  const charts = [];

  // Bar: datasets por secretaría (top 10)
  const orgCount = {};
  for (const d of datasets) {
    const o = d.organization_name || 'Sin asignar';
    orgCount[o] = (orgCount[o] || 0) + 1;
  }
  const orgRanking = Object.entries(orgCount)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 10)
    .map(([id, value]) => ({ id, datasets: value }));
  if (orgRanking.length > 0) {
    charts.push({
      id: 'chart-orgs',
      type: 'bar',
      title: 'Datasets por área que publica',
      sectionId: 'areas-que-publican',
      data: orgRanking,
      config: { xAxis: 'id', layout: 'horizontal' },
    });
  }

  // Pie: distribución de formatos
  const formatCount = {};
  for (const r of recursos) {
    const fmt = (r.formato || '').toUpperCase() || inferFormatoFromFile(r.recurso_nombre || '');
    if (!fmt) continue;
    formatCount[fmt] = (formatCount[fmt] || 0) + 1;
  }
  const pieData = Object.entries(formatCount)
    .sort((a, b) => b[1] - a[1])
    .map(([id, value]) => ({ id, label: id, value }));
  if (pieData.length > 0) {
    charts.push({
      id: 'chart-formats',
      type: 'pie',
      title: 'Distribución de formatos',
      sectionId: 'formatos-disponibles',
      data: pieData,
    });
  }

  // Line: datasets publicados por mes (timeline)
  const monthCount = {};
  for (const d of datasets) {
    const created = d.created_at;
    if (!created) continue;
    const month = created.slice(0, 7); // YYYY-MM
    monthCount[month] = (monthCount[month] || 0) + 1;
  }
  const months = Object.keys(monthCount).sort();
  if (months.length >= 2) {
    charts.push({
      id: 'chart-timeline',
      type: 'line',
      title: 'Datasets publicados por mes',
      sectionId: 'timeline-de-publicacion',
      data: months.map(m => ({ mes: m, datasets: monthCount[m] })),
      config: { xAxis: 'mes' },
    });
  }

  // Rankings: top 5 datasets por cantidad de archivos
  const dsArchivos = datasets.map(d => {
    const count = recursos.filter(r => r.dataset_id === String(d.id)).length;
    return { name: d.title, value: count };
  }).sort((a, b) => b.value - a.value).slice(0, 5);

  const rankings = dsArchivos.length > 0 ? [{
    id: 'rank-datasets-archivos',
    title: 'Datasets con más archivos',
    sectionId: '',
    items: dsArchivos,
    order: 'desc',
  }] : [];

  return {
    meta: {
      id: catSlug,
      title: catTitle,
      category: catTitle,
      source: 'Portal de Datos Abiertos – Luján de Cuyo (datos.lujandecuyo.gob.ar)',
      date: today,
    },
    kpis,
    charts,
    rankings,
    mapData: [],
  };
}

function inferFormatoFromFile(name) {
  const ext = path.extname(name).toLowerCase().replace('.', '');
  if (!ext) return '';
  return ext.toUpperCase();
}

function buildReportMarkdown(catTitle, catSlug, datasets) {
  const lines = [];
  lines.push(`# ${catTitle}`);
  lines.push('');
  lines.push(`Esta sección reúne los **${datasets.length} dataset${datasets.length === 1 ? '' : 's'}** publicados por el municipio de Luján de Cuyo en la categoría **${catTitle}**, descargados directamente del portal oficial de datos abiertos.`);
  lines.push('');
  lines.push('Los archivos provienen de [datos.lujandecuyo.gob.ar](https://datos.lujandecuyo.gob.ar) y conservan su licencia y atribución originales.');
  lines.push('');

  if (datasets.length > 0) {
    lines.push('## Datasets disponibles');
    lines.push('');
    for (const d of datasets) {
      const desc = (d.description || '').trim().split('\n')[0] || 'Sin descripción.';
      lines.push(`- **[${d.title}](/explorar/${d.id})** — ${desc}`);
      if (d.organization_name) {
        lines.push(`  _Publicado por: ${d.organization_name}_`);
      }
      lines.push('');
    }
  }

  lines.push('## Áreas que publican');
  lines.push('');
  lines.push('Distribución de datasets por secretaría / área del municipio responsable de la publicación.');
  lines.push('');

  lines.push('## Formatos disponibles');
  lines.push('');
  lines.push('Mix de formatos en los archivos publicados de esta categoría — útil para entender qué tan analizable es el material disponible (CSV/XLSX/JSON vs documentos PDF/DOCX).');
  lines.push('');

  lines.push('## Timeline de publicación');
  lines.push('');
  lines.push('Cuándo se subieron al portal los datasets de esta categoría.');
  lines.push('');

  lines.push('## Fuente');
  lines.push('');
  lines.push('Portal oficial: <https://datos.lujandecuyo.gob.ar>. Los datos son responsabilidad de las áreas que los publican; este dashboard se limita a indexarlos y hacerlos navegables.');
  lines.push('');

  return lines.join('\n');
}

// ─── Main ───

console.log('═══════════════════════════════════════════════════════════');
console.log('  Dashboard Luján de Cuyo — build-data');
console.log('═══════════════════════════════════════════════════════════');

if (!fs.existsSync(DATA_DIR)) {
  console.error(`✗ No existe ${DATA_DIR}. Corré primero descargar_datos.py en la raíz del workdir.`);
  process.exit(1);
}

// Cargar catálogo
const datasetsRaw = JSON.parse(fs.readFileSync(path.join(DATA_DIR, 'catalogo', 'datasets.json'), 'utf-8'));
const catsRaw = JSON.parse(fs.readFileSync(path.join(DATA_DIR, 'catalogo', 'categories.json'), 'utf-8'));
const datasetsList = datasetsRaw.data || datasetsRaw;
const categories = catsRaw.data || catsRaw;
const manifestRows = readManifestCSV();

console.log(`  Catálogo: ${datasetsList.length} datasets, ${categories.length} categorías, ${manifestRows.length} filas en manifest`);

// Slugs de TODAS las categorías a las que pertenece un dataset
function dsCategorySlugs(d) {
  const out = new Set();
  for (const c of (d.categories || [])) {
    if (c.slug) out.add(c.slug);
  }
  if (out.size === 0) {
    const title = d.category || '';
    const slug = CATEGORY_TITLE_TO_SLUG[title];
    if (slug) out.add(slug);
  }
  return Array.from(out);
}

// Categoría "primaria" para el explorer (la primera de categories[])
function dsPrimarySlug(d) {
  const slugs = dsCategorySlugs(d);
  return slugs[0] || 'sin-categoria';
}

// Estructura de salida
ensureDir(path.join(PUBLIC_DIR, 'data', 'explorer'));
ensureDir(path.join(PUBLIC_DIR, 'data', 'informes'));
ensureDir(path.join(PUBLIC_DIR, 'reports'));

// ─── 1. Explorer detail por dataset + index ───
console.log('\n[1/3] Generando datos del Explorer...');
const explorerIndex = [];
let datasetsSinPreview = 0;

for (const d of datasetsList) {
  const idStr = String(d.id);
  const archivosDir = path.join(DATA_DIR, 'datasets', `${d.id}-${slugSafe(d.slug)}`, 'archivos');
  const recursos = manifestRows
    .filter(r => r.dataset_id === idStr && r.http_status === '200' && Number(r.bytes) > 0)
    .map(r => ({
      nombre: (r.recurso_nombre || '').replace(/^\d{10,}-/, '') || path.basename(r.url_origen || ''),
      formato: (r.formato || '').toUpperCase() || inferFormatoFromFile(r.url_origen || ''),
      url: r.url_origen,
      bytes: Number(r.bytes) || 0,
    }));

  // Construir preview solo si hay CSV/XLSX/etc. analizable
  const preview = buildPreview(archivosDir);
  if (!preview) datasetsSinPreview++;

  const catSlug = dsPrimarySlug(d);
  const catTitle = (CATEGORY_REGISTRY.find(c => c.slug === catSlug) || {}).title || d.category || '';

  const detail = {
    id: idStr,
    title: d.title,
    source: d.organization_name || '',
    description: d.description || '',
    category: catTitle,
    categorySlug: catSlug,
    updatedAt: d.updated_at,
    createdAt: d.created_at,
    files: recursos,
    columns: preview ? preview.columns : [],
    rows: preview ? preview.rows : [],
    totalRows: preview ? preview.totalRows : 0,
    previewSourceFile: preview ? preview.previewSourceFile : undefined,
    municipios: [],
  };
  writeJSON(path.join(PUBLIC_DIR, 'data', 'explorer', `${idStr}.json`), detail);

  const formats = Array.from(new Set(recursos.map(r => r.formato).filter(Boolean)));
  explorerIndex.push({
    id: idStr,
    title: d.title,
    source: d.organization_name || '',
    category: catTitle,
    categorySlug: catSlug,
    rows: preview ? preview.totalRows : 0,
    columns: preview ? preview.columns.length : 0,
    files: recursos.length,
    formats,
    hasPreview: !!preview,
    municipios: 0,
  });
}

writeJSON(path.join(PUBLIC_DIR, 'data', 'explorer', 'index.json'), explorerIndex);
console.log(`  ✓ explorer/index.json (${explorerIndex.length} datasets)`);
console.log(`  ✓ explorer/{id}.json × ${datasetsList.length}`);
console.log(`    de los cuales ${datasetsList.length - datasetsSinPreview} tienen preview tabular`);

// ─── 2. Informes por categoría (json + md) ───
console.log('\n[2/3] Generando informes por categoría...');
const datasetsPorCategoria = {};

for (const cat of CATEGORY_REGISTRY) {
  const datasetsCat = datasetsList.filter(d => dsCategorySlugs(d).includes(cat.slug));
  datasetsPorCategoria[cat.slug] = datasetsCat.length;

  // Los JSON e MD de informe se generan con scripts/build-informes-data.py
  // y scripts/write-reports.py (analíticos del fenómeno municipal). Aquí
  // sólo escribimos un fallback si el archivo todavía no existe en el repo
  // (clone fresco sin haber corrido los scripts Python).
  const jsonPath = path.join(PUBLIC_DIR, 'data', 'informes', `${cat.slug}.json`);
  if (FORCE || !fs.existsSync(jsonPath)) {
    const reportData = buildReportData(cat.title, cat.slug, datasetsCat, manifestRows);
    writeJSON(jsonPath, reportData);
  }

  const mdPath = path.join(PUBLIC_DIR, 'reports', `${cat.slug}.md`);
  if (FORCE || !fs.existsSync(mdPath)) {
    fs.writeFileSync(mdPath, buildReportMarkdown(cat.title, cat.slug, datasetsCat), 'utf-8');
  }

  console.log(`  ✓ ${cat.slug}: ${datasetsCat.length} datasets`);
}

// ─── 3. Manifest summary global ───
console.log('\n[3/3] Generando manifest-summary.json...');
const totalRecursos = manifestRows.filter(r => r.http_status === '200' && Number(r.bytes) > 0).length;
const totalBytes = manifestRows.reduce((s, r) => s + (Number(r.bytes) || 0), 0);
const formatos = new Set();
for (const d of datasetsList) {
  for (const f of (d.formats || [])) {
    if (f) formatos.add(String(f).toUpperCase());
  }
}
const orgs = new Set(datasetsList.map(d => d.organization_name).filter(Boolean));

const summary = {
  total_datasets: datasetsList.length,
  total_recursos: totalRecursos,
  total_bytes: totalBytes,
  total_mb: Math.round(totalBytes / (1024 * 1024)),
  total_categorias: CATEGORY_REGISTRY.length,
  total_formatos: formatos.size,
  total_organizaciones: orgs.size,
  datasets_por_categoria: datasetsPorCategoria,
  generated_at: new Date().toISOString(),
};
writeJSON(path.join(PUBLIC_DIR, 'data', 'manifest-summary.json'), summary);
console.log(`  ✓ manifest-summary.json: ${summary.total_datasets} datasets, ${summary.total_recursos} archivos, ${summary.total_mb} MB`);

console.log('\n═══════════════════════════════════════════════════════════');
console.log('  ✓ Build de datos completo');
console.log('═══════════════════════════════════════════════════════════');
