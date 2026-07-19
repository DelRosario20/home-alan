# home-alan

Sitio web personal y portafolio de proyectos de **Alan Del Rosario** — economía aplicada y análisis de datos, Ecuador.

**Sitio en vivo:** https://delrosario20.github.io/home-alan/

## Cómo está construido

```
Positron/Obsidian (Markdown + R) → Git/GitHub → Quarto → GitHub Pages
```

Este repositorio contiene únicamente el **sitio web** (páginas, posts, perfil). Cada investigación vive en su propio repositorio independiente (`proj-*`) y se vincula desde aquí.

## Estructura

- `index.qmd` — portada y propuesta híbrida Research/BI
- `about.qmd` — perfil ES/EN
- `projects/` — casos y sus dos salidas (`*-research.qmd`, `*-dashboard.qmd`)
- `research/` — catálogo académico automático
- `bi/` — catálogo de dashboards automático
- `posts/` — blog de análisis rápidos (una carpeta por post, con sus datos)
- `design-system/` — tokens, componentes y overrides de página
- `_plantillas/portafolio/` — trío copiable Caso/Research/BI
- `_quarto.yml` — configuración del sitio
- `styles.scss` — estilos propios
- `_gobernanza/` — plan maestro, protocolo de calidad económica/econométrica, checklist de publicación y roles del equipo IA
- `AGENTS.md` — reglas operativas para cualquier agente IA que trabaje en este repo

## Control de calidad

Nada se publica sin pasar el [protocolo de calidad](_gobernanza/PROTOCOLO_CALIDAD.md) (coherencia con teoría económica, datos con fuente oficial, reproducibilidad, revisión de cuatro ojos) y el [checklist de publicación](_gobernanza/CHECKLIST_PUBLICACION.md). Los errores detectados tras publicar se corrigen con fe de erratas visible, nunca en silencio.

## Comandos

```bash
quarto preview          # vista local: muestra borradores con su banner Draft
quarto render           # salida de producción: excluye páginas draft
quarto publish gh-pages # solo tras checklist, draft:false y aprobación de Alan
```

## Demostración reproducible

El post piloto de homicidios implementa el flujo completo a pequeña escala con una fuente oficial: descarga por API → validación → indicadores → gráfico → pruebas → verificación → render.

```powershell
./posts/2026-07-homicidios-wb/reproducir.ps1
```

Los artefactos derivados se versionan junto con el código que los produce. El checklist conserva por separado la evidencia técnica y las dos autorizaciones editoriales que ningún script puede sustituir: revisión independiente y aprobación de Alan.

La separación visual y funcional de Caso, Research y BI se define en [`_gobernanza/ARQUITECTURA_PORTAFOLIO.md`](_gobernanza/ARQUITECTURA_PORTAFOLIO.md).

## Licencia

Contenido bajo [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.es). Código bajo MIT.
