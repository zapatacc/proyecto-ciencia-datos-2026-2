# Muestras Green Taxi para el laboratorio de drift

Estos tres CSV son la alternativa reducida a las descargas del laboratorio.
Cada CSV contiene 1,200 viajes de su mes, las cinco variables de entrada
del curso y la duración observada, en minutos.

| Mes de inicio | Fuente TLC | SHA-256 del CSV |
|---|---|---|
| Marzo de 2026 | [Green Taxi, marzo](https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2026-03.parquet) | `5c1b47534f6f73ef2d6fca9e79f256dd114d9e3e43cf0655b140d2eb6e615320` |
| Abril de 2026 | [Green Taxi, abril](https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2026-04.parquet) | `a756f8b799d98d208b336bfcf52f8f8280f7649284cf0071f571dfa07d407cae` |
| Mayo de 2026 | [Green Taxi, mayo](https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2026-05.parquet) | `b63602ed5599ffc5d90419b2c8cc9590f60a4636437e2d0f494f42f2fe2c9ff0` |

Para reproducirlos, ejecuta `preparar_mes` de la guía con el Parquet y el mes
correspondientes. La función filtra por fecha de inicio y por los rangos del
caso, obtiene una muestra con la semilla 42 y conserva el contrato de Green
Taxi. Guarda el resultado con `to_csv(index=False, lineterminator="\n")`.
La fuente original es la [NYC Taxi & Limousine Commission](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page).

Copia los CSV que necesites a `datos/` dentro de tu repositorio de práctica.
