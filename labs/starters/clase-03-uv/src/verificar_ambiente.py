"""Muestra que el proyecto usa Python y dependencias declaradas."""

from __future__ import annotations

import sys

import requests


def preparar_url(viaje_id: int, pasajeros: int) -> str:
    """Construye una URL local sin enviar una solicitud por internet."""
    solicitud = requests.Request(
        method="GET",
        url=f"http://127.0.0.1:8000/viajes/{viaje_id}",
        params={"pasajeros": pasajeros},
    )
    return solicitud.prepare().url or ""


def main() -> None:
    """Imprime información observable del ambiente virtual activo."""
    print(f"Python: {sys.version.split()[0]}")
    print(f"requests: {requests.__version__}")
    print(f"URL preparada: {preparar_url(viaje_id=42, pasajeros=2)}")


if __name__ == "__main__":
    main()
