// ═══════════════════════════════════════════════════════════════
// Types for the Data Explorer
// ═══════════════════════════════════════════════════════════════

export interface ExplorerColumn {
  name: string;
  type: 'number' | 'string';
  label: string;
}

export interface ExplorerFile {
  nombre: string;
  formato: string;
  url: string;       // URL absoluta al portal oficial (datos.lujandecuyo.gob.ar/recursos/...)
  bytes: number;
}

export interface ExplorerDataset {
  id: string;
  title: string;
  source: string;            // organización (secretaría) que publica
  description?: string;
  category?: string;
  categorySlug?: string;
  updatedAt?: string;
  createdAt?: string;
  // Recursos descargables (todos los archivos del dataset).
  files: ExplorerFile[];
  // Vista previa tabular (vacío si no hay CSV/XLSX parseable).
  columns: ExplorerColumn[];
  rows: Record<string, unknown>[];
  totalRows: number;
  previewSourceFile?: string;  // qué archivo se usó para la vista previa
  // Mantenemos campo histórico para compatibilidad con código heredado:
  municipios?: string[];
}

export interface ExplorerIndexEntry {
  id: string;
  title: string;
  source: string;
  category?: string;
  categorySlug?: string;
  rows: number;
  columns: number;
  files: number;       // número de archivos descargables
  formats: string[];
  hasPreview: boolean;
  // Mantenemos para back-compat (siempre 0 en Luján porque es un único municipio):
  municipios: number;
  file?: string;
}
