# Tarea 8 — Tercera entrega del proyecto: aplicación desplegada en AWS

## 🎯 Propósito

Completar el proyecto desde los datos hasta una predicción accesible en AWS. Es la **última entrega parcial antes de la entrega final**: corrijan las observaciones anteriores, completen lo pendiente e integren la aplicación que ya desarrollaron.

## Entregable y fecha

- **Trabajo:** en equipo, en el repositorio privado existente del proyecto.
- **Rama:** `feat/tercera-entrega`, creada desde `main` actualizado.
- **Límite:** miércoles **18 de noviembre de 2026, 19:55**, hora de Ciudad de México.
- **Canvas:** cada integrante entrega la misma URL del PR hacia `main`, revisado, **Merged** y cerrado.

**Esta tarea es el trabajo de la asesoría de Clase 21.** Comiencen durante la sesión por corregir las observaciones anteriores y continúen con los componentes pendientes de esta consigna. Todo el avance se incorpora al mismo proyecto y PR de esta entrega. El profesor registra la participación individual durante la asesoría, sin pedir otro envío.

No creen otro repositorio ni una carpeta de tarea con una copia del proyecto.

## 📚 Recursos

- [Guía del proyecto](../../project/README.md).
- [Tarea 7 — Segunda entrega](tarea-07-segunda-entrega-proyecto.md).
- [Clase 17 — Docker](../../modulo-03-produccion/clase-17-docker.ipynb).
- [Clase 19 — Red host y Compose](../../modulo-03-produccion/clase-19-compose.ipynb).
- [Clase 20 — EC2](../../modulo-03-produccion/clase-20-aws-ec2-compose.ipynb).
- [Clase 21 — Asesoría](../../modulo-03-produccion/clase-21-asesoria-proyecto.ipynb).

## 1. Correcciones y continuidad

Consulten comentarios y rúbricas de entregas anteriores en Canvas. Corrijan directamente informe, notebooks, código, mapa del sistema y README; ejecuten las comprobaciones afectadas y actualicen la interpretación de resultados. **No se pide una bitácora ni un documento adicional de correcciones.**

Conserven completos y coherentes los requisitos de la Tarea 7:

- Tres familias con HPO, comparación justificada y evaluación final separada del tuning.
- MLflow remoto en un único workspace de Databricks, tres versiones trazables y alias `champion`.
- Flow de Prefect que coordina preparación, búsqueda, ajuste, evaluación y registro.
- FastAPI que carga el modelo seleccionado, valida entradas y comunica la versión; Streamlit que consulta la API por HTTP.

Mantengan los nombres de experimentos, runs y modelos definidos en la Tarea 7. No se piden familias adicionales ni repetir HPO correcto sólo para producir actividad nueva. Si una corrección cambia datos, preprocesamiento o evaluación, regeneren los resultados/modelos afectados y documenten la nueva versión. Entrenamiento e inferencia deben conservar el mismo procesamiento; la API no reentrena por petición.

## 2. 🛠️ Completar los contenedores y Compose

Creen imágenes separadas para API y frontend, con Python 3.12 y dependencias consistentes con `pyproject.toml`/`uv.lock`. Usen archivos llamados **`Dockerfile`**; pueden ubicarlos junto al código en `src/api/` y `src/frontend/`. Si exportan requisitos, genérenlos desde el lock, sin mantener otra lista manual.

El archivo Compose de la raíz debe levantar ambos servicios. Sigan el recorrido enseñado de **red host**, explicando qué significa `localhost` en ese contexto. Los servicios pueden llamarse `api` y `ui`; la carpeta del frontend sigue siendo `src/frontend/`. Documenten contextos de construcción, nombres de imágenes/contenedores, comandos, direcciones y puertos configurados externamente. Para NYC Taxi conserven los nombres utilizados en las prácticas; para otro proyecto usen un identificador propio y consistente.

Mantengan secretos fuera de Git y de las imágenes. Versionen `.env.example` con valores ficticios y usen `.dockerignore` para excluir secretos, ambientes y archivos innecesarios. La interfaz no necesita credenciales del modelo.

**Comprobación local:** construir las imágenes, levantar ambos servicios, obtener una predicción desde Streamlit y detener únicamente los contenedores de este proyecto. El README debe indicar los comandos exactos y cómo reconocer que la API ya cargó el modelo.

## 3. ☁️ Desplegar en la instancia de un integrante

**Usen una sola EC2 ya asignada a alguno de los integrantes**, en `us-east-1`; no creen una instancia por persona ni una nueva sólo para esta entrega. Acuerden quién administra esa instancia y quién realiza la ejecución remota. Puede ser una persona distinta de quien administra Databricks. Todos deben comprender y poder explicar el despliegue.

