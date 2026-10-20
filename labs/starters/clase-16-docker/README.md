# Recursos para Clase 16

`api.py` recupera el contrato de cinco features de Clase 14. El recurso permite
concentrar el trabajo en Docker; no contiene el Dockerfile ni las dependencias.
Copia `api.py` a `labs/trabajo-local/clase-16/` como indica el notebook. Crea allí
`.env` usando `.env.example` como referencia y tu configuración personal previa.
No copies tokens a archivos rastreados ni compartas el `.env`.

La API carga una sola vez la versión resuelta desde el alias. `/health` informa
además `version_api`, para observar la reconstrucción de una imagen.

Si el profesor proporciona un MLflow Model local, la variable opcional
`RUTA_MODELO_LOCAL=artefactos/modelo` permite cargarlo con el mismo contrato,
sin autenticación ni Registry. No es evidencia de acceso al modelo remoto.
