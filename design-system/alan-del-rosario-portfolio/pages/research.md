# Override — Investigación (artículo académico)

Estas reglas sustituyen al sistema maestro solo en páginas `*-research.qmd`. Referencia canónica: Boletín analítico ITCER del BCE (ver `_gobernanza/ARQUITECTURA_PORTAFOLIO.md`, §2).

## Trabajo de la página

Sostener una lectura larga y verificable: que un lector técnico pueda reconstruir pregunta, datos, método, resultados y límites sin salir de la página, y que cada cifra citada sea rastreable a un output generado por código.

## Estructura obligatoria

1. Aviso de estado editorial mientras no exista aprobación de Alan.
2. Barra de contexto: Investigación · Tablero · Caso · PDF (los que existan).
3. Cabecera de edición estilo boletín: título del tema, subtítulo con pregunta/país/periodo, autor y fecha visibles.
4. Cuerpo con las secciones del contrato de producto (resumen → referencias), numeradas (`number-sections: true`) y con TOC lateral.
5. Cifras incluidas desde `outputs/` con `{{< include >}}`; nunca transcritas a mano.
6. Figuras numeradas con título, subtítulo de cobertura temporal y `fig-alt` descriptivo.
7. Referencias bibliográficas gestionadas con `.bib`, no escritas a mano.

## Apariencia

- Acento dorado (`--adr-gold-400`) para el eje Research; nunca cian en elementos editoriales.
- Ancho de lectura 65–75 caracteres; densidad baja y espacio vertical generoso.
- Manrope en toda la página; jerarquía por tamaño y peso, no por familias nuevas.
- Prosa estilo boletín: la cifra exacta y su interpretación en la misma oración; sin adjetivos infundados.

## Prohibido

- KPIs, value boxes o gramática de dashboard dentro del artículo.
- Afirmaciones causales sin la justificación exigida por `PROTOCOLO_CALIDAD.md`.
- Números "de memoria": todo dato publicado proviene de un include u output verificado.
- Copiar identidad institucional del BCE (logos, cabeceras azules, escudos).