El integrante responsable utiliza sus propios accesos. No compartan llaves privadas, contraseñas, tokens ni `.env`. Si necesita recuperar el modelo desde el workspace de otra persona, acuerden una transferencia privada de un artefacto propio y confiable, con versión/procedencia documentadas; no compartan credenciales ni lo suban a Git. La predicción desplegada debe corresponder al modelo evaluado y registrado.

Recorrido esperado, adaptando el laboratorio EC2:

1. Verificar instancia, región, capacidad disponible y servicios propios existentes. Usar carpetas y nombres que distingan proyecto, laboratorio y examen; no sobrescribirlos ni borrar recursos para liberar espacio sin revisión.
2. Obtener desde Git el repositorio privado y seleccionar `feat/tercera-entrega` para probar el trabajo antes del merge. La configuración sensible se crea fuera de Git; la autenticación debe ser temporal y limitada al repositorio necesario, sin token en URL o historial.
3. Construir y arrancar API/frontend con Compose. Mantener la administración y la API limitadas a los accesos necesarios; permitir acceso remoto al frontend según las reglas autorizadas.
4. Obtener una predicción desde otra computadora y comprobar la versión del modelo. Documentar qué entrada produjo qué salida.
5. Consultar logs para comprobar carga/peticiones y diagnosticar un error si aparece. Detener los servicios y la instancia al finalizar las comprobaciones; explicar los recursos que todavía generan costo.

> **SSH y cambio de IP:** si cambia la IP pública de la computadora desde la que administran EC2, actualicen el origen de la regla SSH (TCP 22) del grupo de seguridad a su IP actual —**My IP**—. No abran SSH a todo Internet. Comprueben también la dirección pública actual de EC2 antes de conectarse. [Referencia AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/changing-security-group.html).

No necesitan mantener la instancia encendida permanentemente ni contratar servicios o aportar una tarjeta personal. El README debe permitir repetir el arranque y la comprobación. Si hay un bloqueo de acceso o recursos, comuníquenlo al profesor con el error y las comprobaciones realizadas; no sustituyan sin acuerdo el despliegue por una captura local.

## 4. Informe, notebooks y reproducción

Continúen la estructura de la Tarea 7. Además de corregir los cuadernos existentes, desarrollen:

| Archivo | Contenido |
|---|---|
| `notebooks/08-contenedores.ipynb` | Imágenes, Dockerfiles, contexto, configuración, red host, Compose, ejecución local y comprobaciones interpretadas. |
| `notebooks/09-despliegue.ipynb` | Instancia utilizada sin identificadores sensibles, pasos reproducibles, configuración de acceso, despliegue, versión servida, predicción remota, logs, costos y cierre. |
| `informe/informe-final.ipynb` | Síntesis end to end: correcciones incorporadas, decisiones, resultados relevantes, arquitectura actual, despliegue y limitaciones; enlaces al detalle técnico. |
| `README.md` | Datos, ambiente, configuración externa, entrenamiento, API/UI, Compose, despliegue, verificación y cierre, con comandos y salidas esperadas. |
| `docs/mapa-sistema-ml.md` | Sistema actualizado, distinguiendo computadora local, Databricks y EC2, sus componentes y conexiones. |

Los notebooks técnicos documentan procedimiento, resultados e interpretación; el código reutilizable permanece en `src/`. No es necesario arrancar servidores ni aprovisionar recursos al ejecutar un notebook. El informe debe comprenderse por sí solo, sin copiar todos los trials o el código de cada componente.

No se solicitan todavía `10-operacion.ipynb`, CI/CD, monitoreo avanzado ni actualización/rollback: esos temas complementarios no se añaden a esta entrega. La entrega final y su presentación tendrán sus propias instrucciones.

## 5. ✅ Verificación y capturas

Guarden **una imagen por cada caso requerido** en `evidencia/`, enlazada desde el informe o README y acompañada de una interpretación breve. Las imágenes deben mostrar herramienta/comando, acción o solicitud y resultado. Para HTTP usen Postman, `/docs` o `curl` y muestren solicitud, respuesta y estado.

| Caso | Resultado observable |
|---|---|
| Recorrido previo corregido | Evidencias vigentes de tres búsquedas HPO, comparación, tres versiones/`champion`, flow Prefect y API/frontend, según los casos de la Tarea 7. Pueden conservar imágenes anteriores que sigan correspondiendo a la implementación; actualicen las afectadas por correcciones. |
| Ambiente y builds | Reconstrucción con `uv sync --locked` y construcción exitosa de ambas imágenes. |
| Integración local | Estado de ambos servicios y una predicción desde el frontend en contenedores. |
| Instancia y red | Estado de EC2 y reglas necesarias para SSH/frontend, con datos sensibles ocultos. |
| Despliegue | Comando/estado de los servicios ejecutados en EC2. |
| Predicción remota | Formulario, entrada y resultado desde otra computadora; relación con respuesta/log de API y versión concreta servida. |
| Entrada inválida en EC2 | Solicitud y respuesta de validación desde el servidor, sin exponer públicamente la API; puede comprobarse por terminal SSH. |
| Logs | Salida que permita relacionar el arranque o la petición con su resultado, sin secretos. |
| Cierre | Servicios detenidos y estado de instancia detenido; recursos conservados/costos residuales explicados. No terminen la instancia reutilizada sólo por entregar. |

