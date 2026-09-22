"""Carga la muestra preparada de Green Taxi para la Clase 10."""

from pathlib import Path

import pandas as pd

FEATURES_NUMERICAS = ["distancia_km", "pasajeros", "hora_recoleccion"]
FEATURES_CATEGORICAS = ["zona_origen", "zona_destino"]
FEATURES = FEATURES_NUMERICAS + FEATURES_CATEGORICAS
TARGET = "duracion_minutos"


def cargar_muestra(ruta: Path) -> pd.DataFrame:
    """Carga una muestra y conserva los tipos usados por ambos modelos."""
    viajes = pd.read_csv(ruta)
    enteras = ["pasajeros", "hora_recoleccion", "zona_origen", "zona_destino"]
    viajes[enteras] = viajes[enteras].astype(int)
    return viajes[FEATURES + [TARGET]]
