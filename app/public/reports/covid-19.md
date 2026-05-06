# COVID-19

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
