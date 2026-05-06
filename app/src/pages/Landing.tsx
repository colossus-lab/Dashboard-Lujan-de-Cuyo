import { Link } from 'react-router-dom';
import { useEffect, useRef, useState, useCallback } from 'react';
import { Helmet } from 'react-helmet-async';
import { ArrowRight, Search } from 'lucide-react';
import { REPORTS } from '../data/reportRegistry';
import { SectionReveal } from '../components/ui/SectionReveal';
import { SiteFooter } from '../components/layout/SiteFooter';
import type { ReportEntry } from '../types/report';

interface SummaryData {
  total_datasets: number;
  total_recursos: number;
  total_mb: number;
  total_categorias: number;
  total_formatos: number;
  total_organizaciones: number;
  datasets_por_categoria?: Record<string, number>;
}

export function Landing() {
  const [summary, setSummary] = useState<SummaryData | null>(null);

  useEffect(() => {
    fetch('/data/manifest-summary.json')
      .then(r => r.ok ? r.json() : null)
      .then(d => setSummary(d))
      .catch(() => setSummary(null));
  }, []);

  const heroStats = [
    { value: summary?.total_datasets ?? 83, label: 'Datasets', tooltip: 'Datasets publicados en el portal oficial del municipio' },
    { value: summary?.total_recursos ?? 204, label: 'Archivos', tooltip: 'Archivos descargables (CSV, XLSX, PDF, etc.)' },
    { value: summary?.total_categorias ?? 14, label: 'Categorías', tooltip: 'Áreas temáticas con datos publicados' },
    { value: summary?.total_organizaciones ?? 0, label: 'Secretarías', tooltip: 'Áreas del municipio que publican datos', hideIfZero: true },
  ].filter(s => !(s.hideIfZero && !s.value));

  return (
    <div className="landing-page">
      <Helmet>
        <title>Dashboard Luján de Cuyo · Datos Abiertos</title>
        <meta
          name="description"
          content="Plataforma de análisis interactivo sobre los datos abiertos del municipio de Luján de Cuyo (Mendoza, Argentina). 83 datasets en 14 categorías."
        />
      </Helmet>

      <SectionReveal>
        <header className="landing-hero">
          <div className="hero-particles" aria-hidden="true">
            {Array.from({ length: 6 }).map((_, i) => (
              <span key={i} className="hero-particle" style={{ '--i': i } as React.CSSProperties} />
            ))}
          </div>

          <div className="hero-content">
            <div className="hero-badge">
              <span className="hero-badge-dot" />
              Plataforma de Datos Abiertos
            </div>
            <h1 className="hero-title">
              Datos Abiertos
              <span className="hero-title-light">de Luján de Cuyo</span>
            </h1>
            <p className="hero-subtitle">
              Explorá <span className="hero-highlight">{summary?.total_datasets ?? 83} datasets</span> publicados por
              el municipio en {summary?.total_categorias ?? 14} categorías temáticas — desde economía y medio ambiente
              hasta urbanismo, movilidad y elecciones.
            </p>
            <p className="hero-attribution">
              Fuente:{' '}
              <a href="https://datos.lujandecuyo.gob.ar" target="_blank" rel="noopener noreferrer" className="hero-link">
                datos.lujandecuyo.gob.ar
              </a>{' '}
              · Powered by{' '}
              <a href="https://colossuslab.org" target="_blank" rel="noopener noreferrer" className="hero-link">
                ColossusLab
              </a>
            </p>

            <div className="hero-stats">
              {heroStats.map((stat, i) => (
                <div key={stat.label}>
                  {i > 0 && <span className="hero-stat-divider" />}
                  <div className="hero-stat" title={stat.tooltip}>
                    <CountUp target={stat.value} />
                    <span className="hero-stat-label">{stat.label}</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </header>
      </SectionReveal>

      <SectionReveal>
        <section className="landing-section">
          <div className="section-header">
            <div className="section-number">01</div>
            <div>
              <h2 className="section-title">Informes por Categoría</h2>
              <p className="section-desc">
                14 informes ejecutivos, uno por cada área temática del portal de datos abiertos del municipio.
              </p>
            </div>
          </div>
          <div className="report-grid">
            {REPORTS.map((report, i) => (
              <ReportCard key={report.id} report={report} index={i} count={summary?.datasets_por_categoria?.[report.slug]} />
            ))}
          </div>
        </section>
      </SectionReveal>

      <SectionReveal>
        <section className="landing-section landing-section-compact">
          <div className="explore-options">
            <Link to="/explorar" className="explorer-banner explorer-banner-large">
              <div className="explorer-banner-glow" aria-hidden="true" />
              <div className="explorer-banner-content">
                <div className="explorer-banner-icon" aria-hidden="true">
                  <Search size={32} />
                </div>
                <div className="explorer-banner-text">
                  <span className="explorer-banner-title">Catálogo de Datos</span>
                  <span className="explorer-banner-desc">
                    {summary?.total_datasets ?? 83} datasets · {summary?.total_recursos ?? 204} archivos descargables
                  </span>
                </div>
              </div>
              <div className="explorer-banner-arrow">
                <ArrowRight size={24} />
              </div>
            </Link>
          </div>
        </section>
      </SectionReveal>

      <SiteFooter />
    </div>
  );
}

function ReportCard({ report, index, count }: {
  report: ReportEntry;
  index: number;
  count?: number;
}) {
  const miniStat = count ? `${count} dataset${count === 1 ? '' : 's'}` : '';

  return (
    <Link
      to={`/${report.slug}`}
      className="report-card"
      style={{
        '--card-color': report.color,
        animationDelay: `${index * 80}ms`,
      } as React.CSSProperties}
    >
      <div className="report-card-glow" aria-hidden="true" />
      <div className="report-card-header">
        <span className="report-card-number">{String(report.order).padStart(2, '0')}</span>
        <span className="report-card-arrow">→</span>
      </div>
      <div className="report-card-body">
        <span className="report-card-title">{report.shortTitle}</span>
        <span className="report-card-desc">{report.title}</span>
      </div>
      {miniStat && (
        <div className="report-card-stat">
          <span className="report-card-stat-value">{miniStat}</span>
        </div>
      )}
    </Link>
  );
}

function CountUp({ target }: { target: number }) {
  const [value, setValue] = useState(0);
  const ref = useRef<HTMLSpanElement>(null);
  const hasAnimated = useRef(false);

  const animate = useCallback(() => {
    if (hasAnimated.current) return;
    hasAnimated.current = true;
    const reduce = window.matchMedia?.('(prefers-reduced-motion: reduce)').matches;
    if (reduce) {
      setValue(target);
      return;
    }
    const duration = 1500;
    const startTime = performance.now();
    const step = (now: number) => {
      const elapsed = now - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      setValue(Math.floor(eased * target));
      if (progress < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  }, [target]);

  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    const observer = new IntersectionObserver(
      ([entry]) => { if (entry.isIntersecting) animate(); },
      { threshold: 0.4 }
    );
    observer.observe(el);
    return () => observer.disconnect();
  }, [animate]);

  const formatted = value >= 1000
    ? value.toLocaleString('es-AR')
    : `${value}`;

  return (
    <span ref={ref} className="hero-stat-value">
      {formatted}
    </span>
  );
}
