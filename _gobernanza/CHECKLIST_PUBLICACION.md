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
- [ ] Las rutas cruzadas de la tríada resuelven (todo `../posts/<slug>/...` citado en `projects/` existe en disco)
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

## Runbook de publicación (ejecuta: Antigravity)

El deploy a `gh-pages` es mandato exclusivo del rol Antigravity (ver `ROLES_IA.md`).
Publicar es un acto editorial, no técnico: sin las precondiciones completas, el
runbook no se inicia.

**Precondiciones (todas, sin excepción):**
1. Checklist aplicable completo (arriba) y registrado.
2. Aprobación explícita de Alan para esta publicación concreta.
3. Working tree limpio y parado en `main` (`git status` sin cambios; NUNCA
   publicar desde un checkout de `gh-pages` ni con cambios sin commitear).
4. Tests del caso en verde: `python -m unittest discover -s posts/<slug>/tests -v`.

**Secuencia:**
1. `quarto render` en la raíz — debe terminar sin errores ni warnings.
2. Revisión rápida de `_site/` (portada, caso, research, dashboard abren y las
   figuras cargan).
3. `quarto publish gh-pages` — único comando que toca la rama de deploy.
4. Verificar el sitio en vivo (https://delrosario20.github.io/home-alan/):
   página publicada visible, sin 404 nuevos, búsqueda funciona.
5. Registrar la publicación en la tabla de abajo.

**Si algo falla en cualquier paso:** se detiene, se reporta a Alan, y no se
reintenta "a ver si pasa". Los errores tras publicar se corrigen con fe de
erratas visible, nunca en silencio.

## Registro

| Fecha | Pieza | Tipo | Revisor 4-ojos | Resultado |
|---|---|---|---|---|
| 2026-07-21 | home-alan (Caso Homicidios y Estructura) | Sitio / Proyecto | Antigravity (QA) / Alan (Director) | Publicado para revisión |
