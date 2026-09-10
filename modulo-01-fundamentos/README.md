# Módulo 1 — Fundamentos

El módulo conecta las herramientas de trabajo, el control de cambios y los ambientes reproducibles con una API local de predicción. Al final, cada equipo inicia su propio proyecto con estas bases.

| Clase | Qué construimos o aprendimos |
|---|---|
| [1 — Bienvenida y verificación técnica](clase-01-bienvenida.ipynb) | Conocimos el recorrido del curso, preparamos las herramientas y ejecutamos un primer archivo Python. |
| [2 — Python, terminal y Git/GitHub](clase-02-python-vscode.ipynb) | Practicamos rutas y funciones de Python; compartimos cambios mediante ramas, commits y un PR revisado y fusionado. |
| [3 — Ambientes y dependencias con uv](clase-03-ambientes-uv.ipynb) | Aislamos bibliotecas y reconstruimos el ambiente a partir de la versión de Python, `pyproject.toml` y `uv.lock`. |
| [4 — HTTP y primera aplicación FastAPI](clase-04-api-fastapi.ipynb) | Interpretamos solicitudes y respuestas HTTP; construimos y probamos endpoints `GET`. |
| [5 — Entradas validadas con Pydantic](clase-05-validacion-fastapi.ipynb) | Definimos las entradas de una predicción y validamos cuerpos JSON mediante `POST` y modelos Pydantic. |
| [6 — De viajes observados a una API de predicción](clase-06-api-prediccion.ipynb) | Exploramos Green Taxi, preparamos variables, entrenamos y evaluamos un modelo, y cargamos su artefacto desde una API. |
| [7 — Inicio del proyecto en equipo](clase-07-integracion.ipynb) | Creamos el repositorio privado, documentamos la selección de datos y la propuesta inicial, y revisamos y fusionamos el primer PR. |

Estas piezas se conectan en el [Módulo 2 — Ciclo MLOps](../modulo-02-ciclo-mlops/README.md): identificar qué código, datos y modelo producen un resultado, reproducirlo y mantenerlo cuando cambian las condiciones del proyecto.
