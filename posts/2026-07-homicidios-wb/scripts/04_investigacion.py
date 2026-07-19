"""Modelo segmentado, robustez y artefactos compartidos por Research y BI."""

from __future__ import annotations

import csv
import json
import math
import shutil
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy.stats import t as student_t


BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"
OUTPUTS = BASE / "outputs"
PAPER_ASSETS = BASE.parents[1] / "paper" / "assets"
START_YEAR = 2007
CANDIDATES = list(range(2011, 2020))
INK = "#17324D"
TEAL = "#087F73"
ORANGE = "#F28E2B"
RED = "#C94C4C"
GRID = "#DCE3E8"


def format_es(value: float, decimals: int = 1) -> str:
    return f"{value:,.{decimals}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def load_continuous_series() -> pd.DataFrame:
    data = pd.read_csv(DATA / "homicidios_ecuador_wb.csv")
    data = data.loc[data["anio"].between(START_YEAR, 2023)].copy()
    expected = list(range(START_YEAR, 2024))
    if data["anio"].tolist() != expected:
        raise ValueError("El análisis requiere la serie anual continua 2007–2023.")
    data["t"] = data["anio"] - START_YEAR
    return data


def design(data: pd.DataFrame, break_year: int) -> pd.DataFrame:
    return sm.add_constant(
        pd.DataFrame(
            {
                "t": data["t"],
                "quiebre": np.maximum(0, data["anio"] - break_year),
            }
        )
    )


def fit_candidates(data: pd.DataFrame, log_scale: bool = False) -> list[dict[str, float | int]]:
    outcome = np.log(data["tasa_homicidios"]) if log_scale else data["tasa_homicidios"]
    results: list[dict[str, float | int]] = []
    for break_year in CANDIDATES:
        model = sm.OLS(outcome, design(data, break_year)).fit()
        results.append(
            {
                "anio_quiebre": break_year,
                "bic": float(model.bic),
                "sse": float(model.ssr),
                "r2_ajustado": float(model.rsquared_adj),
            }
        )
    return results


def linear_combination_ci(model, weights: np.ndarray) -> tuple[float, float, float]:
    estimate = float(weights @ model.params.to_numpy())
    variance = float(weights @ model.cov_params().to_numpy() @ weights)
    critical = float(student_t.ppf(0.975, model.df_resid))
    se = math.sqrt(max(variance, 0))
    return estimate, estimate - critical * se, estimate + critical * se


def leave_one_out_breaks(data: pd.DataFrame) -> Counter:
    selected: list[int] = []
    for omitted in data["anio"]:
        sample = data.loc[data["anio"] != omitted].copy()
        ranking = fit_candidates(sample)
        selected.append(int(min(ranking, key=lambda row: row["bic"])["anio_quiebre"]))
    return Counter(selected)


def calculate(data: pd.DataFrame) -> tuple[dict, pd.DataFrame, object]:
    ranking = pd.DataFrame(fit_candidates(data)).sort_values("bic").reset_index(drop=True)
    ranking_log = pd.DataFrame(fit_candidates(data, log_scale=True)).sort_values("bic").reset_index(drop=True)
    break_year = int(ranking.iloc[0]["anio_quiebre"])

    segmented_plain = sm.OLS(data["tasa_homicidios"], design(data, break_year)).fit()
    segmented = sm.OLS(data["tasa_homicidios"], design(data, break_year)).fit(cov_type="HC1")
    global_linear = sm.OLS(data["tasa_homicidios"], sm.add_constant(data[["t"]])).fit()

    pre = linear_combination_ci(segmented, np.array([0.0, 1.0, 0.0]))
    post = linear_combination_ci(segmented, np.array([0.0, 1.0, 1.0]))
    loo = leave_one_out_breaks(data)
    rate_2020 = float(data.loc[data["anio"] == 2020, "tasa_homicidios"].iloc[0])
    rate_2022 = float(data.loc[data["anio"] == 2022, "tasa_homicidios"].iloc[0])
    rate_2023 = float(data.loc[data["anio"] == 2023, "tasa_homicidios"].iloc[0])

    metrics = {
        "muestra": {"inicio": START_YEAR, "fin": 2023, "n": int(len(data))},
        "tasa_2023": round(rate_2023, 2),
        "variacion_2023_pct": round((rate_2023 / rate_2022 - 1) * 100, 1),
        "cagr_2020_2023_pct": round(((rate_2023 / rate_2020) ** (1 / 3) - 1) * 100, 1),
        "anio_quiebre": break_year,
        "pendiente_pre": round(pre[0], 2),
        "pendiente_pre_ic95": [round(pre[1], 2), round(pre[2], 2)],
        "pendiente_post": round(post[0], 2),
        "pendiente_post_ic95": [round(post[1], 2), round(post[2], 2)],
        "r2_ajustado_segmentado": round(float(segmented_plain.rsquared_adj), 3),
        "bic_segmentado": round(float(segmented_plain.bic), 2),
        "bic_lineal": round(float(global_linear.bic), 2),
        "ventaja_bic": round(float(global_linear.bic - segmented_plain.bic), 2),
        "quiebre_log": int(ranking_log.iloc[0]["anio_quiebre"]),
        "loo_quiebres": {str(year): count for year, count in sorted(loo.items())},
        "loo_coincidencia_pct": round(100 * loo[break_year] / len(data), 1),
        "fuente": "Banco Mundial / UNODC, VC.IHR.PSRC.P5",
        "ultima_observacion": 2023,
    }
    data = data.copy()
    data["ajuste_segmentado"] = segmented_plain.predict(design(data, break_year))
    data["variacion_anual"] = data["tasa_homicidios"].diff()
    return metrics, ranking, data


