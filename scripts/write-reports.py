"""Genera los 14 markdowns ejecutivos con análisis basados en datos reales.
Reemplaza los starter auto-generados por build-data.cjs.
Run: python scripts/write-reports.py
"""
from pathlib import Path

REPORTS_DIR = Path('public/reports')
REPORTS_DIR.mkdir(exist_ok=True, parents=True)

R = {}

R['gobierto-y-sector-publico.md'] = """# Gobierno Municipal

Es la categoría más grande del portal con **33 datasets** (40% del total publicado), distribuidos en al menos **10 áreas que publican**. Cubre la estructura institucional (organigramas, nóminas), la transparencia activa (declaraciones juradas, pedidos de información, licitaciones), las normativas (ordenanzas, presupuestaria/tarifaria por año) y la gestión administrativa (compras, pauta publicitaria, funcionarios).

Es la sección donde el municipio expone "cómo se gobierna a sí mismo": qué normas se votaron, quién ejecuta el gasto, y bajo qué procedimientos.

## Áreas que publican

Las áreas más activas son la **Secretaría de Hacienda**, la **Secretaría de Economía e Ingresos Públicos**, la **Dirección de Comunicación Estratégica**, la **Secretaría de Innovación, Gobierno Abierto y Gestión del Territorio** y la **Intendencia**. El **Honorable Concejo Deliberante** publica su propia nómina y antecedentes pero la mayor parte del volumen documental viene del Ejecutivo.

## Plantilla y estructura ejecutiva

- **56 funcionarios** en la nómina del Ejecutivo (mayo 2025): 36 Directores, 11 Secretarios de Departamento Ejecutivo, 1 Subsecretario, 1 Jefe de Gabinete, 1 Intendente, además de 2 Pro-secretarios, 2 Secretarios y 2 Jueces del Juzgado Vial.
- Salario básico de **Director: $460.927** mensual (Salarios Medios mayo 2025). Sub-Secretario: $654.367. Pro-Secretario Juzgado Vial: $331.081.
- **50 declaraciones juradas** publicadas para el Ejecutivo + **13 para el HCD** (DDJJ 2025, Ética Pública).

## Compras, contrataciones y pauta

Datos del dataset *Compras y Contrataciones* (2024) — el más voluminoso del portal con **23 archivos** y formatos múltiples:

- **1.585 órdenes de compra** registradas en 2024.
- **$5.065 millones** ejecutados en compras y contrataciones.
- Contrato medio: **$13,3 millones**. Contrato máximo: **$635 millones** (Plan Pavimentación 2024 — VIALMANI).
- **225 proveedores** distintos. Top 5 por monto agregado: **ECUR S.A.** ($695 M, alquiler camiones + servicio de poda), **VIALMANI** ($635 M, pavimentación), **CALZETTA S.A.** ($308 M, redes de agua), **VALENTINO MOTOS** ($231 M, vehículos utilitarios), **FICAMEN S.A.** ($165 M).
- **Pauta publicitaria**: evolución 2020 $24,5 M → 2021 $45,2 M → 2022 $92,8 M → 2023 $194,8 M → **2024 $296,2 M** (×12 nominal en 4 años). 76 medios proveedores listados, distribuidos en gráfica/online/radio/indoor.

## Acceso a la información pública

El dataset *Información Pública* incluye **82 tickets** registrados como pedidos AIP (Acceso a la Información Pública) en lo que va de 2025, con un esquema de seguimiento (estados, fechas, derivación) y 181 movimientos de avance.

## Datasets disponibles

Los 33 datasets cubren: Pauta publicitaria 2025 (#83), Organigrama Municipal (#1), Organigrama HCD (#3), **Ordenanzas Municipales** (#4), Presupuestaria/Tarifaria 2021/2022/2023 (#7, #37, #38, #52, #61, #65, #68, #69), Funcionarios Públicos Municipal (#55), Gasto Público Municipal (#56), Información Pública (#57), **Presupuesto de Gobierno** (#58), Resultado Electorales (#59), **Declaraciones Juradas** (#60), **Compras y Contrataciones** (#70), Estadísticas de Género (#72), Obras Públicas (#74), entre otros.

## Limitaciones

La mayoría de los archivos relacionados con normativas (presupuestaria, tarifaria por año) están en formato **PDF/DOCX** y no son procesables como datos estructurados. Sólo los datasets de pauta, compras, funcionarios, gastos y obras tienen formato tabular analizable.

## Fuente

Portal oficial: <https://datos.lujandecuyo.gob.ar>.
"""

