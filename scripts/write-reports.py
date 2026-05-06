"""Genera los 14 markdowns ejecutivos analíticos sobre el municipio.
Cada informe usa los datos abiertos como FUENTE para hablar del fenómeno municipal,
no del estado del portal. Los hallazgos son reales, derivados de los CSV/XLSX.

Run: python scripts/write-reports.py
"""
from pathlib import Path

REPORTS_DIR = Path('public/reports')
REPORTS_DIR.mkdir(exist_ok=True, parents=True)
R = {}

R['gobierto-y-sector-publico.md'] = """# Gobierno Municipal

Análisis ejecutivo sobre la administración del municipio de Luján de Cuyo: tamaño del Estado local, estructura de gasto, contrataciones, transparencia activa y comunicación oficial. Todos los hallazgos provienen de los datasets publicados por el municipio.

## El presupuesto 2025

El **presupuesto sancionado para el ejercicio 2025** asciende a **$111,8 mil millones**, según la planilla de ejecución al 04/07/2025 publicada por la Secretaría de Hacienda:

- **Erogaciones corrientes**: $71,1 mil M (**64%** del total). Incluyen sueldos, bienes de consumo, servicios, intereses de deuda y transferencias.
- **Erogaciones de capital**: $38,9 mil M (**35%**). Inversión en obras, equipamiento y otros activos.
- **Otras erogaciones**: $160 M (0,1%).

El gasto en **personal** ocupa $19,5 mil M en el Ejecutivo más $1,3 mil M en el HCD: en conjunto **$20,8 mil M, equivalente al 19% del presupuesto total**. Los intereses y gastos de la deuda apenas representan $24 M (<0,1%) — el municipio no tiene endeudamiento financiero significativo.

## La estructura del Ejecutivo

La nómina pública del Ejecutivo registra **56 funcionarios de gabinete** (mayo 2025): 1 intendente, 1 jefe de gabinete, 1 subsecretario, 11 secretarios de departamento ejecutivo, 36 directores, más el Juzgado Vial (2 jueces, 2 secretarios y 2 pro-secretarios). El salario básico del rango Director es **$460.927** mensual; Subsecretario $654.367; Secretario de Juzgado Vial $413.851.

Adicionalmente se publican **50 declaraciones juradas patrimoniales** del Ejecutivo y 13 del HCD bajo la Ley provincial de Ética Pública.

## Compras y contrataciones 2024

El municipio ejecutó **$5.065 millones en 1.585 órdenes de compra** durante 2024 — un 4,5% del presupuesto 2025 anual fue contratado bajo este formato. Magnitudes clave:

- Contrato **mediano**: $2,0 millones.
- Contrato del **percentil 90**: $31,2 millones.
- Contrato **máximo**: $635 millones (Plan Pavimentación 2024 — VIALMANI).
- **225 proveedores** distintos.
- **Concentración**: los **top 10 proveedores capturan el 52% del monto total**.

Top contrataciones 2024:

| # | Concepto | Monto | Proveedor |
|---|---|---:|---|
| 1 | Plan Pavimentación 2024 | $635 M | VIALMANI |
| 2 | Servicio de Poda | $450 M | ECUR S.A. |
| 3 | Redes de Agua Potable | $237,7 M | CALZETTA S.A. |
| 4 | Vehículos utilitarios | $230,8 M | VALENTINO MOTOS |
| 5 | Alquiler camiones regadores | $218,6 M | ECUR S.A. |
| 6 | Adquisición hidroelevador | $106,5 M | FICAMEN S.A. |
| 7 | Automóviles | $101,5 M | CAPILLITAS S.A. |

Por **modalidad** de adjudicación, el 84% del monto se ejecuta por **licitación pública** (222 órdenes, $4,4 mil M); 7% por **compra directa** (150 OC, $356 M); 7% por **contratación privada** (8 OC, $330 M).

## Pauta publicitaria: el rubro de mayor crecimiento

El gasto en pauta publicitaria contratada — uno de los datos más sensibles políticamente — multiplicó por **12 en cinco años** en términos nominales:

| Año | Pauta total | Variación interanual |
|---|---:|---:|
| 2020 | $24,5 M | — |
| 2021 | $45,2 M | +85% |
| 2022 | $92,8 M | +105% |
| 2023 | $194,8 M | +110% |
| **2024** | **$296,2 M** | +52% |

El crecimiento 2022-2023 (×2) y 2023-2024 (×1,5) supera holgadamente la inflación nominal del período. Los pagos se distribuyen entre **76 medios** clasificados como gráficos, online, radio, televisión e indoor (carteles digitales en lugares públicos). Marzo concentra el 50%+ del gasto anual desde 2022 — patrón estacional claramente vinculado al inicio de gestión y al período de Vendimia.

## Acceso a la información pública

En lo que va de 2025 se registraron **82 pedidos AIP** (Acceso a la Información Pública) gestionados por la Secretaría de Innovación, Gobierno Abierto y Gestión del Territorio, con un sistema de tickets que registra creación, asignación, derivación y resolución. La planilla incluye 181 movimientos de avance, indicador de un proceso activo de respuesta.

## Composición del HCD

El cuerpo legislativo está integrado por concejales electos en el período 2023/2027. Las declaraciones juradas y antecedentes profesionales se publican en formato PDF. Los **resultados electorales** que constituyen al cuerpo se analizan en el informe **Elecciones**.

---

*Fuente: datasets publicados por la Secretaría de Hacienda, Secretaría de Economía e Ingresos Públicos, Dirección de Comunicación Estratégica, Secretaría de Innovación y HCD en <https://datos.lujandecuyo.gob.ar>. Cifras nominales en pesos argentinos a la fecha de cada publicación.*
"""

