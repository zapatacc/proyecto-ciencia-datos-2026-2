# Módulo 3 — De local a producción

Este módulo conecta el sistema local de ML con contenedores, despliegue y operación.

| Clase | Material | Resultado |
|---|---|---|
| 17 | [Introducción a contenedores y Docker](clase-17-docker.ipynb) | Distinguir contexto y rutas; construir y ejecutar la API NYC Taxi, comprobar predicciones, observar caché y reconocer el propósito de Compose. |
| 18 | [Práctica Docker](clase-17-docker.ipynb) | Construcción y ejecución de API y frontend; diagnóstico de comunicación. |
| 19 | [Docker Network y Docker Compose](clase-19-compose.ipynb) | Conectar API y Streamlit con network host, conservar localhost y ejecutar la aplicación con Compose. |

Las fechas y los temas previstos se consultan en el [calendario](../docs/calendario-2026.md).
La práctica local utiliza los [recursos de API](../labs/starters/clase-16-docker/README.md);
el Dockerfile y `.dockerignore` se construyen siguiendo el notebook.
La Clase 19 continúa en `labs/trabajo-local/clase-16/`, con las carpetas `api/` y `ui/` ya construidas, y completa su `docker-compose.yaml`.
