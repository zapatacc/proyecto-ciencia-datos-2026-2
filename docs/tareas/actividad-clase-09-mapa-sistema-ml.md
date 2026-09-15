# Actividad en clase 3 — Mapa del sistema de ML

## Propósito

Construir un primer mapa del proyecto como sistema de machine learning que
coordina datos, modelo y código. Este mapa es una guía de diseño: partirá de
la evidencia disponible en el EDA y podrá cambiar conforme el equipo obtenga
nueva información, implemente componentes o valide sus supuestos.

## Recursos

- [Clase 9 — Tres niveles del software de ML](../../modulo-02-ciclo-mlops/clase-09-niveles-software-ml.ipynb).
- [Flujo de trabajo y entrega de tareas](../flujo-tareas.md).
- [Plantilla de pull request](../plantillas/pull-request-tarea.md).
- Documentación de la fuente de datos y del problema elegido por el equipo.

## Entregable

**Repositorio:** repositorio privado del proyecto en equipo, separado de
`pcd-entregas-2026`.

**Rama obligatoria:** `docs/mapa-sistema-ml`

**Archivo principal:** `docs/mapa-sistema-ml.md` (borrador vivo de diseño)

**Evidencia oficial:** URL de un pull request hacia `main`, revisado,
fusionado y cerrado.

Antes de escribir, una persona del equipo actualiza `main` y crea la rama:

```bash
git switch main
git pull
git switch -c docs/mapa-sistema-ml
mkdir -p docs
```

Después creen `docs/mapa-sistema-ml.md` desde VS Code. Las demás personas del
equipo trabajan sobre la misma rama y coordinan sus cambios antes de hacer
push.

El archivo debe incluir. Para cada apartado, distingan entre **evidencia del
EDA**, **decisión inicial**, **supuesto** y **pregunta pendiente**. No se
espera que todas las decisiones estén cerradas en esta etapa.

1. **Contexto:** problema, usuario o sistema consumidor y decisión que apoyará
   la predicción.
2. **Nivel de datos:** fuentes, unidad de observación, target y features
   candidatas que ya puedan justificarse desde el EDA; validaciones,
   preparación y estrategia de entrenamiento/validación/prueba por confirmar.
3. **Nivel del modelo:** tarea de ML, baseline previsto, métrica inicial,
   criterio de aceptación por definir y contenido esperado del artefacto.
4. **Nivel de código:** componentes que probablemente serán necesarios para
   entrenamiento e inferencia, aplicación o API consumidora, dependencias o
   configuración por investigar y señales que convendría registrar.
5. **Interfaces:** al menos tres contratos o conexiones entre niveles. Por
   ejemplo, nombres y tipos de features, formato del artefacto o contrato de la
   API.
6. **Forma de operación:** decidir si el entrenamiento será offline o
   incremental y si la inferencia será batch o bajo demanda. Justificar ambas
   decisiones.
7. **Patrón de serving:** comparar brevemente Model-as-Service,
   Model-as-Dependency y Precompute, y seleccionar el patrón inicial más
   razonable para el proyecto.
8. **Diagrama:** representar el recorrido desde la fuente de datos hasta la
   persona o sistema consumidor. Puede realizarse con Mermaid, un diagrama
   propio legible o un bloque de texto estructurado.
9. **Riesgo prioritario:** identificar una brecha concreta, su consecuencia y
   el siguiente incremento que la reduciría. No basta con proponer una
   herramienta.
10. **Fuentes y supuestos:** enlazar las referencias utilizadas y señalar qué
    información todavía necesita validarse.

El mapa describe el diseño inicial y no un compromiso definitivo. No se exige
implementar durante esta actividad un pipeline automatizado, un servicio nuevo,
Docker, serverless, monitoreo ni aprendizaje online. Actualizar el mapa cuando
una decisión deje de ser un supuesto es parte natural del trabajo posterior.

## Trabajo en equipo

Distribuyan el trabajo, pero revisen el documento completo entre todas las
personas integrantes. Cada integrante debe poder explicar:

- una decisión de datos;
- una decisión de modelo;
- una decisión de código;
- el patrón de operación elegido;
- el riesgo prioritario.

En la descripción del PR indiquen quién revisó cada nivel y qué desacuerdo o
ajuste surgió durante la revisión.

## Commits

Usen mensajes que describan cambios sustantivos. Por ejemplo:

```text
docs(proyecto): describe niveles del sistema de ml
docs(proyecto): agrega diagrama y contratos
docs(proyecto): justifica patron de serving
```

