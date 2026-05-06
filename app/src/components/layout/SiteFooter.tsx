export function SiteFooter() {
  const year = new Date().getFullYear();
  return (
    <footer className="site-footer" role="contentinfo">
      <div className="site-footer-grid">
        <div>
          <h4 className="site-footer-heading">Fuente de los datos</h4>
          <ul>
            <li>
              <a href="https://datos.lujandecuyo.gob.ar" target="_blank" rel="noopener noreferrer">
                datos.lujandecuyo.gob.ar
              </a>
            </li>
            <li>Municipalidad de Luján de Cuyo, Mendoza, AR</li>
            <li>Categorías: 14 · Datasets: 83</li>
          </ul>
        </div>
        <div>
          <h4 className="site-footer-heading">Plataforma</h4>
          <ul>
            <li>
              <a href="https://colossuslab.org" target="_blank" rel="noopener noreferrer">
                ColossusLab.org
              </a>
            </li>
            <li>
              <a href="https://openarg.org" target="_blank" rel="noopener noreferrer">
                OpenArg.org
              </a>
            </li>
          </ul>
        </div>
        <div>
          <h4 className="site-footer-heading">Información</h4>
          <ul>
            <li>Datos refrescados desde el portal oficial</li>
            <li>
              <a href="mailto:contacto@colossuslab.org">Contacto</a>
            </li>
            <li>Licencia: CC-BY 4.0</li>
          </ul>
        </div>
      </div>
      <div className="site-footer-bottom">
        © {year} ColossusLab · Datos abiertos del municipio de Luján de Cuyo
      </div>
    </footer>
  );
}