R['medio-ambiente-y-desarrollo-sustentable.md'] = """# Medio Ambiente y Desarrollo Sustentable

Con **23 datasets**, es la segunda categoría más poblada del portal. Concentra la información ambiental crítica del municipio: gestión de residuos, calidad del aire y del agua, espacios verdes, ordenamiento territorial sustentable y la implementación local de los **Objetivos de Desarrollo Sostenible (ODS)** según el Manual de Adaptación 2ª Edición publicado.

## Áreas que publican

La gestión ambiental se reparte entre la **Secretaría de Higiene Urbana** (residuos, energía), la **Coordinación de Aguas y Servicios Sanitarios** (agua potable, perforaciones, plantas Cipolletti y Santa Elena), la **Secretaría de Infraestructura y Desarrollo Sostenible** (planes y programas) y la **Apoderada Municipal** (ciclovías).

## Gestión de residuos: el dato más rico

El relleno sanitario controlado **El Borbollón** publica toneladas mensuales 2021-2025, con métrica de **toneladas per cápita** referenciada al Censo 2021 (172.109 habitantes):

| Año | Toneladas dispuestas | Observación |
|-----|---------------------:|-------------|
| 2021 | 8.970 | inicio del registro |
| 2022 | 21.470 | +139% interanual |
| 2023 | 36.283 | +69% interanual |
| 2024 | ~8.985 | dato parcial (5 meses) |
| 2025 | ~3.115 | dato parcial (5 meses) |

El crecimiento 2021→2023 (×4) puede reflejar tanto **mayor recolección efectiva** como reactivación económica post-COVID. Los años 2024-2025 figuran con datos parciales — actualización pendiente.

En paralelo, el **Centro Verde** procesa material recuperable. La planilla de ventas 2025 (Ene-May) registra mensualmente: plástico (1.000-5.000 kg/mes), cartón (7.000-13.500 kg/mes), tetra (200-280 kg/mes), aluminio, baterías y chatarra. El programa *Puntos Verdes* alimenta este flujo desde toda la geografía municipal.

## Calidad del aire — telemetría continua

El sensor del **Tótem de Parque Cívico** publica mediciones de Humedad y Temperatura desde abril 2022. El histórico contiene **9.632 mediciones** acumuladas. Es uno de los pocos datasets con granularidad temporal a minutos.

## Calidad del agua

Análisis de laboratorio publicados año a año (2023, 2024, 2025) para las dos plantas: **Cipolletti** y **Santa Elena**, más perforaciones de pozos. El dataset *Calidad del Agua* (#48) reúne 11 planillas — el archivo más completo del bloque ambiental.

## Datasets disponibles

Centro Verde (#89, #40), Disposición Final de Residuos (#88), Calidad del Agua 2025 (#78) y dataset histórico (#48), Perforaciones (#79), Plantas Cipolletti y Santa Elena (#80, #81), Espacios Verdes (#9), **Residuos** (#22), **Manual ODS 2ª Edición** (#29), Plan de Ordenamiento Territorial (#30), GIRSU (#31), Circuito de Ciclovías (#33), **Plan Luján Sustentable** (#34), Torres Solares (#35), Bicisendas Inclusivas (#41), **Calidad del Aire** (#44), Calles por la Vida (#45), Educación y Participación (#47), Economía Circular (#50), Puntos Verdes (#63), Energía / Luminarias LED (#71).

## Limitaciones

Varios datasets de planes (#30 Ordenamiento, #34 Plan Sustentable, #41 Bicisendas, #50 Economía Circular, #63 Puntos Verdes) son enlaces a páginas web sin datos descargables. Para análisis cuantitativo, los datasets útiles se reducen a residuos, agua, aire y energía.

## Fuente

Portal oficial: <https://datos.lujandecuyo.gob.ar>.
"""

R['economia.md'] = """# Economía

**19 datasets** que retratan la economía pública y privada del departamento. Cubre el universo fiscal del municipio (presupuesto, gasto, tarifaria), la registración comercial (comercios por rubro, bancos, estaciones de servicio) y elementos de geografía económica (barrios populares, distritos, obras).

## Áreas que publican

Lidera la **Secretaría de Economía e Ingresos Públicos**, seguida por la **Secretaría de Hacienda** y la **Intendencia**. Hay datos agregados desde el ejercicio 2021 (formato PDF) y planillas de detalle desde 2022 (XLSX).

## La economía privada en cifras

- **11.630 comercios registrados** en el padrón municipal 2025 (dataset #87 *Comercios por Rubro*), distribuidos en **273 rubros** distintos.
- **Valor total declarado** (Unidades Tributarias × valor): **$14.391 millones**.
- **6.975 comercios facturan** (60%) y 4.655 no facturan (40%).
- Rubro dominante: "GENERICO" con 8.129 registros (70%); el resto se reparte entre comercios de almacén, productos no clasificados, servicios, golosinas/cigarrillos, frutas y verduras.

Otra mirada: **9 sucursales bancarias** (Frances, Supervielle, Nación, Galicia, HSBC, San Juan, Macro), **11 estaciones de servicio** (YPF, Vistalba GNC, Comercial Manitta, etc.) y **47 barrios populares** RENABAP que albergan **2.569 familias**.

## Gasto y presupuesto público

El dataset *Gasto Público Municipal* (#56) publica las planillas de ejecución 2021-2025. La planilla 2025 (al 04/07/2025) detalla el cuadro de cuentas:

- Presupuesto de gastos: **$4.443 millones**.
- Erogaciones corrientes: $2.966 M (67%); de operación $2.802 M; **personal $1.518 M** (34% del total); bienes de consumo $271 M; servicios $1.013 M.
- Erogaciones de capital: $1.338 M (30%).
- Intereses y gastos de la deuda: $24 M (<1%).
- Transferencias: $140 M.

El dataset *Presupuesto de Gobierno* (#58) publica recursos y gastos mensuales — útil para análisis de estacionalidad.

## Obras públicas

En *Obras Públicas 2025* (#74) figuran **174 actividades** registradas:

- **67 cumplidas** (39%), **40 no iniciadas** (23%), **34 en implementación** (20%), **18 atrasadas** (10%) y **11 canceladas** (6%).
- **165 actividades** corresponden al eje "Transformación del espacio público"; **9** al eje "Luján Sustentable".

## Compras del año fiscal

Las contrataciones de 2024 (cargadas en *Compras y Contrataciones*) totalizan **$5.065 millones** en 1.585 órdenes — el **20% del presupuesto** se ejecuta vía compras directas/licitaciones. Top contrato: Plan Pavimentación 2024 ($635 M).

## Datasets disponibles

Comercios por Rubro 2025 (#87), Gasto Público 2025 (#84), **Planilla de Licitación 2025** (#82), Barrios Populares (#5), **Limites Administrativos** (#8), Bancos (#25), **Pauta Publicitaria** (#42), Tarifaria/Presupuestaria 2021-2023 (#37, #38, #52, #61, #65, #68), Gasto Público Municipal (#56), Presupuesto de Gobierno (#58), **Unidades Comerciales** (#64), Obras Públicas (#74).

## Limitaciones

Las ordenanzas presupuestaria/tarifaria de cada año vienen como **PDF/DOCX**, no procesables. La planilla de comercios concentra el 70% en el rubro genérico, lo que limita el análisis sectorial fino. No hay datos directos de **empleo** (registración formal/informal) ni de **producción** (vitivinícola, construcción, servicios).

## Fuente

Portal oficial: <https://datos.lujandecuyo.gob.ar>.
"""

