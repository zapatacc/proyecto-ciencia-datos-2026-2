# Actividad de clase 6 — EDA de NYC Green Taxi

## Propósito

Explorar viajes reales antes de construir el modelo que utilizará la API. La
parte calificable comprueba que puedes reconocer una observación, construir la
duración, detectar datos problemáticos e interpretar qué variables podrían ser
útiles para predecir.

El EDA es la primera etapa del trabajo de hoy, no el cierre. Después
continuaremos en la misma rama con preparación, entrenamiento y FastAPI.

## Espacio de trabajo

- Repositorio: `pcd-entregas-2026`.
- Rama única: `feat/clase-06-api-prediccion`.
- Carpeta: `actividades/clase-06-api-prediccion/`.
- Datos locales: `data/nyc-taxi/`.

Antes de descargar, agrega `data/` al `.gitignore` de la raíz. Los Parquet
se pueden volver a obtener desde TLC y no forman parte del historial.

```bash
uv add pandas pyarrow
mkdir -p data/nyc-taxi actividades/clase-06-api-prediccion
curl --fail --location --progress-bar \
  --output data/nyc-taxi/green_tripdata_2026-03.parquet \
  https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2026-03.parquet
curl --fail --location --progress-bar \
  --output data/nyc-taxi/green_tripdata_2026-04.parquet \
  https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2026-04.parquet
```

Marzo se explora y después se usa para entrenamiento. Abril queda reservado
para validar el modelo con otro periodo.

## Entregable calificable

Crea `eda.py` y `README.md` dentro de la carpeta de la actividad. El script
debe leer marzo de 2026 y el README debe presentar:

1. número de filas y columnas;
2. significado de una fila;
3. columnas usadas para calcular `duracion_minutos`;
4. cantidad y porcentaje de viajes con duración entre 1 y 60 minutos;
5. mínimo, mediana, promedio y máximo de `trip_distance` y
   `duracion_minutos` después del filtro;
6. valores faltantes de `passenger_count`;
7. comparación de viajes válidos entre días hábiles y fin de semana, derivada
   de `lpep_pickup_datetime`;
8. cantidad de zonas distintas en `PULocationID` y `DOLocationID`;
9. dos observaciones propias que puedan influir en la selección de features;
10. una captura del script ejecutado, sin rutas personales ni datos sensibles.

El análisis debe explicar los resultados; no basta con copiar
`describe()`. Para cada feature candidata, pregunta si estaría disponible
antes de iniciar el viaje. Por ejemplo, la hora de llegada, la propina y el
importe final no cumplen esa condición.

## Continuación durante la clase

Cuando termines el EDA, realiza un commit de checkpoint si el profesor lo
indica, pero no fusiones el trabajo. En la misma carpeta construiremos:

- `preparar_datos.py`;
- `entrenar_modelo.py`;
- `main.py`.

Antes de generar `modelo-duracion.pkl`, agrega `artifacts/` al
`.gitignore`. El modelo y los Parquet permanecen locales; los scripts,
`.gitignore`, `pyproject.toml`, `uv.lock`, README y evidencia sí se
confirman.

## Un solo pull request al final

Al terminar el recorrido completo:

1. revisa `git status --short`;
2. confirma que no aparezcan archivos `.parquet` ni `.pkl`;
3. abre un único PR hacia `main`;
4. revisa **Files changed** y completa la plantilla;
5. fusiona el PR y confirma que aparezca **Merged**;
6. entrega en Canvas la URL de ese PR.

La fecha y hora límite se publican en Canvas. Aunque el PR contiene el trabajo
guiado posterior, la rúbrica siguiente evalúa únicamente el EDA y su
interpretación.

## Uso de herramientas y colaboración

El EDA es individual. Puedes consultar el notebook, documentación oficial de
pandas y mensajes de error. No se permite usar IA generativa, autocompletado
generativo ni agentes para producir o interpretar el análisis calificable. La
construcción posterior del modelo y la API es una demostración guiada.

## Rúbrica — 100 puntos

| Criterio | Logro completo | Logro parcial | Insuficiente | Máximo |
|---|---|---|---|---:|
| Lectura y comprensión | **18–20:** identifica tamaño, unidad de observación y columnas del target correctamente. | **10–17:** existe una omisión menor. | **0–9:** no permite reconocer el conjunto analizado. | 20 |
| Limpieza y estadísticas | **27–30:** calcula filtro, porcentaje, estadísticos y faltantes de forma reproducible. | **16–26:** falta o es incorrecto un cálculo importante. | **0–15:** los resultados no son reproducibles o contradicen los datos. | 30 |
| Comparaciones y selección de features | **22–25:** compara tipo de día y zonas, y presenta dos observaciones justificadas considerando disponibilidad. | **13–21:** la comparación o interpretación es parcial. | **0–12:** sólo copia salidas o propone variables con fuga sin advertirlo. | 25 |
| Reproducibilidad y control de binarios | **13–15:** el script ejecuta, la captura es legible y los binarios no aparecen en el PR. | **7–12:** existe evidencia parcial o una inconsistencia menor. | **0–6:** falta ejecución o el PR incluye datos/modelos. | 15 |
| Pull request y entrega final | **9–10:** completa la plantilla, revisa el diff, fusiona a `main` y entrega la URL. | **5–8:** falta una evidencia menor. | **0–4:** PR abierto, cerrado sin merge o entrega ausente. | 10 |
| **Total** |  |  |  | **100** |
