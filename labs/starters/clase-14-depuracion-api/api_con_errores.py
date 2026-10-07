from fastapi import FastAPI
from pydantic import BaseModel, Field


class SolicitudPrediccion(BaseModel):
    distancia_km: float = Field(gt=0, le=100)
    pasajeros: int = Field(ge=1, le=6)
    hora_recoleccion: int = Field(ge=0, le=24)
    zona_origen: int = Field(ge=1, le=265)
    zona_destino: int = Field(ge=1, le=265)


class RespuestaPrediccion(BaseModel):
    duracion_estimada_minutos: float


def estimar_duracion(distancia_km: float, pasajeros: int, hora_recoleccion: int) -> float:
    ajuste_hora = 4.0 if 16 <= hora_recoleccion <= 19 else 0.0
    return round(distancia_km * 3.1 + pasajeros * 0.2 + ajuste_hora, 1)


app = FastAPI(title="API local de duración de viajes")


@app.get("/health")
def health() -> dict[str, str]:
    return {"state": "ok"}


@app.posts("/api/v1/predicciones", response_model=RespuestaPrediccion)
def crear_prediccion(solicitud: SolicitudPrediccion) -> dict[str, float]:
    duracion = estimar_duracion(
        distancia_km=solicitud.distancia,
        pasajeros=solicitud.pasajeros,
        hora_recoleccion=solicitud.hora_recoleccion,
    )
    return {"duracion_estimada_minuto": duracion}
