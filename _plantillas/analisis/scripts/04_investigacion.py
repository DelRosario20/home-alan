"""Modelado del eje académico: estimaciones, robustez y sus artefactos.

Contrato: aquí vive el análisis formal que alimenta <slug>-research.qmd
(modelos, selección por criterio de información, robustez). Sus resultados
también van a outputs/ — el artículo los consume por include, no ejecuta
código. Si el caso es puramente descriptivo, este script puede eliminarse
(y quitarse de reproducir.ps1).
Modelo completo: posts/2026-07-homicidios-wb/scripts/04_investigacion.py
"""

from __future__ import annotations

from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
OUTPUTS = BASE / "outputs"


def main() -> None:
    raise NotImplementedError(
        "Implementar: estimar el modelo del eje académico y escribir sus "
        "artefactos (parámetros, tablas, figuras de robustez) en outputs/."
    )


if __name__ == "__main__":
    main()