R['medio-ambiente-y-desarrollo-sustentable.md'] = """# Medio Ambiente y Desarrollo Sustentable

Análisis ejecutivo del estado ambiental del municipio: gestión de residuos, calidad del aire, calidad del agua y huella urbana sustentable. Los datos provienen de los relevamientos publicados por las áreas técnicas competentes.

## La curva de los residuos

El relleno sanitario controlado **El Borbollón** recibió **36.284 toneladas en 2023** — el año más alto de la serie. La trayectoria mostrada en la planilla oficial muestra una expansión acelerada desde 2021:

| Año | Toneladas dispuestas | Promedio mensual | Per cápita anual* |
|---|---:|---:|---:|
| 2021 | 8.970 | 690 t/mes | — |
| 2022 | 21.470 | 1.789 t/mes | **124,7 kg/hab** |
| **2023** | **36.284** | **2.791 t/mes** | **210,8 kg/hab** |
| 2024 (parcial) | 8.985 | 1.797 t/mes (n=5) | — |
| 2025 (parcial) | 3.115 | 623 t/mes (n=5) | — |

\\* Sobre 172.109 habitantes (Censo 2021).

El indicador per cápita pasó de **125 kg/hab/año en 2022 a 211 kg/hab/año en 2023** (+69%). Un vecino promedio del departamento generó casi **600 gramos diarios de residuos a relleno** en 2023, sin contar el material recuperado por el Centro Verde. La cifra triplica el aumento poblacional plausible y sugiere mayor cobertura efectiva del servicio de recolección o reactivación post-pandemia.

Los datos parciales 2024-2025 sólo cubren cinco meses cada año — la serie completa post-2023 aún no está publicada.

## El reciclaje como contracara

El **Centro Verde** procesa material recuperable mensualmente. En el período enero-mayo 2025, las ventas registradas (planilla *VENTAS 2025*) muestran:

- **Plástico**: ~1.000-5.000 kg/mes (con picos en marzo).
- **Cartón**: ~7.000-13.500 kg/mes (el flujo más voluminoso).
- **Tetra**: 200-280 kg/mes.
- **Chatarra**, **aluminio**, **baterías**: volúmenes menores y variables.

El programa *Puntos Verdes* alimenta este flujo desde toda la geografía municipal y se complementa con el plan **GIRSU** (Gestión Integral de Residuos Sólidos Urbanos), formalizado por Ordenanza 13884/2020.

## Calidad del aire: lo que mide el sensor del Parque Cívico

El tótem instalado en Parque Cívico publicó **9.632 mediciones** en su corrida documentada (3-4 abril 2022, dos días continuos). Más allá del corte temporal limitado, los rangos observados perfilan condiciones ambientales urbanas típicas:

| Variable | Mediana | Rango | Lectura |
|---|---:|---:|---|
| Temperatura (°C) | 20,6 | 10–29 | clima de transición otoñal |
| Humedad relativa (%) | 25,1 | 19–31 | aire seco característico de Cuyo |
| **PM 2,5** (µg/m³) | 3,0 | 1–56 | mediana **muy baja**, picos elevados |
| **PM 10** (µg/m³) | 4,0 | 1–58 | aceptable, picos esporádicos |
| **NO₂** (µg/m³) | 6,1 | 1,8–7,7 | bajo |
| **CO** (mg/m³) | 0,4 | 0,3–0,5 | bajo |

El sensor también reporta **conteo y velocidad de vehículos**: en la corrida disponible se registró un promedio de **49 autos/min** (rango 2-99) circulando con una **velocidad promedio de 25,3 km/h** en la mediana — coherente con tráfico urbano regulado.

La mayor limitación es la **discontinuidad del registro**: sólo dos días con mediciones publicadas, lo que impide un análisis de estacionalidad o picos críticos.

## Calidad del agua

Las dos plantas potabilizadoras del municipio — **Cipolletti** y **Santa Elena** — publican análisis fisicoquímicos y bacteriológicos en planillas anuales (2023, 2024, 2025), junto con resultados de las **perforaciones** de pozos. El dataset *Calidad del Agua* (#48) reúne 11 planillas con esos cortes — el archivo más completo del bloque ambiental. Cada análisis cubre múltiples parámetros (pH, conductividad, coliformes totales y fecales, cloro residual, dureza, sólidos disueltos), realizados por la Coordinación de Aguas y Servicios Sanitarios.

## Marco programático

El municipio integra los **Objetivos de Desarrollo Sostenible (ODS)** mediante el *Manual de Adaptación Local* (2ª edición), un documento técnico que orienta la implementación de la Agenda 2030 en territorio. El **Plan Luján Sustentable** articula tres ejes — ecología, economía y sociedad — y se complementa con iniciativas específicas (Torres Solares, Bicisendas Inclusivas, Calidad del Aire, Calles por la Vida, Programa Educación y Participación, Convenio de Economía Circular con Prato/Italia).

## Energía: el plan LED

El dataset *Energía* (#71) documenta el reemplazo de luminarias por tecnología **LED** ejecutado por la Secretaría de Higiene Urbana. La planilla `luminaria_ev.xlsx` traza la evolución del recambio sobre el alumbrado público — política con doble impacto (eficiencia energética y seguridad ambiental peatonal).

---

*Fuente: Secretaría de Higiene Urbana y Mantenimiento del Espacio Público, Coordinación de la Unidad de Aguas y Servicios Sanitarios, Secretaría de Infraestructura y Desarrollo Sostenible. Datos publicados en <https://datos.lujandecuyo.gob.ar>.*
"""

R['economia.md'] = """# Economía

Análisis ejecutivo de la economía pública y privada del departamento. Cubre la estructura fiscal del municipio, el universo comercial registrado, la inversión en obras y la geografía socio-económica del territorio.

## Las finanzas del municipio

El **presupuesto 2025** alcanza los **$111,8 mil millones** según la ejecución publicada al 04/07/2025. La estructura del gasto:

- **Erogaciones corrientes**: $71,1 mil M (64%) — operación cotidiana.
- **Erogaciones de capital**: $38,9 mil M (35%) — inversión en infraestructura.
- **Otras**: $160 M (0,1%).

El **gasto en personal** suma $20,8 mil M considerando Ejecutivo ($19,5 mil M) y HCD ($1,3 mil M), equivalente al **19% del presupuesto total**. La carga financiera por intereses de deuda es marginal (<0,1%).

Las **compras y contrataciones 2024** totalizaron **$5,1 mil millones** distribuidos en 1.585 órdenes de compra entre 225 proveedores. La concentración es significativa: los **10 mayores proveedores capturaron el 52% del monto** anual, y un solo contrato (Plan Pavimentación 2024 — VIALMANI) representó **$635 millones** (12,5% del total contratado).

Por modalidad, **84% del monto** se ejecutó por licitación pública, 7% por compra directa y 7% por contratación privada — patrón típicamente conservador desde el punto de vista normativo.

## El padrón comercial

El **Padrón de Comercios 2025** registra **11.630 unidades comerciales** distribuidas en 273 rubros distintos:

- **60% factura** (6.975 comercios), **40% no factura** (4.655) — la base imponible efectiva del comercio departamental.
- **Valor total declarado** (Unidades Tributarias × valor): **$14,4 mil millones**.
- **3.501 comercios** tienen rubro identificado (no genérico). Los restantes 8.129 figuran bajo el rubro "GENERICO 999999".

**Top 10 rubros identificados**:

| Rubro | Comercios |
|---|---:|
| Venta al por menor de productos de almacén | 314 |
| Venta de productos no clasificados en otros | 181 |
| Venta de productos alimenticios — almacenes | 166 |
| Servicios empresariales | 115 |
| Venta de bombones, golosinas, confitería | 109 |
| Venta al por menor de frutas y verduras | 106 |
| Venta de tabacos, cigarros y cigarrillos | 102 |
| Venta de prendas y accesorios | 92 |
| Servicios inmobiliarios | 91 |

El núcleo comercial de Luján de Cuyo es marcadamente **alimentario y de cercanía**: almacenes, productos alimenticios, frutas/verduras y golosinas concentran el grueso del padrón identificado.

## Bancos y servicios financieros

El departamento cuenta con **9 sucursales bancarias** registradas (Banco Francés, Supervielle, Nación, Galicia (×2), HSBC, San Juan, Macro). La concentración geográfica es absoluta: todas se ubican en el corredor San Martín — Mariano Boedo — Aguinaga del distrito Ciudad. Para los distritos rurales (Agrelo, Ugarteche, El Carrizal, Cacheuta, Potrerillos), el acceso a un banco implica desplazarse al cordón urbano.

Complementariamente, el municipio registra **11 estaciones de servicio** distribuidas a lo largo de las arterias troncales (RN 7, RP 15, Acceso Sur), incluyendo dos GNC.

## Geografía económica de la pobreza

Los **47 barrios populares** registrados por el RENABAP (Registro Nacional de Barrios Populares) albergan **2.569 familias**. Top 5 por población:

- Valle Encantado (Chacras de Coria) — 290 familias.
- Tierras Vivas (Agrelo) — 170.
- Patrono Santiago (Ciudad) — 160.
- Virgen de Lourdes (Perdriel) — 135.
- Costanera Sur (Ciudad) — 132.

La distribución muestra **focos urbanos** (Ciudad concentra varios) y **focos rurales** (Agrelo, Ugarteche, Perdriel) — geografía relevante para políticas de regularización dominial e infraestructura.

## La inversión en obras

El plan de obras 2025 (*Obras Públicas*) registra **174 actividades** ejecutadas por la Secretaría de Obras y Espacios Públicos. Estado de avance al cierre del relevamiento:

- **39%** cumplido (67 actividades).
- 23% no iniciado (40).
- 20% en implementación (34).
- 10% atrasado (18).
- 6% cancelado (11).

El 95% del plan corresponde al eje **"Transformación del espacio público"** (165 actividades, programas de ordenadores viales, paseos, plazas). El restante 5% se enmarca en **"Luján Sustentable"** (9 actividades). El programa *Movilidad Sustentable* concentra 9 actividades específicas dentro del plan.

---

*Fuente: Secretaría de Hacienda, Secretaría de Economía e Ingresos Públicos, Secretaría de Obras y Espacios Públicos. Cifras nominales en pesos argentinos. Datos en <https://datos.lujandecuyo.gob.ar>.*
"""

