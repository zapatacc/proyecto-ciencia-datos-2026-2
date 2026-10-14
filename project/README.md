# Guía del proyecto — Proyecto en Ciencia de Datos

**Edición:** Otoño 2026

## 1. Propósito y recorrido

Construir una aplicación de machine learning que atienda un problema definido,
pueda reproducirse y permita a una persona utilizar sus predicciones.

El proyecto relaciona el problema y los datos con la evaluación del modelo, su
versión, el servicio de predicción, la interfaz y la aplicación publicada.
El equipo debe poder explicar qué hace cada componente y qué evidencia sostiene
sus decisiones.

Esta guía desarrolla el recorrido presentado en la
[Clase 7 — Inicio del proyecto](../modulo-01-fundamentos/clase-07-integracion.ipynb).
Se conserva el repositorio, el informe y el trabajo ya realizado. Las
instrucciones de cada tarea precisan qué parte corresponde entregar y evaluar
en cada etapa; los componentes finales se construyen progresivamente.

**Cómo usar esta guía:** presenta el recorrido completo del proyecto, por lo
que puede incluir temas que todavía no se han trabajado en clase. Para cada
entrega, cíñanse al alcance, requisitos y fecha indicados en la tarea
correspondiente. Usen esta guía como orientación para desarrollar los puntos
que sí aplican; no se pide anticipar componentes que la tarea aún no solicita.

| Etapa | Resultado que permite avanzar |
|---|---|
| Problema y datos | Pregunta, usuario, datos documentados, EDA y preparación. |
| Diseño | Mapa del sistema con componentes, contratos, supuestos y riesgos. |
| Modelado | Baseline, evaluación, experimentos registrados y modelo versionado. |
| Integración local | Entrenamiento reproducible, API e interfaz conectadas. |
| Empaquetado y publicación | Contenedores, ejecución local y aplicación publicada. |
| Operación y cierre | Actualización, recuperación, informe y demostración. |

## 2. Productos y trabajo en equipo

El trabajo se realiza en equipos de dos personas, con un máximo de tres,
dentro del repositorio privado del proyecto, separado de
`pcd-entregas-2026`.

| Producto | Qué comunica o permite comprobar |
|---|---|
| Informe acumulativo | Problema, decisiones, resultados, conclusiones y limitaciones. |
| Repositorio | Código, dependencias, configuración e instrucciones reproducibles. |
| Aplicación | Recorrido funcional desde una entrada hasta una predicción interpretable. |
| Presentación | Explicación, demostración y respuestas fundamentadas. |

La distribución de responsabilidades debe incluir revisión cruzada. Cada
integrante debe poder explicar el sistema completo y las decisiones principales,
además de su contribución.

## 3. Problema, datos y alcance del modelo

El equipo trabaja con el problema y dataset que ha desarrollado durante el
semestre. NYC Taxi sirve como referencia del curso; sus cinco features, fechas,
algoritmos y RMSE no son requisitos universales para otros problemas.

Documenten:

- quién utilizaría el resultado y qué decisión apoyaría;
- qué representa cada fila y cómo se construye el target;
- qué features estarán disponibles al momento de predecir;
- de dónde provienen los datos, su versión o corte y sus condiciones de uso;
- cómo se separan entrenamiento y evaluación;
- qué métrica principal resulta adecuada y cómo debe interpretarse;
- qué riesgos existen por faltantes, sesgo, cobertura o fuga de información.

Un **baseline** es una solución sencilla de referencia, como una regla o un
modelo básico apropiado para el problema. Permite interpretar si el esfuerzo
adicional aporta una mejora útil.

Justifiquen las familias de modelos elegidas, comparen resultados con la misma
estrategia de evaluación y seleccionen el modelo que utilizará la aplicación.
La tarea correspondiente define el número de familias y si exige optimización
de hiperparámetros (HPO). Una familia no se convierte en otra por cambiar
sus hiperparámetros.

Las métricas no sustituyen la interpretación: expliquen sus unidades o
significado, sus limitaciones y la consecuencia de una predicción incorrecta.
La evaluación final debe utilizar datos separados del ajuste y de la selección.

## 4. Organización del repositorio

Se conserva la estructura presentada al iniciar el proyecto. Esta estructura
de referencia muestra cómo puede crecer; creen carpetas cuando tengan contenido
y documenten cualquier adaptación.

