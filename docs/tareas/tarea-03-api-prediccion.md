# Tarea 3 — Comparación de dos modelos servidos por una API

## Propósito

Extender el recorrido construido en la Clase 6 para comparar dos formas de
estimar la duración de un viaje. Entrenarás una regresión lineal y un bosque
aleatorio con exactamente los mismos datos y features, guardarás ambos
artefactos de manera local y crearás un endpoint para cada modelo.

La comparación no termina al elegir el RMSE más bajo. También considerarás el
tiempo de entrenamiento, el tamaño del artefacto y la complejidad de cada
alternativa.

## Recursos

- Notebook de la Clase 5: entradas validadas con Pydantic.
- Notebook de la Clase 6: datos, EDA, entrenamiento, pickle e inferencia.
- Código construido en `actividades/clase-06-api-prediccion/`.
- [Flujo de trabajo y entrega de tareas](../flujo-tareas.md).
- [Plantilla de pull request](../plantillas/pull-request-tarea.md).

## Entregable

**Repositorio:** tu repositorio privado individual `pcd-entregas-2026`.

**Carpeta:** `tareas/tarea-03-api-prediccion/`

**Rama obligatoria:** `feat/03-api-prediccion`

**Fecha límite:** lunes 7 de septiembre de 2026 a las 19:55,
hora de la Ciudad de México.

Parte de `main` después de fusionar la actividad de la Clase 6. Reutiliza el
proyecto `uv` de la raíz; no crees otro proyecto anidado.

## 1. Dos scripts de entrenamiento

Dentro de la carpeta de la tarea incluye:

```text
tareas/tarea-03-api-prediccion/
├── preparar_datos.py
├── entrenar_modelo_lineal.py
├── entrenar_modelo_bosque.py
├── main.py
├── evidencia/
└── README.md
```

Puedes adaptar la función `preparar_viajes` de la clase, pero ambos modelos
deben usar la misma preparación, las mismas cinco features y la misma
separación temporal:

- marzo de 2026 para entrenamiento;
- abril de 2026 para validación;
- `distancia_km`, `pasajeros`, `hora_recoleccion`, `zona_origen` y
  `zona_destino` como features;
- `duracion_minutos` como target.

`entrenar_modelo_lineal.py` reproduce el pipeline de la clase con
`LinearRegression`. `entrenar_modelo_bosque.py` conserva el mismo
`ColumnTransformer` y sustituye únicamente el estimador final por:

```python
RandomForestRegressor(
    n_estimators=100,
    max_depth=12,
    min_samples_leaf=5,
    n_jobs=-1,
    random_state=42,
)
```

Cada script debe:

1. cargar y preparar marzo y abril;
2. ajustar su pipeline con marzo;
3. calcular el RMSE sobre abril;
4. medir el tiempo de entrenamiento;
5. guardar un diccionario con el pipeline, el orden de las features, el nombre
   del algoritmo, una versión y el RMSE;
6. imprimir la ruta y el tamaño final del artefacto.

Los resultados se generan en:

```text
artifacts/nyc-taxi/modelo-duracion-lineal.pkl
artifacts/nyc-taxi/modelo-duracion-bosque.pkl
```

Ejecuta los dos scripts en tu computadora. Conserva en `.gitignore` las reglas
para `data/` y `artifacts/`: los archivos `.parquet` y `.pkl` son pesados o
reconstruibles y **no deben aparecer en ningún commit ni en Files changed**.

## 2. Dos endpoints comparables

Crea una aplicación FastAPI que cargue ambos artefactos una sola vez al iniciar
y exponga:

- `POST /predicciones/regresion-lineal`
- `POST /predicciones/bosque-aleatorio`

Los dos endpoints reciben exactamente el mismo JSON:

```json
{
  "distancia_km": 4.2,
  "pasajeros": 2,
  "hora_recoleccion": 18,
  "zona_origen": 75,
  "zona_destino": 42
}
```

| Campo | Tipo y regla |
|---|---|
| `distancia_km` | `float` mayor que 0 y hasta 100 |
| `pasajeros` | `int` entre 1 y 6 |
| `hora_recoleccion` | `int` entre 0 y 23 |
| `zona_origen` | `int` entre 1 y 265 |
| `zona_destino` | `int` entre 1 y 265 |

Ambos usan el mismo `response_model`:

```json
{
  "duracion_estimada_minutos": 14.8,
  "modelo": "regresion-lineal",
  "version_modelo": "green-taxi-2026-03-lineal-1"
}
```

El valor de duración es ilustrativo: no lo codifiques. Debe provenir del
pipeline correspondiente. El endpoint no abre el pickle ni ejecuta `fit` por
solicitud.

## 3. Comparación en el README

Ejecuta ambos entrenamientos y registra una tabla como ésta con tus resultados:

| Modelo | RMSE en abril (min) | Entrenamiento (s) | Tamaño del `.pkl` (MiB) |
|---|---:|---:|---:|
| Regresión lineal | resultado propio | resultado propio | resultado propio |
| Bosque aleatorio | resultado propio | resultado propio | resultado propio |

Después explica:

1. cuál modelo obtuvo el menor RMSE y qué significa esa diferencia en minutos;
2. cuál requirió más tiempo y produjo el artefacto más grande;
3. cuál elegirías para este ejercicio y qué criterio sostiene tu decisión;
4. dos ventajas y tres limitaciones de servir modelos mediante pickles locales.

