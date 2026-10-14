# Tarea 7 — Segunda entrega del proyecto

## Propósito

Completar el proyecto hasta la integración local: corregir las entregas
anteriores, entrenar y ajustar modelos, registrar experimentos y versiones
en MLflow remoto, ejecutar un pipeline de entrenamiento y conectar una API
con un frontend.

## Recursos

- [Guía del proyecto](../../project/README.md).
- [Clase 12 — MLflow y Databricks](../../modulo-02-ciclo-mlops/clase-12-mlflow-databricks.ipynb).
- [Clase 13 — Pipelines con Prefect](../../modulo-02-ciclo-mlops/clase-13-pipelines.ipynb).
- [Clase 14 — Model as a Service y Streamlit](../../modulo-02-ciclo-mlops/clase-14-model-service-streamlit.ipynb).
- [Clase 15 — Trabajo en el proyecto](../../modulo-02-ciclo-mlops/clase-15-trabajo-proyecto.ipynb).
- [MLflow: experimentos y runs](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html).
- [Databricks: modelos y aliases en Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle).

## Entregable

**Trabajo:** en equipo, en el repositorio privado del proyecto.

**Rama obligatoria:** `feat/segunda-entrega`.

**Fecha límite:** miércoles **21 de octubre de 2026 a las 19:55**,
hora de la Ciudad de México.

**Entrega oficial:** URL del PR hacia `main`, revisado, fusionado y cerrado.
Cada integrante entrega la misma URL en Canvas.

Continúen el repositorio existente. No creen una copia del proyecto dentro de
una carpeta de tarea. Conserven:

- `informe/informe-final.ipynb`: síntesis actualizada del proyecto;
- `notebooks/03-experimentos.ipynb`: desarrollo e interpretación del modelado;
- `notebooks/04-seleccion-registro.ipynb`: selección y registro del modelo;
- `notebooks/05-pipeline.ipynb`: desarrollo y comprobación del flow;
- `notebooks/06-api.ipynb`: contrato y comprobaciones de la API;
- `notebooks/07-frontend.ipynb`: desarrollo y verificación del frontend;
- `src/entrenamiento/`: código reutilizable y pipeline con Prefect;
- `src/api/`: API FastAPI;
- `src/frontend/`: frontend Streamlit;
- `evidencia/`: capturas enlazadas desde informe o README;
- `README.md`, `pyproject.toml` y `uv.lock`: ejecución reproducible.

Los notebooks de EDA y preparación se conservan y corrigen cuando corresponda.
No se requieren Docker, Compose ni despliegue en nube en esta entrega.

## 1. Correcciones

Apliquen las observaciones anteriores directamente en el informe, notebooks,
mapa, README o código afectado. Verifiquen los resultados. No se solicita
un documento adicional ni una bitácora de correcciones.

## 2. Modelado: tres familias con HPO

Entrenen **al menos tres familias distintas**, apropiadas para la tarea de
regresión o clasificación del proyecto. Por ejemplo: modelo lineal, bosque
aleatorio y gradient boosting. Tres configuraciones del mismo algoritmo no
cuentan como tres familias.

Cada familia debe tener una búsqueda de hiperparámetros con Optuna. Una
búsqueda exhaustiva pequeña también es válida cuando el espacio lo justifica.
No basta con ejecutar una configuración fija y llamarla HPO.

En `03-experimentos.ipynb`, expliquen:

- features, target, preprocesamiento y particiones;
- métrica principal y si se minimiza o maximiza;
- hiperparámetros, rangos o valores y presupuesto de búsqueda de cada familia;
- cantidad de trials realizados, mejores parámetros y resultados;
- comparación de los mejores modelos y justificación del seleccionado.

Usen la misma estrategia de evaluación para las familias. La validación usada
para HPO debe separarse de la evaluación final; esta última no interviene en
las funciones objetivo. Fijen semillas donde corresponda y eviten ajustar el
preprocesamiento con los datos de evaluación.

## 3. Una persona ejecuta en Databricks

Elijan **una persona responsable de ejecutar los experimentos remotos y
registrar los modelos**, desde su propia computadora y cuenta personal de
Databricks. Las demás personas colaboran en código, análisis, API, interfaz,
documentación y revisión. Toda la evidencia remota del equipo proviene del
mismo workspace; no es necesario repetirla por integrante.

Las credenciales se guardan localmente en `.env`, ignorado por Git.
No compartan tokens, contraseñas ni archivos `.env`.
La configuración de referencia es la de Clase 12:

- Tracking URI: `databricks`;
- Registry URI: `databricks-uc`.

