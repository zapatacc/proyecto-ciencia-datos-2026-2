# Recursos visuales — Clase 9

Las ocho imágenes de esta carpeta provienen de la Clase 9 de la edición 2025
y se conservan para mantener la continuidad visual del curso. Fueron
contrastadas con la fuente bibliográfica de la sesión:

- Obra: [Three Levels of ML Software](https://ml-ops.org/content/three-levels-of-ml-software).
- Autoría del contenido: Larysa Visengeriyeva, Anja Kammer, Isabel Bär,
  Alexander Kniesz y Michael Plöd; diseño de Sebastian Eberstaller.
- Atribución solicitada por la fuente: INNOQ.
- Licencia declarada por la fuente:
  [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/).
- Verificación de fuente y licencia: 14 de septiembre de 2026.

## Inventario y procedencia

| Archivo local | Uso en la clase | Original enlazado por INNOQ | Nota de procedencia |
|---|---|---|---|
| `model-serving-pattern.png` | Comparar entrenamiento offline/online e inferencia batch/bajo demanda. | [ML workflows](https://ml-ops.org/img/model%20serving%20patterns.jpg) | INNOQ indica además una figura fuente de Quora. Se conserva para analizar sus ejes; el texto de clase corrige la clasificación de AutoML. |
| `model-serving-as-microservice.png` | Reconocer entrenamiento, artefacto, despliegue, API e inferencia. | [Web Service Pattern](https://ml-ops.org/img/model-serving-microservices.jpg) | La lectura de clase contrasta `GET /predict` con el contrato `POST` vigente y señala el riesgo de duplicar la extracción de features. |
| `online-learning.png` | Explicar entrenamiento incremental y su ciclo de evaluación. | [Online Learning ML System](https://ml-ops.org/img/Online%20learning.jpg) | INNOQ remite como figura fuente al libro de Aurélien Géron. |
| `model-as-a-service.png` | Mostrar un modelo servido por una API independiente. | [Model as Service Pattern](https://ml-ops.org/img/model-as-service.jpg) | INNOQ remite como figura fuente al libro de Aurélien Géron. |
| `model-as-a-dependency.png` | Mostrar el modelo empaquetado dentro de la aplicación. | [Model as Dependency](https://ml-ops.org/img/model-as-dependency.jpg) | Se conserva sin modificaciones. |
| `precompute.png` | Mostrar predicciones precalculadas y persistidas. | [Precompute Serving Pattern](https://ml-ops.org/img/precompute-serving-pattern.jpg) | Se conserva sin modificaciones. |
| `deploy-docker.png` | Anticipar el empaquetado del servicio en un contenedor. | [Docker infrastructure](https://ml-ops.org/img/infra-cloud.jpg) | Es un panorama; la implementación se estudia en clases posteriores. |
| `deploy-serverless.png` | Anticipar el despliegue como función administrada. | [Serverless infrastructure](https://ml-ops.org/img/infra-lambda.jpg) | Es un panorama; no prescribe un proveedor. |

Las copias locales no fueron modificadas. En el notebook se muestran
conservando su proporción y con texto alternativo. Cuando INNOQ identifica una
fuente visual previa, el notebook mantiene ese contexto y enlaza la página que
reúne la atribución completa.
