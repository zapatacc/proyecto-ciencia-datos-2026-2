# Tarea 2 — De funciones de viajes a una API local

## Propósito

Convertir las funciones de estimación y resumen de viajes desarrolladas en las actividades 1 y 2 en una API local mínima. Al terminar, podrás explicar cómo `pyproject.toml` y `uv.lock` permiten reconstruir un ambiente, y comprobar mediante solicitudes HTTP que FastAPI responde un contrato definido para consultar y estimar viajes.

## Recursos

- Notebook de la clase 3: ambientes virtuales y dependencias reproducibles con `uv`.
- Notebook de la clase 4: de HTTP a la primera aplicación FastAPI.
- [Flujo de trabajo y entrega de tareas](../flujo-tareas.md).
- [Plantilla de pull request](../plantillas/pull-request-tarea.md).

## Entregable

**Repositorio:** tu repositorio privado individual `pcd-entregas-2026`.

**Carpeta:** `tareas/tarea-02-api-ambiente-uv/`

**Rama obligatoria:** `feat/02-api-ambiente-uv`

Tu repositorio individual ya es un proyecto `uv`: la raíz contiene `pyproject.toml`, `uv.lock` y `.python-version`. No crees un proyecto `uv` anidado dentro de la carpeta de la tarea.

### 1. Dependencias y ambiente

1. Desde la raíz de `pcd-entregas-2026`, revisa `pyproject.toml`.
2. Agrega FastAPI con el extra estándar. Ese extra incluye la CLI `fastapi` y Uvicorn:

   ```bash
   uv add "fastapi[standard]"
   ```

3. Conserva en el pull request los cambios de `pyproject.toml` y `uv.lock` producidos por ese comando. No incluyas `.venv/`.
4. Sincroniza el ambiente desde el lockfile.

El resultado debe poder reconstruirse con:

```bash
uv sync --locked
```

### 2. Funciones de viajes y API

Crea una aplicación FastAPI en `tareas/tarea-02-api-ambiente-uv/`. Organiza el código como consideres más claro, pero `main.py` debe llamar a las funciones `estimar_duracion` y `resumir_viajes`; no copies sus fórmulas dentro de los endpoints.

Implementa o reutiliza estas funciones:

```python
def estimar_duracion(
    distancia_km: float, pasajeros: int, fin_de_semana: bool
) -> float:
    ...


def resumir_viajes(viajes: list[dict]) -> list[dict]:
    ...
```

`estimar_duracion` debe:

1. generar `ValueError` cuando `distancia_km` no sea positiva;
2. calcular una base de 4 minutos por kilómetro más 2 minutos fijos;
3. sumar 3 minutos cuando hay más de 2 pasajeros;
4. reducir el resultado 10 % cuando `fin_de_semana` es `True`;
5. devolver la duración redondeada a una cifra decimal.

`resumir_viajes` debe recibir una lista de diccionarios con `origen`, `destino`, `distancia_km`, `pasajeros` y `fin_de_semana`. Debe devolver una **lista nueva**, sin modificar la lista original, y agregar a cada resumen la clave `duracion_estimada_min`, calculada mediante `estimar_duracion`.

Usa una lista pequeña `VIAJES` con al menos los tres viajes de la actividad 2: `Centro → Chapultepec`, `ITESO → Centro` y `Tlaquepaque → Aeropuerto`.

La API debe tener estos endpoints:

| Solicitud | Respuesta esperada |
|---|---|
| `GET /` | JSON con una clave `mensaje` que identifique una API local de viajes. |
| `GET /api/v1/viajes` | JSON con la clave `viajes` y el resumen de los viajes de `VIAJES`, incluyendo la duración estimada de cada uno. |
| `GET /api/v1/duracion/{distancia_km}?pasajeros=1&fin_de_semana=false` | JSON con `distancia_km`, `pasajeros`, `fin_de_semana` y `duracion_estimada_min`. |

Requisitos del contrato:

- `distancia_km` es un parámetro de path de tipo `float`.
- `pasajeros` es un parámetro de query de tipo `int` y su valor predeterminado es `1`.
- `fin_de_semana` es un parámetro de query de tipo `bool` y su valor predeterminado es `False`.
- El endpoint de duración llama a `estimar_duracion`; el endpoint de viajes llama a `resumir_viajes`.
- Usa type hints y decoradores de FastAPI.
- Da a la aplicación un título claro y usa el prefijo `/api/v1/` para los endpoints de viajes.
- No agregues `POST`, modelos Pydantic, base de datos, autenticación, secretos ni paquetes adicionales: esos temas aún no forman parte del alcance evaluable.

### 3. README y verificación

Crea `tareas/tarea-02-api-ambiente-uv/README.md` que incluya:

