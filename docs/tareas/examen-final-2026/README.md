```text
 ___ _____ _____ ____   ___
|_ _|_   _| ____/ ___| / _ \
 | |  | | |  _| \___ \| | | |
 | |  | | | |___ ___) | |_| |
|___| |_| |_____|____/ \___/
```

# 🎓 Examen final — Del mensaje al modelo

**Nimbo Labs · Proyecto Nimbo SMS · Clasificación de mensajes**

**📅 Fechas clave**

- **Asignación:** 4 de noviembre de 2026.
- **Entrega:** 11 de noviembre de 2026, **19:55**, hora de Ciudad de México, por Canvas.
- **Sustentación:** 11 de noviembre, **T-105**, **8 minutos por estudiante**, incluyendo preguntas. Los turnos se comunicarán por Canvas durante la semana del 9 de noviembre. La puntualidad es obligatoria; consulta la sección 16.

## 1. 🧩 Problema y caso de uso

**Nimbo Labs** es una empresa ficticia que convierte prototipos de ciencia de datos en aplicaciones utilizables. Te incorporas a su equipo para desarrollar **Nimbo SMS**, un prototipo de clasificación de mensajes.

El caso de uso es el siguiente: una persona pega un SMS en inglés en una interfaz, ésta consulta una API y muestra la clasificación **`ham` (legítimo) o `spam` (no solicitado)** y la versión del modelo. El sistema no bloquea ni elimina mensajes automáticamente.

Debes demostrar cómo preparaste los datos, seleccionaste el modelo y conservaste el mismo procesamiento durante entrenamiento e inferencia. Interpreta las consecuencias de falsos positivos —mensajes legítimos marcados como spam— y falsos negativos —spam no detectado—. El corpus es histórico y está en inglés: no demuestra eficacia con mensajes actuales, otros idiomas o todo tipo de fraude.

## 2. 🎯 Objetivo y libertad de decisiones

Desarrolla **individualmente** el recorrido datos → análisis → modelos → tracking y registro → flujo de entrenamiento → API → interfaz → contenedores. Entrega informe, código, evidencias y decisiones justificadas, y sustenta tu solución.

> **Libertad técnica:** puedes utilizar cualquier herramienta, biblioteca, modelo o framework. Las tecnologías mencionadas son referencias del curso. Si eliges alternativas, explica su función, por qué las elegiste, qué alternativas consideraste y cómo verificaste resultados equivalentes. No necesitas autorización adicional para esas elecciones.

Documenta decisiones relevantes, supuestos y validaciones en `reports/decisiones-e-ia.md`, enlazándolas desde el informe. Se mantienen comunes el problema, dataset, resultados mínimos, contrato HTTP, evidencias y entrega. Se evalúan funcionamiento, reproducibilidad y comprensión; no hay una meta mínima de accuracy ni puntos extra por complejidad o servicios de pago. Los temas complementarios posteriores a AWS no son requisitos.

### 2.1 🧭 Qué debes desarrollar en el informe

**El notebook inicial contiene únicamente el planteamiento del problema.** Conserva ese planteamiento y agrega después tus propias secciones y celdas para desarrollar el informe con el contenido de esta tabla. En cada apartado explica **qué hiciste, por qué, qué resultado obtuviste y cómo lo comprobaste**, enlazando código y evidencias.

