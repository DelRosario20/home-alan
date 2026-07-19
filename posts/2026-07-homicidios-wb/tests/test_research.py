from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


BASE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("research", BASE / "scripts" / "04_investigacion.py")
RESEARCH = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(RESEARCH)


class ResearchPipelineTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        data = RESEARCH.load_continuous_series()
        cls.metrics, cls.ranking, cls.modeled = RESEARCH.calculate(data)

    def test_sample_is_continuous(self) -> None:
        self.assertEqual(self.modeled["anio"].tolist(), list(range(2007, 2024)))

    def test_break_is_selected_not_hardcoded(self) -> None:
        best = int(self.ranking.sort_values("bic").iloc[0]["anio_quiebre"])
        self.assertEqual(self.metrics["anio_quiebre"], best)
        self.assertEqual(best, 2019)

    def test_segmented_model_improves_bic(self) -> None:
        self.assertGreater(self.metrics["ventaja_bic"], 10)

    def test_log_specification_agrees(self) -> None:
        self.assertEqual(self.metrics["quiebre_log"], self.metrics["anio_quiebre"])


if __name__ == "__main__":
    unittest.main()