1. qué problema resuelve la API y la diferencia entre cliente y servidor en este caso;
2. cómo cada endpoint reutiliza una de las funciones de viajes;
3. los comandos para sincronizar el ambiente, iniciar FastAPI y detenerlo con `Ctrl+C`;
4. una tabla que documente método, path, parámetros y ejemplo de respuesta de cada endpoint;
5. evidencia escrita de estas cinco pruebas, indicando cliente usado, URL solicitada, código HTTP observado y una breve interpretación:
   - `200` para `GET /`;
   - `200` para `GET /api/v1/viajes`;
   - `200` para `GET /api/v1/duracion/12.5?pasajeros=3&fin_de_semana=false`, con duración `55.0`;
   - `404` para una ruta que no existe;
   - `422` para `GET /api/v1/duracion/no-es-numero`, porque `distancia_km` no puede convertirse a `float`;
6. la URL local de `/docs` y una explicación breve de qué muestra.

Prueba la API con `curl -i`, `/docs` o Postman. Postman es recomendable para practicar el cliente visto en clase, pero no es obligatorio si no puedes instalarlo: registra el error y utiliza una de las otras dos alternativas.

Después de sincronizar desde la raíz, entra a la carpeta de la tarea e inicia FastAPI:

```bash
cd tareas/tarea-02-api-ambiente-uv
uv run fastapi dev
```

## Commits

Realiza al menos dos commits sustantivos. Ejemplos:

```text
chore(tarea-02): declara fastapi standard
feat(tarea-02): expone funciones de viajes
docs(tarea-02): documenta pruebas de la api
```

No hagas commits vacíos sólo para llegar al número solicitado.

## Pull request y cierre obligatorio

El pull request debe apuntar a `main`. Copia todo el contenido de la [plantilla del curso](../plantillas/pull-request-tarea.md) en **Write**, complétala y revisa el resultado en **Preview**.

Antes de entregar, revisa **Files changed**, realiza **Create a merge commit** y confirma que el pull request aparezca como **Merged** y cerrado. Cerrar sin hacer merge no cumple el requisito.

## Entrega en Canvas

- Entrega únicamente la URL del pull request cerrado y fusionado.
- **Fecha límite:** lunes 31 de agosto de 2026, 19:55, hora de Ciudad de México (antes del inicio de clase).

Canvas es el único medio oficial de entrega. La política de entregas tardías de la guía de aprendizaje se aplica por separado.

## Uso de herramientas y colaboración

Esta tarea es individual. No se permite usar IA generativa, autocompletado generativo ni agentes de programación para producir, corregir o explicar el código, el README o la evidencia de verificación. Sí puedes consultar los notebooks del curso, la documentación oficial de FastAPI y `uv`, mensajes de error, documentación de Python, y pedir ayuda al profesor.

## Rúbrica — 100 puntos

| Criterio | Logro completo | Logro parcial | Insuficiente | Máximo |
|---|---|---|---|---:|
| Ambiente reproducible con `uv` | **22–25:** ejecuta `uv add "fastapi[standard]"`, conserva los cambios resultantes en `pyproject.toml` y `uv.lock`, y `uv sync --locked` reconstruye el ambiente sin incluir `.venv/`. | **13–21:** el ambiente funciona, pero hay una inconsistencia menor en declaración, lockfile o evidencia. | **0–12:** falta la dependencia, el lockfile o la reconstrucción no es verificable. | 25 |
| Contrato e implementación de la API | **27–30:** implementa los tres endpoints con método, paths, prefijo, tipos, queries por defecto y JSON solicitados; los endpoints de viajes reutilizan las funciones indicadas. | **16–26:** la API inicia, pero falta o contradice una parte del contrato o de la reutilización. | **0–15:** la aplicación no inicia o no ofrece los endpoints requeridos. | 30 |
| Verificación, README y reutilización de actividades | **18–20:** el README permite repetir la ejecución, documenta cómo reutiliza las funciones de viajes y evidencia e interpreta los tres 200, 404, 422 y `/docs`. | **10–17:** hay evidencia, instrucciones o reutilización sólo de forma parcial. | **0–9:** faltan pruebas esenciales, documentación o reutilización de las funciones. | 20 |
| Historial de Git | **9–10:** usa la rama exacta y al menos dos commits sustantivos con mensajes claros y convencionales. | **5–8:** el historial existe, con un error menor de rama, separación o mensaje. | **0–4:** trabaja en `main`, no deja historial evaluable o fabrica commits vacíos. | 10 |
| Pull request y entrega | **13–15:** completa la plantilla, revisa el diff, fusiona a `main`, confirma el PR cerrado como Merged y entrega su URL en Canvas. | **7–12:** el trabajo llega a `main`, pero falta una evidencia o paso menor. | **0–6:** PR abierto, cerrado sin merge, dirigido a otra rama o sin entrega oficial. | 15 |
| **Total** |  |  |  | **100** |

## Aviso para la siguiente clase

El lunes 31 de agosto, a la hora de clase, habrá un quiz sobre APIs y ambientes virtuales. Repasa especialmente el propósito de un ambiente aislado, `pyproject.toml`, `uv.lock`, `uv add`, `uv sync --locked`, cliente y servidor, HTTP, URL, JSON, endpoints, recursos, parámetros de path y query, FastAPI, Uvicorn, ASGI, `/docs` y los códigos 200, 404 y 422.