R['urbanismo-y-territorio.md'] = """# Urbanismo y Territorio

**14 datasets** que componen la base geográfica del departamento: distritos, barrios, espacios verdes, infraestructura, ordenamiento territorial. Es la "capa cartográfica" del portal, con presencia importante de formatos espaciales (KML, KMZ, GeoJSON, Shapefile).

## La división territorial

Luján de Cuyo se compone de **15 distritos** registrados con coordenadas y población (CSV #8 *Limites Administrativos*):

| Distrito | Población | | Distrito | Población |
|---|---:|---|---|---:|
| Ciudad | 24.594 | | Ugarteche | 6.603 |
| Carrodilla | 23.886 | | El Carrizal | 4.177 |
| Perdriel | 13.687 | | La Puntilla | 2.842 |
| Chacras de Coria | 12.428 | | V. de Pedemonte | 2.428 |
| Vistalba | 8.771 | | Potrerillos | 2.075 |
| Mayor Drumond | 8.223 | | Las Compuertas | 1.353 |
| Agrelo | 7.507 | | Cacheuta | 701 |
| | | | Industrial | 41 |

Los tres distritos del cordón urbano (Ciudad, Carrodilla, Perdriel) concentran ~50% de la población. La zona industrial figura con sólo 41 habitantes residentes (es uso predominantemente productivo). El total censado por distrito (~119.300) es consistente con el Censo 2010; el Censo 2021 reportó 172.109 habitantes departamentales.

Existen además **radios y fracciones censales** publicadas en KMZ (#21) y un dataset complementario *Barrios del Departamento* (#53) con KML de 273+ barrios.

## Espacios verdes

El relevamiento 2025 publica **272 espacios verdes** con **1,35 km² de superficie agregada** (1.346.513 m²). Tipología:

- **Plazas: 56**
- **Espacios verdes (genérico): 65**
- **Boulevards: 60**
- Espacios públicos: 38; Laterales de ruta: 15; Paseos: 15; Rotondas: 9; Pasarelas, cortinas forestales y miradores: 3.

Distribución por distrito (top): **Carrodilla 77** espacios, **Ciudad 59**, **Mayor Drummond 33**, **La Puntilla 26**, **El Carrizal 13**, **Perdriel 12**, **Vistalba 11**.

## Infraestructura urbana

- **Estaciones de servicio: 11** (YPF, GNC Vistalba, Hekar Acceso Sur, Rumaos Ruta 40, Red Mercosur, etc.).
- **Uniones Vecinales** (#10): listado de organizaciones territoriales.
- **Transporte Público** (#54): red de líneas urbanas con KML de recorridos y XLS de horarios.
- **Circuito de Ciclovías** (#33): integrado con Puntos de Encuentro Saludables (PES) — disponible en My Maps.

## Planes territoriales

El **Plan Municipal de Ordenamiento Territorial (PMOT)** y su Código de Uso del Suelo se publican como página web (#30, #16). Existe un dataset *Desarrollo Territorial* específico para esta cuestión, aunque sin descargables tabulares.

## Barrios populares

Los **47 barrios populares** del Registro Nacional (RENABAP) localizados en el departamento totalizan **2.569 familias**. Top: Valle Encantado (Chacras, 290 familias), Tierras Vivas (Agrelo, 170), Patrono Santiago (Ciudad, 160), Virgen de Lourdes (Perdriel, 135), Costanera Sur (Ciudad, 132).

## Datasets disponibles

Limites Administrativos (#8), Espacios Verdes (#9), Uniones Vecinales (#10), Desarrollo Territorial (#16), **Radios Fracciones Censales** (#21), Estaciones de Servicios (#26), PMOT/Código de Uso del Suelo (#30), GIRSU (#31), Ciclovías (#33), Centro Verde (#40), Economía Circular (#50), **Barrios del Departamento** (#53), Transporte Público (#54), Barrios Populares (#5).

## Limitaciones

Los KML de radios censales y barrios deben procesarse con QGIS o similar — no hay versión tabular de estos cortes finos. Falta una serie de población **por distrito y año** para análisis demográfico evolutivo (sólo hay foto Censo 2010).

## Fuente

Portal oficial: <https://datos.lujandecuyo.gob.ar>. Datos espaciales en proyección WGS84.
"""

