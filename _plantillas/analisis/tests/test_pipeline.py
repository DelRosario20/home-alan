"""Pruebas del pipeline del caso <slug>.

Contrato: los tests anclan valores conocidos del dato oficial y las reglas
duras del análisis (esquema, continuidad de la muestra, resultados
recalculados — no hardcodeados). Corren con:
    python -m unittest discover -s posts/<slug-largo>/tests -v
Modelo completo: posts/2026-07-homicidios-wb/tests/test_pipeline.py
"""

from __future__ import annotations

import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]


class PipelineTest(unittest.TestCase):
    def test_placeholder(self) -> None:
        self.skipTest(
            "Implementar: anclas de valores oficiales, validación de esquema "
            "y verificación de que los resultados publicados se recalculan."
        )


if __name__ == "__main__":
    unittest.main()
