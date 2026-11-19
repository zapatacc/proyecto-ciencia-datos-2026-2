# Laboratorio 2 — Integración continua de la API

## Resultado esperado

Configurar GitHub Actions para verificar el contrato de la API cuando se abre o actualiza un pull request hacia `main`. El resultado incluye una ejecución donde una comprobación detecta una regresión y otra que pasa al corregirla.

La **integración continua** ejecuta comprobaciones automáticamente cuando cambia el código. En GitHub Actions, un **workflow** define cuándo se ejecutan y los pasos que debe completar. El **runner** es una computadora que ejecuta esos pasos. Este workflow prueba la API real a través de HTTP, igual que un cliente del servicio: un viaje válido recibe `200` y un viaje con un valor fuera del rango recibe `422`. También comprueba campos de la respuesta que otros clientes necesitan para interpretar una predicción.

## Preparar el proyecto

Actualiza el repositorio público del curso mediante `git status` y `git pull` desde `main`. Crea y clona el repositorio nuevo y privado siguiendo la [consigna común](README.md). Desde la raíz del clon del equipo, ejecuta `git switch -c feat/integracion-continua` para abrir la rama de trabajo.

1. Copia el contenido del [starter de este laboratorio](../../../labs/starters/clase-24-laboratorios-mlops/02-integracion-continua) a la raíz del repositorio del equipo. Conserva las carpetas y los archivos ocultos. La [consigna común](README.md#copiar-los-archivos-del-laboratorio) incluye el comando de copia.
2. Copia `modelos.py` y `preparar_datos.py` del [starter de Clase 10](../../../labs/starters/clase-10-experiment-tracking/README.md) a la raíz. Copia `green-taxi-train.csv` de la Clase 10 a `datos/`. El runner necesita esa muestra versionada para entrenar.
3. Prepara el ambiente desde el repositorio del equipo. `uv sync --locked` instala las versiones del `uv.lock` que viene con el starter.

```bash
uv sync --locked
uv run --locked python --version
```

**Comprueba** con `git status --short` que estás en el repositorio del equipo y que llegaron los archivos del starter. La terminal debe mostrar Python 3.12.

## Probar antes de automatizar

`verificar_api.py` espera que la API esté lista, comprueba el contrato de una predicción válida y verifica que cero pasajeros produzca un rechazo. El código de salida es `0` si pasan las comprobaciones y es distinto de cero si falla alguna.

Primero comprueba el recorrido en dos terminales, ambas situadas en la raíz de tu repositorio. En la primera, inicia la API con regresión lineal en el puerto indicado. En la segunda, señala al script de verificación la dirección base del servidor.

```bash
uv run --locked python api_local.py --modelo linear_regression --puerto 8000
```

```bash
uv run --locked python verificar_api.py --url http://127.0.0.1:8000
```

**Comprueba** que aparecen mensajes `OK` para el viaje válido, los metadatos y el rechazo del viaje inválido. Si el proceso no responde, revisa la terminal de la API y confirma que los dos comandos usan el mismo puerto. Detén el servidor local con **Ctrl+C** cuando termines.

## Automatizar en GitHub Actions

Desde la raíz de tu repositorio, mueve la plantilla a la ubicación donde GitHub descubre los workflows.

```bash
mkdir -p .github/workflows
mv configuracion/ci.yaml .github/workflows/ci.yaml
git status --short
```

**Convención de GitHub Actions.** Los workflows son archivos `.yml` o `.yaml` en `.github/workflows/`, dentro de la raíz del repositorio. El archivo se registra en Git y se publica con la rama. El punto inicial puede ocultar la carpeta en el explorador. La indentación de YAML indica qué pasos pertenecen a cada trabajo. [GitHub — Sintaxis de workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#about-yaml-syntax-for-workflows)

Abre `.github/workflows/ci.yaml`. `on: pull_request` ejecuta la verificación cuando se abre o actualiza un PR dirigido a `main`. `permissions: contents: read` permite que el runner lea el repositorio. El runner instala el ambiente, inicia la API en segundo plano y termina ese proceso al salir del paso. El log de la API aparece si falla la comprobación.

**Comprueba** que la ruta y la indentación son exactas, y que `datos/green-taxi-train.csv` y `uv.lock` forman parte del commit. En el repositorio puedes revisar si **Settings → Actions → General** permite los workflows y las acciones que acabas de declarar. Si la ejecución aparece bloqueada, conserva la salida de la comprobación local y registra la restricción observada. Esa salida permite evaluar el avance local de la práctica.

## Provocar y corregir una regresión

1. Publica la versión válida en tu rama de trabajo y abre un PR a `main`. Consulta **Checks** en el PR o **Actions** en el repositorio y verifica que el job pasó.
2. En esa misma rama cambia únicamente `alias="sin-alias"` por `alias="alias-regresion"` en `api_local.py`. Haz un commit y publica la rama. Conserva el enlace del run fallido y localiza el mensaje `FALLÓ: alias local correcto`.
3. Restaura el valor de `alias`, confirma el cambio y publica la rama. Conserva el enlace del run exitoso. Revisa el PR y fusiónalo a `main` después de la comprobación.

Si la instalación del runner falla, localiza el paso exacto antes de atribuir el problema a la API. Si falla el caso inválido, revisa su estado HTTP y el detalle de validación. Si desaparece el job, revisa la ruta del YAML, el destino del PR y los permisos de Actions del repositorio.

## Evidencia y cierre

Guarda en `evidencia/` una captura del job fallido con el mensaje de la comprobación y otra del job exitoso. Enlaza ambas capturas y los dos runs en el README. Explica qué contrato cambió, cómo lo detectó el job y cómo reproducir la verificación en local. Revisa la [entrega y rúbrica](README.md).

**Qué explicar en el README.** ¿Dónde busca GitHub el workflow, qué evento activa este archivo y cómo se convierte el fallo local del script en un check fallido del PR?

## Referencias

- [Eventos que activan workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#pull_request).
- [Usar uv en GitHub Actions](https://docs.astral.sh/uv/guides/integration/github/).
- [Validación de campos en FastAPI](https://fastapi.tiangolo.com/tutorial/body-fields/).
