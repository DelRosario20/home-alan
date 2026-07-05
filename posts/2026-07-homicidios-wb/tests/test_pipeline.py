from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


BASE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("analysis", BASE / "scripts" / "02_analisis.py")
ANALYSIS = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(ANALYSIS)


class PipelineTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.rows = ANALYSIS.load_data()
        cls.metrics = ANALYSIS.calculate(cls.rows)

    def test_official_snapshot_anchor_values(self) -> None:
        by_year = {row["anio"]: row["tasa_homicidios"] for row in self.rows}
        self.assertAlmostEqual(by_year[2017], 5.79, places=2)
        self.assertAlmostEqual(by_year[2023], 45.72, places=2)

    def test_missing_years_are_not_interpolated(self) -> None:
        years = {row["anio"] for row in self.rows}
        self.assertTrue({2003, 2004, 2005, 2006}.isdisjoint(years))

    def test_main_result_is_recomputed(self) -> None:
        self.assertEqual(self.metrics["anio_minimo"], 2017)
        self.assertEqual(self.metrics["anio_maximo"], 2023)
        self.assertAlmostEqual(self.metrics["multiplicador_min_max"], 7.9, places=1)


if __name__ == "__main__":
    unittest.main()
