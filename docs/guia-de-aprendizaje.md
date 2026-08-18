# Guía de aprendizaje — Proyecto en Ciencia de Datos

**Edición:** Otoño 2026  
**Uso:** documento de orientación para estudiantes

Esta guía presenta el propósito, las competencias, el recorrido, las evidencias y las referencias del curso. Se socializa en la primera clase y se consulta durante el semestre.

## 1. Identificación del Proyecto Formativo

| Campo | Información |
|---|---|
| Asignatura | Proyecto en Ciencia de Datos |
| Programa | Licenciatura en Ciencia de Datos |
| Código | MAF3660Q |
| Créditos | 6 |
| Modalidad | Presencial |
| Idioma | Español, con lectura técnica en inglés |
| Horas con docente | 64 horas programadas |
| Aprendizaje autónomo | 32 horas estimadas |
| Profesor | Cristian Camilo Zapata Zuluaga |
| Correo institucional | cristianz@iteso.mx |
| Horario | Lunes y miércoles, 20:00–22:00; trabajo efectivo 20:10–21:50 |
| Salón | T-105 |
| Asesorías | Dudas por Microsoft Teams o correo; las sesiones se agendan cuando sean necesarias |

### Problema del contexto

En ciencia de datos no basta con desarrollar y evaluar un modelo. Para que una solución genere valor, otras personas o sistemas deben poder ejecutarla, consumir sus resultados y saber qué versión está en uso. El sistema también debe permitir detectar fallas, actualizarse y regresar a una versión anterior cuando sea necesario.

El curso aborda el paso desde una solución analítica hasta una aplicación operable. El énfasis está en integrar prácticas de desarrollo de software, trazabilidad, servicios, contenedores y despliegue, no en realizar una competencia extensa de modelado.

### Descripción de la asignatura

El estudiantado construirá progresivamente un recorrido técnico alrededor de un mismo caso conductor: **NYC Taxi**. El caso evolucionará desde una función Python hasta una aplicación desplegada, pasando por API, tracking, registro del modelo, interfaz, contenedores y operación básica.

Las plataformas cumplen funciones distintas:

- **Databricks:** tracking remoto y Model Registry.
- **Hugging Face Spaces:** publicación accesible de una aplicación Streamlit mediante Docker.
- **AWS:** introducción guiada a infraestructura, red, credenciales, logs, costos y eliminación de recursos.

## 2. Asignaturas con las que se relaciona

| Relación | Asignatura | Competencia relacionada |
|---|---|---|
| Antes | Programación para Análisis de Datos | Manejo básico o intermedio de Python y estructuras de datos. |
| Antes | Proyecto de Ingeniería de Datos | Bases de datos, preparación de datos y fundamentos de Git. |
| Durante | Aprendizaje Máquina | Entrenamiento y evaluación de modelos de machine learning. |

El curso recupera estos conocimientos cuando son necesarios, pero su propósito central es llevarlos a un sistema compartible y operable.

## 3. Competencias a desarrollar

### Competencia 1 — Construir y compartir aplicaciones de datos

Usar Python, VS Code, terminal, Git, GitHub y ambientes aislados; comprender HTTP y JSON; exponer localmente una primera predicción mediante FastAPI.

### Competencia 2 — Diseñar y trazar el ciclo de un sistema de ML

Relacionar datos, modelo y código; comparar patrones de despliegue; diseñar una solución realizable; rastrear experimentos y gestionar versiones mediante MLflow y Databricks.

### Competencia 3 — Empacar, desplegar y operar una aplicación

Crear imágenes y contenedores, conectar API e interfaz con Compose, publicar una aplicación, comprender responsabilidades básicas de nube y realizar una actualización o rollback con evidencia.

## 4. Competencias a través del Proyecto Formativo

Cada clase relacionará cuatro elementos:

