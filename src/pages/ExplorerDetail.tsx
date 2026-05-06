import { useState, useEffect, useMemo } from 'react';
import { useParams, Link } from 'react-router-dom';
import { ResponsiveBar } from '@nivo/bar';
import { ResponsivePie } from '@nivo/pie';
import { SectionReveal } from '../components/ui/SectionReveal';
import { useStore } from '../store/useStore';
import {
  ArrowLeft, Database, BarChart3, FileText,
  PieChart, AlertCircle, Download, ExternalLink, Files,
} from 'lucide-react';
import type { ExplorerDataset, ExplorerColumn, ExplorerFile } from '../types/explorer';

type SortDir = 'asc' | 'desc';
const PAGE_SIZE = 25;

type Tab = 'archivos' | 'tabla' | 'graficos';

export function ExplorerDetail() {
  const { datasetId } = useParams<{ datasetId: string }>();
  const [data, setData] = useState<ExplorerDataset | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [sortCol, setSortCol] = useState('');
  const [sortDir, setSortDir] = useState<SortDir>('asc');
  const [page, setPage] = useState(0);
  const [filterText, setFilterText] = useState('');
  const [tab, setTab] = useState<Tab>('archivos');
  const [chartTab, setChartTab] = useState<'bar' | 'pie'>('bar');
  const theme = useStore(s => s.theme);

  useEffect(() => {
    setLoading(true);
    fetch(`/data/explorer/${datasetId}.json`)
      .then(r => { if (!r.ok) throw new Error('Not found'); return r.json(); })
      .then((d: ExplorerDataset) => {
        setData(d);
        // Default tab: tabla si hay preview, sino archivos
        if (d.rows && d.rows.length > 0) setTab('tabla');
        else setTab('archivos');
        setLoading(false);
      })
      .catch(e => { setError(e.message); setLoading(false); });
  }, [datasetId]);

  const numericCols = useMemo(() => data?.columns.filter(c => c.type === 'number') || [], [data]);
  const stringCols = useMemo(() => data?.columns.filter(c => c.type === 'string') || [], [data]);

  const processedRows = useMemo(() => {
    if (!data) return [];
    let rows = [...data.rows];

    if (filterText) {
      const q = filterText.toLowerCase();
      rows = rows.filter(r =>
        Object.values(r).some(v => String(v).toLowerCase().includes(q))
      );
    }

    if (sortCol) {
      rows.sort((a, b) => {
        const va = a[sortCol] ?? '';
        const vb = b[sortCol] ?? '';
        if (typeof va === 'number' && typeof vb === 'number') return sortDir === 'asc' ? va - vb : vb - va;
        return sortDir === 'asc'
          ? String(va).localeCompare(String(vb))
          : String(vb).localeCompare(String(va));
      });
    }
    return rows;
  }, [data, sortCol, sortDir, filterText]);

  const totalPages = Math.ceil(processedRows.length / PAGE_SIZE);
  const pageRows = processedRows.slice(page * PAGE_SIZE, (page + 1) * PAGE_SIZE);

  function handleSort(col: string) {
    if (sortCol === col) {
      setSortDir(d => d === 'asc' ? 'desc' : 'asc');
    } else {
      setSortCol(col);
      setSortDir('asc');
    }
    setPage(0);
  }

  // Auto charts: solo si hay rows + numérica + string
  const autoChartData = useMemo(() => {
    if (!data || numericCols.length === 0 || stringCols.length === 0) return null;
    const metric = numericCols[0];
    const groupCol = stringCols.find(c => !c.name.toLowerCase().includes('id')) || stringCols[0];

    const groups: Record<string, number> = {};
    for (const r of processedRows) {
      const key = String(r[groupCol.name] || 'Sin dato');
      const val = Number(r[metric.name]);
      if (Number.isFinite(val)) groups[key] = (groups[key] || 0) + val;
    }
    const sorted = Object.entries(groups).sort((a, b) => b[1] - a[1]);
    const barData = sorted.slice(0, 12).map(([id, value]) => ({ id, value }));
    const pieData = sorted.slice(0, 8).map(([id, value]) => ({
      id, label: id.length > 20 ? id.substring(0, 20) + '…' : id, value,
    }));
    return { barData, pieData, metric, groupCol };
  }, [data, processedRows, numericCols, stringCols]);

  const isDark = theme === 'dark';
  const nivoTheme = {
    text: { fill: isDark ? '#94a3b8' : '#475569' },
    axis: {
      ticks: { text: { fill: isDark ? '#94a3b8' : '#475569' } },
      legend: { text: { fill: isDark ? '#cbd5e1' : '#334155' } },
    },
    grid: { line: { stroke: isDark ? '#1e293b' : '#e2e8f0' } },
    tooltip: { container: { background: isDark ? '#1e293b' : '#fff', color: isDark ? '#f1f5f9' : '#0f172a', borderRadius: 8 } },
    labels: { text: { fill: isDark ? '#f1f5f9' : '#0f172a' } },
  };

  if (loading) return (
    <div className="explorer-page">
      <div className="explorer-loading">
        <div className="explorer-spinner" />
        <p>Cargando dataset...</p>
      </div>
    </div>
  );

  if (error || !data) return (
    <div className="explorer-page">
      <div className="explorer-empty" role="status">
        <span aria-hidden="true"><AlertCircle size={36} /></span>
        <p>Dataset no encontrado</p>
        <Link to="/explorar" className="btn-secondary">
          <ArrowLeft size={14} aria-hidden="true" /> Volver al catálogo
        </Link>
      </div>
    </div>
  );

  const hasPreview = data.rows && data.rows.length > 0;

  return (
    <div className="explorer-page">
      <SectionReveal>
        <header className="explorer-detail-header">
          <Link to="/explorar" className="explorer-back">
            <ArrowLeft size={14} aria-hidden="true" /> Catálogo de Datos
          </Link>
          <h1 className="explorer-detail-title">{data.title}</h1>
          {data.description && (
            <p className="explorer-detail-desc" style={{ marginTop: '8px', color: 'var(--text-secondary)' }}>
              {data.description}
            </p>
          )}
          <div className="explorer-detail-meta">
            <span className="explorer-meta-badge">
              <FileText size={14} aria-hidden="true" /> {data.source}
            </span>
            <span className="explorer-meta-badge">
              <Files size={14} aria-hidden="true" /> {data.files.length} archivo{data.files.length === 1 ? '' : 's'}
            </span>
            {hasPreview && (
              <span className="explorer-meta-badge">
                <Database size={14} aria-hidden="true" /> {data.totalRows.toLocaleString('es-AR')} filas
              </span>
            )}
            {data.category && (
              <span className="explorer-meta-badge">
                {data.category}
              </span>
            )}
          </div>
        </header>
      </SectionReveal>

      {/* Tabs */}
      <SectionReveal>
        <div className="explorer-chart-tabs" role="tablist" style={{ marginTop: '20px' }}>
          <button
            role="tab"
            aria-selected={tab === 'archivos'}
            className={`explorer-chart-tab ${tab === 'archivos' ? 'active' : ''}`}
            onClick={() => setTab('archivos')}
          >
            <Files size={14} aria-hidden="true" /> Archivos ({data.files.length})
          </button>
          {hasPreview && (
            <button
              role="tab"
              aria-selected={tab === 'tabla'}
              className={`explorer-chart-tab ${tab === 'tabla' ? 'active' : ''}`}
              onClick={() => setTab('tabla')}
            >
              <Database size={14} aria-hidden="true" /> Tabla
            </button>
          )}
          {hasPreview && autoChartData && (
            <button
              role="tab"
              aria-selected={tab === 'graficos'}
              className={`explorer-chart-tab ${tab === 'graficos' ? 'active' : ''}`}
              onClick={() => setTab('graficos')}
            >
              <BarChart3 size={14} aria-hidden="true" /> Gráficos
            </button>
          )}
        </div>
      </SectionReveal>

      {/* Tab: Archivos */}
      {tab === 'archivos' && (
        <SectionReveal>
          <div className="explorer-files-list" style={{ marginTop: '20px' }}>
            {data.files.map((f, i) => (
              <FileRow key={i} file={f} />
            ))}
            {data.files.length === 0 && (
              <p style={{ color: 'var(--text-tertiary)' }}>Este dataset no tiene archivos descargables.</p>
            )}
            {data.previewSourceFile && (
              <p style={{ marginTop: '12px', fontSize: '0.85rem', color: 'var(--text-tertiary)' }}>
                Vista previa generada desde: <code>{data.previewSourceFile}</code>
              </p>
            )}
          </div>
        </SectionReveal>
      )}

      {/* Tab: Tabla */}
      {tab === 'tabla' && hasPreview && (
        <>
          <SectionReveal>
            <div className="explorer-filters" style={{ marginTop: '20px' }}>
              <input
                type="text"
                className="explorer-filter-input"
                placeholder="Filtrar registros..."
                value={filterText}
                onChange={e => { setFilterText(e.target.value); setPage(0); }}
              />
              <span className="explorer-filter-count">
                {processedRows.length.toLocaleString('es-AR')} de {data.totalRows.toLocaleString('es-AR')} resultados
              </span>
            </div>
          </SectionReveal>

          <SectionReveal>
            <div className="explorer-table-wrap">
              <table className="explorer-table">
                <thead>
                  <tr>
                    {data.columns.map(col => (
                      <th
                        key={col.name}
                        className={`explorer-th ${sortCol === col.name ? 'sorted' : ''} ${col.type === 'number' ? 'num' : ''}`}
                        onClick={() => handleSort(col.name)}
                      >
                        {col.label}
                        <span className="explorer-sort-icon">
                          {sortCol === col.name ? (sortDir === 'asc' ? ' ↑' : ' ↓') : ' ⇅'}
                        </span>
                      </th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {pageRows.map((row, i) => (
                    <tr key={i} className="explorer-tr">
                      {data.columns.map(col => (
                        <td key={col.name} className={`explorer-td ${col.type === 'number' ? 'num' : ''}`}>
                          {formatCell(row[col.name], col)}
                        </td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </SectionReveal>

          {totalPages > 1 && (
            <div className="explorer-pagination">
              <button className="explorer-page-btn" disabled={page === 0} onClick={() => setPage(0)}>«</button>
              <button className="explorer-page-btn" disabled={page === 0} onClick={() => setPage(p => p - 1)}>‹</button>
              <span className="explorer-page-info">Página {page + 1} de {totalPages}</span>
              <button className="explorer-page-btn" disabled={page >= totalPages - 1} onClick={() => setPage(p => p + 1)}>›</button>
              <button className="explorer-page-btn" disabled={page >= totalPages - 1} onClick={() => setPage(totalPages - 1)}>»</button>
            </div>
          )}
        </>
      )}

      {/* Tab: Gráficos */}
      {tab === 'graficos' && autoChartData && (
        <SectionReveal>
          <section className="explorer-charts-section" style={{ marginTop: '20px' }}>
            <div className="explorer-chart-tabs" role="tablist">
              <button
                role="tab"
                aria-selected={chartTab === 'bar'}
                className={`explorer-chart-tab ${chartTab === 'bar' ? 'active' : ''}`}
                onClick={() => setChartTab('bar')}
              >
                <BarChart3 size={14} aria-hidden="true" /> Ranking
              </button>
              <button
                role="tab"
                aria-selected={chartTab === 'pie'}
                className={`explorer-chart-tab ${chartTab === 'pie' ? 'active' : ''}`}
                onClick={() => setChartTab('pie')}
              >
                <PieChart size={14} aria-hidden="true" /> Distribución
              </button>
            </div>
            <div className="explorer-chart-container" style={{ height: 480 }}>
              {chartTab === 'bar' && (
                <ResponsiveBar
                  data={autoChartData.barData.map(d => ({ ...d, [autoChartData.metric.label]: d.value }))}
                  keys={[autoChartData.metric.label]}
                  indexBy="id"
                  theme={nivoTheme}
                  margin={{ top: 20, right: 30, bottom: 100, left: 80 }}
                  padding={0.3}
                  colors={['#7c3aed']}
                  borderRadius={4}
                  axisBottom={{ tickRotation: -35 }}
                  axisLeft={{ format: v => Number(v) >= 1000 ? `${(Number(v) / 1000).toFixed(0)}K` : String(v) }}
                  enableLabel={false}
                  layout="vertical"
                />
              )}
              {chartTab === 'pie' && (
                <ResponsivePie
                  data={autoChartData.pieData}
                  theme={nivoTheme}
                  margin={{ top: 20, right: 100, bottom: 20, left: 100 }}
                  innerRadius={0.5}
                  padAngle={1}
                  cornerRadius={4}
                  colors={{ scheme: 'paired' }}
                  borderWidth={1}
                  borderColor={{ from: 'color', modifiers: [['darker', 0.2]] }}
                  arcLabelsSkipAngle={15}
                  arcLinkLabelsSkipAngle={10}
                  arcLinkLabelsTextColor={isDark ? '#94a3b8' : '#475569'}
                  arcLinkLabelsThickness={2}
                  arcLinkLabelsColor={{ from: 'color' }}
                />
              )}
            </div>
          </section>
        </SectionReveal>
      )}
    </div>
  );
}

function FileRow({ file }: { file: ExplorerFile }) {
  const sizeMb = file.bytes / (1024 * 1024);
  const sizeKb = file.bytes / 1024;
  const sizeLabel = sizeMb >= 1 ? `${sizeMb.toFixed(1)} MB` : `${Math.round(sizeKb)} KB`;
  const Icon = file.url.startsWith('https://datos.lujandecuyo.gob.ar') ? Download : ExternalLink;
  return (
    <a
      href={file.url}
      target="_blank"
      rel="noopener noreferrer"
      className="glass-card"
      style={{
        display: 'flex',
        alignItems: 'center',
        gap: '14px',
        padding: '14px 18px',
        marginBottom: '10px',
        textDecoration: 'none',
        color: 'var(--text-primary)',
        transition: 'transform 0.15s, box-shadow 0.15s',
      }}
    >
      <span style={{
        width: 40, height: 40, borderRadius: 8, display: 'flex',
        alignItems: 'center', justifyContent: 'center',
        background: 'var(--bg-tertiary)', flexShrink: 0,
      }}>
        <FileText size={18} />
      </span>
      <div style={{ flex: 1, minWidth: 0 }}>
        <div style={{ fontWeight: 600, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
          {file.nombre}
        </div>
        <div style={{ fontSize: '0.8rem', color: 'var(--text-tertiary)', display: 'flex', gap: '10px' }}>
          {file.formato && <span style={{
            padding: '1px 8px', borderRadius: 4, background: 'var(--bg-tertiary)',
            fontFamily: 'monospace', fontSize: '0.75rem',
          }}>{file.formato.toUpperCase()}</span>}
          <span>{sizeLabel}</span>
        </div>
      </div>
      <Icon size={18} style={{ color: 'var(--text-secondary)' }} />
    </a>
  );
}

function formatCell(value: unknown, col: ExplorerColumn): string {
  if (value === null || value === undefined) return '—';
  if (col.type === 'number') {
    const num = Number(value);
    if (isNaN(num)) return String(value);
    if (Math.abs(num) >= 1_000_000) return (num / 1_000_000).toFixed(1) + 'M';
    if (Math.abs(num) >= 1_000) return num.toLocaleString('es-AR');
    if (Number.isInteger(num)) return String(num);
    return num.toFixed(2);
  }
  return String(value);
}
