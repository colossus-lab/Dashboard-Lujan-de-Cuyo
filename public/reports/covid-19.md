# COVID-19

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