- **Objetivo:** lo que el estudiantado podrá explicar o realizar.
- **TBCD:** trabajo bajo conducción docente, como demostraciones, prácticas guiadas, debugging y revisión.
- **TIE:** trabajo independiente del estudiante, como preparación, adaptación o documentación.
- **Evidencia:** resultado observable, por ejemplo un archivo, comando, commit, URL, explicación o demostración.

| Módulo | Encuentros efectivos | Resultado acumulativo |
|---|---:|---|
| 1. Fundamentos | 7 | Una predicción expuesta localmente mediante FastAPI. |
| 2. Ciclo MLOps | 11 | Un modelo rastreado, versionado y consumido por API e interfaz. |
| 3. Producción | 11 | Una aplicación contenida, conectada, publicada y operada de forma básica. |

### Temas opcionales

Si el tiempo y el avance del grupo lo permiten, se podrán explorar pruebas automatizadas, CI/CD, observabilidad y monitoreo, Prefect, seguridad de contenedores, fundamentos de Kubernetes, nube avanzada y continuous training. Si no se desarrollan en clase, se compartirán materiales y bibliografía para consulta y autoaprendizaje; no serán requisito de evaluación.

## 5. Evaluación del curso

| Evidencia | Porcentaje |
|---|---:|
| Tareas y actividades de clase | 20 % |
| Quices | 20 % |
| Proyecto en equipo | 30 % |
| Examen final | 30 % |
| **Total** | **100 %** |

El proyecto se divide en reporte (15 %) y exposición (15 %). Los equipos serán de dos personas, con un máximo de tres integrantes.

### Calificación final

Una calificación con decimal menor o igual a 5 se redondeará al entero inferior; por ejemplo, 8.5 será 8. Cuando el decimal sea mayor que 5, se redondeará al entero superior; por ejemplo, 8.6 será 9. Este procedimiento no aplica cuando la calificación es menor a 6: 5.9 será 5.

### Entregas

Todas las tareas, trabajos, actividades, quices, exámenes y entregas del proyecto se realizan exclusivamente en el espacio correspondiente de Canvas. No se aceptan entregas por correo, Teams, mensajes privados u otros medios.

- Una hora o menos de retraso: calificación máxima de 8.
- Más de una hora y hasta dos horas: calificación máxima de 7.
- Dos horas o más: se revisa y devuelve con correcciones, pero no recibe calificación.

## 6. Bibliografía y referencias

### Bibliografía de apoyo

- Chip Huyen, [*Designing Machine Learning Systems*](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/).
- Aurélien Géron, [*Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*, 3.ª ed.](https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/).
- Luciano Ramalho, [*Fluent Python*, 2.ª ed.](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/).
- John M. Stewart y Michael Mommert, [*Python for Scientists*, 3.ª ed.](https://www.cambridge.org/core/books/python-for-scientists/F3921BF92798B4EE46A9E904741EFB91).
- Noah Gift y Alfredo Deza, [*Practical MLOps*](https://www.oreilly.com/library/view/practical-mlops/9781098103002/).
- Mark Treveil et al., [*Introducing MLOps*](https://www.oreilly.com/library/view/introducing-mlops/9781492083283/).
- Emmanuel Ameisen, [*Building Machine Learning Powered Applications*](https://www.oreilly.com/library/view/building-machine-learning/9781492045106/).

Ninguno de estos libros se considera obligatorio en su totalidad. Las lecturas específicas se indicarán por clase.

### Documentación técnica

Los procedimientos evaluados se basarán primero en documentación oficial de Python, Git, FastAPI, MLflow, Databricks, Docker, Hugging Face y AWS. Los enlaces concretos aparecerán en el material de cada sesión.

## Cómo usar esta guía

Al comenzar cada módulo, vuelve a las competencias y al resultado acumulativo. Antes de una entrega, identifica la evidencia esperada y consulta el espacio correspondiente en Canvas. Si esta guía y Canvas parecieran contradecirse, registra la diferencia y consulta al profesor; no asumas silenciosamente cuál versión aplica.
