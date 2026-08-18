"""Reto adicional de funciones y colecciones. Resolver sin ayuda de IA."""

VIAJES = [
    {
        "origen": "Centro",
        "destino": "Chapultepec",
        "distancia_km": 3.2,
    },
    {
        "origen": "ITESO",
        "destino": "Centro",
        "distancia_km": 12.5,
    },
    {
        "origen": "Tlaquepaque",
        "destino": "Aeropuerto",
        "distancia_km": 15.8,
    },
]


def clasificar_distancia(distancia_km: float) -> str:
    """Clasifica un viaje como corto, medio o largo."""
    # TODO 1: producir ValueError si la distancia no es positiva.
    # TODO 2: devolver "corto" hasta 5 km, "medio" hasta 12 km
    # y "largo" para distancias mayores.
    return ""


def resumir_viajes(viajes: list[dict]) -> list[dict]:
    """Crea un resumen nuevo sin modificar la lista recibida."""
    # TODO 3: construir una lista de diccionarios con estas claves:
    # ruta, categoria y duracion_estimada_min.
    # Duración = 4 minutos por km + 2 minutos fijos, redondeada
    # a una cifra decimal.
    return []


# TODO 4: agrega a VIAJES un registro inventado por ti.

resumen = resumir_viajes(VIAJES)
for viaje in resumen:
    print(
        f"{viaje['ruta']} | {viaje['categoria']} | "
        f"{viaje['duracion_estimada_min']} min"
    )