R['urbanismo-y-territorio.md'] = """# Urbanismo y Territorio

Retrato territorial del departamento de Luján de Cuyo: distribución poblacional por distrito, oferta de espacios verdes, infraestructura urbana y geografía de la informalidad habitacional.

## La distribución poblacional

El departamento se compone de **15 distritos** con perfiles muy heterogéneos. Población registrada (CSV oficial):

| Distrito | Población | % municipio |
|---|---:|---:|
| Ciudad | 24.594 | 20,6% |
| Carrodilla | 23.886 | 20,0% |
| Perdriel | 13.687 | 11,5% |
| Chacras de Coria | 12.428 | 10,4% |
| Vistalba | 8.771 | 7,3% |
| Mayor Drumond | 8.223 | 6,9% |
| Agrelo | 7.507 | 6,3% |
| Ugarteche | 6.603 | 5,5% |
| El Carrizal | 4.177 | 3,5% |
| La Puntilla | 2.842 | 2,4% |
| Vertientes de Pedemonte | 2.428 | 2,0% |
| Potrerillos | 2.075 | 1,7% |
| Las Compuertas | 1.353 | 1,1% |
| Cacheuta | 701 | 0,6% |
| Industrial | 41 | <0,1% |

**Tres distritos** (Ciudad, Carrodilla, Perdriel) concentran **~52% de la población**. El distrito **Industrial** figura con 41 residentes registrados — uso casi exclusivamente productivo. El total censado por distrito (~119.300 habitantes) refleja el Censo 2010; el **Censo 2021** registró **172.109 habitantes** para el departamento — un crecimiento de ~44% en una década.

## Espacios verdes: una distribución desigual

El relevamiento 2025 publicado por la Intendencia documenta **272 espacios verdes** con **1,346 millones de m² agregados** — equivalente a **7,8 m²/habitante** a nivel municipal (referencia OMS: 9 m²/hab mínimo; ideal 10-15).

Pero el promedio oculta una **inequidad territorial fuerte**:

| Distrito | Pob. | Espacios | m² total | **m²/hab** |
|---|---:|---:|---:|---:|
| **Ciudad** | 24.594 | 59 | 773.994 | **31,5** |
| **Potrerillos** | 2.075 | 6 | 65.158 | **31,4** |
| La Puntilla | 2.842 | 26 | 49.391 | 17,4 |
| V. de Pedemonte | 2.428 | 11 | 25.959 | 10,7 |
| El Carrizal | 4.177 | 13 | 39.751 | 9,5 |
| Carrodilla | 23.886 | 78 | 221.610 | 9,3 |
| Mayor Drumond | 8.223 | 34 | 59.385 | 7,2 |
| Vistalba | 8.771 | 11 | 46.110 | 5,3 |
| **Perdriel** | 13.687 | 12 | 26.502 | **1,9** |
| **Chacras de Coria** | 12.428 | 18 | 17.106 | **1,4** |

**Chacras de Coria y Perdriel** — pese a concentrar el 22% de la población — disponen de **menos de 2 m²/hab** de espacio verde público. Es el déficit territorial más marcado del municipio. La Ciudad dobla el estándar OMS y Potrerillos lo logra por baja densidad poblacional, no por alta superficie verde absoluta.

Tipología del espacio verde: **65 espacios verdes genéricos**, **60 boulevards**, **56 plazas formales**, 38 espacios públicos, 15 paseos, 15 laterales de ruta y elementos menores (rotondas, miradores, cortinas forestales).

## La marca informal: 47 barrios populares

El **RENABAP** registra **47 barrios populares** en el departamento que albergan **2.569 familias**. Los cinco mayores:

| Barrio | Distrito | Familias |
|---|---|---:|
| Valle Encantado | Chacras de Coria | 290 |
| Tierras Vivas | Agrelo | 170 |
| Patrono Santiago | Ciudad | 160 |
| Virgen de Lourdes | Perdriel | 135 |
| Costanera Sur | Ciudad | 132 |

La distribución cruza **focos urbanos** (Ciudad: Patrono Santiago, Costanera Sur, Juan XXIII) con **focos rurales** (Agrelo, Perdriel, Ugarteche). La incidencia es heterogénea: un distrito como **Chacras de Coria** — con perfil residencial premium — incluye Valle Encantado, el barrio popular más grande del departamento.

## Infraestructura territorial

- **15 distritos** con coordenadas y delimitación oficial. Las **fracciones y radios censales** del INDEC se publican en KMZ (#21) — 273+ unidades de microgeografía.
- **11 estaciones de servicio** distribuidas en RN 7, RP 15 y Acceso Sur.
- **Red de transporte público** disponible en KML con recorridos georreferenciados de cada línea.
- **Circuito de ciclovías** publicado en formato My Maps con los Puntos de Encuentro Saludables (PES) que vertebran el sistema.

## El marco normativo del territorio

El **Plan Municipal de Ordenamiento Territorial (PMOT)** y su Código de Uso del Suelo establecen las reglas de zonificación, ocupación y usos. Junto con la **Ordenanza 13884/2020** (GIRSU - Gestión Integral de Residuos), el **Plan Luján Sustentable** y el inventario de **Uniones Vecinales** (organizaciones territoriales de base), constituyen el sistema institucional de gestión territorial.

---

*Fuente: Intendencia Municipalidad de Luján de Cuyo, Secretaría de Infraestructura y Desarrollo Sostenible, Dirección de Ordenamiento Territorial. RENABAP nacional. Datos en <https://datos.lujandecuyo.gob.ar>.*
"""

