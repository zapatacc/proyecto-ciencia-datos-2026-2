# Laboratorio 5 — Explicar predicciones con SHAP

## Resultado observable

Entrenarás un Random Forest de Green Taxi y compararás dos maneras de describir la importancia de sus entradas. Generarás una gráfica global y una explicación, expresada en minutos, de un viaje de la muestra reservada.

La **importancia por impureza** del bosque mide cuánto contribuye cada columna a reducir el error en las divisiones de sus árboles durante el entrenamiento. Es un resumen global del modelo. Una **atribución SHAP** indica cuánto desplaza una característica la predicción de un viaje respecto al valor de referencia del explicador. Las contribuciones positivas elevan la estimación y las negativas la reducen. Para obtener un resumen global de SHAP, se promedia la magnitud de las atribuciones en varios viajes. Los métodos usan escalas diferentes, por lo que la comparación se hace sobre el orden de las variables y su interpretación. [Scikit-learn — Importancia por impureza](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html) · [SHAP — TreeExplainer](https://shap.readthedocs.io/en/stable/generated/shap.TreeExplainer.html)

El pipeline de Clase 10 conserva tres variables numéricas y convierte las dos zonas en columnas binarias mediante one-hot encoding. Para mostrar cinco variables en la gráfica, se agrupan las columnas de cada zona. En SHAP se suman primero los aportes **con su signo** dentro de cada zona para cada viaje. Después se calcula la magnitud media del aporte agrupado. Una suma agrupada describe la atribución de las columnas codificadas por este modelo.

## Preparar el proyecto

Actualiza el repositorio público del curso mediante `git status` y `git pull` desde `main`. Crea y clona el repositorio nuevo y privado siguiendo la [consigna común](README.md). Desde la raíz del clon del equipo, ejecuta `git switch -c feat/explicabilidad-shap` para abrir la rama de trabajo.

1. Copia el contenido del [starter de este laboratorio](../../../labs/starters/clase-24-laboratorios-mlops/05-explicabilidad-shap) a la raíz del repositorio del equipo. Conserva las carpetas y los archivos ocultos. La [consigna común](README.md#copiar-los-archivos-del-laboratorio) incluye el comando de copia.
2. Copia `modelos.py` y `preparar_datos.py` del [starter de Clase 10](../../../labs/starters/clase-10-experiment-tracking/README.md) a la raíz. Copia el contenido de la carpeta `datos/` de la Clase 10. El bosque se ajusta con marzo y se explica sobre abril.
3. Prepara el ambiente desde el repositorio del equipo. `uv sync --locked` instala las versiones del `uv.lock` que viene con el starter.

```bash
uv sync --locked
uv run --locked python --version
```

**Comprueba** con `git status --short` que estás en el repositorio del equipo y que llegaron los archivos del starter. La terminal debe mostrar Python 3.12.

## Qué calcula el script

`explicar.py` conserva el preprocesamiento de Clase 10 y calcula SHAP sobre 60 viajes de validación. El bosque recibe la matriz transformada. Para presentar resultados en las cinco variables originales, el script agrupa las columnas de cada zona por viaje **antes** de promediar la magnitud de sus atribuciones. La gráfica *waterfall* muestra cómo se llega a una predicción desde el valor de referencia. [SHAP — Gráfica waterfall](https://shap.readthedocs.io/en/stable/generated/shap.plots.waterfall.html)

## Ejecutar y comprobar

**Desde el notebook.** Abre `explicabilidad.ipynb` en la raíz del repositorio del equipo. En VS Code, usa **Select Kernel → Python Environments** y elige el Python 3.12 de `.venv`. Ejecuta las celdas en orden. El kernel es el proceso Python que las ejecuta y determina qué bibliotecas están disponibles. Usa esta opción o los comandos de terminal de abajo.

**Desde la terminal**, ejecuta el script desde la raíz.

```bash
uv run --locked python explicar.py
```

**Comprobación.** La terminal lista cinco variables y muestra la misma duración, al redondear a dos decimales, para la estimación del pipeline y la suma reconstruida con SHAP. `resultados/` contiene `importancias.csv`, `importancias.png` y `explicacion-viaje.png`.

En el README, enlaza la tabla y las dos gráficas. Guarda en `evidencia/` una captura de la terminal con el comando y las dos estimaciones y enlázala desde el README. Identifica la variable de mayor importancia global en cada método y explica cuál aumentó o redujo más la estimación del viaje elegido. Los rankings pueden coincidir. En ese caso describe qué significa cada ranking y cómo difiere una contribución particular del patrón global. La explicación describe el comportamiento del modelo sobre la muestra, sin inferir que una variable causa el cambio real en la duración. Consulta la [consigna y rúbrica comunes](README.md).

**Qué explicar en el README.** ¿Por qué se agrupan las columnas de cada zona por viaje antes de obtener la magnitud promedio? Usa la gráfica individual para distinguir la atribución en minutos del ranking global.