| Contenido del informe | Qué debes implementar o resolver | Qué debes presentar en el informe |
|---|---|---|
| **Problema y diseño** | Define cómo la solución responde al caso de mensajería y conecta sus componentes. | Objetivo general y objetivos específicos de tu solución, usuario, entrada/salida, alcance y herramientas justificadas. |
| **Datos, particiones y EDA** | Adquisición, depuración y separación reproducibles; análisis de entrenamiento. | Fuente, calidad, conteos, ausencia de fuga, gráficas y decisiones derivadas del EDA. |
| **Representación** | Transformación de texto que pueda reutilizarse durante inferencia. | Elección, configuración y prevención de fuga durante la selección. |
| **Modelos y selección** | Baseline, dos familias, tuning, selección y evaluación final. | Comparación de métricas, champion justificado, matriz y análisis de errores. |
| **Tracking y registro** | Experimentos trazables y versiones recuperables. | Relación datos/configuración/métricas/modelo; versiones y capturas de la herramienta elegida. |
| **Entrenamiento coordinado** | Flujo completo ejecutable desde terminal, independiente de Jupyter. | Etapas, comando, resultados guardados, manejo de fallas y evidencia de ejecución. |
| **API** | Carga del modelo seleccionado y contrato HTTP. | Versión servida, paridad y evidencias de solicitudes válidas e inválidas. |
| **Interfaz y contenedores** | Interfaz conectada por HTTP y componentes empacados por separado. | Recorrido del usuario, configuración/red, construcción, funcionamiento y cierre evidenciados. |
| **AWS** | Explicación aplicada del despliegue; ejecución remota opcional. | Decisiones de infraestructura, acceso, verificación, costos y cierre; capturas si desplegaste. |
| **Decisiones e IA** | Bitácora de decisiones y validaciones propias. | Síntesis y enlace a `decisiones-e-ia.md`; prompts, propuestas y comprobaciones cuando uses IA. |
| **Conclusiones y referencias** | Integra los hallazgos y comprueba el entregable. | Respuesta al problema, límites, mejoras propuestas, fuentes e índice de evidencias. |

El informe conecta tu implementación con sus resultados e interpretación. Usa las secciones 5–12 de este README para los requisitos técnicos, la **13 para cada evidencia requerida**, la 14 para IA y la 17 para puntajes. Conserva el código ejecutable en archivos según la sección 3.3; enlázalo desde el informe.

## 3. 🛠️ Repositorio y organización

### 3.1 🌱 Crear, clonar e incorporar los archivos

1. Crea en tu cuenta de GitHub el repositorio privado **`examen-final-pcd-2026`**, inicializado con README y rama `main`. Invita como colaborador a **`zapatacc`**; verifica la aceptación antes de entregar.
2. Copia su URL HTTPS desde **Code**. Desde una carpeta para tus proyectos, en Git Bash (Windows), Zsh (macOS) o Bash (Linux), ejecuta `git clone` seguido de esa URL, sin credenciales en el comando. Entra en el clon:

```bash
cd examen-final-pcd-2026
git status
git switch main
git pull
```

3. Copia localmente los tres archivos del examen —`README.md`, `examen-final.ipynb`, `apoyo-texto.ipynb`— a la raíz del clon, reemplazando el README inicial. Conserva sus nombres y extensiones.
4. Revisa, selecciona y publica esa base inicial; después crea tu rama de desarrollo:

```bash
git status
git diff
git add README.md examen-final.ipynb apoyo-texto.ipynb
git diff --staged
git commit -m "chore(examen): agrega archivos iniciales"
git push origin main
git switch -c feat/examen-final
git status
```

La incorporación inicial queda en `main`; **toda la solución se desarrolla en `feat/examen-final`**. Comprueba que los tres archivos estén en tu repositorio privado y que esa rama esté activa. No trabajes sobre el repositorio público del curso ni el del proyecto en equipo.

### 3.2 ⚙️ Ambiente y configuración

El nombre sugerido del proyecto es **Nimbo SMS** y su identificador técnico, **`nimbo-sms`**. El repositorio de entrega conserva el nombre `examen-final-pcd-2026`: son identificadores con funciones distintas. Puedes elegir otro nombre de proyecto y explicarlo en el informe.

Usa **Python 3.12** para código Python. Con `uv`, inicializa con `uv init --name nimbo-sms --python 3.12` (`--name` establece el nombre en `pyproject.toml`), declara dependencias con `uv add` y versiona `pyproject.toml`, `uv.lock` y `.python-version`. Comprueba con `uv sync --locked`. Otro gestor debe ofrecer versiones fijadas y reconstrucción documentada.

No instales paquetes desde el notebook. Ignora ambientes, datos, artifacts locales, cachés y `.env` mediante `.gitignore`. Entrega `.env.example` con valores ficticios. Excluye secretos, `.git/`, ambientes y datos del contexto de Docker mediante `.dockerignore` o el mecanismo equivalente elegido. Si exportas requisitos para las imágenes, genéralos desde el lock; no mantengas versiones contradictorias a mano.

