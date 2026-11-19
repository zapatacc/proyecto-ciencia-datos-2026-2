"""Compara el error de un modelo con la latencia HTTP de su API local."""

import argparse
from collections import Counter
from math import ceil
from statistics import median
from time import perf_counter

import httpx
from api_local import DATOS, MODELOS, entrenar
from preparar_datos import FEATURES, TARGET, cargar_muestra
from sklearn.metrics import root_mean_squared_error

CALENTAMIENTO = 5
SOLICITUDES = 100


def medir(
    cliente: httpx.Client, viajes: list[dict[str, float | int]]
) -> tuple[list[float], Counter[str]]:
    tiempos = []
    fallos: Counter[str] = Counter()
    for viaje in viajes:
        inicio = perf_counter()
        try:
            respuesta = cliente.post("/api/v1/predicciones", json=viaje)
        except httpx.RequestError as error:
            fallos[type(error).__name__] += 1
            continue
        milisegundos = (perf_counter() - inicio) * 1000
        if respuesta.status_code == 200:
            tiempos.append(milisegundos)
        else:
            fallos[f"HTTP {respuesta.status_code}"] += 1

    return tiempos, fallos


def main() -> None:
    argumentos = argparse.ArgumentParser(description=__doc__)
    argumentos.add_argument("--modelo", choices=MODELOS, required=True)
    argumentos.add_argument("--url", required=True)
    opciones = argumentos.parse_args()

    validacion = cargar_muestra(DATOS / "green-taxi-validation.csv")
    entradas = validacion[FEATURES]
    predicciones = entrenar(opciones.modelo).predict(entradas)
    rmse = root_mean_squared_error(validacion[TARGET], predicciones)

    viajes = entradas.head(SOLICITUDES).to_dict(orient="records")
    with httpx.Client(base_url=opciones.url, timeout=5, trust_env=False) as cliente:
        salud = cliente.get("/health")
        salud.raise_for_status()
        if salud.json()["modelo"] != opciones.modelo:
            raise SystemExit("La API está sirviendo un modelo diferente al solicitado.")

        _, fallos_calentamiento = medir(cliente, viajes[:CALENTAMIENTO])
        if fallos_calentamiento:
            raise SystemExit(f"Corrige los fallos de calentamiento: {dict(fallos_calentamiento)}")

        tiempos, fallos = medir(cliente, viajes)

    print(f"Modelo: {opciones.modelo}")
    print(f"RMSE en {len(validacion)} viajes de abril: {rmse:.2f} min")
    print(f"Solicitudes: {len(viajes)} · éxitos: {len(tiempos)} · fallos: {dict(fallos)}")
    if not tiempos:
        raise SystemExit("Sin respuestas HTTP 200 para calcular latencia.")

    p95 = sorted(tiempos)[ceil(0.95 * len(tiempos)) - 1]
    print(f"Mediana: {median(tiempos):.2f} ms · p95: {p95:.2f} ms")


if __name__ == "__main__":
    main()
