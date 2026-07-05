"""Valida la serie, calcula indicadores y genera artefactos publicables."""

from __future__ import annotations

import csv
import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"
OUTPUTS = BASE / "outputs"
EXPECTED_COLUMNS = {"anio", "tasa_homicidios"}


def format_es(value: float, decimals: int) -> str:
    return f"{value:.{decimals}f}".replace(".", ",")


def load_data() -> list[dict[str, float]]:
    with (DATA / "homicidios_ecuador_wb.csv").open(encoding="utf-8") as file:
        reader = csv.DictReader(file)
        if set(reader.fieldnames or []) != EXPECTED_COLUMNS:
            raise ValueError(f"Esquema inesperado: {reader.fieldnames}")
        rows = [
            {"anio": int(row["anio"]), "tasa_homicidios": float(row["tasa_homicidios"])}
            for row in reader
        ]

    years = [row["anio"] for row in rows]
    if years != sorted(set(years)):
        raise ValueError("Los años deben ser únicos y estar ordenados.")
    if any(row["tasa_homicidios"] < 0 for row in rows):
        raise ValueError("Una tasa de homicidios no puede ser negativa.")
    return rows


def calculate(rows: list[dict[str, float]]) -> dict[str, float | int | list[int]]:
    minimum = min(rows, key=lambda row: row["tasa_homicidios"])
    maximum = max(rows, key=lambda row: row["tasa_homicidios"])
    ratio = maximum["tasa_homicidios"] / minimum["tasa_homicidios"]
    change_pct = (ratio - 1) * 100
    requested = set(range(2000, 2026))
    available = {int(row["anio"]) for row in rows}
    return {
        "anio_minimo": int(minimum["anio"]),
        "tasa_minima": round(minimum["tasa_homicidios"], 2),
        "anio_maximo": int(maximum["anio"]),
        "tasa_maxima": round(maximum["tasa_homicidios"], 2),
        "multiplicador_min_max": round(ratio, 2),
        "variacion_min_max_pct": round(change_pct, 1),
        "diferencia_puntos": round(maximum["tasa_homicidios"] - minimum["tasa_homicidios"], 2),
        "observaciones": len(rows),
        "anios_sin_dato": sorted(requested - available),
    }


def write_text_outputs(metrics: dict[str, float | int | list[int]]) -> None:
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    (OUTPUTS / "indicadores.json").write_text(
        json.dumps(metrics, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    result = (
        f"Entre el mínimo observado de **{format_es(metrics['tasa_minima'], 2)}** en "
        f"**{metrics['anio_minimo']}** y el máximo de **{format_es(metrics['tasa_maxima'], 2)}** en "
        f"**{metrics['anio_maximo']}**, la tasa resultó **{format_es(metrics['multiplicador_min_max'], 1)} veces** "
        f"la del mínimo (**{format_es(metrics['variacion_min_max_pct'], 1)}%** más). La diferencia fue de "
        f"**{format_es(metrics['diferencia_puntos'], 2)} homicidios por cada 100.000 habitantes**.\n"
    )
    (OUTPUTS / "resultado_principal.md").write_text(result, encoding="utf-8")

    missing = ", ".join(str(year) for year in metrics["anios_sin_dato"])
    trace = (
        "| Control | Resultado |\n|---|---:|\n"
        f"| Observaciones no nulas | {metrics['observaciones']} |\n"
        f"| Años solicitados sin dato | {missing} |\n"
        "| Imputaciones o interpolaciones | Ninguna |\n"
        "| Unidad | Homicidios por 100.000 habitantes |\n"
    )
    (OUTPUTS / "trazabilidad.md").write_text(trace, encoding="utf-8")


def plot(rows: list[dict[str, float]], metrics: dict[str, float | int | list[int]]) -> None:
    years = [int(row["anio"]) for row in rows]
    rates = [row["tasa_homicidios"] for row in rows]
    color = "#087F73"
    ink = "#17324D"

    fig, axis = plt.subplots(figsize=(10.8, 6.1), layout="constrained")
    fig.patch.set_facecolor("#FFFFFF")
    axis.set_facecolor("#FFFFFF")
    axis.plot(years, rates, color=color, linewidth=2.8, zorder=2)
    axis.scatter(years, rates, color=color, edgecolor="white", linewidth=0.8, s=42, zorder=3)

    for year, value, label in [
        (metrics["anio_minimo"], metrics["tasa_minima"], "Mínimo observado"),
        (metrics["anio_maximo"], metrics["tasa_maxima"], "Máximo observado"),
    ]:
        axis.annotate(
            f"{label}\n{format_es(value, 2)} · {year}",
            xy=(year, value),
            xytext=(-72 if year == metrics["anio_maximo"] else 12, 18),
            textcoords="offset points",
            color=ink,
            fontsize=10,
            fontweight="bold",
            arrowprops={"arrowstyle": "-", "color": "#7B8794", "lw": 1},
        )

    axis.set_title(
        "La tasa observada alcanzó en 2023 casi ocho veces su mínimo de 2017",
        loc="left",
        color=ink,
        fontsize=17,
        fontweight="bold",
        pad=16,
    )
    axis.set_ylabel("Homicidios por 100.000 habitantes", color=ink)
    axis.set_xlabel("")
    axis.set_xlim(1999.5, 2023.8)
    axis.set_ylim(0, 51)
    axis.xaxis.set_major_locator(MultipleLocator(3))
    axis.yaxis.set_major_locator(MultipleLocator(10))
    axis.grid(axis="y", color="#DCE3E8", linewidth=0.8)
    axis.grid(axis="x", visible=False)
    axis.tick_params(colors="#566573")
    for spine in axis.spines.values():
        spine.set_visible(False)

    fig.text(
        0.01,
        -0.025,
        "Fuente: Banco Mundial, indicador VC.IHR.PSRC.P5. Sin interpolar 2003–2006.\n"
        "Elaboración: Alan Del Rosario — delrosario20.github.io/home-alan",
        color="#566573",
        fontsize=8.7,
    )
    svg_path = OUTPUTS / "tasa_homicidios_ecuador.svg"
    fig.savefig(svg_path, bbox_inches="tight")
    plt.close(fig)
    # Matplotlib añade espacios finales a rutas multilínea; normalizarlos mantiene
    # el artefacto generado compatible con `git diff --check`.
    svg = svg_path.read_text(encoding="utf-8")
    svg_path.write_text(
        "\n".join(line.rstrip() for line in svg.splitlines()) + "\n", encoding="utf-8"
    )


def main() -> None:
    rows = load_data()
    metrics = calculate(rows)
    write_text_outputs(metrics)
    plot(rows, metrics)
    print(f"Análisis generado: {metrics['observaciones']} observaciones; máximo {metrics['tasa_maxima']}.")


if __name__ == "__main__":
    main()