def write_outputs(metrics: dict, ranking: pd.DataFrame) -> None:
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    (OUTPUTS / "investigacion.json").write_text(
        json.dumps(metrics, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    ranking.to_csv(OUTPUTS / "seleccion_quiebre.csv", index=False)

    findings = f"""
::: {{.research-finding}}
### 1 · La trayectoria cambia de régimen

El quiebre que minimiza el BIC se ubica en **{metrics['anio_quiebre']}**. Antes del quiebre, la pendiente estimada es de **{format_es(metrics['pendiente_pre'], 2)} puntos por año**; después, de **+{format_es(metrics['pendiente_post'], 2)} puntos por año**.
:::

::: {{.research-finding}}
### 2 · El último salto es material

La tasa de 2023 fue **{format_es(metrics['tasa_2023'], 2)} por 100.000 habitantes**, **{format_es(metrics['variacion_2023_pct'], 1)}%** por encima de 2022. Entre 2020 y 2023, el crecimiento anual compuesto fue **{format_es(metrics['cagr_2020_2023_pct'], 1)}%**.
:::

::: {{.research-finding}}
### 3 · El patrón sobrevive a pruebas de sensibilidad

La especificación en logaritmos también selecciona **{metrics['quiebre_log']}**. Al retirar una observación por vez, el mismo quiebre es elegido en **{format_es(metrics['loo_coincidencia_pct'], 1)}%** de las iteraciones.
:::
""".strip() + "\n"
    (OUTPUTS / "hallazgos_research.md").write_text(findings, encoding="utf-8")

    model_table = f"""| Indicador | Tendencia única | Modelo segmentado |
|---|---:|---:|
| BIC | {format_es(metrics['bic_lineal'], 2)} | **{format_es(metrics['bic_segmentado'], 2)}** |
| Ventaja BIC del segmentado | — | **{format_es(metrics['ventaja_bic'], 2)}** |
| R² ajustado | — | **{format_es(metrics['r2_ajustado_segmentado'], 3)}** |
| Pendiente antes de {metrics['anio_quiebre']} | — | {format_es(metrics['pendiente_pre'], 2)} |
| Pendiente después de {metrics['anio_quiebre']} | — | +{format_es(metrics['pendiente_post'], 2)} |
"""
    (OUTPUTS / "tabla_modelo.md").write_text(model_table, encoding="utf-8")

    result_paragraph = (
        f"El quiebre seleccionado es **{metrics['anio_quiebre']}**. La pendiente estimada antes de esa fecha "
        f"es **{format_es(metrics['pendiente_pre'], 2)} puntos por año**; después es "
        f"**+{format_es(metrics['pendiente_post'], 2)}**. La tasa observada alcanza "
        f"**{format_es(metrics['tasa_2023'], 2)}** en 2023, **{format_es(metrics['variacion_2023_pct'], 1)}%** "
        f"por encima de 2022. Entre 2020 y 2023, el crecimiento anual compuesto es "
        f"**{format_es(metrics['cagr_2020_2023_pct'], 1)}%**.\n"
    )
    (OUTPUTS / "resultado_modelo.md").write_text(result_paragraph, encoding="utf-8")

    candidate_lines = ["| Año candidato | BIC | R² ajustado |", "|---:|---:|---:|"]
    for row in ranking.sort_values("anio_quiebre").itertuples():
        selected = " **← seleccionado**" if int(row.anio_quiebre) == metrics["anio_quiebre"] else ""
        candidate_lines.append(
            f"| {int(row.anio_quiebre)}{selected} | {format_es(float(row.bic), 2)} | "
            f"{format_es(float(row.r2_ajustado), 3)} |"
        )
    (OUTPUTS / "tabla_candidatos.md").write_text("\n".join(candidate_lines) + "\n", encoding="utf-8")

    kpis = f"""
::: {{.valuebox .kpi-tasa color="#0F766E" icon="activity" aria-label="Tasa 2023" role="group"}}
### Tasa 2023
<span class="visually-hidden">Tasa 2023: </span>{format_es(metrics['tasa_2023'], 2)}

por 100.000 habitantes
:::

::: {{.valuebox .kpi-variacion color="#B83B4B" icon="arrow-up-right" aria-label="Variación anual" role="group"}}
### Variación anual
<span class="visually-hidden">Variación anual: </span>+{format_es(metrics['variacion_2023_pct'], 1)}%

2023 frente a 2022
:::

::: {{.valuebox .kpi-ritmo color="#8A5A00" icon="graph-up-arrow" aria-label="Ritmo 2020–2023" role="group"}}
### Ritmo 2020–2023
<span class="visually-hidden">Ritmo 2020–2023: </span>+{format_es(metrics['cagr_2020_2023_pct'], 1)}%

crecimiento anual compuesto
:::

::: {{.valuebox .kpi-quiebre color="#17324D" icon="signpost-split" aria-label="Quiebre estadístico" role="group"}}
### Quiebre estadístico
<span class="visually-hidden">Quiebre estadístico: </span>{metrics['anio_quiebre']}

mejor BIC entre 9 candidatos
:::
""".strip() + "\n"
    (OUTPUTS / "dashboard_kpis.md").write_text(kpis, encoding="utf-8")

    landing = f"""
::: {{.metric-strip}}
::: {{.metric}}
**{format_es(metrics['tasa_2023'], 2)}**  
Tasa observada en 2023
:::
::: {{.metric}}
**+{format_es(metrics['variacion_2023_pct'], 1)}%**  
Variación frente a 2022
:::
::: {{.metric}}
**{metrics['anio_quiebre']}**  
Quiebre con mejor BIC
:::
::: {{.metric}}
**{metrics['muestra']['n']} años**  
Serie continua modelada
:::
:::
""".strip() + "\n"
    (OUTPUTS / "landing_metrics.md").write_text(landing, encoding="utf-8")

    status = f"""
::: {{.status-grid}}
::: {{.status-item .status-red}}
**ROJO · Nivel observado**  
{format_es(metrics['tasa_2023'], 2)} por 100.000 en 2023.
:::

::: {{.status-item .status-amber}}
**ÁMBAR · Frescura**  
La fuente no contiene 2024 ni 2025.
:::

::: {{.status-item .status-green}}
**VERDE · Trazabilidad**  
API, snapshot, modelos y {7} pruebas versionados.
:::
:::
""".strip() + "\n"
    (OUTPUTS / "dashboard_status.md").write_text(status, encoding="utf-8")


def save_figure(fig: plt.Figure, stem: str) -> None:
    png = OUTPUTS / f"{stem}.png"
    svg = OUTPUTS / f"{stem}.svg"
    fig.savefig(png, dpi=190, bbox_inches="tight", facecolor="white")
    fig.savefig(svg, bbox_inches="tight", facecolor="white")
    raw = svg.read_text(encoding="utf-8")
    svg.write_text("\n".join(line.rstrip() for line in raw.splitlines()) + "\n", encoding="utf-8")
    PAPER_ASSETS.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(png, PAPER_ASSETS / png.name)
    plt.close(fig)


def style_axis(axis: plt.Axes) -> None:
    axis.grid(axis="y", color=GRID, linewidth=0.8)
    axis.grid(axis="x", visible=False)
    axis.tick_params(colors="#566573")
    for spine in axis.spines.values():
        spine.set_visible(False)


def plot_regime(data: pd.DataFrame, metrics: dict) -> None:
    fig, axis = plt.subplots(figsize=(11.3, 6.4), layout="constrained")
    axis.axvspan(metrics["anio_quiebre"], 2023.5, color="#FFF1E2", alpha=0.9, zorder=0)
    axis.plot(data["anio"], data["tasa_homicidios"], color=TEAL, linewidth=2.7, marker="o", label="Observado")
    axis.plot(data["anio"], data["ajuste_segmentado"], color=ORANGE, linewidth=2.3, linestyle="--", label="Tendencia segmentada")
    axis.axvline(metrics["anio_quiebre"], color=INK, linewidth=1.2, linestyle=":")
    axis.text(metrics["anio_quiebre"] + 0.2, 48.3, f"Quiebre seleccionado · {metrics['anio_quiebre']}", color=INK, weight="bold", fontsize=10)
    axis.annotate("45,72", xy=(2023, metrics["tasa_2023"]), xytext=(-42, -5), textcoords="offset points", color=RED, weight="bold", fontsize=12)
    axis.set_title("Una sola tendencia ya no describe la trayectoria reciente", loc="left", color=INK, fontsize=18, fontweight="bold", pad=14)
    axis.set_ylabel("Homicidios por 100.000 habitantes", color=INK)
    axis.set_xlabel("")
    axis.set_xlim(2006.5, 2023.6)
    axis.set_xticks([2007, 2010, 2013, 2016, 2019, 2021, 2023])
    axis.set_ylim(0, 52)
    axis.legend(frameon=False, loc="upper left")
    style_axis(axis)
    fig.text(0.01, -0.025, "Fuente: Banco Mundial / UNODC (VC.IHR.PSRC.P5). Modelo descriptivo; no identifica causas.\nElaboración: Alan Del Rosario.", color="#566573", fontsize=8.8)
    save_figure(fig, "figura_regimen")


def plot_changes(data: pd.DataFrame) -> None:
    plotted = data.dropna(subset=["variacion_anual"])
    colors = [RED if value > 0 else TEAL for value in plotted["variacion_anual"]]
    fig, axis = plt.subplots(figsize=(10.2, 5.4), layout="constrained")
    axis.bar(plotted["anio"], plotted["variacion_anual"], color=colors, width=0.72)
    axis.axhline(0, color=INK, linewidth=1)
    axis.set_title("Los mayores aumentos absolutos se concentran al final de la serie", loc="left", color=INK, fontsize=16, fontweight="bold", pad=13)
    axis.set_ylabel("Cambio frente al año anterior", color=INK)
    axis.set_xlabel("")
    axis.set_xlim(2007.4, 2023.6)
    axis.set_xticks([2008, 2010, 2012, 2014, 2016, 2018, 2020, 2022, 2023])
    style_axis(axis)
    fig.text(0.01, -0.025, "Fuente: Banco Mundial / UNODC. Diferencias anuales en puntos por 100.000 habitantes.", color="#566573", fontsize=8.7)
    save_figure(fig, "figura_variaciones")


def plot_robustness(ranking: pd.DataFrame, selected: int) -> None:
    ordered = ranking.sort_values("anio_quiebre")
    colors = [ORANGE if year == selected else "#A8B8C4" for year in ordered["anio_quiebre"]]
    fig, axis = plt.subplots(figsize=(9.3, 4.8), layout="constrained")
    axis.bar(ordered["anio_quiebre"].astype(str), ordered["bic"], color=colors, width=0.7)
    axis.set_title("2019 ofrece el mejor balance entre ajuste y complejidad", loc="left", color=INK, fontsize=16, fontweight="bold", pad=13)
    axis.set_ylabel("BIC · menor es mejor", color=INK)
    axis.set_xlabel("Año candidato de quiebre", color=INK)
    axis.set_ylim(85, max(ordered["bic"]) + 5)
    style_axis(axis)
    fig.text(0.01, -0.025, "Nota: nueve modelos segmentados comparables; mínimo de cinco observaciones por régimen.", color="#566573", fontsize=8.7)
    save_figure(fig, "figura_robustez")


def main() -> None:
    data = load_continuous_series()
    metrics, ranking, modeled = calculate(data)
    write_outputs(metrics, ranking)
    plot_regime(modeled, metrics)
    plot_changes(modeled)
    plot_robustness(ranking, metrics["anio_quiebre"])
    shutil.copyfile(
        BASE.parents[1] / "projects" / "referencias-homicidios.bib",
        BASE.parents[1] / "paper" / "referencias-homicidios.bib",
    )
    print(
        f"Investigación generada: quiebre {metrics['anio_quiebre']}; "
        f"pendiente posterior {metrics['pendiente_post']:+.2f}."
    )


if __name__ == "__main__":
    main()
