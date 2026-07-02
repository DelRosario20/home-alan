# Plan Maestro — Sistema de Portafolio de Proyectos
**Alan Del Rosario · Julio 2026 · v1.1**
*(v1.1: workspace sin git raíz, .gitignore/seguridad, identidad visual, microdatos, proyecto homicidios)*

Documento de delimitación. Define la arquitectura, el flujo de trabajo y las fases antes de tocar cualquier proyecto. Este archivo vivirá como guía del sistema en el repo del sitio.

---

## 1. Objetivo

Convertir el trabajo de investigación (existente y futuro) en **evidencia pública y demostrable** que respalde el CV, a través de tres canales conectados:

| Canal | Rol | Frecuencia |
|---|---|---|
| **Sitio web** (GitHub Pages) | Vitrina central: perfil + proyectos + posts | Se actualiza con cada entrega |
| **GitHub** (repos) | Proceso y reproducibilidad: código, datos, versiones | Push continuo (constancia visible) |
| **LinkedIn** | Difusión: hallazgos puntuales que enlazan al sitio | 1–2 posts/mes mínimo |

**Principio rector:** todo nace de UN solo trabajo. Un análisis produce → repo (proceso) → página web (resultado) → post LinkedIn (difusión). Nunca se produce contenido tres veces; se produce una vez y se deriva.

---

## 2. Decisión de stack: Quarto, no RPubs

**Recomendación firme: Quarto + GitHub Pages.** Razones:

1. **Es el stack de los ejemplos que te gustaron.** benharrap.com es un sitio Quarto en GitHub Pages. El de Michael Rowe usa Quartz (herramienta similar, orientada a notas de Obsidian, no a análisis en R) también en GitHub Pages. Para tu caso —R, papers, dashboards— Quarto es la opción correcta y produce exactamente ese resultado.
2. **RPubs no sirve como portafolio.** Es publicación suelta de documentos: sin página de perfil, sin estructura, sin dominio propio, sin control de diseño. Todos los dashboards que viste en RPubs se pueden replicar como *Quarto Dashboards* dentro de tu propio sitio, con mejor estética.
3. **Positron tiene soporte nativo de Quarto** (render, preview, visual editor). Tu flujo actual en R no cambia: escribes `.qmd` en vez de `.Rmd`.
4. **Interactividad sin servidor.** Con `plotly`, `leaflet`, `DT`, `gt` y Observable JS obtienes gráficos dinámicos (hover, zoom, filtros) en HTML estático — gratis en GitHub Pages, sin Shiny ni shinyapps.io. Shiny queda como opción futura solo si un proyecto exige filtros con recálculo en vivo.
5. **STATA convive bien:** corres el análisis en STATA, exportas resultados (`.csv`, `.dta`, gráficos) y el `.qmd` los consume desde R. El repo documenta ambos scripts.

**Bilingüe ES/EN — regla pragmática:** el sitio se estructura bilingüe con la extensión `babelquarto` (o dos perfiles), pero **no todo se traduce**. Se traduce al inglés: la página About, y la página-resultado de cada proyecto insignia (abstract + hallazgos clave). Los posts rápidos y dashboards van solo en español. Así capturas reclutadores internacionales sin duplicar el mantenimiento.

---

## 3. Arquitectura de repositorios

**Modelo: 1 repo por proyecto + 1 repo del sitio** (lo que hacen Rowe y Harrap).

```
github.com/DelRosario20/
│
├── delrosario20.github.io      ← EL SITIO (Quarto website)
│   ├── index.qmd               # Home: perfil, foto, highlights
│   ├── about.qmd / about-en.qmd
│   ├── projects/               # 1 página por proyecto (listing automático)
│   │   └── pea-cohortes.qmd    # abstract, hallazgos, links a repo/paper/dashboard
│   ├── posts/                  # blog: análisis rápidos (listing automático)
│   ├── cv.pdf
│   └── _quarto.yml
│
├── proj-homicidios             ← 1 REPO POR INVESTIGACIÓN
│   │   # "Motivaciones Letales y Desigualdad: Homicidios
│   │   #  Instrumentales en Ecuador (2014–2024)" — 4.º proyecto,
│   │   #  aún no en CV, candidato a primera migración
├── proj-pea-cohortes
│   ├── README.md               # resumen, cómo reproducir, changelog vs. ponencia
│   ├── data/  (raw/ + clean/, o instrucciones si datos no publicables)
│   ├── R/     (scripts numerados: 01_limpieza.R, 02_modelos.R ...)
│   ├── stata/ (si aplica)
│   ├── paper/ paper.qmd        → render a PDF (versión completa)
│   └── dashboard/ dashboard.qmd → render a HTML (versión BI)
│
├── proj-bandas-combustibles
├── proj-remesas
└── proj-[cuarto-proyecto]
```

