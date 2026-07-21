# AGENTS.md — Reglas operativas para agentes IA

Todo agente (Claude, Codex, Antigravity, o cualquier modelo futuro) que trabaje en este repositorio o en los repos `proj-*` DEBE leer este archivo y los documentos de `_gobernanza/` antes de ejecutar cualquier tarea. Este sistema está diseñado para que un agente de menor capacidad pueda ejecutar sin inventar: si algo no está definido aquí o en la gobernanza, se pregunta a Alan, no se improvisa.

## Jerarquía documental (ante conflicto, gana el de arriba)

1. Instrucción directa de Alan en la conversación
2. `_gobernanza/PROTOCOLO_CALIDAD.md` — calidad económica/econométrica (INNEGOCIABLE)
3. `_gobernanza/CHECKLIST_PUBLICACION.md` — puerta final antes de publicar
4. `_gobernanza/PLAN_MAESTRO.md` — arquitectura y hoja de ruta del sistema
5. `_gobernanza/ROLES_IA.md` — quién hace qué
6. `_gobernanza/DONDE_TRABAJO.md` — mapa de los dos espacios de trabajo (artesanal vs. refinado) y reglas operativas del repo
7. Este archivo

## Reglas duras (aplican SIEMPRE, sin excepción)

1. **Ningún contenido se publica ni se marca como listo sin pasar el CHECKLIST_PUBLICACION y la aprobación explícita de Alan.**
2. **Nunca inventar, extrapolar ni "completar" datos.** Todo número publicado debe rastrearse a un output real de código ejecutado sobre datos con fuente citada. Si un dato no existe, se dice que no existe.
3. **No hacer push, ni tocar historial de git, ni borrar ramas sin orden explícita.**
4. **Nada de claves/API/tokens en código o commits.** `.gitignore` protege `.Renviron`, `.env`, `_ai/`, `CLAUDE.md`; no debilitarlo.
5. **Toda afirmación causal requiere justificación teórica previa** (ver Puerta 0 del protocolo). En su defecto, el lenguaje es de asociación.
6. **Ensamblar antes que fabricar:** ante una necesidad, buscar primero herramientas/plantillas/extensiones existentes y mantenidas (extensiones Quarto, paquetes CRAN, skills oficiales). Solo se construye desde cero lo que no existe.
7. Contenido del sitio en español (resúmenes en inglés donde el plan lo indica). Sitio 100% estático (GitHub Pages).
8. **Definición de "terminado":** el render corre sin errores/warnings, los números fueron verificados contra el output, el checklist aplicable está completo y Alan aprobó. Antes de eso, nada está terminado.

## Skills del repositorio

El flujo "una idea → dos ejes" está operacionalizado en tres skills versionadas en `.agents/skills/` (espejo operativo para Claude Code en `.claude/skills/`, fuera de git):

- `nuevo-caso` — alta de la tríada caso + investigación + tablero y del espacio artesanal (`posts/<slug>/` desde `_plantillas/analisis/`).
- `articulo-academico` — eje académico, estilo boletín analítico del BCE.
- `dashboard-bi` — eje ejecutivo, estilo IRE del MEF.

Ante una tarea de alta o desarrollo de un eje, el agente sigue la skill correspondiente. Las referencias canónicas de estilo están en `_gobernanza/ARQUITECTURA_PORTAFOLIO.md` §2. Si una skill contradice la gobernanza, gana la gobernanza y se corrige la skill (en ambas copias).

## Regla de cuatro ojos

Lo que un agente produce, lo revisa otro agente (o el mismo en una sesión limpia de verificación) ANTES de llegar a Alan: números re-ejecutados, señales de riesgo del protocolo revisadas una a una. El productor nunca es su propio único revisor.

## Ante la duda

Parar y preguntar a Alan. Una pregunta cuesta un minuto; un post erróneo publicado cuesta credibilidad profesional. Este portafolio representa públicamente a Alan Del Rosario: el estándar es el de una publicación profesional, no el de un borrador.