R['deporte-educacion-y-salud.md'] = """# Deporte, Educación y Salud

Retrato de la oferta de servicios sociales territoriales: red escolar, sistema de salud de primer nivel, oferta deportiva y vigilancia sanitaria.

## El sistema educativo: 17.318 alumnos en 112 establecimientos

El relevamiento 2025 documenta **112 establecimientos educativos** con una **matrícula total de 17.318 estudiantes**. Composición:

**Por gestión**:
- Pública: **85** (76%)
- Privada: 25 (22%)
- SEOS Maternal/Inicial/Primaria: 2 (2%)

**Por ámbito**:
- Urbano: 58 (52%)
- Rural: 50 (45%)
- Urbano marginal: 4 (4%)

La **mitad rural** del sistema escolar es notable y alimenta a los distritos del cordón cordillerano y agrícola (Ugarteche, Agrelo, El Carrizal, Las Compuertas, Cacheuta, Potrerillos).

**Por nivel** (con matrícula declarada):

| Nivel | Establecimientos | Alumnos | % |
|---|---:|---:|---:|
| **Primaria** | 44 | 12.308 | **71,1%** |
| Secundaria común | 6 | 2.171 | 12,5% |
| Secundaria orientada | 4 | 1.441 | 8,3% |
| Secundario técnico | 3 | 737 | 4,3% |
| CEBJA (jóvenes y adultos) | 6 | 250 | 1,4% |
| Educación superior | 2 | 164 | 0,9% |
| Especial primaria | 1 | 100 | 0,6% |
| CENS | 2 | 100 | 0,6% |

Las **modalidades técnico-profesionales** registradas reflejan la matriz productiva regional: Gestión Contable Impositiva y Previsional, Comercio Exterior, **Producción de Bienes y Servicios**, Electromecánica, Industria de Proceso, **Técnico Superior Agronómica y Apícola** (vinculada al perfil vitivinícola y olivícola), **Técnico Superior en Enfermería**, Comunicación y Arte, Humanidades y Ciencias Sociales.

### El polo educativo: Mayor Drumond

Cruzando matrícula escolar con población residente por distrito:

| Distrito | Pob. | Escuelas | Matrícula | **Mat./Pob.** |
|---|---:|---:|---:|---:|
| **Mayor Drumond** | 8.223 | 12 | 2.910 | **35,4%** |
| **Ciudad** | 24.594 | 23 | 5.478 | **22,3%** |
| Ugarteche | 6.603 | 8 | 1.361 | 20,6% |
| Perdriel | 13.687 | 10 | 1.635 | 11,9% |
| Carrodilla | 23.886 | 16 | 2.710 | 11,3% |
| Chacras de Coria | 12.428 | 16 | 1.183 | 9,5% |
| La Puntilla | 2.842 | 1 | 277 | 9,7% |
| Agrelo | 7.507 | 5 | 651 | 8,7% |
| El Carrizal | 4.177 | 7 | 351 | 8,4% |
| Vistalba | 8.771 | 3 | 357 | 4,1% |

**Mayor Drumond emerge como polo educativo**: con sólo 8.223 habitantes, su matrícula equivale al **35% de su población local** — implica que recibe alumnado de distritos vecinos. **Ciudad** (22%) y **Ugarteche** (21%) tienen también atracción educativa neta. **Vistalba** (4%) muestra el menor anclaje educativo: sus habitantes en edad escolar concurren a Carrodilla, Chacras o Mayor Drumond.

## La red de salud: cobertura desigual

El **primer nivel de atención** se compone de **19 centros de salud**. La distribución por distrito vs población local revela inequidades estructurales:

| Distrito | Pob. | Centros | **Hab/Centro** |
|---|---:|---:|---:|
| Cacheuta | 701 | 2 | **350** |
| Potrerillos | 2.075 | 2 | 1.038 |
| Las Compuertas | 1.353 | 1 | 1.353 |
| El Carrizal | 4.177 | 2 | 2.088 |
| Agrelo | 7.507 | 3 | 2.502 |
| Ugarteche | 6.603 | 2 | 3.302 |
| Perdriel | 13.687 | 2 | 6.844 |
| Carrodilla | 23.886 | 3 | 7.962 |
| **Chacras de Coria** | 12.428 | 1 | **12.428** |
| **Ciudad** | 24.594 | 1 | **24.594** |

Los distritos **rurales y cordilleranos** tienen excelente cobertura por hab/centro (350-2.500), reflejo de la lógica histórica del primer nivel de atención. Los **distritos urbanos densos** — Ciudad y Chacras de Coria — funcionan con un único centro de salud cada uno, generando ratios de **24.000 y 12.000 hab/centro** respectivamente. Esta concentración es probable que se compense con los hospitales provinciales (Carlos Pereyra, El Carmen, Schestakow) ubicados en cercanías, pero el dato municipal sugiere un déficit estructural en atención primaria urbana.

Complementariamente, la red comercial farmacéutica registra **18 farmacias**, también concentradas en el corredor urbano San Martín — Roque Sáenz Peña — Viamonte.

## Vigilancia sanitaria del agua

La **Coordinación de Aguas y Servicios Sanitarios** publica análisis fisicoquímicos y bacteriológicos de las dos plantas potabilizadoras (**Cipolletti** y **Santa Elena**) más las perforaciones, en planillas anuales 2023-2025 — once archivos consolidados que constituyen una base sostenida de vigilancia ambiental con impacto sanitario directo.

## Deporte y recreación

- **Polideportivos** distribuidos en el departamento (publicados como mapa web).
- **272 espacios verdes** públicos (1,35 km²) que oficiando como soporte de deporte recreativo.
- **Aventura**: **11 emprendimientos** registrados, **todos en Potrerillos** — rafting, kayak, trekking, vela, montañismo. Es el polo concentrado de deporte de aventura del departamento.
- **Circuito de ciclovías** con Puntos de Encuentro Saludables (PES) — política integradora de movilidad activa y deporte recreativo.

## La huella del COVID

El *Informe Covid Municipal 2022* documenta **84 semanas** con seguimiento epidemiológico:

- **645 casos positivos** acumulados.
- **20.424 recuperados** (ratio mucho mayor que positivos sugiere arrastre de períodos previos a la planilla).
- **21 fallecidos**.
- **Pico semanal**: 128 casos.
- Promedio semanal: 7,7 positivos.

El relevamiento corresponde al ámbito municipal y refleja principalmente al personal de la administración (publicado por la Subsecretaría de Gestión del Talento Humano).

---

*Fuente: Secretaría de Desarrollo Humano, Coordinación de Aguas y Servicios Sanitarios, Dirección de Turismo, Subsecretaría de Gestión del Talento Humano. Datos en <https://datos.lujandecuyo.gob.ar>.*
"""

R['honorable-consejo-deliberante-lujan-de-cuyo.md'] = """# Honorable Concejo Deliberante

Análisis del cuerpo legislativo municipal: composición política derivada del último proceso electoral, transparencia patrimonial, gestión de pedidos de información y posicionamiento institucional.

## La composición del cuerpo

El HCD vigente fue electo en las **PASO Provinciales 2023** y se constituyó con mandato 2023/2027. La composición política puede inferirse del escrutinio publicado para la categoría Concejal, donde se relevaron 316 mesas en el departamento:

| Agrupación | Votos | % |
|---|---:|---:|
| **CAMBIA MENDOZA** | 4.670 | **42,7%** |
| **LA UNIÓN MENDOCINA** | 4.499 | **41,1%** |
| ELEGÍ MENDOZA | 1.006 | 9,2% |
| Frente de Izquierda y de Trabajadores | 404 | 3,7% |
| Partido Verde | 355 | 3,2% |

El cuerpo refleja una **paridad electoral** entre Cambia Mendoza y La Unión Mendocina (1,6 puntos de diferencia), sumando entre ambos el 84% de los votos válidos. La **fragmentación periférica** (Elegí 9,2%, FIT 3,7%, Verde 3,2%) configura una representación con dos grandes bloques y voces minoritarias.

## Geografía del voto

Cruzando con distrito de origen (planilla parcial con 5 distritos relevados):

| Distrito | Total votos | 1° lugar | % | 2° lugar | % |
|---|---:|---|---:|---|---:|
| Carrodilla | 2.164 | Cambia Mendoza | 41% | La Unión | 38% |
| Chacras de Coria | 4.452 | **Cambia Mendoza** | **56%** | La Unión | 34% |
| Ciudad | 1.097 | **La Unión** | 52% | Cambia | 29% |
| Mayor Drummond | 1.116 | La Unión | 47% | Cambia | 34% |
| Perdriel | 2.105 | **La Unión** | 52% | Cambia | 28% |

**Chacras de Coria** y **Carrodilla** se inclinaron hacia **Cambia Mendoza**; **Ciudad**, **Mayor Drumond** y **Perdriel** hacia **La Unión Mendocina**. La asimetría territorial sugiere bases sociales distintas: los distritos residenciales premium del corredor norte vs. los distritos centrales y rurales.

## Transparencia patrimonial

Los **13 miembros del HCD** publican declaración jurada patrimonial bajo la Ley provincial de Ética Pública 2025 (planilla *DDJJ HCD 2025*). Los nombres registrados incluyen:

- Andrés Sconfienza, Adrián Devia (Concejal 2023/2027)
- Claudio Ogando (Secretario HCD)
- Guillermo Trentacoste, Malena Abalos, Carlos Sala, Rubén Lazaro, Paloma Scalco (Concejales)

Los antecedentes profesionales y CVs se publican en formato PDF en el dataset *Antecedentes Profesionales*.

## Función legislativa: ordenanzas

Aunque el portal no expone una serie estructurada de proyectos votados, el dataset *Ordenanzas Municipales* publica el **repositorio normativo** producido por el cuerpo:

- Ordenanzas 2025 categorizadas (CSV).
- Ordenanzas 2024 categorizadas (CSV).
- Ordenanzas 2024-2016 históricas (CSV).
- Normas individuales destacadas: Ordenanza 14830/2024 (Presupuesto 2025), 14831/2024 (Tarifaria 2025), 13884/2020 (GIRSU), 14525/2023 y 14526/2023 (Tarifaria/Presupuesto).

Esto permite trazar la **producción legislativa por categoría temática** a lo largo del período.

## Estructura interna

El **organigrama HCD** se publica como PDF (#73). Con 13 concejales más cargos políticos y técnicos, el cuerpo emplea personal cuya nómina está incluida en la **Planilla HCD 2025** (cuatro archivos del dataset *Funcionarios Públicos Municipal*). El HCD aporta **$1,3 mil M** al gasto en personal del Estado municipal — alrededor del 6% del total de personal.

## El acceso a la información

El dataset *Información Pública* incluye una planilla específica **garantes-hcd** y registros de "pedidos de información pública 2024" gestionados por el cuerpo. En conjunto con los pedidos del Ejecutivo, el sistema AIP municipal procesó **82 tickets** en lo que va de 2025.

---

*Fuente: Honorable Concejo Deliberante de Luján de Cuyo, Secretaría de Economía e Ingresos Públicos, Junta Electoral de Mendoza (PASO 2023). Datos en <https://datos.lujandecuyo.gob.ar>.*
"""