R['deporte-educacion-y-salud.md'] = """# Deporte, Educación y Salud

**9 datasets** que retratan la red de servicios sociales territoriales: escuelas, centros de salud, polideportivos, farmacias, espacios deportivos al aire libre y los análisis sanitarios del agua potable. Es el bloque que muestra "qué oferta de servicios públicos y comerciales tiene el vecino en cada distrito".

## Áreas que publican

La **Secretaría de Desarrollo Humano** lidera con tres datasets clave (Escuelas, Farmacias, Centros de Salud, Polideportivos). Complementan la **Coordinación de Aguas** (Calidad del Agua, transversal con Medio Ambiente), la **Dirección de Turismo** (Aventura, transversal con Cultura/Turismo), la Subsecretaría de Gestión del Talento Humano (COVID) y el Apoderado Municipal (Ciclovías).

## Educación: el mapa escolar

El relevamiento 2025 publica **112 establecimientos educativos** con dirección, distrito, matrícula, nivel, modalidad, ámbito y gestión. Hallazgos:

- **Matrícula total: 17.318 estudiantes** (CSV #6).
- Distribución por nivel:
  - **Primaria**: 54 escuelas
  - **Secundaria** (orientada + técnica + común): 21
  - **Jardín maternal**: 10 (+ 1 SEOS, + 2 Jardín y CAE)
  - **CEBJA / CENS** (jóvenes y adultos): 11
  - **Capacitación laboral**: 5 + 1 centro
  - **Educación superior** (terciario): 4
  - **Educación especial**: 3
- Por **ámbito**: 58 urbanas, 50 rurales, 4 urbano-marginal.
- Por distrito (top): Ciudad 23, Chacras de Coria 16, Carrodilla 16, Mayor Drummond 12, Perdriel 10, Ugarteche 8, El Carrizal 7, Potrerillos 6.
- Modalidades técnicas/orientadas variadas: Gestión Contable, Humanidades, Electricidad, Industria de Proceso, Comercio Exterior, Producción de Bienes y Servicios, Electromecánica, Enfermería, Agronomía y Apicultura.

## Salud: red de centros y servicios

- **19 centros de salud** publicados con coordenadas y dirección (#75). Distribución: Carrodilla 3, Agrelo 3, Ugarteche 2, Potrerillos 2, El Carrizal 2, Perdriel 2, Cacheuta 2, Ciudad 1, Las Compuertas 1, Chacras de Coria 1.
- **18 farmacias** registradas con dirección y geolocalización (#27). Concentración en eje San Martín / Roque Sáenz Peña / Viamonte.
- **Calidad del Agua** (transversal con Medio Ambiente, #48): planillas de laboratorio 2024-2025 para Plantas Cipolletti y Santa Elena, más perforaciones — relevante para vigilancia sanitaria.
- **Informe COVID Municipal 2022** (#67): 84 semanas con casos positivos, recuperados, en tratamiento, fallecidos.

## Deporte y recreación

- **Polideportivos** (#66): mapa de localización (link a página web del municipio).
- **Aventura** (#18): 11 lugares para actividades al aire libre, todos en **Potrerillos**.
- **Espacios Verdes** (transversal con Urbanismo, #9): 272 espacios públicos con 56 plazas formales — soporte para deporte recreativo.
- **Circuito de Ciclovías** (#33): conectividad activa con PES (Puntos de Encuentro Saludables).

## Datasets disponibles

Escuelas (#6), Espacios Verdes (#9), Aventura (#18), Farmacias (#27), Ciclovías (#33), Calidad del Agua (#48), Polideportivos (#66), Informe COVID Municipal (#67), Centros de Salud (#75).

## Limitaciones

No hay datos de **rendimiento educativo** (Aprender, repitencia, terminalidad) ni de cobertura/utilización de centros de salud (consultas, pacientes atendidos, derivaciones a hospitales provinciales). El dataset COVID llega hasta 2022.

## Fuente

Portal oficial: <https://datos.lujandecuyo.gob.ar>. Datos del año 2025 salvo indicación.
"""

R['honorable-consejo-deliberante-lujan-de-cuyo.md'] = """# Honorable Concejo Deliberante

**9 datasets** específicos del Poder Legislativo municipal de Luján de Cuyo. Reúnen información institucional sobre la composición del cuerpo (concejales, antecedentes, estructura), su nómina de personal, los pedidos de información que recibe, las declaraciones juradas patrimoniales y los resultados electorales que constituyen al cuerpo.

## Áreas que publican

El propio **HCD de Luján de Cuyo** publica organigrama, nómina, antecedentes profesionales y estructura. La **Secretaría de Economía e Ingresos Públicos** publica funcionarios públicos (incluyendo HCD) y normativa presupuestaria. La **Secretaría de Innovación** centraliza los pedidos de información. Las **DDJJ** del HCD se publican en conjunto con las del Ejecutivo.

## Composición del cuerpo

- **13 declaraciones juradas** publicadas para el HCD (mayo 2025), correspondientes a concejales en mandato 2023/2027 y secretarios del Concejo: Andrés Sconfienza, Adrián Devia, Claudio Ogando (Secretario), Guillermo Trentacoste, Malena Abalos, Carlos Sala, Rubén Lazaro, Paloma Scalco, entre otros (DDJJ HCD 2025, #60).
- **Antecedentes profesionales** y **CVs** del HCD se publican en PDF (#19) — útil para escrutinio público.
- La **Estructura HCD** está disponible como organigrama PDF (#73).

## Pedidos de información pública

El cuerpo gestiona pedidos AIP (Acceso a la Información Pública) — hay una planilla de **garantes-hcd** y "pedidos de información pública 2024" en *Información Pública* (#57). Junto al pulido por el Ejecutivo, en lo que va de 2025 se registran **82 tickets** AIP combinados (Ejecutivo + HCD).

## Resultados electorales

Las **elecciones provinciales PASO 2023** definieron la composición vigente. El detalle escrutado se publica en *Resultado Electorales* (#59):

- Categorías publicadas: Gobernador, Senadores Provinciales, Diputados Provinciales, **Concejal**, escrutinio definitivo del 24/09/2024 — total 8 archivos PDF + XLS.
- El dataset *Voto electoral* (#49) detalla las **316 mesas** de la categoría Concejales con desglose por agrupación, votos en blanco, impugnados, comando electoral.

## Sueldos del Cuerpo

El dataset *Funcionarios Públicos Municipal* (#55) publica también la **Nómina HCD 2025** (4 archivos XLSX). Junto a la nómina del Ejecutivo conforma el padrón completo de empleados del Estado municipal.

## Datasets disponibles

Nómina de Concejales (#17), Antecedentes Profesionales HCD (#19), Tarifaria 2023 (#52), **Funcionarios Públicos Municipal** (#55, parcialmente HCD), **Información Pública** (#57), Resultado Electorales (#59), Declaraciones Juradas (#60), Presupuestaria (#68), **Estructura HCD** (#73).

## Limitaciones

La mayoría de los datos del HCD están en **PDF** (organigramas, nóminas, antecedentes, presupuestaria) — no son datos estructurados. Para análisis de la actividad legislativa (proyectos presentados, votaciones nominales, asistencia de concejales) hay que recurrir al sitio del HCD directamente: el portal de datos abiertos no expone esa serie.

## Fuente

Portal oficial: <https://datos.lujandecuyo.gob.ar>.
"""

