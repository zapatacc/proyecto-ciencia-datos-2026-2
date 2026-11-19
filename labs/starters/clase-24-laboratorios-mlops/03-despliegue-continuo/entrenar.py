"""Entrena la regresión de Green Taxi y guarda el artefacto propio."""

import pickle
from pathlib import Path

from modelos import construir_pipeline
from preparar_datos import FEATURES, TARGET, cargar_muestra

viajes = cargar_muestra(Path("datos/green-taxi-train.csv"))
modelo = construir_pipeline("linear_regression").fit(viajes[FEATURES], viajes[TARGET])

with Path("modelo.pkl").open("wb") as archivo:
    pickle.dump(modelo, archivo)