**Por qué así:** cada repo cuenta su propia historia (commits = proceso demostrable), el sitio se mantiene liviano, y un reclutador puede ir de la página bonita al código en un clic.

---

## 4. Los dos productos por proyecto

Nacen del **mismo `.qmd` fuente de resultados**, cambiando formato y profundidad:

| | Versión completa (academia) | Versión BI (empresas) |
|---|---|---|
| Formato | `paper.qmd → PDF` (estilo research paper: intro, revisión, metodología, resultados, conclusiones) | `dashboard.qmd → HTML` (Quarto Dashboard: value boxes, gráficos interactivos, 3–5 hallazgos clave) |
| Extensión | 15–30 págs | 1 pantalla scrolleable |
| Vive en | repo del proyecto + link en el sitio | página dentro del sitio |
| Regla de oro | rigor y citas | **resultados primero**, cero jerga innecesaria |

**Actualización de ponencias:** cada proyecto migrado declara en su README y en la página web: *"Versión 2.0 — actualizada y corregida a partir de la ponencia presentada en [congreso, año]. Cambios: [lista]"*. Eso convierte la corrección de errores en señal de madurez, no en debilidad.

---

## 5. Los dos ritmos de producción

### Ritmo A — Proyectos insignia (los 4 actuales)
Ciclo largo (4–8 semanas c/u). Entregable: repo + paper PDF + dashboard + página en el sitio + 2–3 posts de LinkedIn derivados (uno al anunciar, uno con el hallazgo más visual, uno con el dashboard).

### Ritmo B — Publicaciones rápidas (la constancia)
Ciclo corto (2–4 horas, máx. 1 tarde). Formato: post en el blog del sitio + post LinkedIn con el gráfico. Ejemplos: evolución de una variable del BCE/INEC, una correlación comentada, estadística descriptiva de coyuntura, mini-réplica de un resultado conocido con datos de Ecuador.