```text
.
├── README.md
├── LICENSE
├── .gitignore
├── .python-version
├── pyproject.toml
├── uv.lock
├── .env.example
├── data/
│   └── README.md
├── docs/
│   └── mapa-sistema-ml.md
├── evidencia/
│   ├── eda-ejecutado.png             # exploración y resultado observable
│   ├── preparacion-ejecutada.png     # resultado de preparación
│   ├── mlflow-experimento.png        # ruta y vista general de runs
│   ├── hpo-familia-a.png             # trials, parámetros y métricas de una familia
│   ├── comparacion-modelos.png       # comparación de los mejores resultados
│   ├── registry-versiones.png        # versiones y alias del modelo
│   ├── prefect-flow.png              # flow y tasks ejecutados
│   ├── api-prediccion-valida.png      # solicitud y respuesta válida
│   ├── api-entrada-invalida.png       # solicitud y respuesta de validación
│   └── frontend-prediccion.png        # formulario y predicción de la API
├── informe/
│   └── informe-final.ipynb
├── notebooks/
│   ├── 01-eda.ipynb
│   ├── 02-preparacion-datos.ipynb
│   ├── 03-experimentos.ipynb
│   ├── 04-seleccion-registro.ipynb
│   ├── 05-pipeline.ipynb
│   ├── 06-api.ipynb
│   ├── 07-frontend.ipynb
│   ├── 08-contenedores.ipynb
│   ├── 09-despliegue.ipynb
│   └── 10-operacion.ipynb
├── src/
│   ├── entrenamiento/
│   ├── api/
│   └── frontend/
├── compose.yaml
└── despliegue/
```

- **Notebooks:** un cuaderno propio por componente, con desarrollo técnico
  detallado, resultados y comprobaciones; véase la sección 5.5.
- **Archivos Python en `src/`:** código reutilizable de preparación,
  entrenamiento e inferencia.
- **Informe:** explicación integrada que sintetiza y referencia ese trabajo.
- **Evidencia:** imágenes legibles de las comprobaciones realizadas.
- **Mapa del sistema:** diseño actualizado con diferencias claras entre lo
  implementado, lo propuesto y lo pendiente.

Los nombres de imágenes del árbol son ejemplos de su contenido. Guarden tantas
capturas como necesiten para cubrir los casos de la tarea, con nombres claros
y sin crear archivos vacíos. Creen únicamente los notebooks de los componentes
que correspondan al alcance solicitado. `frontend/` identifica el código de
la interfaz de usuario; `api/` conserva el servicio que ésta consume.

Mantengan fuera de Git ambientes, secretos, datos descargados y modelos
generados. Documenten cómo obtener o reconstruir cada recurso necesario.
`.env.example` describe la configuración mediante valores ficticios;
`.env` conserva los valores locales y permanece ignorado.
El código propio utiliza MIT; los datos y recursos externos conservan sus
condiciones de uso y atribuciones.

## 5. Informe acumulativo

Continúen `informe/informe-final.ipynb`. El informe integra el hilo completo
del proyecto; los notebooks técnicos conservan el detalle de ejecución.
Cada sección presenta resultados interpretados y referencias a los archivos
que los respaldan.

**Distribución obligatoria del contenido:**

| Ubicación | Contenido esperado |
|---|---|
| `notebooks/` | Desarrollo técnico detallado: procedimientos, código de análisis y experimentación, preparación, parámetros y espacios de búsqueda, resultados, gráficas, comparaciones, comprobaciones e interpretación técnica. |
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
preprocesamiento, particiones, HPO de las familias cuando aplique, parámetros, métricas
y análisis de los experimentos. El informe presenta la comparación principal,
explica qué modelo se seleccionó y por qué, interpreta sus resultados y
limitaciones y referencia ese notebook. No necesita repetir todos los trials
ni el código del entrenamiento.

### 5.1. Título, contexto e introducción

El título identifica el problema y el propósito de la solución.
La introducción explica el contexto, la relevancia, el usuario previsto y el
alcance. Debe quedar claro para qué serviría la predicción y qué queda fuera
de la solución.

### 5.2. Antecedentes

Mantengan y amplíen las fuentes pertinentes del proyecto.
Expliquen qué aporta cada referencia al problema, a la selección de datos,
a la evaluación o al diseño. Una lista de enlaces sin interpretación no
permite reconocer su contribución.

### 5.3. Objetivos

Conserven un objetivo general y entre tres y cinco objetivos específicos
coherentes con el alcance real. Utilicen resultados observables: por ejemplo,
evaluar un modelo con una partición justificada o permitir que el usuario
obtenga una predicción mediante una interfaz.

Indiquen cómo reconocerán el logro. Los umbrales de desempeño deben justificarse;
si aún no existe evidencia para fijarlos, declaren esa incertidumbre.

### 5.4. Planteamiento del problema y datos

