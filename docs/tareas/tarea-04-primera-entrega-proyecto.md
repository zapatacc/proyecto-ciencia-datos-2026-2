# Tarea 4 — Primera entrega del proyecto

## Propósito

Convertir el avance de la Clase 7 en una primera versión coherente y
reproducible del proyecto. El equipo definirá el problema, justificará los
datos elegidos, realizará el análisis exploratorio y documentará la preparación
que servirá como base para el modelado posterior.

Esta entrega inicia el **informe final**, un producto acumulativo que crecerá
durante el semestre. Los notebooks conservan el detalle técnico; el informe
sintetiza el problema, las decisiones, los hallazgos y sus implicaciones.

## Recursos

- [Clase 7 — Inicio del proyecto en equipo](../../modulo-01-fundamentos/clase-07-integracion.ipynb).
- [Flujo de trabajo y entrega de tareas](../flujo-tareas.md).
- [Plantilla de pull request](../plantillas/pull-request-tarea.md).
- Documentación original, licencia y diccionario del dataset elegido.

## Entregable

**Repositorio:** repositorio privado del proyecto en equipo.

**Rama obligatoria:** `feat/primera-entrega`

**Fecha límite:** lunes 14 de septiembre de 2026 a las 19:55, hora de la
Ciudad de México.

La rama debe crearse desde `main` actualizado después de fusionar el PR de la
actividad de clase:

```bash
git switch main
git pull
git status
git switch -c feat/primera-entrega
```

La entrega incluye:

```text
.
├── .gitignore
├── .python-version
├── README.md
├── pyproject.toml
├── uv.lock
├── data/
│   └── README.md
├── evidencia/
│   ├── eda-ejecutado.png
│   └── preparacion-ejecutada.png
├── informe/
│   └── informe-final.ipynb
├── notebooks/
│   ├── 01-eda.ipynb
│   └── 02-preparacion-datos.ipynb
└── src/
```

`src/` puede permanecer sin archivos en esta entrega. Git la mostrará cuando
el equipo agregue posteriormente el primer módulo reutilizable.

## 1. Informe inicial

En `informe/informe-final.ipynb` desarrollen:

1. título provisional del proyecto;
2. contexto e introducción;
3. antecedentes con dos a cuatro fuentes iniciales;
4. un objetivo general y de tres a cinco objetivos específicos;
5. planteamiento del problema;
6. descripción y justificación de los datos;
7. síntesis de los hallazgos del EDA y de la preparación;
8. conclusiones parciales y siguientes pasos;
9. referencias.

El planteamiento debe identificar al menos la pregunta del proyecto, el
usuario o grupo que podría beneficiarse, la unidad de observación, el target,
las features iniciales, los supuestos, el alcance y riesgos como datos
faltantes, sesgo o fuga de información.

## 2. Dataset documentado

El dataset debe tener relación clara con el problema y cumplir estas
condiciones:

- fuente pública o acceso permitido;
- licencia o condiciones de uso identificables;
- una muestra significativa para el problema que el equipo quiere estudiar;
- variables suficientes para analizar y construir un modelo;
- una variable objetivo identificable o construible;
- tamaño manejable en las computadoras del equipo;
- ausencia de datos personales o sensibles que no sean necesarios.

No existe un número mínimo universal de registros. En `data/README.md`, el
equipo debe justificar por qué la cobertura, el periodo, las categorías y la
cantidad de observaciones disponibles permiten estudiar razonablemente su
problema. También debe documentar:

- URL y organización responsable de la fuente original;
- licencia o condiciones de uso;
- significado de una fila y columnas principales;
- target y features iniciales;
- versión, periodo o corte utilizado;
- procedimiento para obtener los datos;
- archivos que permanecen localmente fuera de Git.

No agreguen el dataset completo al repositorio. Mantengan los archivos locales
bajo `data/raw/`, ruta excluida mediante `.gitignore`.

## 3. Análisis exploratorio

`notebooks/01-eda.ipynb` debe ejecutar de principio a fin y presentar:

- tamaño, columnas y tipos de datos;
- significado de la unidad de observación;
- valores faltantes, duplicados y valores atípicos relevantes;
- distribuciones y relaciones útiles para el problema;
- visualizaciones legibles, con título y etiquetas;
- interpretación de los hallazgos;
- riesgos para el modelado, incluidos sesgo y fuga de información;
- conclusiones que orienten la preparación de datos.

No basta con mostrar `describe()` o gráficas sin interpretación.

## 4. Preparación de datos

`notebooks/02-preparacion-datos.ipynb` debe ejecutar de principio a fin y:

- aplicar reglas explícitas de limpieza;
- justificar el tratamiento de faltantes, duplicados y valores inválidos;
- construir o seleccionar el target y las features iniciales;
- mostrar evidencia antes y después de las transformaciones principales;
- describir el dataset resultante;
- evitar transformaciones que utilicen información del futuro;
- registrar decisiones pendientes para la etapa de modelado.

El notebook puede trabajar con una muestra local manejable, siempre que el
equipo explique cómo se obtuvo y por qué es significativa para el problema.

