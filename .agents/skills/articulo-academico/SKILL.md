---
name: articulo-academico
description: Redacta o edita el artículo académico (<slug>-research.qmd) del portafolio de Alan al estilo boletín analítico del BCE. Usa esta skill SIEMPRE que Alan pida desarrollar, escribir, ampliar o corregir la investigación, el paper, el artículo, la "lectura técnica" o el eje académico de un caso — incluso si lo pide de forma casual ("mejora la sección de método", "redacta los resultados de X", "convierte este análisis en artículo"). También al revisar prosa, figuras o referencias de una página *-research.qmd.
---

# Artículo académico (eje Research)

El artículo es el producto madre de cada caso: desarrolla la evidencia en extenso y de él se deriva el tablero BI. Su referencia canónica de presentación es el **Boletín analítico ITCER del BCE** (`_gobernanza/ARQUITECTURA_PORTAFOLIO.md`, §2): rigor institucional, secciones numeradas, cifras exactas interpretadas en la misma oración.

## Antes de escribir

1. Lee `_gobernanza/PROTOCOLO_CALIDAD.md` — el lenguaje causal está regulado y es innegociable: sin justificación teórica previa, el lenguaje es de asociación.
2. Lee el override de diseño `design-system/alan-del-rosario-portfolio/pages/research.md` — estructura obligatoria y prohibiciones.
3. Verifica que los `outputs/` del caso existen y están generados por código. Si un número no existe en outputs, **no existe**: se genera primero el output o se dice que falta. Nunca escribas cifras de memoria ni "aproximadas" — cada número publicado se rastrea a un output real, y esa trazabilidad es lo que diferencia este portafolio de un blog.

## Contrato del documento

Front matter: `title`, `subtitle` (pregunta/país/periodo), `description` para el catálogo, `author`, `date`, `draft: true`, `categories` con `research`, `image`, `toc: true`, `number-sections: true`, `page-layout: article`, `bibliography` cuando haya citas.

Cuerpo, en este orden (contrato §4 de ARQUITECTURA_PORTAFOLIO):

1. Callout de estado editorial (se mantiene hasta aprobación de Alan).
2. `.research-context-bar` con enlaces a Investigación, Tablero, Caso y PDF.
3. Dentro de `.research-document`: Resumen (con palabras clave y JEL) → Hallazgos → Pregunta y marco → Datos → Método → Resultados → Robustez → Discusión → Limitaciones → Reproducibilidad → Referencias.

## Estilo boletín (lo que se toma del BCE)

- Cabecera de edición: el subtítulo funciona como línea de edición (tema, país, periodo); autor y fecha visibles.
- Cada cifra se reporta con nivel, variación y dirección en la misma oración: "el ITCER registró una depreciación del 0,98%, al ascender de 108,96 en abril a 110,03 en mayo" es el patrón a imitar.
- Figuras con título numerado, subtítulo de cobertura ("En puntos y tasa de variación mensual, ene. 2022 – may. 2026") y `fig-alt` que describa el patrón, no solo el tipo de gráfico.
- Definir el indicador antes de usarlo (qué mide, cómo se construye, qué implica que suba o baje).
- Secciones cortas y numeradas; la profundidad va en Método/Robustez, no en la introducción.

## Cómo se insertan los números

- Tablas y párrafos con cifras: `{{< include ../ruta/outputs/archivo.md >}}`.
- Figuras: SVG/PNG generados por los scripts del caso, referenciados por ruta relativa.
- Si al redactar necesitas una cifra que no está en outputs, detente y genera el output (o pide a Alan el dato); no rellenes.

## Antes de entregar

- `quarto render` sin errores ni warnings; revisar 375/768/1024/1440 px.
- Releer con `PROTOCOLO_CALIDAD.md` en mano: cada afirmación causal, cada intervalo, cada limitación.
- La pieza queda `draft: true` y con el aviso editorial: pasa a cuatro ojos y a `CHECKLIST_PUBLICACION.md` antes de cualquier aprobación.

## Ejemplo de referencia

`projects/homicidios-research.qmd` implementa el patrón completo (includes desde outputs, figuras con alt, lenguaje descriptivo sin causalidad, bibliografía en `.bib`).