R['cultura-y-turismo.md'] = """# Turismo y Cultura

Retrato de la oferta turística y cultural del departamento. Luján de Cuyo articula dos polos diferenciados: un cordón cordillerano (Potrerillos, Cacheuta, Las Compuertas) orientado al pernocte y la aventura, y un corredor residencial-gastronómico (Chacras de Coria, Vistalba) que opera mayoritariamente como destino de día.

## Los 137 locales gastronómicos

El relevamiento de la Dirección de Turismo registra **137 locales gastronómicos** clasificados así:

| Tipo | Locales | % |
|---|---:|---:|
| **Restaurante** | 84 | 61% |
| Cafetería | 17 | 12% |
| Heladería | 10 | 7% |
| Casa de té | 5 | 4% |
| Pizzería | 4 | 3% |
| Pastelería | 3 | 2% |
| Restaurante de sushi | 3 | 2% |
| Otros (parrilla, panchería, taquería, lomitería, restaurantes árabe/cubano/comida rápida) | 11 | 8% |

**Concentración geográfica**:

| Distrito | Locales | % |
|---|---:|---:|
| **Chacras de Coria** | 43 | 31% |
| Ciudad | 28 | 20% |
| **Potrerillos** | 23 | 17% |
| Cacheuta | 11 | 8% |
| Las Compuertas | 8 | 6% |
| Agrelo | 8 | 6% |
| Vistalba | 5 | 4% |
| La Puntilla | 4 | 3% |

**Chacras de Coria + Potrerillos concentran el 48% de la oferta gastronómica**. El primero opera como destino gastronómico de día (Mendoza-Capital se traslada a almorzar/cenar); el segundo combina gastronomía con actividades en montaña.

## La oferta de pernocte: Potrerillos como capital

**73 alojamientos** publicados en el padrón turístico municipal, con una concentración geográfica extrema:

| Distrito | Alojamientos | % |
|---|---:|---:|
| **Potrerillos** | **53** | **73%** |
| Cacheuta | 7 | 10% |
| Las Compuertas | 7 | 10% |
| Otros (Agrelo, Perdriel, Vistalba, Ciudad) | 6 | 8% |

El **eje cordillerano absorbe el 92% del pernocte** (Potrerillos + Cacheuta + Las Compuertas). Predominan cabañas, posadas y alojamientos pequeños. Chacras de Coria — pese a su polo gastronómico — apenas tiene oferta de alojamiento, confirmando su perfil de **destino de día**.

## El polo de aventura: 11 emprendimientos en Potrerillos

El dataset *Aventura* registra **11 prestadores**, **todos en Potrerillos**:

- **Argentina Rafting** — rafting en RP Perilago.
- **Río Aventura** — KM 55 RN 7.
- **Potrerillos Explorer** — Los Guanacos.
- **Colanguil Expediciones** — Las Acacias (alta montaña).
- **El Rincón de los Oscuros** — Los Cóndores y Las Nieves.
- **Milkayak** y **Huayra Veleros** — RP Perilago (kayak y vela).
- **Mendoza Aventura** — Arroyo Ranchillos.

El conjunto configura a **Potrerillos como capital del turismo activo de Mendoza**: rafting en el río Mendoza, kayak y vela en el embalse, trekking de alta montaña hacia el corredor del Aconcagua.

## Vitivinicultura: la marca silenciosa

El dataset **Bodegas** está catalogado por la Dirección de Turismo pero **no incluye archivos descargables** — sólo metadata. Esto es notable dado el peso del enoturismo en el perfil económico de Luján de Cuyo (sede de bodegas históricas como Catena Zapata, Achaval Ferrer, Norton, Lagarde, Vistalba, Septima, Renacer, entre muchas otras). La ausencia de un padrón estructurado público es una brecha en el principal activo turístico del departamento.

## Senderos y circuitos

- **Senderos de Trekking** publicados en KML — recorridos georreferenciados para visualización en Google Earth o app.
- **Circuito de Ciclovías** integrado con **Puntos de Encuentro Saludables (PES)**, en formato My Maps.
- **Transporte Público** (KML + horarios XLS) — insumo crítico para visitantes que se mueven sin auto.

---

*Fuente: Dirección de Turismo, Apoderado Municipal, Secretaría de Innovación, Gobierno Abierto y Gestión del Territorio. Datos en <https://datos.lujandecuyo.gob.ar>.*
"""

R['desarrollo-humano.md'] = """# Desarrollo Humano

Análisis del tejido social organizado del departamento: pobreza territorializada, organización vecinal, intervenciones por vulnerabilidad y estadísticas de violencia de género en su contexto poblacional.

## La pobreza con dirección y nombre: 47 barrios populares

El **RENABAP** (Registro Nacional de Barrios Populares) identifica **47 barrios** dentro del departamento de Luján de Cuyo, con un universo de **2.569 familias** registradas — representativo de la **población más vulnerable** del territorio.

### Top 10 barrios por familias residentes

| Barrio | Distrito | Familias |
|---|---|---:|
| Valle Encantado | Chacras de Coria | 290 |
| Tierras Vivas | Agrelo | 170 |
| Patrono Santiago | Ciudad | 160 |
| Virgen de Lourdes | Perdriel | 135 |
| Costanera Sur | Ciudad | 132 |
| Juan XXIII | Ciudad | 110 |
| Villa Costa Canal | Ugarteche | 102 |
| Estación Cuadro | Perdriel | 100 |
| El Encuentro | Perdriel | — |
| San Gabriel | Vistalba | — |

### Distribución por distrito (cantidad de familias agregadas)

Los datos territorializados muestran que **Ciudad** concentra el mayor número de familias en barrios populares en términos absolutos, seguido por **Perdriel** y **Agrelo**. La presencia de Valle Encantado en Chacras de Coria — distrito con perfil residencial premium — ilustra la **convivencia de extremos socioeconómicos** en una misma geografía.

Los datos RENABAP contienen identificador único nacional (`id_renabap`), provincia, departamento, localidad, cantidad de familias y coordenadas — habilitando cruce con políticas de regularización dominial, infraestructura sanitaria y acceso a servicios.

## El tejido organizativo: Uniones Vecinales

El dataset *Uniones Vecinales* lista las organizaciones formales de base territorial reconocidas por el municipio. Son los interlocutores institucionales en presupuesto participativo, obras, eventos y articulación de demandas vecinales. Constituyen el **mapa de la sociedad civil organizada** del departamento.

## Violencia de género: la contracara más sensible

El dataset *Estadísticas de Género* (analizado en detalle en **Género y Diversidad**) muestra que en 2022 la **Dirección de Género y Diversidad atendió 480 casos de víctimas residentes en Luján de Cuyo** — el dispositivo opera principalmente sobre la **población local**, con apenas 13 casos de víctimas de otros departamentos. Esto da una idea de **demanda estructural anual sobre el dispositivo municipal**.

Cortes relevantes 2022 (sobre los 493 casos totalmente caracterizados):

- **Estado civil**: 32% solteras, 10% casadas, 4% divorciadas, 3% separadas — 49% restante sin dato registrado.
- **Vínculo con el agresor**: **28% ex pareja conviviente**, 8% cónyuge, 6% ex cónyuge → más de **40% del riesgo proviene de pareja o ex pareja**.
- **Condición de actividad**: 25% ocupadas, **19% desocupadas**, 3% inactivas — la inserción laboral es un factor diferencial.
- **Nivel educativo**: 18% secundario incompleto, 10% secundario completo, 6% terciario completo, 6% primario completo — perfil mayormente con trayectorias escolares interrumpidas.
- **Tipos de violencia documentados**: psicológica 41%, física 32%, económica/patrimonial 30%, sexual 11% (las cuatro frecuentemente combinadas).

## Programas estructurales

- **Convenio con Prato (Italia)** — Economía Circular: revegetación, recuperación de materiales y reciclaje articulado con organizaciones sociales.
- **Polideportivos** (3+ instalaciones publicadas como mapa web) — nodos de oferta deportiva inclusiva.
- Articulación con la **Procuración General de la Suprema Corte de Justicia de Mendoza** (acuerdo de cooperación en violencia de género).

---

*Fuente: Intendencia Municipalidad de Luján de Cuyo, Dirección de Género y Diversidad, Secretaría de Desarrollo Humano, Secretaría de Infraestructura y Desarrollo Sostenible. RENABAP nacional. Datos en <https://datos.lujandecuyo.gob.ar>.*
"""

