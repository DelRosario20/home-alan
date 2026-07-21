# Plantillas del espacio artesanal

Andamiaje para la carpeta de análisis de un tema nuevo: `posts/<slug-largo>/`
(convención de nombre: `AAAA-MM-<tema>-<fuente>`, p. ej. `2026-07-homicidios-wb`).

**El slug de la carpeta es inmutable tras el alta**: las páginas de `projects/`
lo referencian con rutas relativas y renombrarlo las rompe en silencio.

## Contrato

Todo número, tabla o figura visible en el sitio nace en `outputs/` generado por
código; las páginas refinadas (`projects/*.qmd`) solo consumen con
`{{< include >}}`, `![](...)` o `FileAttachment`. Nunca se copian cifras a mano.

## Estructura que producen estas plantillas

```
posts/<slug-largo>/
├── reproducir.ps1        # orquestador: scripts → tests → verificación → render
├── data/                 # datos crudos + fuente.json (procedencia)
├── scripts/
│   ├── 01_descarga.py    # obtiene el dato crudo desde la fuente oficial
│   ├── 02_analisis.py    # valida esquema, calcula indicadores, genera outputs/
│   ├── 03_verificar.py   # QA de lenguaje/consistencia de los outputs
│   └── 04_investigacion.py  # modelado del eje académico (si aplica)
├── tests/
│   └── test_pipeline.py  # unittest: anclas de valores y reglas duras
├── outputs/              # únicos artefactos que consumen las páginas
└── qa/
    └── CHECKLIST.md      # registro de verificaciones del caso
```

## Uso

1. Copia esta carpeta completa a `posts/<slug-largo>/` renombrando los stubs.
2. Sustituye los marcadores `<slug>`, `<fuente>`, `<indicador>` de cada stub.
3. El caso modelo completo es `posts/2026-07-homicidios-wb/` — ante duda, imita.
