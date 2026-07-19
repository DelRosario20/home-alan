---
name: nuevo-caso
description: Da de alta un tema nuevo en el portafolio de Alan creando la tríada caso + investigación + tablero a partir de una sola idea. Usa esta skill SIEMPRE que Alan proponga un tema, proyecto, caso o investigación nueva ("quiero analizar X", "nuevo caso de Y", "empecemos con el piloto de Z", "crea las páginas de W"), aunque no mencione la palabra "caso". También cuando pida convertir un análisis existente (post, script, paper) en piezas del portafolio.
---

# Alta de un nuevo caso

Un tema se procesa **una sola vez** y produce tres páginas hermanas que comparten `slug` y outputs. El artículo académico y el tablero BI no son contenidos distintos: nacen de la misma investigación y se derivan mutuamente. Esta skill deja la estructura lista; el desarrollo de cada eje lo hacen las skills `articulo-academico` y `dashboard-bi`.

## Antes de tocar archivos

1. Lee `_gobernanza/ARQUITECTURA_PORTAFOLIO.md` (§2 ejes, §3 contrato de archivos, §6 alta de caso). Es el contrato; ante conflicto con esta skill, gana el documento.
2. Confirma con Alan la **Puerta 0** del `PROTOCOLO_CALIDAD.md`: pregunta, fuente de datos real y alcance (descriptivo vs. causal). Sin Puerta 0 aprobada no se crea nada.
3. Define el `slug` en minúsculas y sin tildes (p. ej. `homicidios`, `remesas`). Los tres archivos lo comparten obligatoriamente.

## Pasos

1. Copia las tres plantillas de `_plantillas/portafolio/` a `projects/` renombrando `tema-ejemplo` por el slug:
   - `<slug>.qmd` — puerta del caso (alcance + estado + salidas).
   - `<slug>-research.qmd` — eje académico.
   - `<slug>-dashboard.qmd` — eje BI.
2. Añade `<slug>.qmd` al listing de `projects/index.qmd`. Investigación y Tableros entran solos a sus catálogos (`research/`, `bi/`) por el sufijo del archivo.
3. Crea (o localiza) la carpeta de análisis del tema con su `outputs/`: todo número que aparezca en las páginas debe generarse por código ahí y consumirse con `{{< include >}}` o `FileAttachment`. Nunca se copian cifras a mano — esa es la única garantía de que artículo y tablero digan lo mismo.
4. Mantén `draft: true` y el aviso de estado editorial en las tres páginas. "Render correcto" no es "aprobado": solo Alan levanta el draft tras el `CHECKLIST_PUBLICACION.md`.
5. Registra en el caso qué outputs comparte la tríada y desde qué script se regeneran.

## Después del alta

- Desarrolla primero el eje académico (skill `articulo-academico`): es el producto madre.
- Deriva después el tablero (skill `dashboard-bi`) desde los mismos outputs.
- Verifica el render (`quarto render`) y revisa 375/768/1024/1440 px antes de presentar avances.

## Ejemplo de referencia

El caso piloto `homicidios` ya implementa el patrón completo: revisa `projects/homicidios.qmd`, `projects/homicidios-research.qmd` y `projects/homicidios-dashboard.qmd` con sus outputs en `posts/2026-07-homicidios-wb/outputs/`.