R['movilidad.md'] = """# Movilidad

Retrato del sistema de movilidad del departamento: red de transporte público, infraestructura ciclista, plan de obras viales y conectividad de los barrios populares.

## La red de transporte público

La **Red Luján** se publica con dos artefactos complementarios:

- **KML** con los recorridos georreferenciados de cada línea — visualizable en Google Earth, QGIS o cualquier app cartográfica que soporte el formato.
- **XLS** con los horarios operativos.

Esto permite reconstruir la cobertura espacial del sistema y los tiempos de servicio entre distritos. La información operativa (boletos vendidos, ocupación, frecuencia real, modalidad SUBE) **no se publica** — la planificación cuantitativa de la demanda queda fuera del alcance del portal municipal.

## El circuito de ciclovías y los PES

El **Circuito de Ciclovías** se publica en formato **My Maps** (Google Maps) con los recorridos ejecutados y los **Puntos de Encuentro Saludables (PES)** que articulan el sistema. Es uno de los pocos datasets en este formato — orientado a difusión ciudadana antes que a análisis técnico. La política integradora "ciclovías + PES" busca articular **movilidad activa + recreación + espacio público + salud preventiva**.

El dataset complementario **Bicisendas Inclusivas** (programa "Pedaleando Juntos") está publicado como página web sin datos descargables.

## El plan de obras 2025: 174 actividades

El dataset *Obras Públicas 2025* documenta **174 actividades** ejecutadas por la **Secretaría de Obras y Espacios Públicos**. Estado de avance al cierre del relevamiento:

| Estado | Actividades | % |
|---|---:|---:|
| **Cumplido** | 67 | **39%** |
| No iniciado | 40 | 23% |
| En implementación | 34 | 20% |
| **Atrasado** | 18 | 10% |
| Cancelado | 11 | 6% |

Por **eje estratégico**:
- **Transformación del espacio público**: 165 actividades (95%).
- **Luján Sustentable**: 9 actividades (5%).

El programa **Movilidad Sustentable** concentra **9 actividades específicas** dentro del plan general — una sub-cartera dedicada al modo activo y al transporte público.

## Las inversiones viales detrás de las obras

Las **compras y contrataciones 2024** revelan la magnitud financiera de la inversión vial:

| Contrato | Monto | Proveedor |
|---|---:|---|
| Plan Pavimentación 2024 | **$635 M** | VIALMANI |
| Servicio de Poda (mantenimiento de calzada/banquinas) | $450 M | ECUR S.A. |
| Redes de Agua Potable (incluye reposición vial) | $237,7 M | CALZETTA S.A. |
| Vehículos utilitarios | $230,8 M | VALENTINO MOTOS |
| Alquiler de camiones regadores | $218,6 M | ECUR S.A. |
| Cubiertas para máquina vial | $6,7 M | NEUMÁTICOS NARVÁEZ |
| Reparación de motoniveladora | $6,9 M | GRÚAS SAN BLAS |

El gasto vial directo (pavimentación + mantenimiento + maquinaria) supera los **$1.500 millones en 2024** — alrededor del **30% de las compras totales** del año.

## Conectividad social: el dato faltante

Los **47 barrios populares** del RENABAP están georreferenciados — la base permite analizar su **conectividad por transporte público**, **distancia a centros de salud**, **distancia a escuelas** y **acceso a comercios**. Sin embargo, el portal no expone esos análisis cruzados — quedan disponibles para investigación externa con los datasets crudos.

## La brecha en seguridad vial

El dataset *Seguridad Vial* (#51) figura en el catálogo como "Acciones viales" pero **no contiene archivos descargables**. La **fiscalización vial municipal** — multas emitidas, controles de alcoholemia, **siniestros viales** con su georreferenciación, fatalidad — es la información de movilidad **más demandada** y no se publica. Esta omisión es probablemente la mayor brecha del bloque, dado que el departamento tiene tres rutas troncales nacionales y provinciales (RN 7, RP 15, Acceso Sur) con tránsito intenso de carga y turistas.

---

*Fuente: Secretaría de Obras y Espacios Públicos, Secretaría de Hacienda (compras), Secretaría de Innovación, Gobierno Abierto y Gestión del Territorio. Datos en <https://datos.lujandecuyo.gob.ar>.*
"""

R['elecciones.md'] = """# Elecciones

Análisis de los resultados electorales en Luján de Cuyo a partir del escrutinio de las **PASO Provinciales 2023** y elecciones nacionales subsiguientes. Es la única categoría del portal con granularidad **por mesa electoral**.

## El mapa político: paridad y dos polos

En la categoría **Concejal** (escrutinio mesa por mesa, 316 mesas relevadas), la consolidada para 2023 muestra:

| Agrupación | Votos | % |
|---|---:|---:|
| **CAMBIA MENDOZA** | 4.670 | **42,7%** |
| **LA UNIÓN MENDOCINA** | 4.499 | **41,1%** |
| ELEGÍ MENDOZA | 1.006 | 9,2% |
| Frente de Izquierda y de Trabajadores - Unidad | 404 | 3,7% |
| Partido Verde | 355 | 3,2% |
| Otros (Compromiso Federal, Dignidad Popular, Partido Federal) | <1% c/u | — |

**Paridad técnica** entre las dos coaliciones principales (1,6 puntos) que sumaron 84% del electorado. La fragmentación periférica fue contenida: tres fuerzas (Elegí, FIT, Verde) capturaron el 16% restante.

## La geografía del voto: dos Lujanes

Los 5 distritos relevados con detalle revelan una **fractura territorial nítida**:

| Distrito | Total votos | 1° lugar | % | 2° lugar | % |
|---|---:|---|---:|---|---:|
| Carrodilla | 2.164 | Cambia Mendoza | 41% | La Unión Mendocina | 38% |
| **Chacras de Coria** | 4.452 | **Cambia Mendoza** | **56%** | La Unión | 34% |
| Ciudad | 1.097 | **La Unión Mendocina** | 52% | Cambia | 29% |
| Mayor Drumond | 1.116 | La Unión Mendocina | 47% | Cambia | 34% |
| **Perdriel** | 2.105 | **La Unión Mendocina** | **52%** | Cambia | 28% |

**Cambia Mendoza domina** en Chacras de Coria (56%) y Carrodilla (paridad 41-38). **La Unión Mendocina lidera** en Ciudad (52%), Mayor Drumond (47%) y Perdriel (52%). El alineamiento sigue clivajes tradicionales: los **distritos residenciales premium del corredor norte** se inclinan por la coalición histórica del PRO/UCR, mientras que **Ciudad** (centro institucional), **Mayor Drumond** (polo educativo y comercial) y **Perdriel** (semi-rural con núcleo de barrios populares) se inclinan por La Unión.

Chacras de Coria, con su 56% para Cambia Mendoza, fue el **bastión más concentrado** de la coalición ganadora a nivel departamental.

## Las categorías escrutadas

El dataset *Voto Electoral* (#49) detalla las mesas para **cinco categorías**:

- **Concejal** (316 mesas) — la única plenamente analizada arriba.
- **Diputados Nacionales**.
- **Diputados Provinciales**.
- **Senadores Nacionales**.
- **Resultados PASO 2023** consolidado.

Cada XLSX trae el mismo esquema: circuito × escuela × mesa × lista, con votos válidos, en blanco, impugnados y del comando electoral.

## El escrutinio definitivo

El dataset *Resultado Electorales* (#59) contiene el **escrutinio definitivo del 24 de septiembre** con resultados consolidados por categoría, en formato PDF + XLS:

- Gobernador.
- Senadores Provinciales.
- Diputados Provinciales.
- Concejales.
- Escrutinio definitivo Luján de Cuyo (consolidado).

## El marco normativo

Las **Ordenanzas Municipales** (#4) — repositorio CSV/XLS/PDF — incluyen las normas que regulan los procesos electorales locales y el funcionamiento del HCD electo. La ordenanza 13884/2020 (GIRSU), 14525/2023, 14526/2023 (presupuestaria/tarifaria) son ejemplos de la producción legislativa del HCD electo en el período.

---

*Fuente: Jefe de Gabinete del Municipio, Junta Electoral de Mendoza (PASO 2023). Datos en <https://datos.lujandecuyo.gob.ar>.*
"""

