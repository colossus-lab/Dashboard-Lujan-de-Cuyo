# Elecciones

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