R['cultura-y-turismo.md'] = """# Turismo y Cultura

**8 datasets** dedicados al ecosistema turístico y cultural departamental, fuertemente concentrados en la zona de **Potrerillos / Las Compuertas / Cacheuta** (cordón cordillerano) y el corredor **Chacras de Coria** (gastro-vitivinicultura).

## La oferta gastronómica

El relevamiento de la Dirección de Turismo registra **137 locales gastronómicos** (#20) clasificados así:

- **Restaurantes: 84** (61% del total)
- **Cafeterías: 17**
- **Heladerías: 10**
- Casas de Té: 5
- Pizzerías: 4
- Pastelerías: 3
- Restaurantes de Sushi: 3
- Otros (parrilla, panchería, taquería, lomitería, restaurantes árabe/cubano/comida rápida): 11

**Concentración geográfica** — top distritos: **Chacras de Coria 43**, Ciudad 28, **Potrerillos 23**, Cacheuta 11, Las Compuertas 8, Agrelo 8, Vistalba 5, La Puntilla 4. Chacras y Potrerillos concentran casi la mitad del mapa gastronómico — coherente con el perfil turístico-residencial de cada zona.

## Alojamiento

**73 alojamientos** registrados (#12). Distribución por distrito:

- **Potrerillos: 53** (73% del total) — perfil cabañas/posadas/turismo aventura.
- **Cacheuta: 7** y **Las Compuertas: 7** (cordón termal y montaña).
- Agrelo, Perdriel, Vistalba, Ciudad: pequeños volúmenes (1-2 cada uno).

Esta concentración refleja que el **eje turístico de pernocte está en montaña**, mientras que Chacras opera más como destino de día.

## Aventura y vitivinicultura

- **Aventura** (#18): 11 emprendimientos, **todos en Potrerillos** — rafting (Argentina Rafting, Río Aventura), kayak (Milkayak), trekking (Potrerillos Explorer, Mendoza Aventura), navegación a vela (Huayra Veleros), expediciones de alta montaña (Colanguil Expediciones).
- **Bodegas** (#13): listado publicado por la Dirección de Turismo (sin archivos descargables — sólo la metadata del dataset).
- **Senderos de Trekking** (#14): KML con recorridos.

## Movilidad turística

El **Transporte Público** (#54) y el **Circuito de Ciclovías** (#33) — ambos con KML — son insumos relevantes para la planificación de visitantes.

## Datasets disponibles

Alojamiento (#12), Bodegas (#13), Senderos de Trekking (#14), Aventura (#18), Gastronomía (#20), Ciclovías (#33), Transporte Público (#54).

## Limitaciones

No hay series temporales de **ocupación hotelera**, **cantidad de visitantes**, **derrama turística** ni **eventos culturales realizados** — sólo el inventario estático de oferta. Para indicadores de demanda turística hay que recurrir a la Provincia (Subsecretaría de Turismo) o al INDEC. Bodegas no tiene archivos descargables, lo que es notorio dado el peso del enoturismo en la economía local.

## Fuente

Portal oficial: <https://datos.lujandecuyo.gob.ar>. Direcciones y coordenadas en proyección WGS84.
"""

R['desarrollo-humano.md'] = """# Desarrollo Humano

**5 datasets** que reúnen el "tejido social organizado" del departamento: barrios populares, uniones vecinales, polideportivos, programas de economía circular y las estadísticas de violencia de género (transversal con la categoría Género). Es la sección más cercana a la agenda de inclusión, vulnerabilidad y participación comunitaria.

## La población vulnerable territorializada

El **Registro Nacional de Barrios Populares (RENABAP)** identifica **47 barrios** en Luján de Cuyo (#5):

- **2.569 familias** registradas en estas geografías.
- Top barrios por familias:
  - Valle Encantado (Chacras de Coria) — 290 familias
  - Tierras Vivas (Agrelo) — 170
  - Patrono Santiago (Ciudad) — 160
  - Virgen de Lourdes (Perdriel) — 135
  - Costanera Sur (Ciudad) — 132
  - Juan XXIII (Ciudad) — 110
  - Villa Costa Canal (Ugarteche) — 102
  - Estación Cuadro (Perdriel) — 100

La distribución muestra que **Ciudad y los distritos urbanos peri-centrales** concentran la mayor cantidad de familias en barrios populares, aunque también hay focos en zonas rurales (Agrelo, Ugarteche, Perdriel).

Estos datos provienen del relevamiento RENABAP nacional y permiten cruzar con políticas de regularización dominial y obras de servicios.

## Organización vecinal

El listado de **Uniones Vecinales** (#10) es el directorio formal de organizaciones de base territorial — interlocutor habitual del municipio en obras locales, presupuesto participativo y eventos.

## Estadísticas de género (transversal)

El dataset *Estadísticas de Género* (#72) — analizado en detalle en su categoría dedicada — registra los casos atendidos por la Dirección de Género y Diversidad mediante fichas RUC. En 2022, **Luján de Cuyo concentró 480 casos**, frente a 9 en Capital, 2 en Godoy Cruz, 1 en Guaymallén y 1 en Maipú. Las planillas 2025 (datos crudos) tienen 87 dimensiones por ficha (nivel educativo, vínculo, violencia previa, intentos de homicidio, consecuencias civiles/penales).

## Polideportivos y deporte social

Los **Polideportivos** (#66) son nodos clave para el desarrollo humano — su localización está publicada como mapa web del municipio.

## Economía circular

El convenio con **Prato (Italia)** (#50) impulsa programas de economía circular con foco en revegetación, recuperación de materiales y reciclaje — articulado con organizaciones sociales locales.

## Datasets disponibles

Barrios Populares (#5), Uniones Vecinales (#10), Economía Circular (#50), Polideportivos (#66), Estadísticas de Género (#72).

## Limitaciones

No hay datos de **programas sociales municipales** (becas, subsidios, alimentación, copa de leche, etc.), de **personas atendidas** por área, ni de **vacantes/cobertura** en jardines maternales y CDIs. Tampoco hay series de **pobreza/indigencia** local (el INDEC publica a nivel del Gran Mendoza, no del departamento). Esto es probablemente la mayor brecha del portal.

## Fuente

Portal oficial: <https://datos.lujandecuyo.gob.ar>. Datos RENABAP corresponden al relevamiento nacional.
"""

