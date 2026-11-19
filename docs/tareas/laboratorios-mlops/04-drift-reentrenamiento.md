# Laboratorio 4 — Detectar drift y decidir si reentrenar

## Resultado observable

Construirás un flujo local de Prefect que compara las zonas de origen de dos ventanas de viajes Green Taxi. Cuando la diferencia alcanza un umbral, el flujo entrena un candidato, lo compara con el modelo vigente y guarda la decisión en un JSON.

**Data drift** es un cambio en la distribución de las entradas. Por ejemplo, si una zona pasa del 10 % al 15 % de los viajes, su proporción cambió **5 puntos porcentuales**. Usarás el mayor cambio absoluto entre todas las zonas, incluidas las que aparecen en una sola ventana. Para decidir si el candidato reduce el error utilizarás **RMSE**, expresado en minutos. Este segundo cálculo necesita las duraciones observadas al terminar los viajes. Recupera los conceptos de task y flow en la [Clase 13](../../../modulo-02-ciclo-mlops/clase-13-pipelines.ipynb).

| Ventana de Green Taxi | Uso |
|---|---|
| Marzo de 2026 | Referencia de entradas y ajuste del modelo inicial. |
| Abril de 2026 | Observación de entradas. Si hay alerta, ajustar el candidato con las duraciones de abril disponibles después de los viajes. |
| Mayo de 2026 | Evaluación reservada. Usar las mismas filas para calcular el RMSE de ambos modelos. |

Es una reproducción histórica de un escenario de operación. Los datos de TLC registran viajes terminados y la distancia histórica actúa como aproximación a la distancia estimada antes del viaje. Los filtros y las muestras delimitan la población sobre la que interpretarás los resultados. [NYC TLC — Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

## Preparar el proyecto

Actualiza el repositorio público del curso mediante `git status` y `git pull` desde `main`. Crea y clona el repositorio nuevo y privado siguiendo la [consigna común](README.md). Desde la raíz del clon del equipo, ejecuta `git switch -c feat/drift-reentrenamiento` para abrir la rama de trabajo.

1. Copia el contenido del [starter de este laboratorio](../../../labs/starters/clase-24-laboratorios-mlops/04-drift-reentrenamiento) a la raíz del repositorio del equipo. Conserva las carpetas y los archivos ocultos. La [consigna común](README.md#copiar-los-archivos-del-laboratorio) incluye el comando de copia.
2. Copia `modelos.py` y `preparar_datos.py` del [starter de Clase 10](../../../labs/starters/clase-10-experiment-tracking/README.md) a la raíz. Prepara la carpeta `datos/` siguiendo el apartado de descarga. Las muestras de Clase 10 se usan en otros laboratorios.
3. Prepara el ambiente desde el repositorio del equipo. `uv sync --locked` instala las versiones del `uv.lock` que viene con el starter.

```bash
uv sync --locked
uv run --locked python --version
```

**Comprueba** con `git status --short` que estás en el repositorio del equipo y que llegaron los archivos del starter. La terminal debe mostrar Python 3.12.

## 2. Descargar los tres meses

Ejecuta el bloque desde Git Bash, Zsh o Bash. El bucle prueba si ya existe cada archivo. `curl --fail` marca errores HTTP como fallos, `--location` sigue redirecciones y `--output` establece la ruta de destino. La descarga queda primero en un archivo temporal `.part`. El bloque lo renombra sólo al terminar correctamente. Así se conservan las descargas válidas entre ejecuciones.

```bash
mkdir -p datos
for mes in 03 04 05; do
  archivo="datos/green_tripdata_2026-${mes}.parquet"
  if [ ! -f "$archivo" ]; then
    curl --fail --location --output "$archivo.part" \
      "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2026-${mes}.parquet" \
      && mv "$archivo.part" "$archivo"
  fi
done
```

**Si falla la descarga**, copia los tres CSV de las [muestras de contingencia](../../../labs/starters/clase-24-laboratorios-mlops/drift/README.md) a `datos/`. Contienen filas reales de los mismos meses, seleccionadas con el procedimiento del laboratorio. Usa `--muestras` al ejecutar. La ruta Parquet verifica SHA-256 antes de leer cada archivo y filtra por mes de inicio, que puede diferir del mes del archivo en registros atípicos.

## 3. Qué compara el flujo

`drift.py` comprueba la huella SHA-256 de cada Parquet y limita cada ventana a 1,200 filas con una semilla fija. Compara las proporciones de zonas de origen, incluidas las ausentes en una ventana. El umbral didáctico es **3 puntos porcentuales**. El candidato resulta apto si mejora el RMSE de mayo por al menos **0.10 minutos**.

El escenario controlado concentra la **señal de observación** en una zona. El modelo candidato sigue entrenando con la muestra histórica ordinaria de abril. Mayo queda reservado para evaluar ambos modelos.

## 4. Ejecutar y comprobar

**Desde el notebook.** Abre `drift.ipynb` en la raíz del repositorio del equipo. En VS Code, usa **Select Kernel → Python Environments** y elige el Python 3.12 de `.venv`. Ejecuta las celdas en orden. El kernel es el proceso Python que las ejecuta y determina qué bibliotecas están disponibles. Usa esta opción o los comandos de terminal de abajo.

**Desde la terminal**, ejecuta los tres escenarios desde la raíz del repositorio. `unset` retira de esa terminal la URL y la clave que pudieras tener configuradas para otro servidor de Prefect. Las variables que siguen activan un servidor temporal local y sitúan su base de datos en la carpeta del laboratorio.

```bash
export PREFECT_HOME="$PWD/.prefect"
unset PREFECT_API_URL PREFECT_API_KEY
export PREFECT_SERVER_EPHEMERAL_ENABLED=true
export PREFECT_SERVER_ANALYTICS_ENABLED=false
uv run --locked python drift.py control
uv run --locked python drift.py historico
uv run --locked python drift.py controlado
```

Con los CSV de contingencia, agrega `--muestras` al final de cada comando. El argumento elige la fuente de las tres ventanas.

- **Control.** El cambio es cero. El JSON muestra `sin_reentrenamiento` y el log no contiene una corrida de la tarea `evaluar_candidato`.
- **Histórico.** El JSON registra una zona, su cambio y la decisión que corresponde al umbral. Si aparece `sin_reentrenamiento`, el cambio histórico quedó por debajo del umbral con estas muestras.
- **Controlado.** La diferencia supera el umbral. El log muestra `evaluar_candidato` y el JSON registra los dos RMSE y la decisión. Una alerta puede terminar en `conservar_vigente` si el candidato no alcanza la mejora establecida.

En el README, enlaza los tres JSON. Guarda en `evidencia/` una captura por escenario donde se vea el comando y la decisión y enlázala desde el README. Explica de dónde sale la alerta, qué datos se usaron para medir error y qué evidencia permitiría revisar este umbral en un sistema real. Consulta la [consigna y rúbrica comunes](README.md).

El servidor temporal se detiene al finalizar el proceso. Cierra la terminal del ejercicio para terminar la sesión con estas variables.

**Qué explicar en el README.** ¿Por qué un cambio de proporciones puede disparar el entrenamiento y qué evidencia exige la decisión sobre el candidato? Identifica el papel de cada mes en tus resultados.
