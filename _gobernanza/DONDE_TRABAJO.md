# ¿Dónde trabajo?

Mapa de una página para saber, ante cualquier tarea, en qué espacio se trabaja.
Alan investiga; los procesos de desarrollo están resueltos por este mapa y las
skills — si algo obliga a "chocar" con el desarrollo, es un bug del sistema y
se corrige aquí, no improvisando.

## Los dos espacios

| | Espacio artesanal | Espacio refinado |
|---|---|---|
| **Dónde** | `posts/<slug-largo>/` (p. ej. `posts/2026-07-homicidios-wb/`) | `projects/*.qmd` (+ catálogos automáticos `research/`, `bi/`) |
| **Qué se hace** | Investigar: descargar data, calcular, modelar, probar | Redactar: narrativa oficial, hallazgos, figuras referenciadas |
| **Qué contiene** | `data/`, `scripts/`, `tests/`, `outputs/`, `qa/`, `reproducir.ps1` | La tríada `<slug>.qmd`, `<slug>-research.qmd`, `<slug>-dashboard.qmd` |
| **Regla dura** | Todo número/figura publicable se genera aquí, en `outputs/` | Nunca ejecuta código ni copia cifras a mano: consume `outputs/` vía `{{< include >}}`, `![](...)` o `FileAttachment` |
| **Cómo se regenera** | `./posts/<slug-largo>/reproducir.ps1` (falla ruidoso si algo se rompe) | `quarto render` / `quarto preview` |

**Un tema nuevo** → skill `nuevo-caso`: crea ambos espacios de una vez desde
`_plantillas/analisis/` (artesanal) y `_plantillas/portafolio/` (tríada).

## Reglas operativas del repositorio

1. **El working tree vive SIEMPRE en `main`.** La rama `gh-pages` es solo la
   salida construida del sitio: la toca únicamente `quarto publish gh-pages`
   (ejecutado por Antigravity según su runbook). Nunca hacer checkout local de
   `gh-pages` para trabajar.
2. **El slug de la carpeta artesanal es inmutable tras el alta.** Las páginas de
   `projects/` la referencian con rutas relativas; renombrarla rompe la tríada
   en silencio.
3. **`_ai/` es material interno** (contexto de mercado, prompts). Está
   gitignorado y nada de su contenido pasa a archivos versionados ni a páginas.
4. **Publicar es un acto editorial, no técnico.** "Render correcto" ≠
   "aprobado": la puerta final es `CHECKLIST_PUBLICACION.md` + aprobación de
   Alan; el deploy lo ejecuta Antigravity.

## Referencias

- `ARQUITECTURA_PORTAFOLIO.md` — contrato de archivos y ejes.
- `PROTOCOLO_CALIDAD.md` — calidad económica/econométrica (innegociable).
- `CHECKLIST_PUBLICACION.md` — puerta final y runbook de publicación.
- Skills: `nuevo-caso` (alta), `articulo-academico` (eje BCE), `dashboard-bi` (eje IRE).