**Fuentes de datos priorizadas (micro > macro cuando se pueda):** los microdatos dan muestras grandes y mejor material visual que las series macro anuales/trimestrales. Canasta base: [ANDA — Catálogo de microdatos INEC](https://anda.inec.gob.ec/anda5/index.php/catalog/) (ENEMDU, ENCV, censos), [Datos Abiertos Ecuador](https://www.datosabiertos.gob.ec/) (multi-área: salud, seguridad, educación — de aquí salió homicidios), BCE para macro, y a futuro bases internacionales (World Bank micro, IPUMS, etc.). El alcance temático no se limita a macroeconomía: sociodemografía, bienestar, seguridad y salud entran con igual peso — es "análisis aplicado con datos de Ecuador", no "macro de Ecuador".

**Regla anti-consumo-de-tiempo:** un post rápido que pasa de una tarde se corta o se convierte en candidato a proyecto. La constancia vale más que la profundidad en el Ritmo B.

**Cadencia objetivo:** 2 posts rápidos/mes + avance visible (commits) en 1 proyecto insignia a la vez. Nunca dos insignia en paralelo.

---

## 6. Flujo de trabajo (por pieza de contenido)

```
Idea/actualización
   → carpeta local (espejo del repo) → trabajar en Positron (R/Quarto) o STATA
   → commits frecuentes con mensajes descriptivos → push
   → render Quarto (paper y/o dashboard)
   → añadir/actualizar página en el sitio → push del sitio (se publica solo)
   → redactar post LinkedIn (plantilla: hallazgo + gráfico + link al sitio + hashtags)
```

**Espacio local en tu PC (workspace):**

```
~/Delrosario20/                ← carpeta contenedora, SIN git init
├── delrosario20.github.io/    ← repo 1 (el sitio; aquí viven README, Quarto, etc.)
├── proj-homicidios/           ← repo 2 (cada uno con su propio .git)
├── proj-pea-cohortes/         ← repo 3
├── proj-.../
└── _plantillas/               ← sin git o repo privado (templates, theme ggplot)
```

**Regla estructural:** la raíz del workspace NUNCA lleva `git init`. Git no maneja bien repos anidados y GitHub no tiene concepto de "workspace": en tu perfil los repos aparecen todos al mismo nivel. La jerarquía existe solo en tu disco. Cada carpeta hija se crea en GitHub primero y se clona (o `git init` local + `git remote add`). Diagnóstico de errores: cada repo es un compartimento estanco — historial, push y fallos independientes.

**Seguridad (.gitignore obligatorio en el commit cero de cada repo):**

```
.Renviron          # API keys — se leen con Sys.getenv(), nunca en el script
.env
CLAUDE.md
.claude/
data/raw/          # datos crudos pesados o sensibles (se documenta la fuente)
.Rhistory
.RData
.DS_Store / Thumbs.db
/.quarto/
```

Advertencia: lo que se subió una vez queda en el historial aunque lo borres después. Por eso el `.gitignore` entra antes del primer commit (viene incluido en la plantilla de repo).

**Publicación del sitio:** `quarto publish gh-pages` desde la raíz del sitio, o GitHub Actions para render automático en cada push (se configura en Fase 1 y te olvidas).

**Rol de las suscripciones IA:** Claude para estructurar análisis, redactar (paper, posts ES/EN) y revisar código; Copilot/Codex para autocompletar en Positron; Antigravity para tareas agénticas largas (migraciones, refactors). Regla: la IA acelera, pero cada número publicado lo verificas tú contra el output real.

---

## 7. Fases (sin fechas de proyecto todavía — solo el sistema)

**Fase 0 — Infraestructura (1 sesión de trabajo conmigo):**
crear repo del sitio con Quarto + tema + estructura bilingüe, publicar en GitHub Pages con tu perfil y CV. *Resultado: la web existe y ya es linkeable desde el CV y LinkedIn.*

**Fase 1 — Plantillas e identidad visual (1–2 sesiones):**
(a) *Identidad visual* al estilo El Quantificador: paleta propia (3–4 colores base + escalas secuencial/divergente), tipografía, `theme_delrosario()` de ggplot2 en `_plantillas/` para que todo gráfico salga uniforme con una línea, pie estándar obligatorio ("Fuente: [datos]. Elaboración: Alan Del Rosario — delrosario20.github.io") y monograma/marca simple. (b) *Templates*: repo de proyecto (con `.gitignore` incluido), `paper.qmd`, `dashboard.qmd`, post LinkedIn. *Resultado: producir contenido se vuelve mecánico y con marca reconocible.*

**Fase 2 — Migración insignia (1 proyecto a la vez):**
orden sugerido: **homicidios instrumentales** primero (no está en el CV → mayor valor marginal; microdatos → mejor material visual; es el trabajo que más te gusta → mejor carta de presentación), luego PEA-cohortes (el más reciente → menos corrección). Cada migración: repo + v2.0 + paper + dashboard + página + posts.

**Fase 3 — Régimen permanente:**
Ritmo B activo (2 posts/mes) + siguiente insignia. Revisión trimestral del sistema.

---

## 8. Convenciones

En cuanto a nombres: repos de proyecto con prefijo `proj-`, scripts numerados (`01_`, `02_`), commits en español descriptivos ("Agrega modelo probit por cohorte" y no "cambios"). Cada repo lleva README con: qué es, hallazgo principal, cómo reproducir, changelog vs. versión original, y licencia (MIT para código; datos citan fuente). Los datos sensibles o pesados no se suben: se sube el script de descarga/limpieza y la instrucción de fuente (INEC, BCE, ENEMDU). Página de proyecto en el sitio siempre con la misma estructura: abstract (ES/EN) → 3 hallazgos → gráfico estrella → botones [Paper PDF] [Dashboard] [Repo].

---

## 9. Qué queda decidido y qué queda abierto

**Decidido:** Quarto + GitHub Pages; bilingüe pragmático; 1 repo por proyecto; dos productos por insignia; dos ritmos; interactividad estática (plotly/OJS) sin Shiny por ahora.

**Abierto (se decide en su momento):** tema visual del sitio (se elige en Fase 0 viendo opciones), dominio propio `.com` (opcional, ~USD 12/año, se puede añadir después sin romper nada), orden exacto de migración de los 4 proyectos, y si algún dashboard futuro justifica shinylive/webR.