La persona responsable puede ejecutar también la demostración completa
API–frontend con su configuración. El resto puede verificar localmente un
artefacto confiable obtenido por el equipo, conservando su procedencia y
versión fuera de Git, sin compartir credenciales.

## 4. Nombres de experimentos, runs y modelos

Elijan un identificador breve y descriptivo del proyecto. Utilicen minúsculas,
caracteres ASCII y ningún nombre personal, correo, matrícula o usuario.

### Experimento: ruta absoluta de Workspace

```text
/Shared/pcd-otono-2026-proyecto-<proyecto-en-kebab-case>
```

Es la ruta del experimento remoto de MLflow, no una carpeta del repositorio ni
el catálogo del modelo. Sustituyan el marcador por el proyecto con palabras
separadas por guiones. Ejemplo:

```text
/Shared/pcd-otono-2026-proyecto-abandono-clientes
```

Usen este experimento para todas las familias y ejecuciones del proyecto.
No reutilicen los experimentos de clase o de las tareas individuales.
Documenten la ruta exacta en el README y muéstrenla en las capturas.

### Runs dentro del experimento

Cada familia tiene un parent run `hpo-<familia>`, child runs `trial-NNN`
con tres dígitos y un run `<familia>-final` para su mejor modelo reentrenado:

```text
hpo-random-forest
├── trial-000
├── trial-001
├── ...
└── random-forest-final
```

Usen nombres análogos, por ejemplo `hpo-logistic-regression` y
`hpo-gradient-boosting`, según los algoritmos realmente utilizados.
Cada trial registra hiperparámetros y métrica de tuning.
Cada run final registra parámetros seleccionados, métrica de evaluación y
el artefacto completo. No es necesario guardar el modelo de cada trial.

### Modelo registrado: nombre de tres niveles en Unity Catalog

```text
workspace.default.pcd_otono_2026_<proyecto_en_snake_case>
```

Aquí las palabras del proyecto se separan con guiones bajos. Para el mismo
ejemplo:

```text
workspace.default.pcd_otono_2026_abandono_clientes
```

El catálogo es **`workspace`** y el esquema es **`default`**. Utilicen esos
valores y sustituyan únicamente el identificador del proyecto. No utilicen
el identificador de la URL como nombre del catálogo.

El nombre usa **puntos**, no barras, entre catálogo, esquema y modelo.
Sustituyan los marcadores: no deben quedar escritos literalmente.

Registren el mejor pipeline de cada familia como una versión del **mismo
modelo registrado**: al menos tres versiones en esta entrega. Incluyan
preprocesamiento, firma de entrada/salida y ejemplo de entrada, como en clase.
Identifiquen la familia y relacionen cada versión con su run y métricas.

Asignen el alias `champion` a la versión seleccionada. No fijen de antemano
qué familia debe ganar. La API debe utilizar ese modelo y poder identificar
la versión concreta que cargó.

## 5. Pipeline de entrenamiento con Prefect

El flow coordina carga y validación de datos, preparación, HPO de las familias,
entrenamiento de sus mejores modelos, evaluación y registro en MLflow remoto
y Unity Catalog.

El código reutilizable vive en `src/entrenamiento/`. El README indica el
comando exacto para ejecutar el flow. Las tasks deben tener responsabilidades
identificables y una ejecución exitosa debe poder revisarse en Prefect.

Mantengan el mismo preprocesamiento en entrenamiento e inferencia.
No se requieren deployments, schedules, workers ni Prefect Cloud.

## 6. API y frontend conectados

La API FastAPI de `src/api/` carga el pipeline seleccionado, valida la
entrada y devuelve una predicción con significado claro y la versión del
modelo. Documenten un ejemplo válido e inválido y sus respuestas.
El entrenamiento no se repite al atender cada solicitud.

Streamlit en `src/frontend/` presenta un formulario, llama a la API por HTTP
y muestra la predicción y su interpretación. Debe manejar fallas de conexión
o validación con un mensaje comprensible.

El README indica los comandos de arranque de ambos procesos y su configuración.
La URL de la API y la referencia del modelo son configurables; no incluyan
credenciales ni rutas personales en el código.

## 7. Informe y README

Desarrollen cada componente técnico de esta tarea en su propio notebook:
`03-experimentos.ipynb`, `04-seleccion-registro.ipynb`, `05-pipeline.ipynb`,
`06-api.ipynb` y `07-frontend.ipynb`, todos dentro de `notebooks/`.
Cada cuaderno explica propósito, decisiones, procedimiento, código o llamadas
a `src/`, resultados, comprobaciones e interpretación detallada del componente.
Para API y frontend, documenten el arranque y las pruebas de los procesos
externos; no es necesario iniciarlos automáticamente al ejecutar el notebook.

