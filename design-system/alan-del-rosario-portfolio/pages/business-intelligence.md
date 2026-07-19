# Override — Business Intelligence

Estas reglas sustituyen al sistema maestro solo en dashboards.

## Trabajo de la página

Permitir que un reclutador o decisor responda en menos de 30 segundos: qué ocurre, frente a qué periodo, con qué cobertura, qué tan actual es y dónde está la evidencia.

## Estructura obligatoria

1. Barra de contexto: dominio, cobertura, frecuencia, fuente, actualización y estado editorial.
2. KPIs: tres a cinco, con unidad y comparación visible.
3. Visual principal: tendencia o comparación que responda la pregunta ejecutiva.
4. Desglose: territorio, categoría o periodo, solo si el dato lo permite.
5. Lectura ejecutiva: señal, decisión informada y límite crítico.
6. Gobierno: fuente, trazabilidad, calidad, enlace al Research y descarga de datos cuando corresponda.

## Apariencia

- Lienzo claro `#EEF3F8`; barra superior azul noche.
- Retícula de 12 columnas y ancho útil hasta 1400 px.
- Densidad alta, tarjetas con radio de 4 px, borde visible y sombra mínima.
- Cian identifica datos e interacción. Dorado se reserva para vínculo metodológico; nunca para series arbitrarias.
- Cifras tabulares; títulos de panel en 10–12 px y mayúsculas moderadas.

## Interacción

- Un control visible debe funcionar. Si el gráfico no puede responder, mostrar contexto estático, no un filtro simulado.
- Filtros globales arriba: periodo, geografía y segmento cuando existan en la fuente.
- Todo filtro indica selección actual y ofrece restablecimiento.
- Hover aporta valor exacto, pero la lectura central no depende del hover.
- Series diferenciadas por color y estilo; incluir leyenda y alternativa tabular.

## Prohibido

- Párrafos académicos extensos dentro de tarjetas.
- Más de cinco KPIs en la primera fila.
- Gauges sin meta real, tortas con más de cinco categorías o mapas sin tabla alternativa.
- Colores rojo/verde como única señal.
- Controles decorativos o datos con fechas de actualización ambiguas.
