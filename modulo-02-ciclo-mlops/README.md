# Módulo 2 — Ciclo MLOps

Este módulo conecta el modelo con un producto que pueda revisarse, repetirse y
mantenerse. Comienza con los problemas concretos de reproducibilidad,
versiones y operación que aparecen cuando una predicción debe repetirse,
identificarse y mantenerse. Las clases 8 y 9 establecen el ciclo, los tres
niveles, las interfaces y los patrones iniciales; la Clase 10 incorpora
trazabilidad de experimentos con MLflow y la Clase 11 convierte los modelos
seleccionados en versiones identificables dentro de Model Registry.
La Clase 12 guía primero la creación de una cuenta Databricks Free Edition y
usa tuning de hiperparámetros como caso para trasladar ese recorrido a su
servidor administrado de MLflow.

## Clases disponibles

- [Clase 8 — Introducción a MLOps](clase-08-introduccion-mlops.ipynb): recorre
  la definición, motivación, componentes, prácticas, ciclo y niveles de
  madurez 0–4. El caso NYC Taxi conecta datos, entrenamiento, evaluación,
  artefacto, versión e inferencia con código ejecutable.
- [Clase 9 — Tres niveles del software de ML](clase-09-niveles-software-ml.ipynb):
  organiza un sistema mediante datos, modelo y código; compara entrenamiento,
  inferencia y patrones de serving, y termina con un mapa calificable del
  proyecto entregado mediante PR.
- [Clase 10 — Experiment tracking con MLflow](clase-10-experiment-tracking.ipynb):
  registra y compara `LinearRegression` y `RandomForestRegressor` con los mismos
  datos, features y métrica; distingue runs, parámetros, métricas, datasets y
  artifacts sin adelantar Model Registry.
- [Clase 11 — Model Registry con MLflow](clase-11-model-registry.ipynb):
  retoma autologging, compara dos candidatos mediante parent y child runs, y
  recorre de forma interactiva el registro, versionado y carga mediante los
  aliases `champion` y `challenger`.
- [Clase 12 — Tuning de hiperparámetros con MLflow y Databricks](clase-12-mlflow-databricks.ipynb):
  crea o recupera una cuenta Free Edition, compara las configuraciones local y
  remota de Tracking, ajusta Linear Regression y Random Forest mediante parent
  y child runs, y registra en Unity Catalog los dos modelos finales del mismo
  caso Green Taxi.
