import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { Helmet } from 'react-helmet-async';
import { Search, Database, ArrowRight, ArrowLeft } from 'lucide-react';
import { SectionReveal } from '../components/ui/SectionReveal';
import { getCategoryIcon, type IconComp } from '../lib/categoryIcons';
import { REPORTS } from '../data/reportRegistry';
import type { ExplorerIndexEntry } from '../types/explorer';

const CATEGORY_COLOR: Record<string, string> = Object.fromEntries(
  REPORTS.map(r => [r.slug, r.color])
);

export function ExplorerIndex() {
  const [datasets, setDatasets] = useState<ExplorerIndexEntry[]>([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState('');
  const [activeCat, setActiveCat] = useState<string>('');

  useEffect(() => {
    fetch('/data/explorer/index.json')
      .then(r => r.json())
      .then(d => { setDatasets(d); setLoading(false); })
      .catch(() => setLoading(false));
  }, []);

  const filtered = datasets.filter(d => {
    if (activeCat && d.categorySlug !== activeCat) return false;
    if (!search) return true;
    const q = search.toLowerCase();
    return (
      d.title.toLowerCase().includes(q) ||
      (d.source || '').toLowerCase().includes(q) ||
      (d.category || '').toLowerCase().includes(q)
    );
  });

  // Agrupar por categoría
  const grouped: Record<string, ExplorerIndexEntry[]> = {};
  for (const d of filtered) {
    const cat = d.category || 'Sin categoría';
    if (!grouped[cat]) grouped[cat] = [];
    grouped[cat].push(d);
  }
  // Ordenar categorías por el orden de REPORTS
  const orderedCategories = Object.keys(grouped).sort((a, b) => {
    const ia = REPORTS.findIndex(r => r.category === a);
    const ib = REPORTS.findIndex(r => r.category === b);
    return (ia === -1 ? 999 : ia) - (ib === -1 ? 999 : ib);
  });

  const totalFiles = datasets.reduce((s, d) => s + (d.files || 0), 0);

  return (
    <div className="explorer-page">
      <Helmet>
        <title>Catálogo de Datos · Dashboard Luján de Cuyo</title>
        <meta
          name="description"
          content="83 datasets navegables del portal de datos abiertos del municipio de Luján de Cuyo. Filtrá, buscá y descargá los archivos oficiales."
        />
      </Helmet>
      <SectionReveal>
        <header className="explorer-header">
          <Link to="/" className="explorer-back">
            <ArrowLeft size={14} aria-hidden="true" /> Volver al Dashboard
          </Link>
          <h1 className="explorer-title">
            <span className="explorer-title-icon" aria-hidden="true">
              <Database size={28} />
            </span>
            Catálogo de Datos
          </h1>
          <p className="explorer-subtitle">
            {datasets.length} datasets · {totalFiles} archivos descargables
          </p>
          <div className="explorer-search-wrap">
            <input
              type="text"
              className="explorer-search"
              placeholder="Buscar datasets, secretaría o categoría..."
              value={search}
              onChange={e => setSearch(e.target.value)}
              aria-label="Buscar datasets"
            />
            <span className="explorer-search-icon" aria-hidden="true">
              <Search size={16} />
            </span>
          </div>
          {!loading && (
            <div
              className="explorer-cat-chips"
              style={{ display: 'flex', flexWrap: 'wrap', gap: '8px', marginTop: '16px' }}
            >
              <button
                className={`explorer-chip${activeCat === '' ? ' is-active' : ''}`}
                onClick={() => setActiveCat('')}
                style={chipStyle(activeCat === '')}
              >
                Todas
              </button>
              {REPORTS.map(r => (
                <button
                  key={r.slug}
                  className={`explorer-chip${activeCat === r.slug ? ' is-active' : ''}`}
                  onClick={() => setActiveCat(activeCat === r.slug ? '' : r.slug)}
                  style={chipStyle(activeCat === r.slug, r.color)}
                >
                  {r.shortTitle}
                </button>
              ))}
            </div>
          )}
        </header>
      </SectionReveal>

      {loading ? (
        <div className="explorer-loading" role="status" aria-live="polite">
          <div className="explorer-spinner" />
          <p>Cargando catálogo de datos...</p>
        </div>
      ) : (
        <div className="explorer-grid-wrap">
          {orderedCategories.map(catLabel => {
            const items = grouped[catLabel];
            const slug = items[0]?.categorySlug || '';
            const color = CATEGORY_COLOR[slug] || '#64748b';
            const Icon: IconComp = getCategoryIcon(slug);
            return (
              <SectionReveal key={catLabel}>
                <div className="explorer-category">
                  <h2 className="explorer-cat-title" style={{ color }}>
                    <span aria-hidden="true"><Icon size={20} /></span>
                    {catLabel}
                    <span className="explorer-cat-count">{items.length}</span>
                  </h2>
                  <div className="explorer-cards">
                    {items.map((ds, i) => (
                      <DatasetCard key={ds.id} dataset={ds} index={i} />
                    ))}
                  </div>
                </div>
              </SectionReveal>
            );
          })}
          {filtered.length === 0 && (
            <div className="explorer-empty" role="status">
              <span aria-hidden="true"><Search size={36} /></span>
              <p>No se encontraron datasets {search ? `para "${search}"` : ''}</p>
              {(search || activeCat) && (
                <button className="btn-secondary" onClick={() => { setSearch(''); setActiveCat(''); }}>
                  Limpiar filtros
                </button>
              )}
            </div>
          )}
        </div>
      )}
    </div>
  );
}

function chipStyle(active: boolean, color: string = '#7c3aed'): React.CSSProperties {
  return {
    padding: '6px 14px',
    borderRadius: '999px',
    border: `1px solid ${active ? color : 'var(--border-glass)'}`,
    background: active ? color : 'transparent',
    color: active ? '#fff' : 'var(--text-secondary)',
    fontSize: '0.85rem',
    fontWeight: 500,
    cursor: 'pointer',
    transition: 'all 0.15s',
  };
}

function DatasetCard({ dataset, index }: { dataset: ExplorerIndexEntry; index: number }) {
  const slug = dataset.categorySlug || '';
  const color = CATEGORY_COLOR[slug] || '#64748b';
  const Icon: IconComp = getCategoryIcon(slug);

  return (
    <Link
      to={`/explorar/${dataset.id}`}
      className="explorer-card"
      style={{ animationDelay: `${index * 60}ms`, '--card-accent': color } as React.CSSProperties}
    >
      <div className="explorer-card-top">
        <span className="explorer-card-icon" aria-hidden="true">
          <Icon size={20} />
        </span>
        <span className="explorer-card-source">{dataset.source}</span>
      </div>
      <h3 className="explorer-card-title">{dataset.title}</h3>
      <div className="explorer-card-stats">
        <div className="explorer-stat">
          <span className="explorer-stat-value">{dataset.files}</span>
          <span className="explorer-stat-label">archivo{dataset.files === 1 ? '' : 's'}</span>
        </div>
        {dataset.hasPreview && dataset.rows > 0 && (
          <div className="explorer-stat">
            <span className="explorer-stat-value">{dataset.rows.toLocaleString('es-AR')}</span>
            <span className="explorer-stat-label">filas</span>
          </div>
        )}
        {dataset.formats && dataset.formats.length > 0 && (
          <div className="explorer-stat">
            <span className="explorer-stat-value" style={{ fontSize: '0.85rem' }}>
              {dataset.formats.slice(0, 3).join(' · ')}
            </span>
            <span className="explorer-stat-label">formatos</span>
          </div>
        )}
      </div>
      <div className="explorer-card-arrow">
        Explorar <ArrowRight size={14} aria-hidden="true" />
      </div>
    </Link>
  );
}
