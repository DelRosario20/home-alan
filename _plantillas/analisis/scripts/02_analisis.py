"""Valida la serie, calcula indicadores y genera los artefactos publicables.

Contrato: todo número, tabla o figura que aparezca en las páginas del sitio
nace AQUÍ (o en 04_investigacion.py) y se escribe en outputs/. Las páginas
refinadas solo consumen esos archivos; nunca se transcriben cifras a mano.
Genera: outputs/*.md (includes de texto con cifras), outputs/*.json (KPIs),
outputs/*.svg y *.png (figuras), outputs/*.csv (tablas derivadas).
Formato numérico: coma decimal (es-EC) en los .md visibles.
Modelo completo: posts/2026-07-homicidios-wb/scripts/02_analisis.py
"""

from __future__ import annotations

from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"
OUTPUTS = BASE / "outputs"


def format_es(value: float, decimals: int) -> str:
    return f"{value:.{decimals}f}".replace(".", ",")


def main() -> None:
    OUTPUTS.mkdir(exist_ok=True)
    raise NotImplementedError(
        "Implementar: cargar data/, validar esquema (columnas, orden, rangos), "
        "calcular indicadores y escribir los artefactos en outputs/."
    )


if __name__ == "__main__":
    main()
