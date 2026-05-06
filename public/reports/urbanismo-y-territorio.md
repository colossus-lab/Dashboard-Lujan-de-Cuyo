# Urbanismo y Territorio

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
