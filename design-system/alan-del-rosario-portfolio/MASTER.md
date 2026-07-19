# Sistema visual — Portafolio Alan Del Rosario

Fuente de verdad para la interfaz. Antes de editar una página, revisar también `pages/` por si existe una especificación particular.

## Dirección

**Idea:** institucionalidad económica ecuatoriana + evidencia trazable. La referencia del BCE aporta orden, azul profundo, navegación estable y lectura de datos; el portafolio reduce su densidad institucional y adopta una identidad personal más clara.

**Firma:** el “boletín de evidencia” convierte cada pieza en una ficha legible: estado editorial, fuente, cobertura, método y rutas de lectura. La página se recuerda por su precisión informativa, no por un efecto visual.

**No usar:** estética fintech, verde de trading, fondos oscuros en todo el sitio, gradientes decorativos, glassmorphism generalizado, tarjetas redondeadas idénticas para Research y BI o código monoespaciado como tipografía principal.

## Tokens

| Rol | Token | Valor | Uso |
|---|---|---:|---|
| Institucional | `--adr-navy-950` | `#071B33` | Navbar, hero, footer |
| Marca | `--adr-blue-800` | `#123B7A` | Acciones, enlaces, foco secundario |
| BI | `--adr-cyan-400` | `#18A9C1` | Dashboard, datos, conexiones |
| Research | `--adr-gold-400` | `#D9A63A` | Paper, método, evidencia académica |
| Lienzo | `--adr-paper` | `#F6F8FB` | Fondo general claro |
| Texto | `--adr-ink` | `#17263A` | Contenido principal |
| Secundario | `--adr-muted` | `#586A7E` | Metadatos y ayuda |
| Borde | `--adr-line` | `#D7E0EA` | Separación estructural |

Los colores de estado no sustituyen texto: toda alerta incluye etiqueta y explicación.

## Tipografía

- **Familia única del portafolio:** Manrope, pesos 400–800, para interfaz, títulos, lectura extensa, investigación y tableros.
- La jerarquía se construye con tamaño, peso, ancho y espaciado; no se introducen familias serif, mono ni display adicionales.
- Indicadores y tablas usan Manrope con `font-variant-numeric: tabular-nums`.
- Cuerpo mínimo: 16 px en sitio; 14 px solo en dashboard de escritorio, con reflujo móvil.
- Longitud de lectura académica: 65–75 caracteres.

## Escala y forma

- Espaciado basado en 4/8 px: 8, 12, 16, 24, 32, 48, 64, 96.
- Radios: 4 px en controles y 0–4 px en módulos informativos.
- Sombras: reservadas para navegación o superposición; la estructura principal usa planos y bordes.
- Objetivos interactivos: mínimo 44 × 44 px.
- Movimiento: 150–200 ms para estados; ninguna animación ambiental continua.

## Componentes

### Navegación principal

Fondo azul noche, ubicación activa visible, marca en dos líneas y máximo cinco destinos primarios. Research y BI siempre aparecen como rutas separadas.

### Página de caso

Es el punto común de un tema. Contiene pregunta, alcance, evidencia compartida y dos tarjetas de salida. No imita ni al paper ni al dashboard.

### Tarjeta Research

Borde superior dorado, título serif, mayor espacio vertical y vocabulario de profundidad: pregunta, método, robustez, limitaciones.

### Tarjeta BI

Borde o acento cian, tipografía de interfaz, densidad mayor y vocabulario ejecutivo: KPI, tendencia, desglose, alerta, actualización.

### Estado editorial

Las páginas con resultados no aprobados muestran un aviso textual. La verificación técnica nunca equivale a aprobación editorial.

## Responsive y accesibilidad

- Puntos de control: 375, 768, 1024 y 1440 px.
- Sin desplazamiento horizontal en 375 px.
- Foco visible de 3 px; navegación completa por teclado.
- Contraste mínimo 4.5:1 para texto normal.
- `prefers-reduced-motion` desactiva transiciones no esenciales.
- Imágenes significativas con `alt`; gráficos con resumen textual y tabla alternativa cuando sean interactivos.
