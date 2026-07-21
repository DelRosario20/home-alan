"""Descarga el dato crudo de <indicador> desde <fuente>.

Contrato: este script es la ÚNICA puerta de entrada del dato al caso.
Escribe en data/ el crudo tal cual (CSV) más data/fuente.json con la
procedencia (URL, fecha de consulta, licencia). Nada se edita a mano en data/.
Modelo completo: posts/2026-07-homicidios-wb/scripts/01_descarga.py
"""

from __future__ import annotations

from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"


def main() -> None:
    DATA.mkdir(exist_ok=True)
    raise NotImplementedError(
        "Implementar: descargar desde la API/fuente oficial, validar la "
        "estructura de la respuesta, escribir data/<slug>.csv y data/fuente.json."
    )


if __name__ == "__main__":
    main()
