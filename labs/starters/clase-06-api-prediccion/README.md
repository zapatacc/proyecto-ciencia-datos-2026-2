# Recurso inicial — Clase 6

Esta carpeta publica únicamente una muestra pequeña para el showcase del
notebook.
Contiene 24 viajes reales seleccionados de
`green_tripdata_2026-03.parquet`, publicado por NYC Taxi & Limousine
Commission.

El notebook la lee directamente desde esta ubicación con `pandas`. No hace
falta copiarla porque durante el showcase sólo se consulta y no se modifica.

La muestra conserva columnas originales de zonas, distancia y pasajeros, y
agrega las variables preparadas `duracion_minutos`, `distancia_km`,
`hora_recoleccion` y `fin_de_semana`. Sólo incluye viajes de 1 a 60
minutos, distancia positiva y entre 1 y 6 pasajeros.

El dataset completo se descarga con `curl` dentro de `pcd-entregas-2026`,
como indica el notebook. Esta carpeta no distribuye el modelo entrenado: cada
estudiante lo reconstruye localmente después del EDA y `artifacts/` permanece
ignorado por Git.

Fuente: [NYC TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page).
