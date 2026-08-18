"""Valida estructura y, opcionalmente, ejecución de notebooks activos."""

from __future__ import annotations

import argparse
from pathlib import Path

import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[2]
ACTIVE_MODULES = (
    ROOT / "modulo-01-fundamentos",
    ROOT / "modulo-02-ciclo-mlops",
    ROOT / "modulo-03-produccion",
)


def notebook_paths() -> list[Path]:
    return sorted(path for module in ACTIVE_MODULES for path in module.glob("*.ipynb"))


def validate(path: Path, execute: bool) -> None:
    notebook = nbformat.read(path, as_version=4)
    nbformat.validate(notebook)
    if execute:
        NotebookClient(notebook, timeout=120, kernel_name="python3").execute(
            cwd=str(path.parent)
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--execute", action="store_true", help="ejecuta también todas las celdas de código"
    )
    args = parser.parse_args()

    paths = notebook_paths()
    for path in paths:
        validate(path, execute=args.execute)
        print(f"OK {path.relative_to(ROOT)}")
    print(f"{len(paths)} notebook(s) válido(s)")


if __name__ == "__main__":
    main()