Precisen la pregunta, el usuario, la unidad de observación, las entradas,
el target, los supuestos, las restricciones y los riesgos.
Enlacen la fuente original y `data/README.md`, donde se documentan permiso,
corte, significado de columnas y procedimiento de obtención.

### 5.5. Desarrollo de la solución

**Cada componente que solicite la tarea debe desarrollarse detalladamente en
su propio notebook dentro de `notebooks/`.** No basta con nombrarlo en el
informe o enlazar un script: el notebook explica propósito, decisiones,
procedimiento, código o llamadas al módulo reutilizable, resultados,
comprobaciones e interpretación técnica. El código ejecutable reutilizable
permanece en `src/`; no es necesario copiar su implementación completa al
notebook. Las verificaciones de API e interfaz pueden documentar la ejecución
de procesos externos sin iniciarlos automáticamente desde el cuaderno.

En el informe escrito, cada subsección contiene el **consolidado con los
highlights**: hallazgos principales, decisiones justificadas, resultados
clave y limitaciones. Incluyan las tablas o gráficas necesarias para
comprenderlos y una referencia explícita al notebook técnico. No repitan todo
el código, todas las pruebas ni cada resultado intermedio.

| Componente | Notebook técnico con desarrollo detallado | Highlights en el informe |
|---|---|---|
| EDA | `01-eda.ipynb`: exploración, distribuciones, relaciones, calidad, gráficas y análisis de riesgos. | Hallazgos principales y su consecuencia para el problema y los datos. |
| Preparación | `02-preparacion-datos.ipynb`: reglas, transformaciones, resultados antes/después, esquema y prevención de fuga. | Decisiones de preparación y cambios relevantes en los datos. |
| Entrenamiento y evaluación | `03-experimentos.ipynb`: baseline, familias, particiones, HPO cuando aplique, parámetros, métricas y comparación completa. | Comparación principal e interpretación del desempeño. |
| Selección y registro | `04-seleccion-registro.ipynb`: criterio de selección, run de procedencia, registro, versiones, aliases y comprobación de carga. | Modelo elegido, justificación, versión y limitaciones. |
| Pipeline de entrenamiento | `05-pipeline.ipynb`: etapas, entradas/salidas, dependencias, ejecución, logs y diagnóstico de fallas. | Funcionamiento general y resultado principal de la ejecución. |
| API | `06-api.ipynb`: contrato, validación, carga del modelo, solicitudes/respuestas y pruebas válidas e inválidas. | Cómo se consume la predicción y qué resultados se comprobaron. |
| Frontend | `07-frontend.ipynb`: formulario, llamada HTTP, presentación del resultado y manejo de errores. | Experiencia del usuario y evidencia clave de integración. |
| Contenedores | `08-contenedores.ipynb`: Dockerfiles, configuración de Compose, conexiones, ejecución y comprobaciones. | Arquitectura ejecutable y resultado de integración. |
| Despliegue | `09-despliegue.ipynb`: configuración, procedimiento de publicación y verificación de la aplicación. | Aplicación publicada y comprobación principal. |
| Operación | `10-operacion.ipynb`: identificación de versión, logs, actualización y recuperación. | Resultado de operación, limitaciones y recuperación. |

Este mapa organiza el proyecto completo. Desarrollen sólo los componentes
solicitados en la tarea vigente; los notebooks de temas aún no vistos se
incorporan cuando corresponda. El informe mantiene la historia consolidada
de lo efectivamente realizado.

### 5.6. Conclusiones y recomendaciones

Relacionen resultados con objetivos. Expliquen logros, limitaciones y riesgos
pendientes. Propongan mejoras apoyadas en lo observado y distingan lo que
funciona de lo que sólo quedó diseñado.

### 5.7. Referencias

Utilicen un formato consistente para antecedentes, fuentes de datos,
documentación y recursos externos. Toda fuente citada debe poder localizarse.

## 6. Trazabilidad, versión y entrenamiento reproducible

MLflow conserva los experimentos: datos de referencia, parámetros, métricas
y artefactos. Databricks cumple el papel de tracking y Registry remoto en el
recorrido del curso. La aplicación publicada no depende de desplegarse allí.

El modelo seleccionado debe tener una versión identificable en Model Registry,
relacionada con su evaluación. Si utilizan un alias, documenten la versión a
la que apuntaba al verificar el sistema; un alias puede cambiar.

Conserven el preprocesamiento junto con el modelo o mediante una vinculación
inequívoca y reproducible. Entrenamiento e inferencia deben usar las mismas
definiciones de features y transformaciones. Carguen únicamente artefactos
propios y confiables.

