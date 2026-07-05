# Control de calidad — post de homicidios (Banco Mundial)

**Estado:** borrador técnico para revisión. No aprobado para publicación.

## Puertas aplicables

- [x] Puerta 0: pregunta descriptiva y ausencia de estimando causal declaradas antes de interpretar.
- [x] Puerta 1: fuente oficial, indicador, cobertura, fecha de descarga y URL de API documentados.
- [x] Puerta 2: no hay filtros ni imputaciones; los años nulos se registran explícitamente.
- [x] Puerta 4: lenguaje de descripción y asociación; límites declarados.
- [ ] Puerta 5: pendiente de revisión independiente y aprobación de Alan.

## Checklist de post rápido

- [x] Fuente citada con período y fecha de descarga; script de descarga incluido.
- [x] Todos los números centrales proceden de `outputs/indicadores.json` y se insertan desde output generado.
- [x] No aplica factor de expansión: no es una encuesta de hogares.
- [x] Señales de riesgo revisadas: brecha 2003–2006 visible; no hay inferencia causal, regresión ni desagregaciones pequeñas.
- [x] Gráfico con título-hallazgo, ejes, fuente, elaboración y texto alternativo.
- [x] Pruebas y verificación técnica ejecutadas.
- [x] Render local sin errores ni warnings.
- [x] Ortografía revisada por el agente productor.
- [ ] Revisión de cuatro ojos independiente (quién: ______; fecha: ______).
- [ ] Aprobación explícita de Alan.

## Evidencia de ejecución

Comando: `./reproducir.ps1`

La ejecución valida los valores ancla 2017/2023, confirma que 2003–2006 no fueron interpolados, recalcula el multiplicador, comprueba artefactos y renderiza el post. El commit conserva datos, scripts, pruebas y outputs en la misma versión.
