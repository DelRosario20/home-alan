"""Puerta técnica: comprueba trazabilidad, artefactos y lenguaje del post."""

from __future__ import annotations

import json
import re
from pathlib import Path


BASE = Path(__file__).resolve().parents[1]


def main() -> None:
    required = [
        BASE / "data" / "homicidios_ecuador_wb.csv",
        BASE / "data" / "fuente.json",
        BASE / "outputs" / "indicadores.json",
        BASE / "outputs" / "resultado_principal.md",
        BASE / "outputs" / "trazabilidad.md",
        BASE / "outputs" / "tasa_homicidios_ecuador.svg",
    ]
    missing = [str(path.relative_to(BASE)) for path in required if not path.exists()]
    if missing:
        raise AssertionError(f"Faltan artefactos: {missing}")

    metrics = json.loads((BASE / "outputs" / "indicadores.json").read_text(encoding="utf-8"))
    generated = (BASE / "outputs" / "resultado_principal.md").read_text(encoding="utf-8")
    post = (BASE / "index.qmd").read_text(encoding="utf-8")

    for value in [metrics["tasa_minima"], metrics["tasa_maxima"], metrics["anio_minimo"], metrics["anio_maximo"]]:
        visible_value = str(value).replace(".", ",")
        if visible_value not in generated:
            raise AssertionError(f"El resultado generado no contiene el valor trazable {value}.")

    if "{{< include outputs/resultado_principal.md >}}" not in post:
        raise AssertionError("El post no incluye el resultado generado por código.")

    causal_terms = re.findall(r"\b(causó|provocó|debido a)\b", post, flags=re.I)
    if causal_terms:
        raise AssertionError(f"Lenguaje causal no sustentado: {causal_terms}")

    print("Verificación técnica superada: artefactos completos y resultado trazable.")


if __name__ == "__main__":
    main()
