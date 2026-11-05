# Módulo 3 — De local a producción

Este módulo conecta el sistema local de ML con contenedores, despliegue y operación.

| Clase | Material | Resultado |
|---|---|---|
| 17 | [Introducción a contenedores y Docker](clase-17-docker.ipynb) | Distinguir contexto y rutas; construir y ejecutar la API NYC Taxi, comprobar predicciones, observar caché y reconocer el propósito de Compose. |
| 18 | [Práctica Docker](clase-17-docker.ipynb) | Construcción y ejecución de API y frontend; diagnóstico de comunicación. |
| 19 | [Docker Network y Docker Compose](clase-19-compose.ipynb) | Conectar API y Streamlit con network host, conservar localhost y ejecutar la aplicación con Compose. |
| 20 | [Despliegue en AWS con EC2 y Docker Compose](clase-20-aws-ec2-compose.ipynb) | Ejecutar API y Streamlit en Ubuntu, comprobar una predicción remota y detener la instancia. |
| 21 | [Asesoría de la Tarea 8](clase-21-asesoria-proyecto.ipynb) | Trabajar en la tercera entrega: correcciones, integración, contenedores y despliegue del equipo. |

Las fechas y los temas previstos se consultan en el [calendario](../docs/calendario-2026.md).
La práctica local utiliza los [recursos de API](../labs/starters/clase-16-docker/README.md);
el Dockerfile y `.dockerignore` se construyen siguiendo el notebook.
La Clase 19 continúa en `labs/trabajo-local/clase-16/`, con las carpetas `api/` y `ui/` ya construidas, y completa su `docker-compose.yaml`.

La práctica de Clase 20 es individual. Reutiliza la aplicación de
`labs/trabajo-local/clase-16/`: guarda API, UI y Compose en
`pcd-entregas-2026/actividades/clase-20-ec2/`, clona el repositorio en EC2 y crea
allí el `.env` desde `.env.example`. Cada estudiante utiliza su propia instancia.

Después del laboratorio de AWS, las sesiones se concentran en el examen final y el cierre del proyecto. Los temas complementarios de nube, automatización, monitoreo y operación son de enriquecimiento; sus herramientas no se añaden a los requisitos de evaluación. Consulta el calendario y las instrucciones oficiales en Canvas.

La asesoría de Clase 21 cuenta como tarea por el trabajo activo, sin entregable adicional. La [Tarea 8 — Tercera entrega del proyecto](../docs/tareas/tarea-08-tercera-entrega-proyecto.md) define el recorrido hasta AWS: una instancia existente de un integrante por equipo.
