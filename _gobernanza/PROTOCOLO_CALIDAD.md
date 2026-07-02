# Protocolo de Calidad Económica y Econométrica

Ningún análisis avanza a la puerta siguiente sin cerrar la anterior. Aplica completo a proyectos insignia; los posts rápidos usan la versión reducida marcada con ⚡.

## Puerta 0 — Coherencia teórica (ANTES de tocar datos) ⚡

Se escribe un pre-registro ligero (5–10 líneas en el README del análisis): pregunta, marco teórico que la sustenta, relación esperada entre variables y **dirección causal esperada con su justificación**. Regla central: la teoría económica define la especificación; los datos la estiman.

- Si la relación es simultánea o bidireccional (ej. gasto↔PIB: identidad contable + multiplicador), se declara y se trata con el método adecuado (variables instrumentales, rezagos, VAR/Granger, diseño cuasiexperimental) — o el análisis se limita explícitamente a describir asociación.
- Si el resultado estimado contradice la teoría (signo inesperado), NO se publica como hallazgo novedoso por defecto: primero se sospecha del dato, la limpieza y la especificación. Solo si sobrevive a esa auditoría se presenta, con la contradicción discutida abiertamente.

## Puerta 1 — Datos ⚡

Fuente oficial identificada y citada (INEC/ANDA, BCE, Datos Abiertos, Banco Mundial), con período, cobertura, unidad de análisis y fecha de descarga. Encuestas de hogares (ENEMDU, ENCV): **uso obligatorio del factor de expansión** y diseño muestral; nunca porcentajes sin ponderar. Datos macro del BCE: verificar si la serie es provisional o revisada. Diccionario de variables usadas en el repo.

## Puerta 2 — Limpieza y procesamiento

Script reproducible numerado (`01_limpieza.R`), con log de decisiones: tratamiento de NA, outliers (criterio explícito, no borrado silencioso), filtros aplicados y **conteo de observaciones antes/después de cada filtro**. Si se pierde >10% de la muestra en un paso, se documenta el porqué y se evalúa sesgo de selección.

## Puerta 3 — Modelación

Supuestos del método chequeados y reportados (según aplique: heterocedasticidad, autocorrelación, multicolinealidad, estacionariedad en series, separación en logit). Al menos una especificación alternativa como robustez. Distinguir siempre **significancia estadística de relevancia económica**: un coeficiente significativo pero de magnitud irrisoria se reporta como tal.

## Puerta 4 — Interpretación ⚡

Lenguaje calibrado al diseño: "causa/efecto/impacto" SOLO con identificación causal defendible; en caso contrario "asociación", "correlación", "se relaciona con". Limitaciones declaradas (siempre existen). Prohibido extrapolar fuera del soporte de los datos o del período analizado.

## Puerta 5 — Publicación ⚡

`_gobernanza/CHECKLIST_PUBLICACION.md` completo + regla de cuatro ojos (AGENTS.md) + aprobación de Alan. Insignias: 24 horas de reposo entre "terminado" y publicado, releer en frío.

---

## Señales de riesgo (detener y auditar si aparece cualquiera)

- Signo de coeficiente contrario a la teoría sin explicación trabajada
- R² o ajuste "demasiado bueno" (sospecha: variable dependiente filtrada en los regresores, fuga de información, identidad contable)
- Correlación entre dos series con tendencia común sin controlar tendencia (espuria clásica)
- Quiebres estructurales de Ecuador ignorados: dolarización (2000), COVID (2020), crisis de seguridad (2021+), cambios metodológicos del INEC
- Muestra pequeña o celdas con pocas observaciones al desagregar (típico al cruzar provincia × grupo)
- Resultados que solo "funcionan" con una especificación exacta (indicio de p-hacking involuntario)
- Porcentajes de encuesta sin factor de expansión
- Cifra que no se puede rastrear a un output de código ejecutado

## Errores ya publicados (protocolo de erratas)

Un error detectado tras publicar NUNCA se borra en silencio. Se corrige el contenido, se añade nota visible de errata con fecha ("Corrección [fecha]: la versión anterior indicaba X; lo correcto es Y, debido a Z") y commit descriptivo. En LinkedIn: comentario propio en el post corrigiendo. La corrección transparente construye credibilidad; el borrado silencioso la destruye.
