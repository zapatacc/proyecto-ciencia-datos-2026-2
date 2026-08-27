"""Starter de la primera aplicación FastAPI."""

from fastapi import FastAPI

app = FastAPI(title="API de viajes del curso")


@app.get("/")
def inicio() -> dict[str, str]:
    """Confirma que la aplicación está activa."""
    # TODO 1: devuelve un diccionario con la clave "mensaje".
    return {"mensaje": "TODO"}


# TODO 2: registra una ruta GET /viajes/{viaje_id}.
# TODO 3: define consultar_viaje con viaje_id entero y pasajeros entero igual a 1.
# TODO 4: devuelve ambos valores en un diccionario.