No realicen commits vacíos ni trabajen directamente sobre `main`.

## Verificación

Antes de abrir el PR, comprueben:

```bash
git status --short
git diff
```

Después revisen el archivo desde GitHub y confirmen que:

- el diagrama se puede leer;
- los enlaces funcionan;
- no aparecen credenciales, datos personales, rutas locales ni datasets;
- el PR contiene únicamente los archivos de esta actividad;
- todas las personas integrantes comprenden y aprueban las decisiones.

## Pull request y cierre obligatorio

El PR debe apuntar a `main`. Para preparar su descripción:

1. abran la [plantilla del curso](../plantillas/pull-request-tarea.md);
2. copien todo su contenido y péguenlo en **Write**;
3. adapten el resumen, la verificación y la lista de requisitos;
4. indiquen la contribución y revisión de cada integrante;
5. comprueben el resultado con **Preview**;
6. agreguen como reviewers a las demás personas del equipo;
7. revisen **Files changed** y atiendan las observaciones;
8. fusionen mediante **Create a merge commit**.

Antes de entregar, el PR debe aparecer como **Merged** y cerrado. Cerrar sin
merge no completa la actividad.

## Entrega en Canvas

Cada integrante entrega en la actividad correspondiente de Canvas la URL del
mismo PR cerrado y fusionado. La descripción del PR debe identificar a todas
las personas integrantes. La fecha y hora límite se publican en Canvas.

## Uso de herramientas y colaboración

El trabajo se realiza en equipo. Pueden consultar el material del curso,
documentación oficial y herramientas de IA como apoyo. El equipo debe revisar
toda sugerencia, citar las fuentes utilizadas y poder explicar el contenido y
las decisiones. Una respuesta generada por IA no sustituye la discusión, la
revisión cruzada ni la justificación propia.

## Rúbrica — 100 puntos

| Criterio | Logro completo | Logro parcial | Insuficiente | Máximo |
|---|---|---|---|---:|
| Nivel de datos | **18–20:** separa evidencia del EDA, decisiones iniciales, supuestos y preguntas sobre fuente, observación, target, features, validaciones, preparación y particiones. | **10–17:** el nivel se reconoce, pero faltan elementos o no se distingue qué necesita confirmación. | **0–9:** la descripción no permite saber qué datos alimentan el sistema o presenta certezas sin evidencia. | 20 |
| Nivel del modelo | **18–20:** propone tarea, baseline, métrica, aceptación, salida de entrenamiento y artefacto esperado; declara con claridad lo que aún no puede decidirse. | **10–17:** presenta componentes del modelo, pero omite decisiones importantes o confunde evaluación, prueba y artefacto. | **0–9:** sólo nombra un algoritmo o no permite reconocer cómo se evaluaría y conservaría el modelo. | 20 |
| Nivel de código e interfaces | **18–20:** distingue componentes probables de entrenamiento, inferencia y consumidor; documenta al menos tres contratos o preguntas verificables y señales de operación. | **10–17:** reconoce los componentes, pero las interfaces o señales son incompletas. | **0–9:** el código aparece como una caja aislada o no se conecta con datos, modelo y consumidor. | 20 |
| Operación y patrón de serving | **13–15:** formula una elección inicial de entrenamiento, inferencia y patrón después de comparar alternativas pertinentes y declarar supuestos. | **7–12:** existe una elección razonable, pero la comparación o justificación es parcial. | **0–6:** selecciona herramientas o patrones sin relacionarlos con frecuencia, consumidor o necesidades del proyecto. | 15 |
| Diagrama, riesgo y siguiente incremento | **9–10:** el diagrama comunica el diseño inicial y el riesgo o incertidumbre prioritaria conduce a un siguiente incremento concreto y proporcional. | **5–8:** el recorrido o la relación riesgo–mejora necesita aclaraciones. | **0–4:** falta el diagrama, no es legible o la propuesta no responde al riesgo o incertidumbre identificado. | 10 |
| Colaboración, historial Git, PR y Canvas | **13–15:** registra contribuciones y revisión, usa la rama indicada y commits sustantivos, revisa el diff, fusiona a `main` y entrega la URL correcta. | **7–12:** el trabajo llega a `main`, pero falta una evidencia de colaboración, revisión o cierre. | **0–6:** trabaja en `main`, deja el PR abierto/cerrado sin merge o no entrega la URL oficial. | 15 |
| **Total** |  |  |  | **100** |

La política de entregas tardías se aplica por separado según la guía de
aprendizaje.