El **pipeline de entrenamiento** es el recorrido que carga y valida los datos,
prepara, entrena, evalúa y guarda o registra resultados. No es lo mismo que
`sklearn.pipeline.Pipeline`, que encadena transformaciones y estimador.
El flujo debe ejecutarse desde código documentado, sin depender del orden
oculto de celdas. Prefect permite coordinar y observar etapas como preparación,
HPO, entrenamiento, evaluación y registro remoto. La tarea precisa qué etapas
y herramientas deben implementarse en cada momento.

### Workspace y nombres del proyecto

Una persona del equipo ejecuta los experimentos y registra los modelos desde
su cuenta personal de Databricks. Todas las personas desarrollan y revisan el
proyecto; no se comparten contraseñas ni tokens ni se exige repetir las corridas
en cada cuenta. La evidencia remota corresponde a ese único workspace.

Elijan un identificador descriptivo del proyecto, sin datos personales:

- Experimento: `/Shared/pcd-otono-2026-proyecto-<proyecto-en-kebab-case>`.
- Modelo registrado: `workspace.default.pcd_otono_2026_<proyecto_en_snake_case>`.

Por ejemplo, `abandono-clientes` produce el experimento
`/Shared/pcd-otono-2026-proyecto-abandono-clientes` y el nombre de modelo
`workspace.default.pcd_otono_2026_abandono_clientes`.
El catálogo del curso es `workspace` y el esquema es `default`.
El nombre del modelo usa **puntos**, no barras, entre catálogo, esquema y modelo.

Los mejores modelos de las familias se registran como versiones de ese mismo
modelo. El alias `champion` identifica la versión seleccionada. Las reglas de
runs y las capturas requeridas están en la tarea; el informe conserva la
comparación y justificación.

## 7. API e interfaz

En la integración local, FastAPI expone la predicción y Streamlit actúa como
consumidor HTTP. La [Clase 14](../modulo-02-ciclo-mlops/clase-14-model-service-streamlit.ipynb)
desarrolla esta separación.

La API debe documentar:

- campos, tipos, restricciones y ejemplo de entrada válida;
- salida, unidades o significado y versión del modelo utilizada;
- respuesta ante una entrada inválida;
- comportamiento cuando el modelo no puede cargarse;
- una comprobación de disponibilidad cuyo significado quede claro.

El modelo se entrena mediante su propio recorrido y se carga para servir
predicciones. No se reentrena al atender cada solicitud.

La interfaz presenta un formulario comprensible, envía la solicitud y muestra
el resultado y sus limitaciones. Una falla de conexión o validación debe
producir un mensaje útil. La interfaz no debe presentar como predicción un
valor inventado cuando el servicio falla.

## 8. Contenedores, publicación y operación

La integración local utiliza Docker y Compose para ejecutar y conectar API e
interfaz. Documenten configuración, conexión entre servicios, arranque,
comprobación y detención.

La ruta mínima prevista de publicación es una aplicación Streamlit autocontenida
mediante Docker en Hugging Face Spaces. El diseño local con API e interfaz
separadas y el diseño publicado deben explicarse por separado. La aplicación
publicada conserva el preprocesamiento y la versión identificable del modelo;
no requiere reentrenar al recibir una entrada. Separar API e interfaz en dos
Spaces es una extensión, no el requisito mínimo.

AWS forma parte de la introducción guiada a infraestructura y no es una ruta
obligatoria del proyecto. No se exige contratar servicios ni aportar una
tarjeta personal. Las alternativas ante restricciones de acceso se acuerdan
con el profesor.

Documenten cómo observar errores, actualizar la aplicación o el modelo,
comprobar la versión activa y recuperar una versión anterior.
Para cualquier recurso con costo o acceso restringido, expliquen permisos,
configuración de secretos, detención y eliminación.

## 9. README y reproducibilidad

El README debe permitir a otra persona reconocer y ejecutar el trabajo:

1. problema, alcance y estado actual;
2. estructura y enlaces al informe y al mapa;
3. obtención de datos y recursos necesarios;
4. preparación del ambiente con Python 3.12;
5. configuración externa con ejemplos sin secretos;
6. ejecución del entrenamiento;
7. arranque y verificación de API e interfaz;
8. ejecución con contenedores y acceso a la aplicación publicada, cuando existan;
9. limitaciones, errores conocidos y procedimiento de recuperación.

`pyproject.toml` y `uv.lock` son la fuente de dependencias del proyecto.
La reproducción utiliza `uv sync --locked`. Si el despliegue necesita otro
formato, se genera desde esa configuración; no se mantiene una lista manual
incompatible.