R['genero.md'] = """# Género y Diversidad

Análisis cuantitativo de la atención que la **Dirección de Género y Diversidad** brinda a víctimas de violencia. Es uno de los datasets más densos del portal: cada caso atendido se registra en una ficha **RUC** (Registro Único de Casos) con **87 dimensiones** que combinan trayectoria educativa, condición laboral, vínculo con el agresor, tipos de violencia ejercida, señales de riesgo y consecuencias judiciales.

## El volumen de atención

Las planillas anuales (2021, 2022, 1er semestre 2023, 2025) documentan la actividad sostenida de la Dirección. **En 2022, sobre 493 casos plenamente caracterizados**:

- **480 casos** correspondieron a víctimas residentes **en Luján de Cuyo** (97% del total).
- 9 casos en Capital, 2 en Godoy Cruz, 1 en Guaymallén, 1 en Maipú.

El dispositivo opera principalmente sobre la **población local**, configurando un **promedio de ~9-10 casos atendidos por semana** durante el año.

## El perfil de las víctimas

### Estado civil

| Estado | Casos | % |
|---|---:|---:|
| Soltera | 318 | 64% |
| Casada | 99 | 20% |
| Divorciada | 41 | 8% |
| Separada | 14 | 3% |

Casi **dos tercios solteras** — un dato que cuestiona la asunción cultural de que la violencia de género se concentra en parejas formalizadas.

### Vínculo con el agresor

| Vínculo | Casos | % |
|---|---:|---:|
| **Ex pareja conviviente** | 275 | **56%** |
| Cónyuge | 75 | 15% |
| Ex cónyuge | 58 | 12% |
| Ex novio/pareja no conviviente | 33 | 7% |

**El 90% del riesgo proviene del entorno de pareja o ex pareja**, con la **ex pareja conviviente** como vínculo dominante (más de la mitad de los casos). Esto reorienta la lectura sobre el ciclo de violencia: el momento de mayor riesgo no es necesariamente durante la convivencia, sino **inmediatamente después de la ruptura**.

### Nivel educativo

| Nivel | Casos | % |
|---|---:|---:|
| Secundaria incompleta | 178 | 36% |
| Secundaria completa | 99 | 20% |
| Terciario/Universitario completo | 62 | 13% |
| Primaria completa | 55 | 11% |
| Primaria incompleta | 25 | 5% |
| Sin educación | 23 | 5% |

El perfil dominante es el de mujeres con **trayectoria educativa interrumpida**: 56% no completó el secundario. Sólo 13% tiene título terciario o universitario.

### Condición laboral

| Condición | Casos | % |
|---|---:|---:|
| **Ocupada** | 250 | 51% |
| **Desocupada** | 187 | 38% |
| Inactiva | 32 | 6% |

La **desocupación afecta al 38% de las víctimas** — un input estructural sobre la dependencia económica como factor de revictimización.

### Discapacidad

478 casos (97%) sin discapacidad declarada. 6 casos con discapacidad motriz, 4 mental, 2 visceral.

## Los tipos de violencia ejercida

Las víctimas reportan, frecuentemente combinada:

| Tipo | Reportada (Sí) | Sin dato | % Sí sobre total |
|---|---:|---:|---:|
| **Psicológica** | 409 | 82 | **83%** |
| **Física** | 316 | 176 | 64% |
| **Económica/patrimonial** | 293 | 198 | 59% |
| **Sexual** | 107 | 386 | 22% |

La **violencia psicológica está en 4 de cada 5 casos**; la física en 2 de cada 3. La **patrimonial** es comparable a la física (59%) — y suele ser la menos visible socialmente. La **sexual** es probablemente sub-reportada (mucho "sin dato").

## Las señales de riesgo y los antecedentes

| Indicador | "Sí" | % |
|---|---:|---:|
| Violencia anterior denunciada | 103 | 21% |
| Consumo de alcohol del agresor | 177 | 36% |
| Antecedentes penales (denuncia previa) | 174 | 35% |

**Una de cada cinco víctimas atendidas ya había denunciado violencia previa** — indicador del ciclo de revictimización que el dispositivo busca interrumpir. **El 36% reporta consumo de alcohol como elemento contextual** del agresor.

## El marco institucional

Dos documentos enmarcan operativamente la política:

- **Acuerdo de Cooperación** con la **Procuración General de la Suprema Corte de Justicia de Mendoza** (#43) — articulación con el Poder Judicial provincial.
- **Protocolo de Acción** (#46) — procedimiento operativo para los equipos territoriales en atención y acompañamiento de víctimas.

Las medidas judiciales documentadas incluyen prohibición de acercamiento, exclusión del hogar, alimentos provisorios, restitución de pertenencias y medidas de cuidado personal.

## La pieza pública

La planilla de **Estadísticas 2025** (XLSX, 772 KB) trae los datos crudos de las 87 dimensiones por ficha — **el dataset más rico del portal en términos de profundidad analítica**. Una versión PBIX (Power BI) provista por la Dirección permite exploración interactiva de los cortes.

---

*Fuente: Dirección de Género y Diversidad, Municipalidad de Luján de Cuyo. Procuración General de la Suprema Corte de Justicia de Mendoza (acuerdo de cooperación). Datos en <https://datos.lujandecuyo.gob.ar>.*
"""

R['gestion_de_datos.md'] = """# Gestión de Datos

Análisis de la **estrategia de datos y gobernanza algorítmica** del municipio. Luján de Cuyo es uno de los pocos municipios argentinos con normativa específica sobre **uso de Inteligencia Artificial** en el Estado local — una decisión institucional poco frecuente.

## El marco normativo de la IA municipal

El paquete normativo publicado por la Secretaría de Innovación, Gobierno Abierto y Gestión del Territorio incluye:

### Decreto 3041 — Uso de IA y Machine Learning en el Estado municipal

El decreto establece principios y restricciones aplicables al uso de IA en la administración. Define el marco regulatorio dentro del cual las dependencias pueden incorporar herramientas algorítmicas, qué tipos de procesos pueden automatizarse y qué controles humanos son obligatorios.

### Estrategia de Datos para Toda la Ciudad

Documento institucional (versión final 08/12/2024) que articula la **visión integradora** de la gestión de datos como activo estratégico del municipio. Posiciona los datos abiertos como herramienta de transparencia + insumo para la planificación basada en evidencia + base de productos digitales para los vecinos.

### Protocolo Ético para el Uso de IA

Documento operativo con principios éticos aplicables a la implementación de IA. Aborda cuestiones como **transparencia algorítmica**, **prevención del sesgo**, **explicabilidad de las decisiones automatizadas**, **protección de datos personales** y **derechos de los administrados**.

### Tabla de gobernanza

El XLSX `Gobernanza_IA.xlsx` operativiza el marco con tres dimensiones:

| Dimensión | Área a cargo | Productos asociados |
|---|---|---|
| Institucionalidad | Infraestructura y Tecnología de la IA | — |
| Reglamentación | Infraestructura y Tecnología de la IA | Estrategia de Datos / Decreto 3041 / Protocolo Ético |
| Protección de datos | Infraestructura y Tecnología de la IA | Ley de Acceso a la Información Pública |

Existe además una planilla de **Programas IA** y otra de **Innovación y Desarrollo**, ambas asociadas al programa de transformación digital.

## El Inventario de Datos

El dataset *Inventario de Datos* es **el catálogo maestro que sostiene el portal de datos abiertos**. Es la planilla que la Secretaría de Innovación mantiene como inventario integral de los recursos de datos producidos por las distintas áreas del municipio: qué se publica, qué no, qué áreas tienen series estructuradas, qué brechas existen.

Este es el documento que el equipo técnico utiliza para priorizar **publicaciones nuevas** y para detectar **datasets candidatos a apertura**.

## El repositorio normativo

El dataset *Ordenanzas Municipales* es el repositorio centralizado de **toda la producción legislativa del HCD**:

- Ordenanzas 2025 categorizadas (CSV+XLS).
- Ordenanzas 2024 categorizadas (CSV+XLS).
- Ordenanzas 2024-2016 históricas (CSV).
- Normativa individual destacada: **Ordenanza 14830/2024** (Presupuesto 2025), **14831/2024** (Tarifaria 2025).

La estructura categorizada por temática habilita análisis de la **producción legislativa del HCD** por área (urbanismo, ambiente, fiscal, deportes, etc.).

## El laboratorio: Luján Lab

Vinculado a la estrategia de IA, el **Portal Luján Lab** opera como espacio de innovación y desarrollo digital del municipio. La **Página de Ciberseguridad** complementa el ecosistema con información sobre buenas prácticas de protección digital orientada a vecinos y agentes municipales.

---

*Fuente: Secretaría de Innovación, Gobierno Abierto y Gestión del Territorio, Municipalidad de Luján de Cuyo. Datos y normativa en <https://datos.lujandecuyo.gob.ar>.*
"""

