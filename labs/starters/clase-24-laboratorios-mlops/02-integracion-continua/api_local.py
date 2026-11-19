"""API local de Green Taxi con un modelo entrenado desde una muestra conocida."""

import argparse
from pathlib import Path

import pandas as pd
import uvicorn
from fastapi import FastAPI
from modelos import construir_pipeline
from preparar_datos import FEATURES, TARGET, cargar_muestra
from pydantic import BaseModel, Field
from sklearn.pipeline import Pipeline

RAIZ = Path(__file__).resolve().parent
DATOS = RAIZ / "datos"
MODELOS = ("linear_regression", "random_forest")


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


def entrenar(nombre: str) -> Pipeline:
    """Ajusta el modelo con marzo antes de atender solicitudes."""
    entrenamiento = cargar_muestra(DATOS / "green-taxi-train.csv")
    pipeline = construir_pipeline(nombre)
    return pipeline.fit(entrenamiento[FEATURES], entrenamiento[TARGET])


def crear_app(nombre: str) -> FastAPI:
    """Prepara una aplicación que conserva el mismo modelo durante su ejecución."""
    modelo = entrenar(nombre)
    app = FastAPI(title="API local Green Taxi")

    @app.get("/health")
    def salud() -> dict[str, str]:
        return {"status": "ok", "modelo": nombre}

    @app.post("/api/v1/predicciones", response_model=RespuestaPrediccion)
    def predecir(solicitud: SolicitudPrediccion) -> RespuestaPrediccion:
        datos = pd.DataFrame([solicitud.model_dump()], columns=FEATURES)
        duracion = float(modelo.predict(datos)[0])
        return RespuestaPrediccion(
            duracion_estimada_minutos=round(duracion, 1),
            modelo=nombre,
            alias="sin-alias",
            version="muestra-marzo-v1",
        )

    return app


def main() -> None:
    argumentos = argparse.ArgumentParser(description=__doc__)
    argumentos.add_argument("--modelo", choices=MODELOS, required=True)
    argumentos.add_argument("--puerto", type=int, default=8000)
    opciones = argumentos.parse_args()
    uvicorn.run(crear_app(opciones.modelo), host="127.0.0.1", port=opciones.puerto)


if __name__ == "__main__":
    main()