Oculten correo, avatar, URL personal del workspace, cuentas, IP y credenciales. Conserven visibles los nombres del experimento/modelo, métricas, versiones, estados y reglas necesarias para comprender lo comprobado. Una captura de código no sustituye una ejecución. No inventen resultados para un componente que siga fallando.

## Commits, PR y entrega en Canvas

Desde `main` actualizado, creen `feat/tercera-entrega`. Si hay cambios o PR pendientes, inspeccionen `git status` y coordinen su integración antes de cambiar de rama; no eliminen trabajo previo.

Realicen commits sustantivos con Conventional Commits, por ejemplo `fix(proyecto): corrige evaluacion` o `feat(proyecto): despliega aplicacion en ec2`. No hay un mínimo artificial. Revisen diff y staging, excluyendo datos, modelos, ambientes y secretos.

El PR apunta a `main`. Copien la [plantilla del curso](../plantillas/pull-request-tarea.md) en **Write**, complétenla y revisen **Preview**. Identifiquen contribuciones, responsable de Databricks y responsable del despliegue. Soliciten revisión entre integrantes, comprueben **Files changed** y fusionen con **Create a merge commit**.

Publiquen `feat/tercera-entrega` para probarla en EC2 y guarden las evidencias en esa misma rama antes de fusionar. Después del merge, cambien la copia de EC2 a `main`, actualícenla y comprueben que conserva la versión y predicción demostradas. Si cambió código, configuración o modelo, repitan los casos afectados. Así el PR incluye código y evidencia y el estado final coincide con la aplicación comprobada. El PR debe quedar **Merged** y cerrado; cada integrante pega su URL en Canvas antes del límite. No se aceptan entregas por correo, Teams o mensajes privados.

## Herramientas y colaboración

Trabajo en equipo con revisión cruzada. Pueden utilizar material del curso, documentación e IA como apoyo; verifiquen propuestas, citen fuentes y expliquen decisiones/código/resultados. Mantengan la política de colaboración de la Tarea 7. El permiso del examen para elegir otras herramientas no modifica automáticamente los requisitos del proyecto.

## Rúbrica — 100 puntos

| Criterio | Logro completo | Logro parcial | Insuficiente | Máximo |
|---|---|---|---|---:|
| Correcciones y continuidad del recorrido | **18–20:** atiende comentarios y conserva datos/evaluación sin fuga, tres familias con HPO, Prefect, tracking remoto y tres versiones trazables. | **10–17:** hay avances verificables, pero alguna corrección o conexión sigue incompleta. | **0–9:** faltan componentes previos o persisten errores que invalidan resultados. | 20 |
| API y frontend integrados | **13–15:** predicción real por HTTP, entradas validadas, mismo procesamiento y versión identificable; coherencia local/remota. | **7–12:** funciona parcialmente o falta validación/versión/paridad. | **0–6:** no hay recorrido verificable o se simulan resultados. | 15 |
| Docker y Compose | **18–20:** imágenes separadas, dependencias coherentes, configuración segura y arranque/comunicación/cierre reproducibles. | **10–17:** ejecución parcial o instrucciones/configuración insuficientes. | **0–9:** no construye o no conecta los componentes. | 20 |
| Despliegue EC2 | **18–20:** instancia existente de un integrante, acceso limitado, aplicación remota verificable, versión trazable, logs y cierre comprobado. | **10–17:** despliegue parcial o evidencia de acceso/versión/cierre incompleta. | **0–9:** sólo ejecución local o sin predicción remota verificable. | 20 |
| Informe, notebooks y evidencias | **13–15:** síntesis interpretada, detalle en 08/09, mapa actualizado y capturas de todos los casos coherentes con lo entregado. | **7–12:** faltan interpretación, enlaces o algunas comprobaciones. | **0–6:** documentación o evidencia no permite comprender/verificar el sistema. | 15 |
| Reproducción, colaboración y entrega | **9–10:** README/lock/configuración permiten repetir, contribuciones claras y PR revisado/Merged entregado correctamente. | **5–8:** omisiones menores de reproducción o flujo de entrega. | **0–4:** no se reproduce, no hay integración verificable o falta PR/entrega. | 10 |
| **Total** | | | | **100** |

La política de retrasos se aplica por separado según la [guía de aprendizaje](../guia-de-aprendizaje/README.md).
