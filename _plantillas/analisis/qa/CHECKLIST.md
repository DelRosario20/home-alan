# Checklist de calidad del caso <slug>

Registro de verificaciones antes de pedir aprobación editorial.
(Complementa, no sustituye, el `_gobernanza/CHECKLIST_PUBLICACION.md`.)

- [ ] `reproducir.ps1` corre de punta a punta sin errores.
- [ ] Tests en verde (`python -m unittest discover -s tests -v`).
- [ ] Todo número visible en las páginas proviene de `outputs/` (cero cifras a mano).
- [ ] Las rutas cruzadas de la tríada (`projects/<slug>*.qmd` → `posts/<slug-largo>/`) resuelven.
- [ ] El slug de la carpeta no se ha renombrado desde el alta.
- [ ] Lenguaje acorde al alcance (descriptivo vs. causal) verificado por `03_verificar.py`.
- [ ] `draft: true` sigue activo hasta la aprobación de Alan.
