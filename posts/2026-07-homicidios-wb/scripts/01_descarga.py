"""Descarga la serie oficial de homicidios de Ecuador desde el Banco Mundial."""

from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen


BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"
API_URL = (
    "https://api.worldbank.org/v2/country/ECU/indicator/VC.IHR.PSRC.P5"
    "?format=json&per_page=100&date=2000:2025"
)


def main() -> None:
    request = Request(API_URL, headers={"User-Agent": "home-alan-reproducibility/1.0"})
    with urlopen(request, timeout=30) as response:
        payload = json.load(response)

    if not isinstance(payload, list) or len(payload) != 2:
        raise RuntimeError("La API no devolvió la estructura esperada [metadatos, datos].")

    api_meta, observations = payload
    non_null = sorted(
        (
            {"anio": int(item["date"]), "tasa_homicidios": float(item["value"])}
            for item in observations
            if item["value"] is not None
        ),
        key=lambda row: row["anio"],
    )

    if not non_null:
        raise RuntimeError("La API no devolvió observaciones no nulas.")

    DATA.mkdir(parents=True, exist_ok=True)
    with (DATA / "homicidios_ecuador_wb.csv").open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["anio", "tasa_homicidios"])
        writer.writeheader()
        writer.writerows(non_null)

    missing_years = sorted(int(item["date"]) for item in observations if item["value"] is None)
    metadata = {
        "fuente": "Banco Mundial — World Development Indicators",
        "indicador": "VC.IHR.PSRC.P5",
        "definicion": "Intentional homicides (per 100,000 people)",
        "pais": "Ecuador (ECU)",
        "url_api": API_URL,
        "fecha_descarga_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "api_ultima_actualizacion": api_meta.get("lastupdated"),
        "periodo_solicitado": "2000–2025",
        "observaciones_no_nulas": len(non_null),
        "anios_sin_dato": missing_years,
        "nota": "Los años sin observación se conservan en los metadatos y no se interpolan.",
    }
    (DATA / "fuente.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Descarga validada: {len(non_null)} observaciones; {len(missing_years)} años sin dato.")


if __name__ == "__main__":
    main()