R['movilidad.md'] = """# Movilidad

**5 datasets** que cubren la infraestructura de movilidad del departamento: transporte público urbano, ciclovías, obras viales, seguridad vial y la red de barrios populares (relevante para conectividad). El bloque tiene un fuerte componente de **datos espaciales (KML)** con baja densidad de información tabular.

## Transporte público

El dataset *Transporte Público* (#54) publica:

- **Red Luján** en formato **KML** (recorridos de líneas urbanas para visualización en Google Earth o QGIS).
- **Red de transporte urbano** en XLS con horarios.
- Página web con información operativa actualizada.

Esto permite reconstruir cobertura geográfica del transporte municipal, frecuencias y conectividad entre distritos.

## Ciclovías y movilidad activa

El **Circuito de Ciclovías** (#33) está publicado en formato **My Maps** (Google) con los recorridos de las ciclovías ejecutadas y los **Puntos de Encuentro Saludables (PES)** que las articulan. Es uno de los pocos datasets en este formato dentro del portal.

## Obras viales

El dataset *Obras Públicas* (#74) — transversal con Economía y Urbanismo — contiene **174 actividades** en 2025, mayoritariamente del eje "Transformación del espacio público" (165 actividades / 95%). Estado de avance:

- **Cumplido**: 67 (39%)
- **No iniciado**: 40 (23%)
- **En implementación**: 34 (20%)
- **Atrasado**: 18 (10%)
- **Cancelado**: 11 (6%)

Las **compras 2024** detallaron contratos viales de gran porte: Plan Pavimentación 2024 ($635 M, VIALMANI), redes de agua potable ($238 M, CALZETTA), reparación de motoniveladora ($7 M), cubiertas para máquinas viales — dan dimensión del esfuerzo de mantenimiento de la red vial.

## Seguridad vial

El dataset *Seguridad Vial* (#51) está listado como "Acciones viales" y comparte información con la Secretaría de Gobierno; sin embargo, no tiene archivos descargables — sólo la metadata. Es una brecha clara, dado que es el indicador más sensible de movilidad.

## Conectividad social

Los **47 barrios populares** (#5) entran en esta categoría como territorios cuya conectividad con el resto del departamento depende fuertemente del transporte público y la red vial.

## Datasets disponibles

Barrios Populares (#5), Ciclovías (#33), Seguridad Vial (#51), Transporte Público (#54), Obras Públicas (#74).

## Limitaciones

Es la categoría con **menor densidad de datos cuantitativos** entre las relevantes. Faltan: series temporales de **siniestros viales** (cantidad, fatalidad, lugar), **flujo vehicular** (aforo en arterias clave), **uso del transporte público** (boletos vendidos, frecuencias por línea, modalidad SUBE), e indicadores de **calidad** del servicio. Las ciclovías están relevadas pero no hay datos de aforos ciclistas o accidentes.

## Fuente

Portal oficial: <https://datos.lujandecuyo.gob.ar>. Datos espaciales en KML/My Maps (proyección WGS84).
"""

R['elecciones.md'] = """# Elecciones

**4 datasets** que documentan los resultados electorales recientes en Luján de Cuyo, fundamentalmente de las **PASO Provinciales 2023** y categorías nacionales subsiguientes. Es la única categoría del portal con un nivel de granularidad **a mesa** — algo poco común en datos abiertos municipales.

## PASO Provinciales 2023

El dataset *Elecciones Departamental* (#32, 14 archivos) publica el escrutinio mesa por mesa. Análisis del XLSX consolidado *resultados_pasos_2023.xlsx* (categoría Concejal):

- **474 filas** de resultados (combinación mesa × lista).
- Distritos relevados: Chacras de Coria 178 mesas, Perdriel 103, Carrodilla 95, Ciudad 50, Mayor Drummond 48 (planilla parcial).
- **Top agrupaciones por votos** (en mesas relevadas):
  - **CAMBIA MENDOZA**: 4.670 votos
  - **LA UNIÓN MENDOCINA**: 4.499 votos
  - **ELEGÍ MENDOZA**: 1.006
  - **FRENTE DE IZQUIERDA Y DE TRABAJADORES**: 404
  - **PARTIDO VERDE**: 355

## Voto desagregado por categoría

El dataset *Voto Electoral* (#49) suma la categoría **Concejales** mesa por mesa con **316 mesas** (XLSX *consejales*) y replica el mismo formato para Diputados Nacionales/Provinciales y Senadores Nacionales en archivos separados. Desglose por mesa: votos por lista + votos en blanco + votos impugnados + votos del comando electoral.

## Resultado Electorales 24/09 (definitivo)

El dataset *Resultado Electorales* (#59, 8 archivos) publica el **escrutinio definitivo** del 24 de septiembre con los resultados consolidados por categoría:

- **Gobernador** (PDF + XLSX)
- **Senadores Provinciales** (PDF)
- **Diputados Provinciales** (PDF)
- **Concejales** (PDF)
- **Escrutinio definitivo Luján de Cuyo** (PDF + XLSX)

## Marco normativo

Las **Ordenanzas Municipales** (#4) — repositorio CSV/XLS/PDF — incluyen las normas que regulan los procesos electorales locales y el funcionamiento del HCD electo.

## Datasets disponibles

Ordenanzas Municipales (#4), Elecciones Departamental (#32), Voto Electoral (#49), Resultado Electorales (#59).

## Limitaciones

Los archivos están en formatos **mixtos** (XLS, XLSX, PDF) y a veces nombrados con código de circuito sin metadata clara (`zona_circ_0057.xls`, etc.) — requieren trabajo manual para consolidar. **No hay datos** de elecciones anteriores (2017, 2019, 2021) ni de las **municipales 2023** propiamente — sólo provinciales/nacionales del mismo año. Tampoco se publican padrones, vacantes asignadas o datos de simultaneidad de votación.

## Fuente

Portal oficial: <https://datos.lujandecuyo.gob.ar>. Datos del escrutinio provisional y definitivo, Junta Electoral de Mendoza.
"""

