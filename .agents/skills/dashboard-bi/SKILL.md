---
name: dashboard-bi
description: Construye o edita el tablero ejecutivo (<slug>-dashboard.qmd) del portafolio de Alan al estilo IRE del Ministerio de Economía y Finanzas. Usa esta skill SIEMPRE que Alan pida un dashboard, tablero, vista ejecutiva, KPIs, "versión BI" o la traducción ejecutiva de una investigación — incluso si lo pide de forma casual ("hazle el tablero a X", "agrega un filtro al dashboard", "los KPIs no se ven bien"). También al revisar interacciones OJS/Plotly o el CSS de un *-dashboard.qmd.
---

# Tablero ejecutivo (eje BI)

El tablero traduce una investigación ya desarrollada a lectura de decisión: un reclutador o decisor debe responder en menos de 30 segundos qué ocurre, frente a qué periodo, con qué cobertura y dónde está la evidencia. Su referencia canónica es el **IRE del MEF** (`_gobernanza/ARQUITECTURA_PORTAFOLIO.md`, §2). No es contenido nuevo: consume los mismos `outputs/` que el artículo académico.

## Antes de construir

1. Verifica que el eje académico del caso existe (`<slug>-research.qmd`) y que los `outputs/` están generados. El tablero se **deriva** de la investigación; si no hay investigación, primero va la skill `articulo-academico`.
2. Lee el override `design-system/alan-del-rosario-portfolio/pages/business-intelligence.md` — estructura obligatoria, apariencia y prohibiciones.
3. Usa el formato `dashboard` de Quarto con `css: dashboard.css` (ya existe en `projects/`).

## Estructura obligatoria (en orden)

1. **Commandbar** (`.dashboard-commandbar`): identidad ADR · BI LAB, dominio, cobertura, frecuencia, fuente real, estado editorial y acciones (Investigación · Caso · Descargar datos). El enlace a la Investigación es persistente — es la garantía de trazabilidad del eje.
2. **KPIs** (3–5, nunca más de 5): patrón IRE — valor con unidad, periodo, dirección del cambio y banda inferior con la comparación interanual ("May 2025: 0.46%"). Generados desde outputs compartidos, no calculados a mano.
3. **Visual principal**: tendencia o comparación que responda la pregunta ejecutiva, con selectores de rango reales cuando el dato lo permita (desde/hasta, 10A/5A/Todo).
4. **Desglose**: territorio, categoría o periodo — solo si el dato lo sostiene.
5. **Lectura ejecutiva**: señal, decisión informada y límite crítico, en frases cortas.
6. **Gobierno**: fuente, trazabilidad, calidad de la señal, enlace al Research y descarga CSV.

## Reglas duras del eje

- **Ningún control decorativo.** Un filtro visible debe modificar una vista; si el gráfico no puede responder, se muestra contexto estático. Un filtro simulado destruye la credibilidad de todo el portafolio.
- Datos vía `FileAttachment` (OJS) o includes desde los outputs del caso — la misma fuente que el artículo, para que ambos ejes digan siempre lo mismo.
- Cifras tabulares (`tabular-nums`), cian para datos e interacción, dorado solo para el vínculo metodológico.
- Fecha de actualización y cobertura siempre visibles; nada de fechas ambiguas.
- Hover aporta el valor exacto, pero la lectura central no depende del hover (accesibilidad y móvil).
- Sin párrafos académicos dentro de tarjetas: la profundidad vive en el artículo, aquí viven la señal y el límite.
- Habla el vocabulario del mercado BI (KPI, tendencia, forecast, segmentación, desglose, decisión): el tablero es también evidencia de competencia profesional. Si existe `_ai/PERFIL_MERCADO.md` (archivo privado), revísalo antes de diseñar KPIs.

## Antes de entregar

- `quarto render` sin errores; probar los filtros de verdad (mover el control y ver el cambio).
- Revisar 375/768/1024/1440 px; en 375 px no puede haber scroll horizontal.
- `draft: true` y estado editorial visible hasta checklist y aprobación de Alan.

## Ejemplo de referencia

`projects/homicidios-dashboard.qmd`: commandbar completa, KPIs desde `dashboard_kpis.md`, filtro OJS funcional sobre el CSV compartido y sección de gobierno con descarga.
