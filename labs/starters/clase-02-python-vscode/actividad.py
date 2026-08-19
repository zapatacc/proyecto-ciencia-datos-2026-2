"""Starter de la actividad conductora de la clase 2."""

from datos_viajes import VIAJES


def estimar_duracion(
    distancia_km: float, pasajeros: int, fin_de_semana: bool
) -> float:
    """Estima minutos de viaje con reglas didácticas sencillas."""
    # TODO 1: validar que distancia_km sea positiva.
    # TODO 2: calcular base = 4 minutos por km + 2 minutos fijos.
    # TODO 3: sumar 3 minutos si hay más de 2 pasajeros.
    # TODO 4: reducir 10 % si es fin de semana y redondear el resultado
    # a una cifra decimal antes de devolverlo.
    return 0.0


def resumir_viajes(viajes: list[dict]) -> list[dict]:
    """Agrega una duración estimada a cada viaje sin modificar el original."""
    # TODO 5: construir y devolver una lista de resúmenes.
    return []


if __name__ == "__main__":
    resumen = resumir_viajes(VIAJES)
    for viaje in resumen:
        print(
            f"{viaje['origen']} → {viaje['destino']}: "
            f"{viaje['duracion_estimada_min']} min"
        )
