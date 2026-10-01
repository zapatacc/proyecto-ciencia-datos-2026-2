# Tarea 5 — Comparar tres familias con HPO y MLflow

## Propósito

Retomar el caso NYC Taxi que construiste en la Tarea 3 y llevarlo a un
experimento remoto. Conservarás los mismos datos, cinco features y
preprocesamiento. Esta vez ajustarás hiperparámetros de tres familias:
`LinearRegression`, `RandomForestRegressor` y `GradientBoostingRegressor`.

Cada familia tendrá su propio estudio, organizado mediante un parent run y sus
child runs. Al final registrarás el mejor pipeline de cada familia, los
compararás con abril y asignarás los aliases `champion`, `challenger` y
`candidate` según los resultados obtenidos.

El propósito no es obtener el menor RMSE posible a cualquier costo. Debes
conservar una separación correcta entre tuning y evaluación final, y considerar
también tiempo, complejidad y reproducibilidad.

## Fecha de entrega

**Lunes 5 de octubre de 2026 a las 19:55**, antes de la clase.

La entrega oficial es la URL del pull request cerrado y fusionado en Canvas.
El trabajo debe estar completo en `main` antes de esa hora.

## Recursos y consultas

- [Clase 12 — Tuning de hiperparámetros con MLflow y Databricks](../../modulo-02-ciclo-mlops/clase-12-mlflow-databricks.ipynb)
- [Tarea 3 — API para comparar modelos de predicción](tarea-03-api-prediccion.md)
- [Flujo de trabajo y entrega de tareas](../flujo-tareas.md)
- [Plantilla de pull request](../plantillas/pull-request-tarea.md)
- [Crear una cuenta de Databricks Free Edition](https://docs.databricks.com/aws/en/getting-started/free-edition)
- [Diferencias entre Free Edition y free trial](https://docs.databricks.com/aws/en/getting-started/free-trial-vs-free-edition)
- [Databricks: Personal Access Tokens](https://docs.databricks.com/aws/en/dev-tools/auth/pat)
- [Databricks: variables de autenticación](https://docs.databricks.com/aws/en/dev-tools/auth/env-vars)
- [python-dotenv](https://bbc2.github.io/python-dotenv/)
- [MLflow: Tracking Hyperparameter Tuning](https://mlflow.org/docs/latest/ml/getting-started/hyperparameter-tuning/)
- [MLflow: Parent and Child Runs](https://mlflow.org/docs/latest/ml/traditional-ml/tutorials/hyperparameter-tuning/part1-child-runs/)
- [MLflow: Search Logged Models](https://mlflow.org/docs/latest/ml/search/search-models/)
- [Databricks-hosted MLflow Tracking](https://docs.databricks.com/aws/en/mlflow/tracking-server-configuration)
- [Databricks: Log, load and register models](https://docs.databricks.com/aws/en/mlflow/models)
- [Optuna documentation](https://optuna.readthedocs.io/en/stable/)

## Entregable

**Repositorio:** tu repositorio privado individual `pcd-entregas-2026`.

**Carpeta:** `tareas/tarea-05-tuning-mlflow-databricks/`

**Rama obligatoria:** `feat/05-tuning-mlflow-databricks`

Reutiliza el proyecto `uv` de la raíz. No crees un segundo proyecto dentro de
la tarea.

La carpeta debe contener:

```text
tareas/tarea-05-tuning-mlflow-databricks/
├── README.md
├── ajustar_modelos.py
└── evidencias/
    ├── 01-runs-anidados.png
    ├── 02-comparacion-y-registry.png
    └── 03-carga-por-alias.png
```

No agregues CSV, Parquet, pickles, tokens, `.env`, modelos
descargados ni contenido de `.venv/`.

## Punto de partida: retomar la Tarea 3

No estás comenzando otro proyecto de NYC Taxi. Usa como referencia el código
que ya construiste en `tareas/tarea-03-api-prediccion/`, en particular:

- `preparar_datos.py` y el contrato de las cinco features;
- el `ColumnTransformer` compartido;
- la configuración de `LinearRegression` de
  `entrenar_modelo_lineal.py`;
- la configuración fija de `RandomForestRegressor` de
  `entrenar_modelo_bosque.py`;
- marzo para desarrollo, abril para validación y RMSE en minutos.

Puedes reutilizar y adaptar código propio, pero no copies a la nueva carpeta
los archivos de datos ni los pickles de la Tarea 3. Los tres modelos se
entrenan de nuevo dentro del experimento para conservar su procedencia, sus
parámetros y sus métricas.

## 0. Cuenta y workspace antes de programar

Usa una cuenta individual de **Databricks Free Edition para uso personal**. No
uses la prueba empresarial de 14 días ni un workspace de otra persona. Free
Edition no requiere tarjeta, cuenta de AWS, Azure o Google Cloud, y crea un
workspace serverless de forma automática.

Si todavía no tienes la cuenta, completa primero las secciones 3.1–3.6 de la
Clase 12:

1. registra la cuenta en la página oficial de Free Edition;
2. entra al workspace creado automáticamente;
3. identifica su URL base;
4. confirma que puedes ver Experiments y Catalog Explorer;
5. crea un Personal Access Token desde **Settings → Developer**;
6. guarda la URL en `DATABRICKS_HOST` y el token en `DATABRICKS_TOKEN` dentro
   del archivo `.env` de la raíz;
7. confirma que Git ignora el archivo con `git check-ignore .env`.

No incluyas capturas del registro de la cuenta, correo, nombre personal, URL
completa del workspace ni contenido de `.env` en la entrega. La evidencia
empieza en el experimento de MLflow y debe ocultar identificadores personales.

Free Edition está sujeta a cuotas. No dejes la tarea para la última hora: si
una cuota suspende temporalmente el servicio, conserva el código local y
retoma la captura de evidencia cuando el acceso se restablezca. El servidor
local de las clases 10–11 sirve para depurar, pero no sustituye la evidencia
remota solicitada.

## 1. Servidor y experimento exclusivos

Usa el servidor administrado de MLflow incluido en **tu propia cuenta de
Databricks**. No uses el servidor local de las clases 10 y 11 para producir la
evidencia de esta tarea.

Carga las credenciales con `load_dotenv()` y usa `mlflow.set_tracking_uri(
"databricks")` y `mlflow.set_registry_uri("databricks-uc")`. No escribas el
host, token, correo o credenciales dentro del script.

El `.env` de la raíz debe seguir esta estructura y nunca se incluye en Git:

```dotenv
DATABRICKS_HOST=https://<identificador-del-workspace>.cloud.databricks.com
DATABRICKS_TOKEN=<token-personal>
```

El experimento obligatorio es:

```text
/Shared/pcd-otono-2026-tarea-05-nyc-taxi
```

Cada estudiante puede usar exactamente el mismo nombre porque cada cuenta
individual tiene su propio workspace. No agregues nombre, correo, matrícula ni
usuario de GitHub al nombre del experimento.

Este experimento pertenece únicamente a la Tarea 5. No reutilices el
experimento guiado `/Shared/pcd-otono-2026-clase-12-nyc-taxi` y no acumules en
él runs de otras tareas o del proyecto semestral.

Si el profesor asignara posteriormente un workspace institucional compartido,
se entregará un identificador anónimo y la ruta cambiará a:

```text
/Shared/pcd-otono-2026-tarea-05-nyc-taxi-<identificador-asignado>
```

No inventes ese identificador ni uses datos personales.

## 2. Naming y distribución de runs

El experimento contiene tres parent runs, uno por familia:

```text
tuning-linear-regression
├── trial-000
├── trial-001
└── linear-regression-final

tuning-random-forest
├── trial-000
├── trial-001
├── ...
├── trial-NNN
└── random-forest-final

tuning-gradient-boosting
├── trial-000
├── trial-001
├── ...
├── trial-NNN
└── gradient-boosting-final
```

Usa estas reglas:

- `tuning-linear-regression`, `tuning-random-forest` y
  `tuning-gradient-boosting` son los tres parent runs;
- cada combinación se llama `trial-NNN`, con tres dígitos;
- cada run terminado en `-final` es hijo de su estudio y contiene el mejor
  pipeline de esa familia reentrenado con todo marzo;
- no crees un experimento distinto por trial;
- no nombres runs como `prueba`, `final`, `ahora-si` o `mejor`;
- usa tags para describir curso, periodo, tarea, familia del modelo y función del run.

Tags mínimos:

| Tag | Valor esperado |
|---|---|
| `course` | `proyecto-ciencia-datos` |
| `term` | `otono-2026` |
| `task` | `05` |
| `model_family` | `linear_regression`, `random_forest` o `gradient_boosting` |
| `role` | `tuning-trial`, `tuning-study` o `family-final` |

## 3. Datos y separación para tuning

Mantén el mismo contrato del curso:

- marzo de 2026 como datos de desarrollo;
- abril de 2026 como validación final;
- `distancia_km`, `pasajeros`, `hora_recoleccion`, `zona_origen` y
  `zona_destino` como features;
- `duracion_minutos` como target;
- RMSE en minutos.

Divide marzo de forma reproducible en:

- entrenamiento interno;
- validación para tuning.

Las búsquedas sólo pueden consultar esas dos particiones durante los trials. No
uses abril dentro de ninguna función objetivo. Después de elegir
hiperparámetros:

1. reconstruye el pipeline;
2. entrénalo con todo marzo;
3. evalúalo una sola vez con abril.

Registra la procedencia de los datasets con contextos distintos:

- `training`;
- `tuning-validation`;
- `final-validation`.

## 4. HPO para las tres familias

Los tres estudios deben usar el mismo tipo de `Pipeline` de las clases
anteriores. Conserva el `ColumnTransformer` y cambia únicamente el estimador
final y los hiperparámetros de la familia correspondiente. Así la comparación
mantiene el mismo contrato de datos y preprocesamiento.

Mantén una sola interfaz para construir pipelines. Puedes ampliar la función
que ya seleccionaba el modelo mediante un `if` para aceptar las tres familias,
o construir los pipelines de forma explícita en el script. No crees una
colección de funciones con nombres diferentes que dupliquen el mismo
preprocesamiento.

### 4.1 `LinearRegression`

Realiza exactamente **2 trials exhaustivos** para `fit_intercept`:

```text
True
False
```

Al existir sólo dos posibilidades, debes probar ambas. No uses TPE para esta
búsqueda: una lista explícita, un ciclo corto o `GridSampler` comunica mejor
que se está recorriendo todo el espacio.

### 4.2 `RandomForestRegressor`

Realiza entre **6 y 8 trials** y explora por lo menos:

- `n_estimators`;
- `max_depth`;
- `min_samples_leaf`.

Conserva `random_state=42` y `n_jobs=-1`. Los rangos deben incluir valores
cercanos a la configuración de la Tarea 3 para que puedas observar si el HPO
mejora el bosque que ya conocías.

### 4.3 `GradientBoostingRegressor`

Realiza entre **6 y 8 trials** y explora por lo menos:

- `n_estimators`;
- `learning_rate`;
- `max_depth`;
- `min_samples_leaf`.

En los estudios de Random Forest y Gradient Boosting fija una semilla para el
sampler. Define rangos razonables y explica en el README por qué no son
arbitrariamente grandes. Si usas `TPESampler`, configura explícitamente
`n_startup_trials=3` y explica que esos primeros intentos generan la evidencia
inicial antes de que TPE aproveche los resultados.

Cada child run debe registrar:

- número del trial;
- hiperparámetros;
- RMSE de tuning;
- tiempo de entrenamiento;
- tags obligatorios.

No registres un modelo completo en cada trial. Los child runs conservan la
comparación mediante parámetros y métricas. Registra el pipeline completo sólo
en `linear-regression-final`, `random-forest-final` y
`gradient-boosting-final`.

Cada parent run debe registrar:

- sampler o estrategia de búsqueda;
- semilla, cuando corresponda;
- número de trials;
- nombre de la métrica objetivo;
- número del mejor trial;
- mejores hiperparámetros;
- mejor RMSE de tuning.

Selecciona el mejor trial de cada familia mediante la API de Optuna, la
comparación exhaustiva de Linear Regression o `mlflow.search_runs()`. No pidas
al usuario que copie un `run_id`.

## 5. Registry y aliases

Usa Unity Catalog. El catálogo del workspace normalmente comparte el nombre
real del workspace; cópialo de Catalog Explorer. El nombre esperado es:

```text
<catalogo-del-workspace>.default.nyc_taxi_trip_duration_tarea_05
```

Si Catalog Explorer muestra otro esquema disponible, cambia esa parte y
documenta el nombre completo en el README. No reemplaces el catálogo por el
identificador de la URL del workspace.

Registra como tres versiones del mismo modelo registrado:

1. el mejor `LinearRegression`;
2. el mejor `RandomForestRegressor`;
3. el mejor `GradientBoostingRegressor`.

Agrega tags con la familia, el RMSE final y el periodo de validación. Carga las
tres versiones y calcula sus predicciones sobre las mismas filas de abril.

Ordena las versiones usando primero el RMSE de abril y, si la diferencia es
pequeña, considera también tiempo, complejidad y reproducibilidad. Asigna:

- `champion` al modelo seleccionado como mejor opción operativa;
- `challenger` al segundo modelo del ranking;
- `candidate` al tercero.

Los aliases representan el resultado de la comparación, no una familia fija.
Linear Regression puede ser `champion` si su desempeño y sencillez justifican
elegirlo. La rúbrica evalúa que el ranking esté respaldado por evidencia; no
exige que gane el modelo más complejo.

## 6. README y análisis

El README debe incluir:

1. objetivo del experimento;
2. Tracking URI y nombre del experimento, sin mostrar host ni credenciales;
3. diagrama textual de parent y child runs;
4. separación entre marzo interno y abril final;
5. tabla con los tres espacios de búsqueda y el número de trials;
6. número y parámetros del mejor trial de cada familia;
7. tabla final:

| Familia | Mejores hiperparámetros | RMSE abril | Tiempo | Versión | Alias final |
|---|---|---:|---:|---:|---|
| Linear Regression | resultado propio | resultado propio | resultado propio | versión | alias |
| Random Forest | resultado propio | resultado propio | resultado propio | versión | alias |
| Gradient Boosting | resultado propio | resultado propio | resultado propio | versión | alias |

8. interpretación de la diferencia en minutos;
9. ranking final y justificación de los tres aliases;
10. dos limitaciones de la búsqueda realizada;
11. instrucciones reproducibles para ejecutar el script.

No copies resultados del notebook de clase ni de otra persona.

## 7. Verificación y evidencia

Ejecuta el script desde la raíz del repositorio individual:

```bash
uv run python tareas/tarea-05-tuning-mlflow-databricks/ajustar_modelos.py
```

Guarda y enlaza desde el README estas tres imágenes:

| Evidencia | Debe mostrar |
|---|---|
| `01-runs-anidados.png` | los tres parent runs y sus child runs `trial-NNN` en el experimento exclusivo |
| `02-comparacion-y-registry.png` | métricas comparables, nombre de tres niveles, tres versiones y aliases finales |
| `03-carga-por-alias.png` | carga de `champion`, `challenger` y `candidate` por alias y predicciones observables |

Recorta o anonimiza correos, nombres, host, IDs personales y cualquier
credencial. El nombre del experimento, los nombres de runs, las métricas y los
aliases sí deben ser visibles.

Antes del commit:

```bash
git status
git diff
```

Confirma que ningún dato, modelo o secreto aparezca en Git.

## Archivos de dependencias

Optuna y `python-dotenv` son dependencias directas de esta tarea. Si todavía no
aparecen en el proyecto `uv` del repositorio individual, agrégalas desde la
raíz:

```bash
uv add "optuna>=4,<5" "python-dotenv>=1,<2"
```

Incluye los cambios de `pyproject.toml` y `uv.lock` en el PR. No incluyas
`.venv/`.

## Commits

Realiza commits sustantivos. Por ejemplo:

```text
feat(tarea-05): registra hpo de tres familias
feat(tarea-05): registra y compara modelos en databricks
docs(tarea-05): justifica ranking y aliases
```

No hagas commits vacíos para alcanzar una cantidad.

## Pull request y cierre obligatorio

El PR debe apuntar a `main`, usar la plantilla, revisarse y fusionarse mediante
**Create a merge commit**. Antes de entregar debe aparecer como **Merged** y
cerrado. Cerrar sin merge no cumple el requisito.

La plantilla estudiantil está en
`docs/plantillas/pull-request-tarea.md` dentro del repositorio público. Copia
todo su contenido en **Write**, complétalo, revisa **Preview** y comprueba
**Files changed** antes del merge.

## Entrega en Canvas

- URL del PR cerrado y fusionado.
- Las tres evidencias permanecen dentro del PR y enlazadas desde el README.

La fecha y hora límite se publican en Canvas.

## Uso de herramientas y colaboración

La tarea es individual. Puedes consultar los notebooks del curso, la
documentación oficial enlazada, mensajes de error y al profesor. No se permite
usar IA generativa, autocompletado generativo ni agentes de programación para
producir, corregir o explicar el código, README o evidencias.

## Rúbrica — 100 puntos

| Criterio | Logro completo | Logro parcial | Insuficiente | Máximo |
|---|---|---|---|---:|
| Experimento remoto y runs anidados | **18–20:** usa el servidor de su cuenta, el nombre obligatorio y tres parent runs con sus child runs correctamente nombrados y etiquetados. | **10–17:** el tracking remoto funciona, pero hay inconsistencias de jerarquía, naming, tags o cantidad de trials. | **0–9:** usa el servidor local, no existe un experimento exclusivo o los trials no son trazables. | 20 |
| HPO de las tres familias y separación de datos | **28–30:** ejecuta 2 trials exhaustivos de Linear Regression, 6–8 de Random Forest y 6–8 de Gradient Boosting con espacios justificados y reproducibles; abril se usa sólo al final. | **16–27:** ajusta las tres familias, pero falta justificación, reproducibilidad o existe una inconsistencia menor de cantidad o separación. | **0–15:** falta el HPO de una familia, usa abril durante el tuning o el mejor trial se elige sin evidencia. | 30 |
| Modelos finales, Registry y aliases | **18–20:** registra tres pipelines completos como versiones del mismo modelo, usa nombre de tres niveles y carga correctamente `champion`, `challenger` y `candidate`. | **10–17:** registra las tres familias, pero falta una operación, tag, alias o carga por alias. | **0–9:** falta una versión, se registra sólo el estimador o los aliases no permiten recuperar los tres modelos. | 20 |
| Comparación, ranking y decisión | **13–15:** presenta resultados propios de las tres familias, interpreta las diferencias y justifica el ranking considerando RMSE, tiempo, complejidad y limitaciones. | **7–12:** hay comparación de las tres familias, pero la interpretación, el ranking o la decisión son parciales. | **0–6:** no hay resultados comparables o los aliases no se apoyan en evidencia. | 15 |
| Evidencia, seguridad y reproducibilidad | **9–10:** incluye las tres imágenes, instrucciones ejecutables y excluye datos, modelos y secretos. | **5–8:** la evidencia permite revisar la mayor parte del recorrido, con una omisión menor. | **0–4:** faltan evidencias esenciales, no puede reproducirse o se expone información sensible. | 10 |
| Git, PR y entrega | **4–5:** usa rama correcta, commits sustantivos, PR completo, merge y entrega oficial. | **2–3:** el trabajo llega a `main`, pero hay una omisión de historial, plantilla o cierre. | **0–1:** trabaja en `main`, el PR no está fusionado o no existe entrega oficial. | 5 |
| **Total** |  |  |  | **100** |

La política de entregas tardías se aplica por separado según la guía de
aprendizaje.
