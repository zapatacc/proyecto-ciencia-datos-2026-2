import os

import mlflow
import pandas as pd
from dotenv import load_dotenv
from fastapi import FastAPI
from mlflow import MlflowClient
from pydantic import BaseModel, Field

load_dotenv(override=False)

VERSION_API = "v1"
RUTA_MODELO_LOCAL = os.getenv("RUTA_MODELO_LOCAL", "")

TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", "databricks")
REGISTRY_URI = os.getenv("MLFLOW_REGISTRY_URI", "databricks-uc")
MODELO_REGISTRADO = os.getenv("MODELO_REGISTRADO", "")
ALIAS_MODELO = os.getenv("ALIAS_MODELO", "champion")

mlflow.set_tracking_uri(TRACKING_URI)
mlflow.set_registry_uri(REGISTRY_URI)

if RUTA_MODELO_LOCAL:
    modelo = mlflow.pyfunc.load_model(RUTA_MODELO_LOCAL)
    version_modelo = "local"
    nombre_modelo = "nyc-taxi-contingencia"
    alias_modelo = "sin-alias"
else:
    if not MODELO_REGISTRADO:
        raise ValueError("Configura MODELO_REGISTRADO o RUTA_MODELO_LOCAL.")
    cliente = MlflowClient(registry_uri=REGISTRY_URI)
    version = cliente.get_model_version_by_alias(MODELO_REGISTRADO, ALIAS_MODELO)
    # Se carga la versión resuelta, aunque después se mueva el alias.
    modelo = mlflow.pyfunc.load_model(f"models:/{MODELO_REGISTRADO}/{version.version}")
    version_modelo = str(version.version)
    nombre_modelo = MODELO_REGISTRADO
    alias_modelo = ALIAS_MODELO


class SolicitudPrediccion(BaseModel):
    distancia_km: float = Field(gt=0, le=100)
    pasajeros: int = Field(ge=1, le=6)
    hora_recoleccion: int = Field(ge=0, le=23)
    zona_origen: int = Field(ge=1, le=265)
    zona_destino: int = Field(ge=1, le=265)


class RespuestaPrediccion(BaseModel):
    duracion_estimada_minutos: float
    modelo: str
    alias: str
    version: str


app = FastAPI(title="API de duración de viajes Green Taxi")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "version_api": VERSION_API}


@app.post("/api/v1/predicciones", response_model=RespuestaPrediccion)
def crear_prediccion(solicitud: SolicitudPrediccion) -> RespuestaPrediccion:
    entrada = pd.DataFrame([solicitud.model_dump()])
    duracion = float(modelo.predict(entrada)[0])
    return RespuestaPrediccion(
        duracion_estimada_minutos=round(duracion, 1),
        modelo=nombre_modelo,
        alias=alias_modelo,
        version=version_modelo,
    )
