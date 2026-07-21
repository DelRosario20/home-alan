---
name: nuevo-caso
description: Da de alta un tema nuevo en el portafolio de Alan creando la tríada caso + investigación + tablero Y el espacio artesanal de análisis (data, scripts, tests, outputs) a partir de una sola idea. Usa esta skill SIEMPRE que Alan proponga un tema, proyecto, caso o investigación nueva ("quiero analizar X", "nuevo caso de Y", "empecemos con el piloto de Z", "crea las páginas de W"), aunque no mencione la palabra "caso". También cuando pida convertir un análisis existente (post, script, paper) en piezas del portafolio.
---

# Alta de un nuevo caso

Un tema se procesa **una sola vez** y produce dos espacios que nacen juntos:

- **Espacio artesanal** — `posts/<slug-largo>/`: donde Alan investiga. Data cruda,
  scripts, tests, outputs. Aquí se calcula todo.
- **Espacio refinado** — `projects/`: las tres páginas hermanas que consumen los
  outputs. Aquí solo se redacta; nunca se ejecuta código ni se copian cifras a mano.

El artículo académico y el tablero BI no son contenidos distintos: nacen de la
misma investigación. Esta skill deja AMBOS espacios listos; el desarrollo de cada
eje lo hacen las skills `articulo-academico` y `dashboard-bi`.

## Antes de tocar archivos

1. Lee `_gobernanza/ARQUITECTURA_PORTAFOLIO.md` (§2 ejes, §3 contrato de archivos,
   §6 alta de caso) y `_gobernanza/DONDE_TRABAJO.md`. Son el contrato; ante
   conflicto con esta skill, ganan los documentos.
2. Confirma con Alan la **Puerta 0** del `PROTOCOLO_CALIDAD.md`: pregunta, fuente
   de datos real y alcance (descriptivo vs. causal). Sin Puerta 0 aprobada no se
   crea nada.
3. Define los dos identificadores, en minúsculas y sin tildes:
   - `slug` corto para las páginas (p. ej. `homicidios`, `remesas`).
   - `slug largo` para la carpeta artesanal: `AAAA-MM-<tema>-<fuente>`
     (p. ej. `2026-07-homicidios-wb`).
   **Ambos son inmutables tras el alta**: las páginas referencian la carpeta con
   rutas relativas (`../posts/<slug-largo>/outputs/...`) y renombrar rompe la
   tríada en silencio. Si un nombre resulta incómodo, se decide ANTES de crear.

## Pasos

### A. Espacio artesanal (primero: sin outputs no hay páginas)

1. Copia `_plantillas/analisis/` completa a `posts/<slug-largo>/`. Trae
   `reproducir.ps1`, stubs de `scripts/01-04`, `tests/`, `qa/CHECKLIST.md` y
   la estructura `data/` + `outputs/`.
2. Sustituye los marcadores `<slug>`, `<fuente>`, `<indicador>` en cada stub.
3. Si el caso no tiene eje de modelado formal, elimina `04_investigacion.py`
   y su línea en `reproducir.ps1`.
4. El caso modelo es `posts/2026-07-homicidios-wb/` — ante cualquier duda de
   implementación, imita ese patrón.

### B. Espacio refinado (la tríada)

5. Copia las tres plantillas de `_plantillas/portafolio/` a `projects/`
   renombrando `tema-ejemplo` por el slug:
   - `<slug>.qmd` — puerta del caso (alcance + estado + salidas).
   - `<slug>-research.qmd` — eje académico.
   - `<slug>-dashboard.qmd` — eje BI.
6. Añade `<slug>.qmd` al listing de `projects/index.qmd`. Investigación y
   Tableros entran solos a sus catálogos (`research/`, `bi/`) por el sufijo.
7. Registra en el caso qué outputs comparte la tríada y desde qué script se
   regeneran.

### C. Reglas que garantizan la coherencia

- **Todo número visible nace en `outputs/`** y se consume con `{{< include >}}`,
  `![](...)` o `FileAttachment`. Nunca se copian cifras a mano — esa es la única
  garantía de que artículo y tablero digan lo mismo.
- **Toda ruta cruzada referenciada debe existir**: antes de presentar avances,
  verifica que cada `../posts/<slug-largo>/...` citada en la tríada resuelve en
  disco (el `03_verificar.py` del caso debe chequearlo; falla ruidosa es mejor
  que rotura silenciosa).
- Mantén `draft: true` y el aviso de estado editorial en las tres páginas.
  "Render correcto" no es "aprobado": solo Alan levanta el draft tras el
  `CHECKLIST_PUBLICACION.md`.

## Después del alta

- Desarrolla primero el eje académico (skill `articulo-academico`): es el
  producto madre.
- Deriva después el tablero (skill `dashboard-bi`) desde los mismos outputs.
- Verifica el render (`quarto render`) y revisa 375/768/1024/1440 px antes de
  presentar avances.

## Ejemplo de referencia

El caso piloto `homicidios` implementa el patrón completo: revisa
`projects/homicidios.qmd`, `projects/homicidios-research.qmd` y
`projects/homicidios-dashboard.qmd`, con su espacio artesanal en
`posts/2026-07-homicidios-wb/` (scripts, tests, `reproducir.ps1` y outputs).
