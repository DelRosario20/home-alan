# Roles del equipo IA

Principio de diseño: **los procesos se escriben para el trabajador de menor capacidad futuro.** Hoy hay tres suscripciones pro (etapa de construcción, capital alto); a futuro quedará Claude y versiones gratuitas del resto. Por eso nada depende del "criterio" del agente: todo depende de protocolos, plantillas y checklists que cualquier modelo pueda seguir.

## Matriz actual (etapa de construcción)

| Agente | Rol | Responsabilidades | NO hace |
|---|---|---|---|
| **Claude** | Gerente general / editor | Arquitectura del sistema, redacción final, revisión metodológica, decisiones de estructura, verificación de números | Publicar sin aprobación de Alan |
| **Antigravity** | Gestor de repositorio / QA | Control de versiones, renders completos, validación de links, migraciones mecánicas, vincular carpetas de proyectos en su workspace, hacer cumplir `.gitignore` | Rediseñar contenido por su cuenta; push sin orden |
| **Codex** | I+D / ideación | Búsqueda de referencias, brainstorm de temas para posts, exploración de herramientas/extensiones existentes ("ensamblar, no fabricar") | Modificar archivos del sitio sin tarea asignada |
| **Alan** | Dueño / director | Decisión final SIEMPRE: aprueba publicaciones, define estilo, firma todo | Delegar la aprobación final |

Regla de cuatro ojos: el productor de una pieza nunca es su único revisor (detalle en `AGENTS.md`).

## Matriz futura (régimen sostenible)

Los mismos roles, ejecutados por versiones gratuitas siguiendo los protocolos ya escritos. Trabajo de los agentes pro HOY: dejar plantillas y procesos tan explícitos que la degradación de capacidad no degrade la calidad. Cada plantilla nueva se prueba con esta pregunta: *¿un asistente junior sin contexto podría ejecutarla sin inventar nada?* Si no, falta especificación.

## Flujo de una pieza (quién toca qué, en orden)

```
Idea (Codex/Alan) → Puerta 0 aprobada por Alan → análisis (Claude + Alan)
→ QA técnico: render, reproducibilidad, .gitignore (Antigravity)
→ revisión cuatro ojos (agente distinto al productor)
→ CHECKLIST_PUBLICACION → aprobación de Alan → publish + post LinkedIn
```

## Nota sobre workspaces de Antigravity

Antigravity puede añadir a su workspace las carpetas de los repos `proj-*` junto a `home-alan` para trabajar el conjunto. Eso NO cambia la regla estructural: cada carpeta sigue siendo un repo git independiente; el workspace del IDE es solo una vista, igual que la carpeta contenedora en el disco.

## Sujeto a definición por Alan (pendientes abiertos)

Estilo de redacción propio (mientras tanto: estándar académico de economía — claro, directo, sin adjetivos infundados), diseño definitivo de gráficos/posts (en exploración con referencias de Codex), y paleta/identidad visual (Fase 1).