La verificación parte de las instrucciones documentadas y evita rutas
personales, archivos ocultos y estado previo de notebooks.

## 10. Evidencias

Una evidencia comunica qué se comprobó, qué resultado se obtuvo y qué
conclusión sostiene. Conserven una imagen por cada caso solicitado en la
tarea correspondiente, enlazada desde README, informe o PR.

| Etapa | Qué debe poder comprobarse al completarla |
|---|---|
| EDA y preparación | Ejecución e interpretación de resultados. |
| Modelo | Evaluación, experimento y versión seleccionada. |
| Entrenamiento | Recorrido completo y diagnóstico de una falla controlada. |
| API | Solicitud válida e inválida con sus respuestas. |
| Interfaz | Entrada del usuario y resultado obtenido. |
| Contenedores | Componentes funcionando y comunicándose. |
| Publicación | Aplicación accesible y predicción verificable. |
| Operación | Cambio de versión y recuperación. |

Las imágenes muestran la acción o solicitud y su resultado, con texto legible
y sin datos sensibles. Las capturas complementan el código y las instrucciones.
Los endpoints se pueden comprobar con Postman, `/docs` o `curl`; no se exige
una herramienta de pruebas automatizadas que no se haya enseñado.

## 11. Correcciones de entregas anteriores

Apliquen las observaciones directamente en los notebooks, informe, código y
documentación correspondientes. Comprueben los resultados y actualicen las
interpretaciones afectadas. No se solicita una bitácora ni un archivo separado
de seguimiento de correcciones.

## 12. Colaboración, Git y Canvas

Consulten el [flujo de tareas](../docs/flujo-tareas.md).
Cada entrega utiliza la rama indicada, commits sustantivos, revisión de las
demás personas del equipo y un PR hacia `main`.
Revisen `Files changed` y atiendan observaciones antes de fusionar mediante
**Create a merge commit**. El PR debe quedar **Merged** y cerrado.

La entrega oficial se realiza en Canvas con la URL del PR según las
instrucciones de cada actividad. Canvas publica fechas, requisitos parciales
y rúbricas. Correo, Teams y mensajes privados no sustituyen la entrega.

La política de herramientas y uso de IA se define en cada actividad. El equipo
conserva la responsabilidad de revisar, citar fuentes y explicar todo el trabajo
que presenta. Las restricciones de una tarea individual siguen aplicándose a
esa tarea.

## 13. Evaluación y presentación

El proyecto representa el **30 % de la calificación del curso**:
**15 % corresponde al reporte y 15 % a la exposición**.
Las tareas y actividades parciales se evalúan en el apartado correspondiente
del curso, con sus propias instrucciones.

Los aspectos que deben poder revisarse son la coherencia del problema y los
datos, la evaluación y trazabilidad del modelo, la integración, la
reproducibilidad, la publicación, las limitaciones y la colaboración.
Los pesos detallados y la duración de la exposición se comunicarán en los
instrumentos oficiales de evaluación.

La exposición debe explicar el problema, mostrar evidencia de las decisiones
principales, presentar la arquitectura y demostrar una predicción completa.
El equipo debe reconocer la versión utilizada y responder preguntas sobre
resultados, limitaciones y responsabilidades.

## 14. Comprobación final

- [ ] El informe corresponde al sistema construido y enlaza su respaldo técnico.
- [ ] Las correcciones anteriores están aplicadas en los archivos correspondientes.
- [ ] Los datos, sus condiciones de uso y su preparación están documentados.
- [ ] El baseline y el modelo tienen una evaluación interpretada.
- [ ] La versión activa puede relacionarse con un experimento y un artefacto.
- [ ] El entrenamiento se reproduce sin depender de celdas previas.
- [ ] API e interfaz se comunican localmente.
- [ ] Los contenedores funcionan con la configuración documentada.
- [ ] La aplicación publicada permite obtener e interpretar una predicción.
- [ ] Se documentaron actualización y recuperación.
- [ ] El README permite reproducir las comprobaciones.
- [ ] Cada integrante puede explicar el recorrido completo.

## Recursos del curso

- [Clase 7 — Inicio del proyecto](../modulo-01-fundamentos/clase-07-integracion.ipynb).
- [Actividad en clase 3 — Mapa del sistema](../docs/tareas/actividad-clase-09-mapa-sistema-ml.md).
- [Clase 15 — Trabajo en el proyecto](../modulo-02-ciclo-mlops/clase-15-trabajo-proyecto.ipynb).
- [Calendario](../docs/calendario-2026.md).
- [Guía de aprendizaje](../docs/guia-de-aprendizaje/README.md).
