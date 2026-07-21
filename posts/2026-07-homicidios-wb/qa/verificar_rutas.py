"""Verifica que toda ruta cruzada de la tríada resuelva en disco.

Las páginas de projects/ referencian la carpeta artesanal con rutas relativas
(includes, imágenes, FileAttachment, enlaces de descarga). Renombrar o mover
un archivo las rompe en silencio: el render "pasa" pero la página queda con
huecos. Este check convierte esa rotura silenciosa en fallo ruidoso y corre
dentro de reproducir.ps1.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]   # posts/<slug-largo>/
ROOT = BASE.parents[1]                       # raíz del repo
PROJECTS = ROOT / "projects"
SLUG = "homicidios"

PATH_PATTERNS = [
    re.compile(r"\{\{<\s*include\s+([^\s>]+)\s*>\}\}"),          # includes Quarto
    re.compile(r"!\[[^\]]*\]\(([^)\s]+)"),                        # imágenes markdown
    re.compile(r"FileAttachment\(\"([^\"]+)\"\)"),               # OJS
    re.compile(r"\]\((\.\./[^)\s#]+)"),                           # enlaces relativos
    re.compile(r"href=\"(\.\./[^\"#]+)\""),                       # enlaces HTML
]


def referenced_paths(qmd: Path) -> set[str]:
    text = qmd.read_text(encoding="utf-8")
    found: set[str] = set()
    for pattern in PATH_PATTERNS:
        for match in pattern.findall(text):
            candidate = match.split("#")[0].strip()
            if candidate.startswith(("http://", "https://", "mailto:")):
                continue
            if "/" in candidate and not candidate.endswith((".html", ".qmd")):
                found.add(candidate)
    return found


def main() -> None:
    pages = sorted(PROJECTS.glob(f"{SLUG}*.qmd"))
    if not pages:
        raise AssertionError(f"No se encontraron páginas projects/{SLUG}*.qmd")

    broken: list[str] = []
    checked = 0
    for page in pages:
        for ref in sorted(referenced_paths(page)):
            target = (page.parent / ref).resolve()
            checked += 1
            if not target.exists():
                broken.append(f"{page.name} -> {ref}")

    if broken:
        detail = "\n  ".join(broken)
        raise AssertionError(f"Rutas cruzadas rotas ({len(broken)}):\n  {detail}")

    print(f"Rutas cruzadas verificadas: {checked} referencias en {len(pages)} páginas resuelven.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
