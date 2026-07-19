# Arquitectura del portafolio híbrido

Contrato de estructura y diseño. Complementa `PLAN_MAESTRO.md`; no reemplaza el protocolo económico ni el checklist de publicación.

## 1. Modelo de información

```text
Inicio
├── Casos                         # puerta común de cada tema
│   └── <slug>.qmd
├── Investigación                 # catálogo académico
│   └── <slug>-research.qmd
├── Tableros                      # catálogo ejecutivo
│   └── <slug>-dashboard.qmd
├── Notas                         # análisis rápidos
└── Perfil                        # CV se añade cuando exista el PDF real
```

Un tema no se duplica. Se procesa una vez y produce tres páginas con funciones distintas:

| Página | Pregunta que responde | Densidad | Identidad |
|---|---|---:|---|
| Caso | ¿Qué es y qué puedo abrir? | Media | Institucional compartida |
| Investigación | ¿Cómo se sostiene el resultado? | Baja, lectura larga | Manrope + dorado |
| Tablero | ¿Qué señal importa para decidir? | Alta, escaneable | Manrope + cian |

La familia tipográfica única del portafolio es **Manrope**. Investigación y tableros se distinguen por densidad, jerarquía, color y estructura, no mediante familias tipográficas diferentes.

## 2. Los dos ejes y sus referencias canónicas

Todo tema nace de **una** idea que se investiga una sola vez y se ramifica en dos productos hermanos. No son contenidos distintos: el artículo académico desarrolla la evidencia en extenso y el tablero traduce esa misma evidencia a lectura ejecutiva. Ambos consumen los mismos `outputs/` generados por código.

```text
Idea → investigación (datos + método + outputs verificados)
        ├── Eje académico → <slug>-research.qmd   (artículo estilo boletín)
        └── Eje BI        → <slug>-dashboard.qmd  (tablero ejecutivo)
```

El eje académico es el más extenso y suele desarrollarse primero; el tablero se deriva de él. Ninguno se redacta desde cero por separado.

| Eje | Referencia canónica aprobada | URL |
|---|---|---|
| Académico | Boletín analítico ITCER — Banco Central del Ecuador | <https://contenido.bce.fin.ec/documentos/informacioneconomica/SectorExterno/ix_TipoCambioReal.html> |
| BI | IRE · Precios — Ministerio de Economía y Finanzas | <https://ire.finanzas.gob.ec/s/r/precios.php> |

### Qué se toma del boletín BCE (eje académico)

- Cabecera de edición: título del tema + subtítulo de edición (p. ej. "Boletín mensual: mayo – 2026"), autoría y fecha de publicación visibles.
- Secciones numeradas y cortas con tabla de contenidos lateral persistente.
- Prosa que reporta la cifra exacta y su interpretación en la misma oración (nivel, variación, dirección del cambio).
- Figuras numeradas con título, subtítulo de cobertura ("En puntos y tasa de variación mensual, ene. 2022 – may. 2026") y leyenda de series.
- La estructura de secciones sigue siendo la del contrato de producto (§4): el boletín aporta la capa de presentación, no reemplaza el contrato.

### Qué se toma del IRE del MEF (eje BI)

- Fila de KPI: valor con unidad, periodo, dirección del cambio y banda inferior con la comparación interanual ("May 2025: 0.46%").
- Visual principal con selectores de rango reales (10A/5A/Todo) y control temporal tipo brush cuando el dato lo permite.
- Paneles de desglose comparables lado a lado con la misma gramática visual.
- Fuente visible al pie de cada panel; enlaces relacionados agrupados en la parte superior.
- La navegación lateral por dominios del IRE equivale aquí al catálogo `bi/` y a la barra de comando del tablero.

**Qué NO se copia de las referencias:** identidad visual institucional (logos, azules del Estado, banderas), librerías con marca de agua y controles decorativos que no filtran nada. La identidad visual es la del design system (`design-system/alan-del-rosario-portfolio/MASTER.md` y sus overrides en `pages/`).

## 3. Contrato de archivos por tema

```text
projects/
├── <slug>.qmd
├── <slug>-research.qmd
└── <slug>-dashboard.qmd
```

Las tres páginas usan el mismo `slug`. Las salidas numéricas se generan fuera de la capa de presentación y se incluyen desde una única carpeta `outputs/`. No se copian cifras manualmente entre páginas.

## 4. Contrato de producto

### Caso

- Enuncia alcance, no desarrolla el paper.
- Muestra estado editorial.
- Ofrece acciones diferenciadas: Investigación, Tablero, PDF y repo cuando existan.
- Explica de dónde provienen los outputs compartidos.

### Investigación

- Resumen, pregunta, teoría, datos, método, resultados, robustez, discusión, limitaciones, reproducibilidad y referencias.
- Ancho legible y tabla de contenidos.
- Barra de contexto hacia Caso, Tablero y PDF.
- Lenguaje causal según `PROTOCOLO_CALIDAD.md`.

### Tablero

- Barra de contexto, 3–5 KPIs, visual principal, desglose, lectura ejecutiva y gobierno de datos.
- Las interacciones deben funcionar; nunca se presentan filtros decorativos.
- La fuente, cobertura y fecha de actualización permanecen visibles.
- El enlace a la Investigación es persistente.

## 5. Estados

| Estado | Puede renderizarse | Puede marcarse listo | Puede publicarse |
|---|---:|---:|---:|
| Estructura | Sí | No | No |
| Resultado técnico verificado | Sí | No | No |
| Cuatro ojos completo | Sí | No | No |
| Checklist + aprobación de Alan | Sí | Sí | Sí |

El diseño nunca oculta estos estados. “Render correcto” no significa “publicado” ni “aprobado”.

## 6. Alta de un nuevo caso

1. Copiar los tres archivos de `_plantillas/portafolio/` y reemplazar `<slug>`.
2. Añadir `<slug>.qmd` al listing de `projects/index.qmd`.
3. Investigación y Tableros entran automáticamente a sus catálogos por el sufijo del archivo.
4. Conectar los mismos outputs generados en ambos productos.
5. Renderizar, revisar 375/768/1024/1440 px y ejecutar cuatro ojos.
6. Mantener `draft: true` y el aviso editorial hasta aprobación explícita de Alan.
7. Cambiar a `draft: false` únicamente después de checklist y aprobación; `draft-mode: gone` excluye borradores del render de producción.

## 7. Responsabilidad de contenido

Las skills del repositorio (`nuevo-caso`, `articulo-academico`, `dashboard-bi`) operacionalizan este contrato: la primera da de alta la tríada de archivos, las otras dos desarrollan cada eje respetando sus referencias canónicas. Cualquier conflicto entre una skill y este documento se resuelve a favor de este documento.

Claude puede desarrollar texto y análisis dentro de estos contratos. No debe cambiar navegación, tokens, sufijos, jerarquía de producto o reglas de dashboard sin una decisión explícita de Alan.
