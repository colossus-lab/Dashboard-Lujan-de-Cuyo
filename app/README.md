# Dashboard Luján de Cuyo — Datos Abiertos

Plataforma interactiva para explorar los datasets publicados por el municipio de Luján de Cuyo (Mendoza, AR) en su [portal oficial de datos abiertos](https://datos.lujandecuyo.gob.ar).

## ¿Qué incluye?

- **Landing** con KPIs globales (datasets, archivos, categorías, secretarías).
- **14 informes ejecutivos**, uno por categoría del portal (Gobierno, Medio Ambiente, Economía, Urbanismo, etc.) con KPIs, charts (barras / pie / línea) y un markdown editable.
- **Catálogo de datos** con los 83 datasets, búsqueda y filtros por categoría. Cada dataset muestra:
  - Lista de archivos descargables (link al portal oficial).
  - Vista previa tabular si tiene CSV/XLSX (sort, filtro, paginación, charts auto-generados).

## Stack

React 19 · TypeScript 5.7 · Vite 6 · Nivo (bar/pie/line) · Recharts · Zustand · React Router 7 · React Markdown · Papaparse · SheetJS · Framer Motion · Lucide.

## Pipeline de datos

Los datos crudos vienen de `../data/` (en la raíz del workdir, generado por `descargar_datos.py`):

```
../data/
├── catalogo/
│   ├── datasets.json
│   ├── categories.json
│   └── manifest.csv
└── datasets/{id}-{slug}/archivos/*  (CSV/XLSX/PDF/...)
```

`scripts/build-data.cjs` los procesa y emite:

```
public/data/explorer/index.json          # catálogo del Explorer
public/data/explorer/{id}.json           # detalle por dataset (con preview tabular)
public/data/informes/{slug}.json         # KPIs + charts por categoría
public/data/manifest-summary.json        # totales globales para la landing
public/reports/{slug}.md                 # markdown del informe (editable)
```

Los archivos descargables NO se copian al bundle: las URLs de descarga apuntan al portal oficial (`datos.lujandecuyo.gob.ar/recursos/...`).

## Comandos

```bash
npm install
npm run build-data    # regenera public/data/* desde ../data/
npm run dev           # http://localhost:5173
npm run build         # build de producción → dist/
npm run preview       # sirve dist/
```

Para regenerar los markdown desde cero (perdiendo ediciones manuales):

```bash
node scripts/build-data.cjs --force
```

## Estructura

```
src/
├── pages/                  # Landing, ReportView, ExplorerIndex, ExplorerDetail
├── components/
│   ├── layout/             # Layout, TopBar, Sidebar, PersistentSidebar, SiteFooter
│   ├── charts/             # ChartRenderer (bar/pie/line/pyramid)
│   ├── ui/                 # KPICounter, SectionReveal, ThemeToggle, CommandPalette, ...
│   └── report/             # CitationBox
├── data/reportRegistry.ts  # 14 informes (slug, title, color, mdPath, dataPath)
├── types/                  # report.ts, explorer.ts
├── store/useStore.ts       # Zustand (theme, sidebar, command palette)
└── lib/categoryIcons.tsx   # íconos lucide por categoría
scripts/
└── build-data.cjs          # pipeline único
```

## Licencia

MIT — los datos provienen del portal oficial del municipio y conservan su licencia y atribución originales.

Construido sobre la base del [Dashboard PBA](https://github.com/colossus-lab/dashboard-pba) — adaptado al contexto municipal por **ColossusLab**.