### 3.3 📓 Notebook y archivos de código

| Parte | Responsabilidad |
|---|---|
| `examen-final.ipynb` | EDA, gráficas, experimentos iniciales, decisiones e interpretación de resultados. |
| Archivos de código (`.py` para Python) | Preparación reutilizable, modelado y flujo completo ejecutable desde terminal, sin abrir Jupyter. |
| API e interfaz | Arrancan independientemente del notebook; la API carga el modelo y la interfaz la consulta por HTTP. |

Puedes explorar en el notebook y trasladar la lógica reutilizable a archivos que éste importe. **Los programas no deben necesitar variables, funciones o modelos que sólo existan en memoria de Jupyter.** El flujo guarda métricas y modelos; el informe final lee esos resultados, produce análisis y ejecuta con kernel nuevo sin repetir tuning ni registro para mostrarlos.

### 3.4 🗂️ Estructura sugerida y entregables

**Este árbol es sólo una sugerencia**, usando `uv` y Docker como referencia. Puedes adaptar carpetas y módulos si justificas su organización y documentas cómo ejecutar cada componente. Conserva los tres archivos iniciales y las rutas de `reports/` solicitadas para localizar los entregables.

```text
examen-final-pcd-2026/
├── README.md
├── examen-final.ipynb
├── apoyo-texto.ipynb
├── pyproject.toml
├── uv.lock
├── .python-version
├── .gitignore
├── .env.example
├── .dockerignore
├── compose.yaml
├── src/
│   ├── datos.py
│   ├── entrenamiento.py
│   └── train_flow.py
├── api/
│   ├── main.py
│   └── Dockerfile
├── ui/
│   ├── app.py
│   └── Dockerfile
├── reports/
│   ├── decisiones-e-ia.md
│   ├── despliegue-aws.md
│   ├── metricas.csv
│   └── evidencias/
├── data/                  # local; ignorada por Git
└── artifacts/             # local; ignorada por Git
```

La propuesta agrupa en `src/` la preparación, modelado y coordinación reutilizables; separa API/UI porque son servicios que se ejecutan y empacan independientemente; reúne análisis y evidencias en `reports/`; y mantiene datos/modelos locales fuera de Git. Las dependencias comunes se declaran una sola vez en la raíz. Los archivos de implementación los desarrollarás tú.

**Sustenta tu organización:** explica la responsabilidad de cada componente, sus entradas/salidas, por qué elegiste esa separación y cómo la verificaste. Si usas otra estructura o herramientas, documenta sus equivalencias en `reports/decisiones-e-ia.md`.

Conserva el enunciado y agrega al final del README **Ejecución de mi solución**, con requisitos, configuración, comandos, entradas, resultados esperados y cierre.

## 4. 📚 Recursos de apoyo

Consulta las clases y [apoyo-texto.ipynb](apoyo-texto.ipynb), con ejemplos pequeños de TF-IDF, clasificadores y métricas. Puedes adaptar sus patrones; no constituye una solución del examen. Aquí **`spam` es la clase positiva**, independientemente del sentimiento del mensaje.

