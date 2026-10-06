# Tarea 6 — Orquestar el pipeline de entrenamiento con Prefect

## Propósito

Refactorizar el trabajo de la Tarea 5 como un workflow reproducible de Prefect.
No entrenarás familias nuevas: conservarás `LinearRegression`,
`RandomForestRegressor` y `GradientBoostingRegressor`, sus cinco features, HPO,
MLflow y aliases dinámicos.

## Entregable

**Repositorio:** `pcd-entregas-2026`.

**Carpeta:** `tareas/tarea-06-pipeline-prefect/`

**Rama obligatoria:** `feat/06-pipeline-prefect`

**Fecha y hora límite:** viernes 9 de octubre de 2026 a las 19:55, hora de la
Ciudad de México. La entrega oficial se realiza en Canvas.

Incluye `pipeline_prefect.py`, `mejores-parametros.json`, `README.md` y una
carpeta `evidencias/`. Parte de tu código de la Tarea 5 y conserva secretos,
Parquet, modelos y `.env` fuera de Git.

## Requisitos

1. Una task comprueba si marzo y abril existen bajo `data/nyc-taxi/` y descarga
   únicamente los archivos faltantes.
2. Ambos meses pasan por la misma preparación y validación de contrato.
3. Marzo se divide en entrenamiento interno y validación de tuning. Abril no
   puede ser argumento de una función objetivo ni de una task de HPO.
4. El flow acepta `hacer_tuning`. Con `True`, ejecuta los tres estudios y
   actualiza `mejores-parametros.json`; con `False`, reutiliza ese archivo.
5. Cada familia se reentrena con marzo completo y se evalúa una vez con abril.
6. MLflow registra únicamente los tres modelos finales. Registry asigna
   `champion`, `challenger` y `candidate` según el RMSE, no por familia.
7. Los reintentos se reservan para la descarga o una operación externa; un
   schema inválido debe fallar sin reintentos.

No se requieren deployments, schedules, workers ni Prefect Cloud.

## Verificación y evidencia

Incluye tres imágenes enlazadas desde el README:

- flow exitoso con `hacer_tuning=True` y las tasks identificables;
- ejecución con `hacer_tuning=False` que reutiliza parámetros;
- falla controlada por una columna faltante, con la task fallida y el mensaje.

Documenta además el diagrama del flow, la función de cada task, el ranking de
los modelos y por qué abril permanece fuera del HPO. No expongas rutas
personales, host, token, correo ni identificadores de cuenta.

## Commits, pull request y entrega

Realiza commits sustantivos con Conventional Commits. El PR apunta a `main`,
copia la plantilla de `docs/plantillas/pull-request-tarea.md`, se revisa y se
fusiona mediante **Create a merge commit**. La entrega oficial en Canvas es la
URL del PR cerrado y fusionado.

## Uso de herramientas y colaboración

La tarea es individual. No se permite usar IA generativa, autocompletado
generativo ni agentes de programación para producir, corregir o explicar el
código, README o evidencia. Puedes consultar los notebooks, documentación
oficial, mensajes de error y pedir ayuda al profesor.

## Rúbrica — 100 puntos

| Criterio | Logro completo | Logro parcial | Insuficiente | Máximo |
|---|---|---|---|---:|
| Flow y tasks | **23–25:** responsabilidades y dependencias son observables y el flow termina correctamente. | **13–22:** el flow funciona con una separación menor poco clara. | **0–12:** sólo se decoró el script completo o el flow no ejecuta. | 25 |
| Datos y separación temporal | **18–20:** descarga sólo faltantes, prepara ambos meses igual y excluye abril del HPO. | **10–17:** funciona con una inconsistencia menor. | **0–9:** preparación divergente o fuga de abril. | 20 |
| HPO activable | **18–20:** tres familias, ambos modos y JSON reproducible funcionan. | **10–17:** un modo o familia queda incompleto. | **0–9:** la flag no cambia el recorrido o falta HPO. | 20 |
| MLflow y Registry | **13–15:** registra tres finales y asigna aliases por ranking. | **7–12:** tracking o aliases tienen una omisión. | **0–6:** no hay registro verificable o aliases fijos. | 15 |
| Verificación y documentación | **9–10:** tres evidencias, diagrama e interpretación permiten reproducir el trabajo. | **5–8:** evidencia o explicación parcial. | **0–4:** no se puede verificar. | 10 |
| Git, PR y entrega | **9–10:** rama, commits, PR fusionado y entrega correctos. | **5–8:** existe una omisión menor. | **0–4:** historial no evaluable o PR sin merge. | 10 |
| **Total** |  |  |  | **100** |
