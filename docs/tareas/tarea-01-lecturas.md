# Tarea 1 — Primeras perspectivas sobre MLOps

## Propósito

Comparar cómo distintas organizaciones explican MLOps y practicar por primera vez el flujo completo de una tarea: rama, commits, pull request, revisión, merge y entrega oficial en Canvas.

## Lecturas

Lee **por lo menos dos** de las siguientes fuentes:

- AWS, [What is MLOps?](https://aws.amazon.com/what-is/mlops/)
- Red Hat, [What is MLOps?](https://www.redhat.com/en/topics/ai/what-is-mlops)
- Microsoft, [MLOps Maturity Model](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/mlops-maturity-model)
- MLOps.org, [Machine Learning Operations](https://ml-ops.org/)
- InfoQ, [MLOps: Continuous Delivery of Machine Learning Systems](https://www.infoq.com/news/2021/08/continuous-delivery-ML-systems/) — lectura aproximada de 5 minutos
- Fiddler AI, [MLOps Lifecycle](https://www.fiddler.ai/blog/mlops-lifecycle)
- Kreuzberger, Kühl y Hirschl, [Machine Learning Operations (MLOps): Overview, Definition, and Architecture](https://epub.uni-bayreuth.de/id/eprint/7577/1/Machine_Learning_Operations_MLOps_Overview_Definition_and_Architecture.pdf)

Las primeras tres lecturas son introducciones y modelos generales. Las siguientes tres son textos breves sobre principios, entrega continua y ciclo de vida. El último artículo, de Kreuzberger, Kühl y Hirschl, es una revisión académica extensa y queda como opción avanzada: puedes consultar sólo las secciones que sean pertinentes para tu comparación.

No necesitas leer todas. Elige fuentes que te permitan contrastar perspectivas y en el resumen deja claro cuáles utilizaste.

## Entregable

Crea este archivo dentro de tu repositorio individual:

```text
tareas/tarea-01-lecturas/resumen.md
```

El archivo debe contener:

1. una definición propia de MLOps;
2. una síntesis de cada fuente consultada;
3. por lo menos dos coincidencias y dos diferencias entre las fuentes;
4. un ejemplo de un problema que MLOps busca resolver;
5. una reflexión final: ¿qué parte de MLOps esperas aprender o practicar en este curso?;
6. enlaces directos a las fuentes utilizadas.

No hay una extensión medida únicamente por palabras. Se evaluará que la comparación sea clara, específica y escrita con tus propias palabras.

## Rama y commits

Esta tarea produce documentación, no una funcionalidad de software. Por eso utiliza el tipo `docs` y la rama debe llamarse exactamente:

```text
docs/01-lecturas
```

Comienza desde `main` actualizado y crea tanto la rama como la carpeta antes de redactar:

```bash
git switch main
git pull
git switch -c docs/01-lecturas
mkdir -p tareas/tarea-01-lecturas
code tareas/tarea-01-lecturas/resumen.md
```

Si `code` no está disponible, abre el repositorio en VS Code y crea `resumen.md` desde el explorador lateral.

Realiza por lo menos dos commits con cambios sustantivos. Ejemplos válidos:

```text
docs(tarea-01): agrega sintesis de las lecturas
docs(tarea-01): compara perspectivas sobre mlops
```

Dividir un mismo párrafo artificialmente o hacer cambios vacíos no cuenta como historial sustantivo.

Una vez terminado el texto:

```bash
git status
git diff
git add tareas/tarea-01-lecturas/resumen.md
git diff --staged
git commit -m "docs(tarea-01): compara perspectivas sobre mlops"
git push -u origin docs/01-lecturas
```

## Pull request y cierre obligatorio

Abre un pull request desde `docs/01-lecturas` hacia `main`. La [plantilla de pull request](../plantillas/pull-request-tarea.md) permanece en el repositorio público del curso: abre ese archivo, copia todo su contenido y pégalo en **Write**, dentro de la descripción del PR. Sustituye las indicaciones por información de tu tarea, marca las casillas cumplidas y utiliza **Preview** para revisar el resultado. Después revisa **Files changed** y corrige cualquier archivo accidental.

Antes de entregar:

1. completa todas las secciones y la checklist de la plantilla;
2. fusiona el pull request a `main` con **Create a merge commit**;
3. confirma que GitHub lo muestre como **Merged** y cerrado;
4. actualiza tu `main` local con `git pull`.

Cerrar el PR sin hacer merge no cumple el requisito. Consulta el [flujo general de tareas](../flujo-tareas.md) si necesitas el procedimiento completo.

## Entrega en Canvas

**Fecha y hora límite:** consulta la actividad correspondiente en Canvas.

Entrega en el espacio correspondiente:

- la URL del pull request cerrado y fusionado.

Canvas es la fuente oficial si se comunica algún ajuste. Aplican las políticas de entrega tardía de la guía de aprendizaje.

## Uso de herramientas

La lectura, comparación y redacción son individuales. No se permite usar IA generativa para resumir las fuentes, redactar el entregable o producir la reflexión. Puedes consultar diccionarios, documentación de Markdown, mensajes de Git y al profesor. El uso de correctores ortográficos sin generación de texto está permitido.

## Rúbrica

| Criterio | Logro completo | Logro parcial | Insuficiente | Máximo |
|---|---|---|---|---:|
| Comprensión y síntesis | **22–25:** explica correctamente y con palabras propias las ideas centrales de al menos dos fuentes. | **13–21:** comprende la idea general, pero presenta omisiones, imprecisiones o paráfrasis poco desarrolladas. | **0–12:** reproduce fragmentos, confunde los conceptos centrales o utiliza menos de dos fuentes. | 25 |
| Comparación | **22–25:** desarrolla al menos dos coincidencias y dos diferencias específicas y justificadas. | **13–21:** identifica comparaciones pertinentes, pero alguna queda superficial o sin explicación. | **0–12:** presenta resúmenes aislados o comparaciones vagas sin evidencia. | 25 |
| Ejemplo y reflexión | **13–15:** propone un problema pertinente para MLOps y conecta una reflexión propia con el curso. | **7–12:** incluye ejemplo y reflexión, pero su relación con MLOps o con el curso es parcial. | **0–6:** falta uno de los elementos o ambos son genéricos y desconectados. | 15 |
| Fuentes, claridad y Markdown | **9–10:** incluye enlaces directos y estructura legible con títulos, párrafos y listas bien utilizados. | **5–8:** las fuentes son identificables, pero existen problemas menores de organización, redacción o Markdown. | **0–4:** faltan fuentes o la organización dificulta comprender el documento. | 10 |
| Historial de Git | **9–10:** usa la rama exacta y al menos dos commits sustantivos con mensajes según la convención. | **5–8:** el historial permite seguir el trabajo, pero tiene un error de rama, cantidad, separación o mensaje. | **0–4:** trabaja en `main`, fabrica commits vacíos o no deja historial evaluable. | 10 |
| Pull request y entrega | **13–15:** completa la plantilla, revisa el diff, usa merge commit, deja el PR **Merged** y cerrado y entrega su URL en Canvas. | **7–12:** el trabajo llega a `main`, pero falta o contiene un error alguna evidencia del PR o Canvas. | **0–6:** el PR queda abierto, se cierra sin merge, apunta a otra rama o no se entrega la evidencia oficial. | 15 |
| **Total** |  |  |  | **100** |

La política de entregas tardías se aplica después de determinar el resultado de esta rúbrica.