**🚀 Extra opcional:** puedes explorar modelos de embeddings, que representan textos mediante vectores. No son obligatorios ni añaden puntos por sí mismos. Si los usas, justifica la elección y conserva la representación en inferencia. Referencia: [Sentence Transformers](https://www.sbert.net/docs/quickstart.html).

## 5. 📥 Dataset y adquisición

Usa [SMS Spam Collection de UCI](https://archive.ics.uci.edu/dataset/228/sms%2Bspam%2Bcollection), Almeida e Hidalgo (2011), licencia **CC BY 4.0**, DOI [10.24432/C5CC84](https://doi.org/10.24432/C5CC84).

El [ZIP oficial](https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip) contiene `SMSSpamCollection`, sin encabezado: cada línea tiene etiqueta, tabulador y mensaje. Separa sólo el primer tabulador. El archivo revisado contiene 5,574 registros; documenta URL, fecha y conteo obtenido. Implementa descarga/carga reproducible y reutiliza la copia local. Si falla la fuente, consulta al profesor por Canvas para obtener una copia autorizada; no sustituyas el dataset.

La entrada es texto libre; la etiqueta es únicamente el objetivo. **No publiques el corpus ni mensajes originales**, tampoco como ejemplos/artifacts en tracking. Parafrasea errores sin datos sensibles y usa textos inventados para API/UI. Conserva atribución y licencia.

## 6. 🔎 Calidad, particiones y EDA

- Valida etiquetas, vacíos, duplicados y contradicciones. Justifica su tratamiento. Como referencia, compara `texto.strip().lower()`, excluye claves contradictorias y conserva la primera aparición de duplicados.
- Separa entrenamiento, validación y prueba reproduciblemente. Justifica proporciones, semilla y balance; informa tamaños y demuestra **cero mensajes equivalentes compartidos**. Referencia: 60/20/20 estratificado, semilla 42; puedes justificar otra estrategia.
- Usa entrenamiento para EDA y ajuste; validación para selección; prueba sólo para evaluación final. Si usas validación cruzada, preserva una prueba independiente y evita fuga en cada partición. La depuración previa no debe aprender vocabulario ni seleccionar modelos.
- Presenta distribución de clases y longitud, diagnóstico de calidad y **dos observaciones interpretadas**. Explica el desbalance, cómo lo atenderás y por qué accuracy puede resultar engañosa.

## 7. 🧠 Representación, entrenamiento y selección

1. Elige y justifica una representación numérica del texto. TF-IDF con Pipeline es una referencia; también puedes explorar **modelos de embeddings como otra opción, completamente voluntaria**. No necesitas implementar ni comparar ambas representaciones; usar embeddings no añade puntos por sí mismo. Ajusta transformaciones aprendidas **sólo con entrenamiento durante selección**; registra juntos o vincula inequívocamente procesamiento y modelo. Para recursos preentrenados identifica procedencia, versión y licencia.
2. Evalúa un **baseline sencillo** y al menos **dos familias distintas**. El baseline no cuenta como familia; variar hiperparámetros tampoco crea otra. Regresión logística y Multinomial Naive Bayes son opciones.
3. Realiza tuning con **al menos cuatro configuraciones por familia**. Justifica herramienta, parámetros, rangos y presupuesto; Optuna es una referencia.
4. Define **antes del tuning** métrica principal y desempate según el caso de uso. Compara con las mismas particiones; informa accuracy y precision, recall y F1 de `spam`.
5. Elige un finalista por familia y el **champion con validación**. Cerrada la selección, reajusta con entrenamiento/validación si corresponde y evalúa baseline/finalistas sobre prueba. No vuelvas al tuning ni cambies champion por resultados de prueba.
6. Guarda en `reports/metricas.csv` conjunto, familia, configuración, métricas y experimento de origen, distinguiendo validación y prueba. Presenta matriz de confusión del champion en prueba con filas reales/columnas predichas, orden `ham`, `spam`. Analiza hasta tres falsos positivos y tres falsos negativos; si hay menos, indica el conteo y analiza los disponibles.

## 8. 🧪 Tracking y registro de versiones

MLflow + Databricks es el camino de referencia; se permiten equivalentes locales o remotos persistentes. Debes conservar parámetros, semilla, fuente y versión o fecha de datos, particiones, métricas y duración de experimentos; y **dos versiones registradas**, ligadas a sus experimentos, con procesamiento, esquema de entrada/salida y ejemplo inventado.

Identifica champion/challenger mediante aliases o mecanismo equivalente. La API resuelve champion al iniciar y conserva esa versión durante la ejecución; un cambio de selección se adopta al reiniciar.

Nombres de referencia en Databricks:

```text
Experimento: /Shared/pcd-2026-examen-sms-<usuario-github>
Modelo: workspace.default.pcd_2026_examen_sms_<usuario_github>
Aliases: champion / challenger
```

Sustituye los marcadores; en el modelo cambia guiones por guiones bajos. Con otra herramienta documenta nombres, ubicaciones y equivalencias. Conserva evidencia/exportaciones revisables sin compartir credenciales personales.

## 9. 🔄 Flujo de entrenamiento

Implementa un programa que coordine adquisición/validación → preparación/particiones → búsqueda/selección → ajuste/evaluación final → registro. **Prefect es una referencia**, pero puedes justificar otro mecanismo. Explica etapas, dependencias, reutilización de datos y comportamiento ante fallas.

Debe ejecutar desde terminal sin Jupyter, guardar métricas/referencias de modelos y no ejecutar el notebook. Para la estructura sugerida:

```bash
uv run python src/train_flow.py
```

Documenta tu comando exacto si cambia. Demuestra ejecución completa y estado de las etapas; con Prefect, muestra flow/tasks en su interfaz local o terminal. No necesitas servicios de pago.

## 10. 🔌 API e interfaz

FastAPI/Pydantic y Streamlit son referencias. Cualquier alternativa debe cumplir:

| Operación | Contrato |
|---|---|
| `GET /health` | HTTP 200 sólo con modelo listo; informa estado, nombre y versión concreta. |
| `POST /predict` | JSON con único campo obligatorio `text`: cadena de 1–2,000 caracteres, no sólo espacios; rechaza campos adicionales. |
| Respuesta válida | HTTP 200 con `label` (`ham`/`spam`), `model_name` y `model_version`, todos cadenas. |
| Entrada inválida | HTTP 422; no devuelvas 200 con un mensaje de error. |

Ejemplo de solicitud válida: `{"text": "Can we meet after class?"}`.

La API recibe texto crudo y aplica el procesamiento/modelo registrado, sin reentrenar ni reglas que fuercen ejemplos. Comprueba igualdad entre modelo y API con **tres textos inventados**. Probabilidades son opcionales.

La interfaz tiene campo de texto, botón y resultado/versión. Consulta la API por HTTP, sin cargar el modelo directamente. Maneja texto inválido o API no disponible; indica que trabaja con inglés y produce una estimación.

## 11. 📦 Contenedores

Empaca API/UI por separado con dependencias fijadas y configuración externa. En Docker usa `api/Dockerfile` y `ui/Dockerfile`; explica contextos de construcción, incluyendo archivos de raíz si deben copiarse.

En Compose, servicios `api`/`ui`; host networking es una referencia, pero puedes justificar otra topología. Documenta direcciones, puertos, conectividad y disponibilidad. Nombres sugeridos: imágenes `sms-api-image:v1`/`sms-ui-image:v1`, contenedores `sms-api-container`/`sms-ui-container`.

Incluye comandos para construir, arrancar, comprobar y cerrar. Referencia: `docker compose up --build`, `docker compose ps`, `docker compose down`. Demuestra predicción desde UI con ambos componentes en contenedores. No incluyas secretos en imágenes ni detengas recursos ajenos; la UI no requiere credenciales del modelo.

## 12. ☁️ Explicación de AWS

En `reports/despliegue-aws.md` explica cómo trasladarías tu solución a EC2 en **`us-east-1`**: sistema/capacidad/disco, SSH, clon privado, Docker/Compose, configuración externa, localhost frente a dirección remota, comunicación API/UI y reglas de acceso. Incluye verificación remota, logs, costos y cierre; distingue detener de terminar y recursos que siguen generando costo.

> **Instancia existente:** para AWS en el examen, reutiliza la EC2 que ya tienes del laboratorio. Si cambió la IP pública de tu computadora, actualiza el origen de la regla SSH (TCP 22) del grupo de seguridad a **My IP**, sin abrir SSH a todo Internet. Comprueba también la dirección pública actual de EC2 antes de conectar.

> **Alcance de AWS:** la explicación es obligatoria; desplegar es opcional y no añade puntos. Si despliegas, adjunta las capturas de la sección 13 y comprueba el cierre. No publiques IP, llaves, datos de cuenta o credenciales ni mantengas EC2 encendida para sustentar.

## 13. ✅ Evidencias obligatorias

Guarda **una captura o imagen por cada caso aplicable** en `reports/evidencias/`, enlázala desde el informe y añade un índice **caso → archivo → resultado observado**. Deben mostrar herramienta/comando, entrada/acción y resultado, sin información sensible. En HTTP incluye solicitud, respuesta y código. Las alternativas de herramientas requieren evidencia equivalente.

| Componente | Casos que debes evidenciar |
|---|---|
| Git y ambiente | PR **Merged** e historial; reconstrucción exitosa del ambiente. |
| Datos/EDA | Conteos de depuración, particiones sin mensajes compartidos; gráficas de clases y longitud interpretadas. |
| Evaluación | Comparación baseline/finalistas y matriz de confusión en prueba. |
| MLflow/Databricks o equivalente | Comparación de experimentos; detalle de un trial con parámetros/métricas; registro de dos versiones con champion/challenger y origen. |
| Prefect o equivalente | Flujo completo desde terminal sin Jupyter, etapas/tasks y estado final, resultados guardados. |
| API válida | Salud 200; predicción 200; paridad modelo/API con tres textos. |
| API inválida: una imagen por caso | Falta `text` (`{}`); tipo incorrecto (`{"text":7}`); sólo espacios; 2,001 caracteres; campo adicional (`{"text":"Hello", "label":"ham"}`). **Todos HTTP 422.** |
| Interfaz | Predicción con etiqueta/versión; mensaje ante API detenida. |
| Contenedores | Build de ambas imágenes; servicios activos y predicción; cierre comprobado. |
| AWS, sólo si despliegas | Instancia/acceso; contenedores y predicción remota; estado final de los recursos. |

No presentes fallas como éxitos: registra qué no quedó resuelto. Las imágenes complementan código y métricas reproducibles. No se requieren pytest, CI/CD, monitoreo o rollback automatizado.

## 14. 🤖 Decisiones, IA y colaboración — 10 puntos

Puedes consultar materiales, documentación, buscadores e IA —incluidos agentes/autocompletado—. La solución y su validación son individuales; no reutilices entregas de otros estudiantes. Atribuye código del curso o externo. No envíes secretos ni mensajes originales del corpus a la IA.

En `reports/decisiones-e-ia.md` justifica las decisiones técnicas y documenta cada uso importante de IA con este registro breve:

```text
Herramienta y para qué la usé:
Prompt que utilicé:
Qué propuso y qué acepté, modifiqué o rechacé, con mi razón:
Cómo lo comprobé, resultado y enlace a evidencia o archivo:
```

Conserva el prompt original; resume sólo la respuesta relevante. Declara límites o comprobaciones pendientes. Otra respuesta de IA no basta como validación. No inventes errores, rechazos o conversaciones ni acumules prompts para obtener puntos.

Si no usas IA, decláralo y documenta dos decisiones propias con alternativas y validación; puedes obtener el máximo. Si la usas poco, completa con decisiones propias. Debes explicar también el código generado que incorpores.

## 15. 📤 Informe, commits y entrega

### 15.1 📓 Informe

Completa `examen-final.ipynb` siguiendo la guía de la sección 2.1. Comprueba que cada apartado incluya decisiones, resultados interpretados y enlaces a su implementación/evidencia, y ejecuta con kernel nuevo según la sección 3.3.

En **Ejecución de mi solución**, documenta en orden ambiente/configuración → adquisición/entrenamiento → informe → API/UI/contenedores → verificación/cierre, con comandos y salidas esperadas. Identifica servicios externos y recuperación de resultados existentes.

### 15.2 📝 Commits

Haz commits sustantivos por etapas, con Conventional Commits; sin mínimo artificial. Ejemplo: `feat(api): sirve el modelo seleccionado`. Revisa `git status`, `git diff` y `git diff --staged` antes de confirmar; excluye archivos accidentales y secretos.

### 15.3 🔗 PR y Canvas

1. Publica con `git push -u origin feat/examen-final` y abre **un PR hacia `main`**, titulado `Examen final — Clasificación de SMS`.
2. Copia `docs/plantillas/pull-request-tarea.md` del repositorio público en **Write**; completa para el examen —ruta raíz— y revisa **Preview**. Enlaza informe, métricas, bitácora y evidencias.
3. Revisa **Files changed** y fusiona con **Create a merge commit**. Confirma **Merged** y cerrado; cerrar sin merge no cumple.
4. Actualiza localmente con `git switch main` y `git pull`. Entrega **sólo la URL del PR fusionado en Canvas** antes del límite y verifica acceso de `zapatacc`.

El PR fija la versión entregada: no la cambies antes de sustentar sin indicación del profesor. Retrasos se rigen por la guía de aprendizaje, fuera de los puntos de la rúbrica.

## 16. 🎤 Sustentación individual — 10 puntos

Preséntate puntualmente a tu turno en T-105 con informe, repositorio, evidencias y aplicación listos. Dispones de **8 minutos, explicación y preguntas incluidas**, sin IA ni ayuda de otras personas.

El profesor preguntará por dos aspectos técnicos —datos/fuga, selección/versionado o recorrido UI/API/modelo— y una decisión de tu bitácora con su validación. No se exige desarrollar una funcionalidad nueva.

> **⚠️ Puntualidad:** si no llegas a la hora de tu turno, este apartado recibe **0/10**.

## 17. ⚖️ Rúbrica — 100 puntos

Cada subcriterio obtiene su máximo si se cumple, crédito parcial proporcional si hay evidencia incompleta y cero si está ausente o no es verificable. Las herramientas equivalentes se califican igual; una falla no anula todo el examen.

| Criterio | Distribución de puntos | Máximo |
|---|---|---:|
| Repositorio, ambiente y Git | Python 3.12 y ambiente reproducible (2); organización y exclusión de secretos/datos (1); rama, commits y PR fusionado entregado (2). | 5 |
| Datos y EDA | Procedencia/depuración reproducible (3); separación justificada sin duplicados compartidos (3); clases/longitud y decisiones interpretadas (2). | 8 |
| Representación | Transformaciones aprendidas sólo con entrenamiento durante selección (3); consistencia evaluación/inferencia (3); elección justificada (1). | 7 |
| Modelos y evaluación | Baseline y dos familias (2); búsquedas y rangos justificados (3); selección con validación y prueba sin retuning (3); métricas/matriz/errores (2). | 10 |
| Tracking y registro | Experimentos trazables, parámetros/métricas (4); dos versiones completas con esquema/ejemplo ficticio, selección y origen (4); evidencia persistente y ubicación documentada (2). | 10 |
| Flujo de entrenamiento | Coordinación independiente del notebook (5); responsabilidades, datos existentes y fallas documentadas (2); ejecución evidenciada (1). | 8 |
| API | Carga inicial y versión concreta (3); contrato válido y paridad (3); cinco casos inválidos (3); salud coherente (1). | 10 |
| Interfaz | Consulta HTTP a API (2); resultado/versión y errores manejados (2); evidencia (1). | 5 |
| Contenedores | Empaquetado separado y ambiente coherente (3); red/configuración sin secretos (2); arranque/predicción/cierre evidenciados (2). | 7 |
| AWS | Recorrido aplicado, SSH/Git/configuración/red (3); costos y detención/terminación/cierre (2). No requiere despliegue real. | 5 |
| Informe y conclusiones | Informe ejecutable y manual reproducible (3); conclusiones sobre errores, desbalance y límites del corpus (2). | 5 |
| Decisiones y uso crítico de IA | Propósito/herramienta/prompts o no uso documentado (2); decisiones razonadas (2); validación independiente con evidencia (3); vínculo con archivos/cambios (2); límites reconocidos (1). | 10 |
| Sustentación individual | Dos aspectos técnicos con evidencia (6: hasta 3 cada uno); decisión y validación de bitácora (4). Impuntualidad: **0/10** en este apartado. | 10 |
| **Total** | | **100** |

Copiar una conversación sin analizarla sólo acredita la trazabilidad que contenga; no demuestra criterio o validación. Aceptar o rechazar una propuesta con fundamento puede obtener el mismo puntaje.

## 18. ✅ Antes de entregar

- [ ] Revisé todos los requisitos y evidencias; ambiente, datos, flujo, informe y servicios son reproducibles.
- [ ] Justifiqué decisiones y uso de IA, preservé prueba y relacioné métricas/modelos/versiones.
- [ ] Verifiqué el contrato, la interfaz y los contenedores; expliqué AWS y cerré recursos utilizados.
- [ ] El profesor tiene acceso; el PR está Merged y entregado en Canvas antes del límite.
- [ ] Consulté mi turno y puedo sustentar puntualmente mi trabajo.
