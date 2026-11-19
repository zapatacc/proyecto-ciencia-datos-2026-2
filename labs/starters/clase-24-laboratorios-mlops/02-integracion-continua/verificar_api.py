"""Comprueba por HTTP el contrato de la API local de Green Taxi."""

import argparse
from math import isfinite
from time import monotonic, sleep

import httpx

VIAJE = {
    "distancia_km": 1.77,
    "pasajeros": 6,
    "hora_recoleccion": 10,
    "zona_origen": 75,
    "zona_destino": 41,
}


def esperar_api(cliente: httpx.Client) -> None:
    limite = monotonic() + 30
    while monotonic() < limite:
        try:
            salud = cliente.get("/health")
            if salud.status_code == 200 and salud.json() == {
                "status": "ok",
                "modelo": "linear_regression",
            }:
                return
        except (httpx.RequestError, ValueError):
            pass
        sleep(0.25)
    raise SystemExit("La API de regresión lineal no estuvo lista dentro de 30 s.")


def comprobar(condicion: bool, mensaje: str) -> None:
    if not condicion:
        raise SystemExit(f"FALLÓ: {mensaje}")
    print(f"OK: {mensaje}", flush=True)


def main() -> None:
    argumentos = argparse.ArgumentParser(description=__doc__)
    argumentos.add_argument("--url", required=True)
    opciones = argumentos.parse_args()

    with httpx.Client(base_url=opciones.url, timeout=3, trust_env=False) as cliente:
        esperar_api(cliente)
        ruta = "/api/v1/predicciones"

        valida = cliente.post(ruta, json=VIAJE)
        comprobar(valida.status_code == 200, f"viaje válido devuelve 200 ({valida.status_code})")
        cuerpo = valida.json()
        duracion = cuerpo.get("duracion_estimada_minutos")
        comprobar(type(duracion) in (int, float) and isfinite(duracion), "duración numérica finita")
        comprobar(cuerpo.get("modelo") == "linear_regression", "identificador del modelo correcto")
        comprobar(cuerpo.get("alias") == "sin-alias", "alias local correcto")
        comprobar(cuerpo.get("version") == "muestra-marzo-v1", "versión local correcta")

        invalida = cliente.post(ruta, json={**VIAJE, "pasajeros": 0})
        comprobar(
            invalida.status_code == 422,
            f"cero pasajeros devuelve 422 ({invalida.status_code})",
        )
        errores = invalida.json()["detail"]
        comprobar(
            any(error["loc"] == ["body", "pasajeros"] for error in errores),
            "el rechazo identifica el campo pasajeros",
        )


if __name__ == "__main__":
    main()
