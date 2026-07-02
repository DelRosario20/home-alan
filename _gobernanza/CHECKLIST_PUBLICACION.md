# Checklist de Publicación

Se copia al final del archivo del análisis (o al PR) y se marca casilla por casilla. Si una casilla no se puede marcar, NO se publica.

## Checklist ⚡ POST RÁPIDO (blog + LinkedIn)

**Fondo**
- [ ] La idea pasó la Puerta 0 (coherencia teórica declarada en 5 líneas)
- [ ] Fuente citada con período y fecha de descarga; datos en `data/` del post o script de descarga
- [ ] Si es encuesta: factor de expansión aplicado
- [ ] Todos los números del texto coinciden con el output del código (re-ejecutado en limpio)
- [ ] Lenguaje causal solo si corresponde; si no, asociación
- [ ] Ninguna señal de riesgo del protocolo activa

**Forma**
- [ ] Gráfico con título-hallazgo, ejes legibles, pie "Fuente: … Elaboración: Alan Del Rosario — [sitio]"
- [ ] `quarto render` sin errores ni warnings
- [ ] Ortografía revisada (es diferencia entre profesional y amateur)
- [ ] Revisión de cuatro ojos hecha (quién: ______)
- [ ] Aprobación de Alan

## Checklist PROYECTO INSIGNIA (adicional al anterior)

- [ ] Las 6 puertas del PROTOCOLO_CALIDAD cerradas y documentadas
- [ ] Repo `proj-*` reproducible de punta a punta: datos (o script de descarga) → limpieza → modelos → figuras
- [ ] README del repo con: resumen, hallazgo principal, cómo reproducir, changelog vs. versión original de la ponencia
- [ ] Robustez: al menos una especificación alternativa reportada
- [ ] Paper (PDF) y dashboard (HTML) generados desde los mismos resultados — sin cifras divergentes entre ambos
- [ ] Página en `projects/` del sitio con botones a paper/dashboard/repo funcionando
- [ ] `.gitignore` verificado: ningún dato sensible ni clave en el historial
- [ ] Reposo de 24 horas + relectura en frío
- [ ] Aprobación final de Alan

## Registro

| Fecha | Pieza | Tipo | Revisor 4-ojos | Resultado |
|---|---|---|---|---|
| | | | | |
