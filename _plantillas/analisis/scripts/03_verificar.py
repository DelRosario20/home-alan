"""QA automático de los outputs: lenguaje, consistencia y rutas.

Contrato: corre al final de la cadena (tras scripts y tests) y falla ruidoso
si un artefacto viola las reglas editoriales — p. ej. lenguaje causal en un
caso descriptivo ("provocó", "causó"), cifras inconsistentes entre outputs,
o rutas referenciadas por las páginas de projects/ que no existen en disco.
Modelo completo: posts/2026-07-homicidios-wb/scripts/03_verificar.py
"""

from __future__ import annotations

from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
OUTPUTS = BASE / "outputs"


def main() -> None:
    raise NotImplementedError(
        "Implementar: leer outputs/*.md y validar reglas de lenguaje; "
        "verificar que toda ruta ../posts/<slug>/ citada en projects/<slug>*.qmd "
        "existe en disco (ver qa/verificar_rutas.py del caso modelo)."
    )


if __name__ == "__main__":
    main()