## 5. README y reproducibilidad

El `README.md` de la raíz debe incluir:

- título provisional e integrantes;
- descripción del problema y resultado esperado;
- enlace a la fuente original y a `data/README.md`;
- explicación de la estructura del repositorio;
- estado actual y siguientes pasos;
- instrucciones para preparar el ambiente y ejecutar ambos notebooks.

Las dependencias utilizadas deben quedar declaradas en `pyproject.toml` y
`uv.lock`. No incluyan `.venv/`, datos descargados, secretos, credenciales ni
artefactos generados.

## Commits

Realicen commits sustantivos con mensajes descriptivos. Por ejemplo:

```text
docs(proyecto): define contexto y objetivos
feat(proyecto): agrega analisis exploratorio
feat(proyecto): prepara datos para modelado
docs(proyecto): sintetiza hallazgos iniciales
```

No hagan commits vacíos para alcanzar una cantidad determinada.

## Verificación

Desde la raíz del repositorio, sin depender del estado de una ejecución
anterior:

1. sincronicen el ambiente con las instrucciones documentadas;
2. reinicien el kernel y ejecuten `notebooks/01-eda.ipynb` de principio a fin;
3. reinicien el kernel y ejecuten `notebooks/02-preparacion-datos.ipynb` de
   principio a fin;
4. guarden una captura legible de cada notebook ejecutado en `evidencia/`;
5. enlacen las dos imágenes desde el README o la descripción del PR;
6. revisen `git status --short` y **Files changed**.

Cada imagen debe mostrar el nombre del notebook y un resultado observable de
su ejecución, sin rutas personales ni datos sensibles. Los outputs guardados
en los notebooks también deben permitir revisar los principales resultados.

## Pull request y cierre obligatorio

El PR debe apuntar a `main`. Abran la
[plantilla del curso](../plantillas/pull-request-tarea.md), copien todo su
contenido en **Write**, completen cada sección y comprueben el resultado con
**Preview**.

Agreguen como reviewers a las demás personas del equipo. Antes de fusionar:

1. revisen todos los archivos en **Files changed**;
2. confirmen que no aparezcan datos, ambientes, secretos ni artefactos;
3. atiendan las observaciones de la revisión;
4. fusionen mediante **Create a merge commit**;
5. confirmen que el PR aparezca como **Merged** y cerrado.

## Entrega en Canvas

Entreguen la URL del PR cerrado y fusionado antes de la
fecha límite. No entreguen una URL de la rama ni un PR abierto. Canvas es el
único medio oficial de entrega.

## Uso de herramientas y colaboración

El trabajo se realiza en equipo. Pueden consultar el material del curso,
documentación oficial y herramientas de IA como apoyo. El equipo debe verificar
toda sugerencia, citar las fuentes utilizadas y poder explicar el contenido,
el código y las decisiones del repositorio. Una respuesta generada por IA no
sustituye la ejecución, la evidencia ni la interpretación propia.

## Rúbrica — 100 puntos

| Criterio | Logro completo | Logro parcial | Insuficiente | Máximo |
|---|---|---|---|---:|
| Informe inicial | **23–25:** contexto, antecedentes, objetivos y problema forman una propuesta coherente; identifica usuario, unidad de observación, target, features, alcance y riesgos, y sintetiza los hallazgos iniciales. | **13–22:** la propuesta es comprensible, pero falta desarrollar o conectar un componente importante. | **0–12:** el informe no permite reconocer con claridad el problema, los objetivos o el uso esperado de los datos. | 25 |
| Análisis exploratorio | **23–25:** el notebook ejecuta, caracteriza los datos, presenta visualizaciones legibles e interpreta hallazgos y riesgos relevantes para el problema. | **13–22:** el análisis existe, pero omite una revisión importante, contiene una inconsistencia menor o interpreta parcialmente los resultados. | **0–12:** el análisis no ejecuta, se limita a salidas sin interpretación o no permite comprender los datos. | 25 |
| Preparación de datos | **23–25:** el notebook ejecuta, documenta y justifica las reglas de limpieza y transformación, muestra evidencia antes y después y describe el dataset resultante sin fuga evidente. | **13–22:** la preparación es utilizable, pero falta justificar, verificar o documentar una decisión importante. | **0–12:** las transformaciones no son reproducibles, dañan el target o utilizan información futura sin advertirlo. | 25 |
| Reproducibilidad, documentación y colaboración | **23–25:** fuente, licencia y muestra están justificadas; README, ambiente, evidencias y exclusiones permiten reproducir el trabajo; el historial identifica contribuciones y el PR fue revisado, fusionado y cerrado. | **13–22:** el trabajo llega a `main`, pero presenta omisiones de documentación, evidencia, ambiente o historial. | **0–12:** la entrega no es reproducible, incluye datos o secretos, carece de evidencia evaluable o el PR no fue fusionado. | 25 |
| **Total** |  |  |  | **100** |

La política de entregas tardías se aplica por separado según la guía de
aprendizaje.
