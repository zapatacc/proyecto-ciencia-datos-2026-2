"""Reproduce una decisión de reentrenamiento con ventanas de Green Taxi."""

import argparse
import json
from hashlib import file_digest
from pathlib import Path

import pandas as pd
from modelos import construir_pipeline
from prefect import flow, get_run_logger, task
from preparar_datos import FEATURES, TARGET, cargar_muestra
from sklearn.metrics import root_mean_squared_error

MESES = {
    "03": "60c8bdfc0aa7826a2d6d2a6cca0f0e0dcb2d8aa7336212a45382794bb55b9cc0",
    "04": "e8dd2a0afde3fe8be942dd638fe1d946f8edbe5b377cf6c1d645e1206b3c7662",
    "05": "15ff57840a1103d49298ad244492730ca4236b4de0d2758a689ded08bc332752",
}
COLUMNAS = [
    "lpep_pickup_datetime",
    "lpep_dropoff_datetime",
    "trip_distance",
    "passenger_count",
    "PULocationID",
    "DOLocationID",
]
UMBRAL_DRIFT = 0.03
MEJORA_MINIMA = 0.10


def preparar_mes(ruta: Path, mes: str) -> pd.DataFrame:
    """Filtra por mes de inicio y reconstruye el contrato del curso."""
    with ruta.open("rb") as archivo:
        if file_digest(archivo, "sha256").hexdigest() != MESES[mes]:
            raise ValueError(f"SHA-256 inesperado para {ruta.name}. Revisa su procedencia.")
    viajes = pd.read_parquet(ruta, columns=COLUMNAS)
    inicio = viajes["lpep_pickup_datetime"]
    fin = viajes["lpep_dropoff_datetime"]
    preparados = pd.DataFrame(
        {
            "distancia_km": viajes["trip_distance"] * 1.60934,
            "pasajeros": viajes["passenger_count"],
            "hora_recoleccion": inicio.dt.hour,
            "zona_origen": viajes["PULocationID"],
            "zona_destino": viajes["DOLocationID"],
            TARGET: (fin - inicio).dt.total_seconds() / 60,
        }
    )
    validos = (
        inicio.dt.year.eq(2026)
        & inicio.dt.month.eq(int(mes))
        & preparados[TARGET].between(1, 60)
        & preparados["distancia_km"].between(0.1, 100)
        & preparados["pasajeros"].between(1, 6)
        & preparados["zona_origen"].between(1, 265)
        & preparados["zona_destino"].between(1, 265)
    )
    preparados = preparados.loc[validos, FEATURES + [TARGET]]
    conteos = ["pasajeros", "hora_recoleccion", "zona_origen", "zona_destino"]
    preparados[conteos] = preparados[conteos].astype(int)
    if preparados.empty:
        raise ValueError(f"El mes {mes} no contiene filas válidas.")
    return preparados.sample(n=min(1200, len(preparados)), random_state=42)


def cargar_mes(mes: str, usar_muestras: bool) -> pd.DataFrame:
    if usar_muestras:
        return cargar_muestra(Path("datos") / f"green-taxi-2026-{mes}.csv")
    return preparar_mes(Path("datos") / f"green_tripdata_2026-{mes}.parquet", mes)


@task
def medir_cambio(referencia: pd.Series, observacion: pd.Series) -> tuple[int, float]:
    """Encuentra la zona con la mayor diferencia absoluta de proporciones."""
    p_referencia = referencia.value_counts(normalize=True)
    p_observacion = observacion.value_counts(normalize=True)
    diferencias = p_referencia.sub(p_observacion, fill_value=0).abs()
    zona = int(diferencias.idxmax())
    return zona, float(diferencias.loc[zona])


@task
def evaluar_candidato(marzo: pd.DataFrame, abril: pd.DataFrame, mayo: pd.DataFrame) -> dict:
    vigente = construir_pipeline("linear_regression").fit(marzo[FEATURES], marzo[TARGET])
    candidato = construir_pipeline("linear_regression").fit(abril[FEATURES], abril[TARGET])
    rmse_vigente = float(root_mean_squared_error(mayo[TARGET], vigente.predict(mayo[FEATURES])))
    rmse_candidato = float(root_mean_squared_error(mayo[TARGET], candidato.predict(mayo[FEATURES])))
    mejora = rmse_vigente - rmse_candidato
    return {
        "rmse_vigente_min": rmse_vigente,
        "rmse_candidato_min": rmse_candidato,
        "mejora_min": mejora,
        "decision": "candidato_aprobado" if mejora >= MEJORA_MINIMA else "conservar_vigente",
    }


@flow(name="green-taxi-deriva")
def ejecutar(escenario: str, usar_muestras: bool) -> dict:
    marzo = cargar_mes("03", usar_muestras)
    abril = cargar_mes("04", usar_muestras)
    referencia = marzo["zona_origen"]
    observacion = abril["zona_origen"]
    if escenario == "control":
        observacion = referencia.copy()
    elif escenario == "controlado":
        proporcion_original = referencia.value_counts(normalize=True)
        zonas_abril = pd.Index(sorted(observacion.unique()))
        zona = proporcion_original.reindex(zonas_abril, fill_value=0).idxmin()
        observacion = observacion.loc[observacion.eq(zona)].sample(
            n=len(observacion), replace=True, random_state=42
        )
    zona, cambio = medir_cambio(referencia, observacion)
    resultado = {
        "escenario": escenario,
        "fuente": "muestras" if usar_muestras else "parquet",
        "zona": zona,
        "cambio_pp": 100 * cambio,
        "umbral_pp": 100 * UMBRAL_DRIFT,
        "mejora_minima_min": MEJORA_MINIMA,
        "decision": "sin_reentrenamiento",
    }
    get_run_logger().info(
        "Escenario %s. Cambio máximo: %.2f puntos porcentuales.", escenario, 100 * cambio
    )
    if cambio >= UMBRAL_DRIFT:
        resultado.update(evaluar_candidato(marzo, abril, cargar_mes("05", usar_muestras)))
    return resultado


if __name__ == "__main__":
    argumentos = argparse.ArgumentParser(description=__doc__)
    argumentos.add_argument("escenario", choices=("control", "historico", "controlado"))
    argumentos.add_argument("--muestras", action="store_true")
    opciones = argumentos.parse_args()
    reporte = json.dumps(ejecutar(opciones.escenario, opciones.muestras), indent=2, allow_nan=False)
    Path("resultados").mkdir(exist_ok=True)
    salida = Path("resultados") / f"drift-{opciones.escenario}.json"
    salida.write_text(reporte + "\n", encoding="utf-8")
    print(f"{salida}\n{reporte}")
