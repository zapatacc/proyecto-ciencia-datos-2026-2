# Laboratorio 1 — Rendimiento de la API de predicción

## Resultado esperado

Comparar dos versiones de un servicio que estima la duración de **un viaje por solicitud**. Al terminar tendrás una medición HTTP por modelo, su RMSE en la misma muestra reservada y una recomendación de qué modelo servir.

El **RMSE** mide el error de predicción en minutos y da más peso a los errores grandes. La **latencia HTTP** en esta práctica es el tiempo desde que el cliente envía la solicitud hasta que recibe la respuesta completa. Incluye conexión local, serialización y procesamiento. El **p95** señala un tiempo que alcanzó o mejoró aproximadamente el 95 % de las solicitudes exitosas. La **mediana** muestra el centro de esos tiempos. Se contabilizan por separado las respuestas fallidas.

## Preparar el proyecto

Actualiza el repositorio público del curso mediante `git status` y `git pull` desde `main`. Crea y clona el repositorio nuevo y privado siguiendo la [consigna común](README.md). Desde la raíz del clon del equipo, ejecuta `git switch -c feat/rendimiento-api` para abrir la rama de trabajo.

1. Copia el contenido del [starter de este laboratorio](../../../labs/starters/clase-24-laboratorios-mlops/01-rendimiento-api) a la raíz del repositorio del equipo. Conserva las carpetas y los archivos ocultos. La [consigna común](README.md#copiar-los-archivos-del-laboratorio) incluye el comando de copia.
2. Copia `modelos.py` y `preparar_datos.py` del [starter de Clase 10](../../../labs/starters/clase-10-experiment-tracking/README.md) a la raíz. Copia el contenido de la carpeta `datos/` de la Clase 10. Incluye las muestras de entrenamiento y evaluación.
3. Prepara el ambiente desde el repositorio del equipo. `uv sync --locked` instala las versiones del `uv.lock` que viene con el starter.

```bash
uv sync --locked
uv run --locked python --version
```

**Comprueba** con `git status --short` que estás en el repositorio del equipo y que llegaron los archivos del starter. La terminal debe mostrar Python 3.12.

## Qué mide el script

`api_local.py` ajusta el modelo al arrancar. `medir_api.py` calcula el RMSE sobre la muestra reservada, envía cinco solicitudes de calentamiento y mide 100 peticiones secuenciales. El cronómetro cubre la ida y vuelta HTTP. La mediana y el p95 se calculan sobre las respuestas exitosas, y las fallas se contabilizan aparte. Mantén las mismas solicitudes y condiciones para ambos modelos.

## Ejecutar y comparar

Trabaja con dos terminales abiertas en la raíz del clon del equipo. En la primera, `--modelo` selecciona el pipeline y `--puerto` cambia el puerto local donde escucha la API.

```bash
uv run --locked python api_local.py --modelo linear_regression --puerto 8000
```

Después de que inicie la API, abre [la documentación interactiva](http://127.0.0.1:8000/docs). En `GET /health` selecciona **Try it out** y **Execute** para ver el nombre del modelo. En la segunda terminal, mide el servicio con la dirección base indicada por `--url`.

```bash
uv run --locked python medir_api.py --modelo linear_regression --url http://127.0.0.1:8000
```

Conserva la salida. Detén la primera API con **Ctrl+C** antes de ejecutar la segunda. Repite en la primera y segunda terminal, respectivamente.

```bash
uv run --locked python api_local.py --modelo random_forest --puerto 8000
```

```bash
uv run --locked python medir_api.py --modelo random_forest --url http://127.0.0.1:8000
```

**Comprueba** que cada corrida dice qué modelo midió, informa el RMSE en 500 viajes y contabiliza las 100 solicitudes. Los tiempos dependen del equipo, la sesión y las aplicaciones activas. Usa la misma computadora, el mismo puerto y condiciones comparables. Si una corrida tiene fallos, corrígelos y repite ambas mediciones para sustentar la comparación.

- Si aparece `Connection refused`, revisa que el servidor haya arrancado y que ambos comandos usen el mismo puerto.
- Si el script detecta un modelo distinto, revisa qué proceso sigue activo en ese puerto. Detén la API anterior y vuelve a consultar `/health`.
- Si aparece `422`, comprueba que el cuerpo tenga sólo las cinco características de entrada y coincida con el contrato publicado en `/docs`.

## Evidencia y cierre

Guarda en `evidencia/` una captura por cada ejecución del script, con el comando y la salida visibles. Enlaza ambas desde `README.md`. Incluye una tabla con modelo, RMSE, mediana, p95 y número de fallos. Explica qué modelo elegirías y qué condición podría cambiar esa decisión. Esta comparación local describe latencia secuencial; una prueba de concurrencia sería una medición distinta.

Detén el último servidor con **Ctrl+C**. Publica tu rama y abre un pull request hacia `main`. Revísalo con tu equipo y fusiónalo cuando lo hayan comprobado. Revisa la [entrega y rúbrica](README.md).

**Qué explicar en el README.** ¿Por qué se descartan las solicitudes de calentamiento y qué tramo mide la latencia HTTP? Usa la mediana, el p95 y los fallos observados para justificar qué modelo servirías.

## Referencias

- [RMSE en scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.root_mean_squared_error.html).
- [Clientes HTTPX](https://www.python-httpx.org/advanced/clients/).
