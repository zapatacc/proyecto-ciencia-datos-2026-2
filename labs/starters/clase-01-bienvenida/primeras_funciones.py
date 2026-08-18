"""Primera actividad con VS Code. Resolver sin ayuda de IA."""


def construir_presentacion(
    nombre: str, semestre: str, expectativa: str
) -> str:
    """Construye una presentación breve para el grupo."""
    # TODO 1: devolver un mensaje que use los tres parámetros.
    return ""


def estimar_duracion(distancia_km: float) -> float:
    """Estima minutos de viaje con una regla didáctica sencilla."""
    # TODO 2: producir ValueError si la distancia no es positiva.
    # TODO 3: calcular 4 minutos por km más 2 minutos fijos
    # y redondear el resultado a una cifra decimal.
    return 0.0


nombre = "Escribe aquí tu nombre"
semestre = "Escribe aquí tu semestre"
expectativa = "Escribe aquí qué esperas del curso"

mensaje = construir_presentacion(nombre, semestre, expectativa)
print(mensaje)

distancia = 3.2
minutos = estimar_duracion(distancia)
print(f"Un viaje de {distancia} km tardaría aproximadamente {minutos} min.")

# TODO 4: llama estimar_duracion con otra distancia e imprime el resultado.