R['genero.md'] = """# Género y Diversidad

**3 datasets** específicos sobre la política pública de género y diversidad en Luján de Cuyo. Es una categoría compacta pero la planilla de estadísticas es uno de los datasets **más ricos en dimensiones analíticas** del portal.

## Marco institucional y normativo

Dos datasets institucionales encuadran la política:

- **Acuerdo de Cooperación** (#43): convenio entre el Municipio de Luján de Cuyo y la **Procuración General de la Suprema Corte de Justicia de Mendoza** — articulación con el Poder Judicial provincial para casos de violencia.
- **Protocolo de Acción** (#46): procedimiento para atención y acompañamiento de mujeres víctimas de violencia y en situación de vulnerabilidad — documento operativo para los equipos territoriales.

## Estadísticas operativas

El dataset estrella es *Estadísticas de Género* (#72): planillas de datos relevados por la **Dirección de Género y Diversidad** desde **2021 hasta 2025**, mediante **fichas RUC** (Registro Único de Casos). Archivos:

- Estadísticas 2025 (XLSX, 772 KB) — datos crudos con **87 dimensiones por ficha**.
- 1er semestre 2023 (XLSX).
- 2022 (XLSX, 556 KB).
- 2021 (XLSX, 687 KB).
- DOCX informativo y un PBIX (Power BI) para visualización.

**Localización de los casos** atendidos en 2022:

| Departamento (víctima) | Casos |
|---|---:|
| **Luján de Cuyo** | **480** |
| Capital | 9 |
| Godoy Cruz | 2 |
| Guaymallén | 1 |
| Maipú | 1 |

El **98% de los casos** atendidos por la Dirección refieren a víctimas residentes en Luján de Cuyo — el dispositivo opera principalmente sobre la población local, con incidencia muy menor desde otros departamentos.

## Las dimensiones del relevamiento

La ficha 2025 captura un panorama integral: nivel educativo, condición de actividad económica, AUH/AUE, cuota alimentaria, salario familiar, Progresar, pensión 7 hijos, vínculo con agresor, tipos de violencia (física, psicológica, económica, patrimonial, sexual), señales de riesgo (intentos de homicidio, lesiones, amenazas, portación de armas, intento suicida), trastornos asociados, impacto laboral/educativo, medidas judiciales (prohibición de acercamiento, exclusión del hogar, alimentos provisorios).

Es uno de los pocos datasets del portal con esta **profundidad analítica** — útil para investigaciones sociales y políticas basadas en evidencia.

## Cifras 2022

Del archivo `estadisticas2022-copia.xlsx` se desprenden hojas resumen con cuentas por dimensión:

- **Nivel educativo de las víctimas**: 23 sin educación, 25 primaria incompleta, 55 primaria completa, 178 secundaria incompleta, 99 secundaria completa, etc.

Esto perfila una población mayoritariamente con **trayectorias educativas interrumpidas** — input clave para articulación con políticas educativas.

## Datasets disponibles

Acuerdo de Cooperación (#43), Protocolo de Acción (#46), Estadísticas de Género (#72).

## Limitaciones

Las **dos primeras filas** de las planillas de estadísticas tienen formato visual (gráficos embebidos como imagen, encabezados desordenados) — el procesamiento automático requiere un script ad-hoc por hoja. No hay un **diccionario de variables** público que documente los códigos de las 87 columnas — para análisis externo se necesita consulta a la Dirección. Tampoco se publica una **serie agregada anual de casos totales** que facilite la comunicación pública.

## Fuente

Portal oficial: <https://datos.lujandecuyo.gob.ar>. Dirección de Género y Diversidad, Municipalidad de Luján de Cuyo.
"""

R['gestion_de_datos.md'] = """# Gestión de Datos

**3 datasets** que documentan la **estrategia institucional** del municipio sobre datos abiertos, gobernanza de la información e inteligencia artificial. Aunque pequeña en cantidad, es la categoría que da contexto al **resto del portal**: explica cómo se decide qué se publica, bajo qué reglas y con qué herramientas.

## Inteligencia Artificial: gobernanza

El dataset *Inteligencia Artificial* (#90) reúne la **Estrategia de Gobernanza de IA** del municipio. Componentes publicados (mayo 2025):

- **Decreto Nro 3041** sobre uso de IA y Machine Learning en el Estado municipal — marco regulatorio que establece principios y restricciones.
- **Estrategia de Datos para Toda la Ciudad** (documento institucional VF 08/12/2024) — visión integradora.
- **Protocolo Ético para el Uso de IA en la Municipalidad de Luján de Cuyo** — documento operativo con principios éticos aplicables.
- **Gobernanza_IA.xlsx**: tabla con dimensiones (Institucionalidad, Reglamentación, Protección de datos), área a cargo y productos generados.
- **Programas IA.xlsx** y **Innovación_Desarrollo.xlsx**: programas asociados.
- Enlaces web a *Laboratorio Inteligente* (Portal Luján Lab) y a la página de **Ciberseguridad** del municipio.

Es uno de los conjuntos documentales más completos del portal y posiciona a Luján de Cuyo entre los pocos municipios argentinos con normativa específica sobre IA.

## Inventario de Datos

El dataset *Inventario de Datos* (#62) ofrece "una visión integral de todos los recursos de datos de la ciudad" — es el **catálogo maestro** que sirve de base al portal de datos abiertos. Está publicado como un único archivo XLSX, mantenido por la Secretaría de Innovación, Gobierno Abierto y Gestión del Territorio.

## Repositorio normativo

El dataset *Ordenanzas Municipales* (#4) es el repositorio centralizado de las ordenanzas votadas por el HCD. Incluye:

- Ordenanzas 2025 categorizadas (CSV+XLS).
- Ordenanzas Categorizadas 2024 (CSV+XLS).
- Ordenanzas 2024-2016 históricas (CSV).
- ORDENANZA Nº 14830-2024 Presupuesto 2025 (DOCX) y 14831-2024 Tarifaria 2025 (PDF).

Permite analizar la **producción legislativa** del HCD por categoría temática.

## Datasets disponibles

Ordenanzas Municipales (#4), Inventario de Datos (#62), Inteligencia Artificial (#90).

## Limitaciones

Los **3 documentos institucionales** sobre IA están en HTML/PDF y aunque marcan políticas claras, su contenido no es procesable como datos. El **Inventario de Datos** es un único archivo y debería actualizarse al menos trimestralmente para reflejar bajas/altas de datasets — no hay un changelog público.

## Fuente

Portal oficial: <https://datos.lujandecuyo.gob.ar>. La estrategia de IA y gobernanza es responsabilidad de la Secretaría de Innovación, Gobierno Abierto y Gestión del Territorio.
"""

