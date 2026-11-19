"""Verifica desde el anfitrión qué revisión respondió a una predicción HTTP."""

import json
import math
import sys
import time
from urllib.error import URLError
from urllib.request import Request, urlopen

url, revision_esperada = sys.argv[1:]
viaje = {
    "distancia_km": 3.5,
    "pasajeros": 1,
    "hora_recoleccion": 8,
    "zona_origen": 74,
    "zona_destino": 75,
}
solicitud = Request(
    f"{url}/api/v1/predicciones",
    data=json.dumps(viaje).encode(),
    headers={"Content-Type": "application/json"},
)
print(f"POST /api/v1/predicciones {viaje}", flush=True)
for _ in range(30):
    try:
        with urlopen(solicitud, timeout=2) as respuesta:
            resultado = json.load(respuesta)
            estado = respuesta.status
    except (URLError, TimeoutError, json.JSONDecodeError) as error:
        ultimo_error = str(error)
    else:
        duracion = resultado.get("duracion_estimada_minutos")
        if (
            estado == 200
            and resultado.get("revision") == revision_esperada
            and type(duracion) in {int, float}
            and math.isfinite(duracion)
            and resultado.get("modelo_sha256")
        ):
            print(f"HTTP {estado} {resultado}")
            break
        ultimo_error = f"Respuesta inesperada: {resultado}"
    time.sleep(1)
else:
    sys.exit(f"La revisión {revision_esperada} no pasó la comprobación: {ultimo_error}")