Actualicen el informe existente con el consolidado de modelado, HPO,
comparación, selección, tracking/Registry, pipeline, API y frontend.
En cada subsección incluyan los **highlights**: hallazgos principales,
decisiones justificadas, resultados clave y limitaciones, más la referencia
al notebook técnico correspondiente. No repitan todo el código ni cada
resultado intermedio.

La guía describe el proyecto completo y puede incluir temas todavía no vistos.
**El alcance obligatorio de esta entrega es el de esta tarea.** Utilicen la
guía para desarrollar los puntos aplicables; no creen notebooks de contenedores,
despliegue u operación para esta entrega.

**Distribución obligatoria del contenido:**

| Ubicación | Contenido esperado |
|---|---|
| `notebooks/` | Un notebook propio por componente, con desarrollo técnico detallado: procedimientos, código de análisis o llamadas a módulos, preparación, parámetros, resultados, gráficas, comprobaciones e interpretación. |
| `informe/informe-final.ipynb` | Consolidado del proyecto: contexto, problema, objetivos, decisiones justificadas, hallazgos principales, resultados relevantes interpretados, limitaciones y conclusiones. Incluye referencias al detalle técnico correspondiente. |
| `src/` | Implementación reutilizable del entrenamiento, pipeline, API e interfaz. Los notebooks pueden importar o llamar estos módulos; no necesitan duplicar su implementación. |
| `README.md` | Instrucciones para configurar, ejecutar y verificar el proyecto. |

El informe debe poder leerse de principio a fin y permitir comprender el
proyecto sin abrir todos los notebooks. **No se solicita copiar al informe
todo el código, todas las gráficas ni cada resultado intermedio** de los
notebooks. Sí deben incluir las tablas, gráficas o capturas clave que sean
necesarias para explicar sus hallazgos y respaldar las decisiones.

En cada subsección del desarrollo, presenten la síntesis y su interpretación
y enlacen el notebook o archivo que contiene el detalle completo. Un informe
formado sólo por enlaces o capturas sin explicación no cumple esta función.

**Ejemplo:** `notebooks/03-experimentos.ipynb` contiene el detalle del
preprocesamiento, particiones, HPO de las tres familias, parámetros, métricas
y análisis de los experimentos. El informe presenta la comparación principal,
explica qué modelo se seleccionó y por qué, interpreta sus resultados y
limitaciones y referencia ese notebook. No necesita repetir todos los trials
ni el código del entrenamiento.

El README debe permitir obtener los datos, preparar el ambiente con
`uv sync --locked`, configurar variables sin secretos, ejecutar el flow,
arrancar API y frontend y repetir la comprobación. Incluyan la ruta exacta
del experimento, el nombre completo del modelo y la versión seleccionada.

Identifiquen en la descripción del PR quién realizó la ejecución remota y
las contribuciones de las demás personas del equipo.

## 8. Verificación y capturas obligatorias

Guarden en `evidencia/` imágenes legibles por cada caso de esta tabla.
Enlácenlas desde el informe o README con una explicación breve del resultado.
Pueden usar varias imágenes para un caso si no cabe con claridad.

| Caso | Qué debe verse en las capturas |
|---|---|
| Experimento remoto | Ruta completa y al menos tres familias con sus runs de HPO. |
| HPO de cada familia | Una captura o conjunto por familia con trials, hiperparámetros, métrica y mejor resultado; las tres búsquedas deben ser verificables. |
| Comparación final | Tabla o vista con familia, mejores parámetros y métrica de evaluación bajo condiciones comparables. |
| Model Registry | Nombre completo, al menos tres versiones, familia/run de procedencia y versión con alias `champion`. |
| Prefect | Flow exitoso y tasks identificables del recorrido completo. |
| API: entrada válida | Cliente, solicitud, respuesta con predicción y versión; usen Postman, `/docs` o `curl`. |
| API: entrada inválida | Solicitud y respuesta de validación, sin devolver una predicción inventada. |
| Frontend integrado | Formulario con los valores utilizados y predicción obtenida a través de la API; incluyan la solicitud/respuesta correspondiente de la API o su log para relacionar ambos. |

En las capturas remotas, recorten u oculten correo, avatar, URL del workspace
e identificadores personales, conservando la ruta del experimento, runs,
métricas y nombre del modelo. Nunca muestren tokens ni el contenido de `.env`.

El código o una captura de la terminal que diga “terminado” no sustituyen las
vistas de MLflow, Registry y Prefect solicitadas. El profesor debe poder
reconstruir qué se ejecutó y cómo se conecta con el resultado de la aplicación.