Usa la misma validación para que la comparación sea justa. No copies cifras del
notebook ni de otra persona: reporta las obtenidas al ejecutar tus scripts.

## 4. Recorrido completo y evidencia

La evidencia debe contar el mismo recorrido que construiste: entrenar los dos
modelos, iniciar la API y obtener predicciones con cada uno. Desde la carpeta
de la tarea, ejecuta en este orden:

```bash
uv run python entrenar_modelo_lineal.py
uv run python entrenar_modelo_bosque.py
uv run fastapi dev
```

Con FastAPI activo, usa la herramienta que prefieras —**Postman**, la interfaz
interactiva `/docs` o `curl`— para enviar el JSON de la sección 2 a los dos
endpoints. Después verifica los dos errores de contrato: una solicitud con
`hora_recoleccion: 24` y otra que omita `zona_destino`.

Guarda las imágenes dentro de `tareas/tarea-03-api-prediccion/evidencia/` y
enlázalas desde el README. No necesitas capturas del entrenamiento: sus
resultados se reportan en la tabla de comparación de la sección 3. Incluye
únicamente estas evidencias:

| Momento | Imagen requerida | Debe mostrar |
|---|---|---|
| Predicción lineal | llamada con `200` | método, URL, JSON válido y respuesta que identifica la regresión lineal |
| Predicción de bosque | llamada con `200` | método, URL, JSON válido y respuesta que identifica el bosque aleatorio |
| Validación de hora | llamada con `422` | método, URL, `hora_recoleccion: 24` y detalle del error |
| Validación de campo requerido | llamada con `422` | método, URL, ausencia de `zona_destino` y detalle del error |

El README debe incluir los tres comandos anteriores, la tabla de comparación de
la sección 3 y enlaces a las cuatro imágenes. Cada imagen debe hacer visible
la solicitud y su respuesta; en `curl`, muestra el comando completo y la salida
en la misma captura. No muestres rutas personales en las capturas. La revisión
del código comprobará que los dos artefactos se cargan una vez al iniciar y que
los endpoints no ejecutan `fit`.

## Archivos que sí y que no se entregan

| Sí forman parte de Git | Permanecen sólo en tu computadora |
|---|---|
| scripts `.py` | archivos `.parquet` |
| `README.md` y evidencia | contenido de `.venv/` |
| `.gitignore` | cachés locales |
| `pyproject.toml` y `uv.lock`, si cambiaron | |

Antes de publicar, revisa `git status` y **Files changed**. Si aparece un
Parquet o un pickle, detén el flujo y corrige `.gitignore` antes de continuar.

## Commits

Realiza al menos dos commits sustantivos, por ejemplo:

```text
feat(tarea-03): entrena dos modelos de duracion
feat(tarea-03): publica endpoints comparables
docs(tarea-03): documenta validacion en postman
docs(tarea-03): compara resultados de validacion
```

No hagas commits vacíos.

## Pull request y entrega

El PR apunta a `main`, copia y completa la plantilla del curso, se revisa en
**Files changed** y termina **Merged** y cerrado. La entrega oficial en Canvas
es únicamente la URL de ese PR antes de la fecha límite.

## Uso de herramientas y colaboración

La tarea es individual. No se permite usar IA generativa, autocompletado
generativo ni agentes de programación para producir, corregir o explicar el
código, README o evidencia. Sí puedes consultar notebooks, documentación
oficial, mensajes de error y pedir ayuda al profesor.

## Rúbrica — 100 puntos

| Criterio | Logro completo | Logro parcial | Insuficiente | Máximo |
|---|---|---|---|---:|
| Entrenamiento reproducible de dos modelos | **27–30:** ambos scripts usan la misma preparación y partición, entrenan el estimador indicado, calculan métricas y generan artefactos con metadatos. | **16–26:** los dos modelos entrenan, pero existe una inconsistencia menor de preparación, evaluación o metadatos. | **0–15:** falta un modelo, no hay validación comparable o depende de artefactos ajenos. | 30 |
| API con dos endpoints | **22–25:** carga ambos artefactos una vez, expone las dos rutas con el mismo contrato y predice con el modelo correcto. | **13–21:** la API inicia, pero una ruta, respuesta o carga presenta una inconsistencia. | **0–12:** falta un endpoint, se reentrena por solicitud o no hay inferencia real. | 25 |
| Comparación y decisiones | **18–20:** reporta RMSE, tiempo y tamaño con resultados propios y argumenta una elección considerando tradeoffs. | **10–17:** presenta resultados, pero la comparación o justificación es parcial. | **0–9:** faltan métricas comparables o se elige sin evidencia. | 20 |
| Validación manual, evidencia y exclusiones | **13–15:** cuatro capturas de llamadas cubren ambos modelos, los casos `200` y los dos casos `422`; ningún Parquet o pickle entra a Git. | **7–12:** validación o evidencia parcial sin comprometer los binarios. | **0–6:** faltan verificaciones esenciales o se confirman datos/artefactos. | 15 |
| Git, PR y entrega | **9–10:** rama correcta, commits sustantivos, README reproducible, PR fusionado y URL entregada a tiempo. | **5–8:** el trabajo llega a `main` con una omisión menor. | **0–4:** historial no evaluable, PR sin merge o entrega ausente. | 10 |
| **Total** |  |  |  | **100** |