R['seguridad.md'] = """# Seguridad

**2 datasets** componen una de las categorías más **subdesarrolladas** del portal — coherente con que la seguridad pública es competencia primaria de la Provincia y la Nación. Lo publicado por el municipio cubre la red de **comisarías** y un dataset de **acciones viales** sin archivos descargables.

## Comisarías del departamento

El dataset *Comisarías Luján de Cuyo* (#24, 2 archivos) publicado por el **Secretario del Juzgado Vial Nro 1** publica la red departamental:

- **Comisarias_2025.xlsx** con dirección, distrito y datos de contacto.
- **comisarias.kml** con coordenadas para visualización.

Es el único dataset de seguridad con contenido tabular accesible.

## Seguridad vial

El dataset *Seguridad Vial* (#51) figura como "Acciones viales" pero **no tiene archivos descargables** ni descripción ampliada — sólo metadata mínima. Es una brecha visible: la fiscalización vial municipal (multas, controles, alcoholemias, siniestros) no se publica con datos abiertos.

## Datasets transversales

Aunque no están etiquetados como "seguridad", varios datasets de otras categorías aportan información relevante:

- **Bancos** (#25, 9 sucursales) — información sensible para planificación de respuesta policial-municipal.
- **Estaciones de Servicios** (#26, 11 ubicaciones) — puntos críticos.
- **Centros de Salud** (#75, 19) y **Farmacias** (#27, 18) — receptores potenciales de emergencias.
- **Comercios por Rubro** (#87) — base para mapeo de actividad económica nocturna y rubros sensibles.
- **Iluminación LED** (#71, dataset *Energía*) — relevante para seguridad ambiental peatonal.

## Datasets disponibles

Comisarías de Luján de Cuyo (#24), Seguridad Vial (#51).

## Limitaciones

Es probablemente la categoría con **mayor brecha de datos** del portal. Falta toda la serie de:

- **Hechos delictivos** (robos, hurtos, lesiones, homicidios) — competencia provincial pero replicable a nivel local con datos del Ministerio de Seguridad y Justicia de Mendoza.
- **Multas y controles viales** — competencia municipal directa, no se publica.
- **Siniestros viales** (cantidad, fatalidad, georreferenciación) — uno de los indicadores más demandados.
- **Operativos** y **denuncias** recibidas en el ámbito municipal.
- **Cuerpo de Inspección General** (urbano y rural) — sus actuaciones no son públicas.

Para análisis de seguridad en Mendoza hay que recurrir a fuentes provinciales o nacionales (SNIC del Ministerio de Seguridad de la Nación).

## Fuente

Portal oficial: <https://datos.lujandecuyo.gob.ar>. La seguridad es competencia primaria del Ministerio de Seguridad y Justicia de la Provincia de Mendoza y el Ministerio de Seguridad de la Nación.
"""

R['covid-19.md'] = """# COVID-19

**1 único dataset** documenta la respuesta municipal a la pandemia: el *Informe Covid Municipal* (#67) publicado por la **Subsecretaría de Gestión del Talento Humano**. La planilla cubre el período de circulación activa del virus durante 2020-2022 con relevamiento semanal.

## Lo que registra el informe

La planilla *informe-covid-2022.xlsx* (84 filas, ~14 KB) lleva un seguimiento epidemiológico semanal con las siguientes variables:

- **Año** y **Semana** (numeración propia desde Semana 1).
- **Mes** y **Periodo** (rango de fechas, ej. "26 al 02").
- **Positivos**: casos confirmados nuevos en la semana.
- **Recuperados**: altas epidemiológicas.
- **En tratamiento**: casos activos al cierre.
- **Total**: stock acumulado al cierre semanal.
- **Fallecidos**: bajas por la enfermedad.

Es el dataset más sencillo del portal, pero permite reconstruir la curva epidémica completa del Municipio durante los meses críticos.

## Posibles análisis

Con esta granularidad semanal por categoría se puede:

1. **Reconstruir curvas epidémicas** (positivos por semana, casos activos, fallecidos acumulados).
2. **Calcular letalidad municipal** (Fallecidos / Positivos acumulados).
3. **Identificar olas** (alpha, delta, ómicron) por velocidad de crecimiento de positivos.
4. **Cruzar** con calendarios de medidas (cuarentenas, fases) y calendario de vacunación provincial para análisis de efectividad.

## Limitaciones

- El dataset llega hasta **2022**: post-pandemia, la vigilancia epidemiológica continuó pero no se publicó como datos abiertos en el portal municipal.
- No hay datos de **vacunación** local (la provincia administra esa serie).
- No se publican **casos por distrito** ni por **grupo de edad/sexo** — sólo agregados departamentales semanales.
- El relevamiento está hecho por la Subsecretaría de Gestión del Talento Humano, lo que sugiere que cubre principalmente al **personal municipal** y no a la población general — aunque el dataset no aclara explícitamente esa cobertura.

## Datasets disponibles

Informe Covid Municipal (#67).

## Fuente

Portal oficial: <https://datos.lujandecuyo.gob.ar>. Subsecretaría de Gestión del Talento Humano, Municipalidad de Luján de Cuyo.
"""

# Escribir todos
for fname, content in R.items():
    fp = REPORTS_DIR / fname
    fp.write_text(content, encoding='utf-8')
    print(f"  written: {fname} ({len(content)} chars)")

print(f"\nTotal: {len(R)} reports")