## Commits

Realicen commits sustantivos según Conventional Commits. Por ejemplo:

```text
fix(proyecto): corrige preparacion de datos
feat(proyecto): integra hpo y tracking remoto
feat(proyecto): conecta api y frontend
docs(proyecto): interpreta resultados y enlaza evidencia
```

No hay un mínimo artificial de commits. Revisen los archivos antes de agregarlos
y mantengan datos, modelos, secretos y `.venv/` fuera de Git.

## Pull request y cierre obligatorio

Desde `main` actualizado y sin cambios pendientes que deban conservar en otra
rama, creen `feat/segunda-entrega`. Si hay un PR abierto, coordinen su cierre
antes de empezar otra entrega.

El PR apunta a `main`. Copien todo el contenido de la
[plantilla del curso](../plantillas/pull-request-tarea.md) en **Write**,
completen las secciones y comprueben **Preview**.
Soliciten revisión a las demás personas del equipo, revisen **Files changed**
y atiendan observaciones. Fusionen mediante **Create a merge commit**.

Antes de entregar, el PR debe aparecer **Merged** y cerrado. Cerrar sin merge
no completa la tarea.

## Entrega en Canvas

Cada integrante entrega la URL del mismo PR revisado, fusionado y cerrado.
Correo, Teams y mensajes privados no sustituyen la entrega oficial.

## Uso de herramientas y colaboración

La tarea es en equipo. Pueden consultar material del curso, documentación y
herramientas de IA como apoyo. Deben verificar toda sugerencia, citar fuentes
utilizadas y poder explicar el código y los resultados.
Las restricciones de las tareas individuales anteriores siguen aplicándose
a esas tareas; esta política no las modifica retrospectivamente.

## Rúbrica — 100 puntos

| Criterio | Logro completo | Logro parcial | Insuficiente | Máximo |
|---|---|---|---|---:|
| Correcciones, datos y preparación | **9–10:** aplica observaciones previas y mantiene target, features, preprocesamiento y particiones coherentes. | **5–8:** hay correcciones o decisiones de datos pendientes sin invalidar todo el recorrido. | **0–4:** persisten errores que impiden evaluar o reproducir la solución. | 10 |
| Tres familias con HPO y comparación | **23–25:** al menos tres familias tienen búsquedas verificables, espacios y presupuesto explicados y una comparación que sustenta la selección sin fuga de evaluación final. | **13–22:** presenta parte del recorrido, con una búsqueda, comparación o justificación incompleta. | **0–12:** faltan familias, predomina configuración fija o la evaluación no sostiene la selección. | 25 |
| Pipeline con Prefect | **13–15:** flow reproducible con etapas identificables que completa preparación, HPO, entrenamiento, evaluación y registro. | **7–12:** funciona con omisiones o pasos manuales no resueltos. | **0–6:** no coordina el recorrido o no ejecuta. | 15 |
| MLflow remoto y Model Registry | **13–15:** un workspace concentra runs claros, parámetros/métricas, tres versiones trazables y `champion`, con nombres y ruta solicitados. | **7–12:** evidencia remota parcial o inconsistencias de naming, versiones o procedencia. | **0–6:** sólo hay tracking local, no hay registro verificable o el modelo servido no corresponde al seleccionado. | 15 |
| API y frontend | **18–20:** API carga la versión seleccionada, valida entradas y el frontend obtiene e interpreta su predicción por HTTP. | **10–17:** una parte funciona, con integración, validación o identificación de versión incompleta. | **0–9:** no hay predicción real o API y frontend no se comunican. | 20 |
| Informe, README y capturas | **9–10:** los notebooks contienen el detalle técnico; el informe consolida e interpreta hallazgos, se entiende por sí solo y referencia ese detalle; README y capturas permiten reproducir y comprobar todos los casos. | **5–8:** síntesis, detalle técnico, instrucciones o imágenes parciales dificultan una comprobación. | **0–4:** faltan evidencias o instrucciones, o el informe no permite comprender el proyecto y sus resultados. | 10 |
| Colaboración, Git, PR y entrega | **5:** contribuciones y ejecución remota identificadas, rama correcta, revisión, merge y URL oficial. | **3–4:** trabajo integrado con una omisión de historial, revisión o entrega. | **0–2:** no hay colaboración verificable, PR fusionado o entrega oficial. | 5 |
| **Total** | | | | **100** |

La política de entregas tardías se aplica por separado según la
[guía de aprendizaje](../guia-de-aprendizaje/README.md).
