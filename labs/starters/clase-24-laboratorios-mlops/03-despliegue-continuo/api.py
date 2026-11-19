"""Sirve el modelo entrenado para esta revisión."""

import os
import pickle
from hashlib import sha256
from pathlib import Path

import pandas as pd
from fastapi import FastAPI
from preparar_datos import FEATURES
from pydantic import BaseModel, Field

artefacto = Path("modelo.pkl").read_bytes()
modelo = pickle.loads(artefacto)
identidad = {"revision": os.environ["REVISION"], "modelo_sha256": sha256(artefacto).hexdigest()}
app = FastAPI(title="Green Taxi")


class Viaje(BaseModel):
    distancia_km: float = Field(gt=0, le=100)
    pasajeros: int = Field(ge=1, le=6)
    hora_recoleccion: int = Field(ge=0, le=23)
    zona_origen: int = Field(ge=1, le=265)
    zona_destino: int = Field(ge=1, le=265)


@app.get("/health")
def salud():
    return {"status": "ok", **identidad}


@app.post("/api/v1/predicciones")
def predecir(viaje: Viaje):
    entrada = pd.DataFrame([viaje.model_dump()], columns=FEATURES)
    duracion = float(modelo.predict(entrada)[0])
    return {"duracion_estimada_minutos": round(duracion, 2), **identidad}