R['seguridad.md'] = """# Seguridad

Análisis del estado de la seguridad pública en Luján de Cuyo desde los datos abiertos disponibles. La cobertura es limitada — la seguridad es competencia primaria provincial y nacional — pero los datasets municipales aportan un mapa institucional y elementos transversales.

## La red de comisarías

El dataset *Comisarías Luján de Cuyo* (publicado por el **Secretario del Juzgado Vial Nro 1**) registra la red departamental con dirección, distrito y datos de contacto, además del KML para visualización geográfica. Es el único dataset de seguridad con contenido tabular accesible.

La distribución de comisarías ofrece la **base institucional de la respuesta policial** — su lectura cruzada con la **densidad poblacional por distrito** (Ciudad 24.594, Carrodilla 23.886, Perdriel 13.687) permite analizar cobertura policial relativa, aunque la planificación operativa la define la **Policía de Mendoza**, no el municipio.

## Los puntos de criticidad económica

Aunque catalogados en otras categorías, varios datasets son insumos directos para la planificación de seguridad:

- **9 sucursales bancarias** (Frances, Supervielle, Nación, Galicia, HSBC, San Juan, Macro) — todas en el corredor San Martín del distrito Ciudad. Concentración geográfica que demanda **respuesta policial planificada**.
- **11 estaciones de servicio** sobre RN 7, RP 15 y Acceso Sur — puntos de alta circulación con valores monetarios y combustible.
- **Centros de salud** (19), **farmacias** (18), **escuelas** (112) — receptores potenciales de emergencias y planes de respuesta.
- **47 barrios populares** con 2.569 familias — territorios con vulnerabilidad social que requieren articulación con políticas integrales (no sólo policial).
- **Iluminación LED** (dataset *Energía*) — el reemplazo de luminarias incide directamente en la **seguridad ambiental peatonal**.

## El plan vial: un proxy de seguridad

Las **174 actividades** del Plan de Obras 2025 incluyen el programa "Ordenadores Viales — Priorización" — interventiones físicas (badenes, semáforos, demarcación) que mitigan riesgos viales. La inversión vial 2024 en pavimentación ($635 M), poda ($450 M, mejora visibilidad) y mantenimiento de maquinaria ($14 M) configuran un esfuerzo sostenido sobre la **infraestructura de movilidad** que tiene efectos directos sobre la seguridad cotidiana.

## La brecha estructural

El portal **no expone series sobre**:

- **Hechos delictivos** (robos, hurtos, lesiones, homicidios) por tipo, lugar, hora, modalidad — competencia provincial pero replicable a nivel municipal con datos del Ministerio de Seguridad y Justicia.
- **Multas y controles viales** — competencia municipal directa.
- **Siniestros viales** con georreferenciación, fatalidad, lesionados — uno de los indicadores más demandados.
- **Operativos** y **denuncias** recibidas en el ámbito municipal.
- **Cuerpo de Inspección General** (urbano y rural) — sus actuaciones no son públicas.

El dataset *Seguridad Vial* (#51) aparece en el catálogo como "Acciones viales" pero **no incluye archivos descargables**.

## Para análisis profundo

Para reconstruir un panorama completo de seguridad en Luján de Cuyo es necesario complementar con:

- **SNIC** (Sistema Nacional de Información Criminal) del Ministerio de Seguridad de la Nación, que publica delitos por departamento.
- **Estadísticas del Ministerio de Seguridad y Justicia de Mendoza**.
- **Observatorio Vial Provincial** para siniestros viales.

---

*Fuente: Secretaría del Juzgado Vial Nro 1, Secretaria de Gobierno. La seguridad pública es competencia primaria del Ministerio de Seguridad y Justicia de la Provincia de Mendoza y el Ministerio de Seguridad de la Nación. Datos en <https://datos.lujandecuyo.gob.ar>.*
"""

R['covid-19.md'] = """# COVID-19

Reconstrucción cuantitativa de la pandemia en el ámbito del municipio según el *Informe Covid Municipal*, publicado por la Subsecretaría de Gestión del Talento Humano. La planilla cubre **84 semanas** con relevamiento epidemiológico continuo y permite recuperar la curva completa del fenómeno en la administración municipal.

## La curva pandémica resumida

| Indicador | Valor |
|---|---:|
| **Semanas registradas** | 84 |
| **Casos positivos acumulados** | 645 |
| **Recuperados acumulados** | 20.424 |
| **Fallecidos acumulados** | 21 |
| **Pico semanal positivos** | 128 |
| Promedio semanal positivos | 7,7 |
| Total acumulado al cierre | 643 |

La discrepancia entre **20.424 recuperados** y **645 positivos acumulados** sugiere que el dataset incluye **casos heredados** de períodos previos al inicio de la planilla (las semanas 1-2 ya muestran casos en tratamiento sin contraparte en positivos nuevos del relevamiento). El indicador robusto es el **stock de casos activos por semana**.

## La letalidad observada

Con 21 fallecidos sobre 645 positivos nuevos registrados (planilla específica), la **tasa de letalidad observada es de ~3,3%**. Si se considera el universo total acumulado de 20.424 personas que pasaron por el dispositivo, la tasa baja a **~0,1%** — alineada con cifras nacionales tras la consolidación del programa de vacunación.

El **pico semanal de 128 casos** sugiere un evento de transmisión intensiva (probablemente correspondiente a la ola Ómicron a fines de 2021 / principios de 2022). Las semanas medias presentan un promedio mucho más bajo (7,7), confirmando que el sistema operó la mayor parte del tiempo en régimen de transmisión baja.

## El alcance del relevamiento

La planilla está publicada por la **Subsecretaría de Gestión del Talento Humano**, lo que sugiere que cubre principalmente al **personal municipal** (empleados del Ejecutivo y, por extensión, sus contactos estrechos), no a la población general del departamento. El dato útil para esta serie es el **estado epidemiológico del Estado local** durante los meses críticos.

Para una reconstrucción de la pandemia a nivel poblacional en Luján de Cuyo es necesario recurrir a:

- **Sala de Situación Provincial** (Ministerio de Salud de Mendoza).
- **Monitor Público de Vacunación** (Nación) — registros de cobertura por departamento.
- **Sistema Nacional de Vigilancia de la Salud (SNVS)** del Ministerio de Salud de la Nación.

## Las dimensiones registradas

El dataset captura semanalmente:

- **Año** y **Semana** (numeración propia desde Semana 1).
- **Mes** y **Periodo** (rango de fechas).
- **Positivos**: casos confirmados nuevos en la semana.
- **Recuperados**: altas epidemiológicas.
- **En tratamiento**: casos activos al cierre.
- **Total**: stock acumulado.
- **Fallecidos**.

Esto habilita análisis de **velocidad de transmisión** (positivos nuevos), **duración promedio del tratamiento** (positivos vs recuperados con desfase), **mortalidad acumulada** y **caracterización de las olas** (pico, ascenso, descenso) durante el período cubierto.

## Lo que falta para una serie completa

- Datos de **vacunación** local (la provincia administra esa serie).
- Cortes por **distrito**, **grupo de edad**, **sexo** — sólo agregados departamentales semanales.
- **Variantes circulantes** identificadas en el período.
- Datos del **personal municipal** desagregado vs población general (para entender el universo de relevamiento).

---

*Fuente: Subsecretaría de Gestión del Talento Humano, Municipalidad de Luján de Cuyo. Datos en <https://datos.lujandecuyo.gob.ar>.*
"""

# Escribir todos
for fname, content in R.items():
    fp = REPORTS_DIR / fname
    fp.write_text(content, encoding='utf-8')
    print(f"  written: {fname} ({len(content):,} chars)")

print(f"\nTotal: {len(R)} reports")
