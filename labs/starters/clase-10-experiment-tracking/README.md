# Starter — Clase 10: Experiment tracking

Este starter contiene una muestra preparada de Green Taxi y dos módulos de
apoyo. No es un proyecto independiente: usa el ambiente y las dependencias de
la raíz del repositorio.

Durante la práctica:

1. crea `labs/trabajo-local/clase-10/`;
2. copia allí el contenido de este directorio;
3. crea `registrar_experimentos.py` siguiendo el notebook;
4. inicia el servidor local de MLflow desde la raíz del repositorio;
5. ejecuta el script y compara los dos runs en la interfaz.

El directorio `labs/trabajo-local/` está ignorado por Git. Los archivos
`mlflow.db`, `mlartifacts/` y los modelos generados permanecen locales.

## Datos

- `datos/green-taxi-train.csv`: 1,200 filas de marzo de 2026.
- `datos/green-taxi-validation.csv`: 500 filas de abril de 2026.
- Fuente: [NYC Taxi & Limousine Commission — Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page),
  [marzo de 2026](https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2026-03.parquet)
  y [abril de 2026](https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2026-04.parquet).

Las muestras se obtuvieron de los archivos oficiales
`green_tripdata_2026-03.parquet` y `green_tripdata_2026-04.parquet`, aplicando
los filtros canónicos del caso NYC Taxi y un muestreo con `random_state=42`. Ya contienen las
cinco features y el target preparados. El proceso es reproducible con
`tools/teacher/generar_fixture_clase_10.py`.

SHA-256 de los CSV publicados:

- entrenamiento: `d6caa8367737b83f9374ca0df3a39f2369158a66f3abae2b7111c53af20beeb1`;
- validación: `c76a018b5627aef2d67c847664412a7649faa49e43cc085d7518d339459f8703`.
