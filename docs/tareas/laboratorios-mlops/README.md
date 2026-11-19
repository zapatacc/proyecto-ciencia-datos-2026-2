# Laboratorios de MLOps — Trabajo por equipo

El servicio de Green Taxi estima la duración de un viaje a partir de cinco características. Cada equipo incorpora una capacidad para verificar, publicar, medir o explicar ese servicio y documenta cómo comprobarla.

## Elijan la guía de su equipo

| Laboratorio | Resultado esperado | Forma de ejecución |
|---|---|---|
| [1. Rendimiento de la API](01-rendimiento-api.md) | Comparar el error y la latencia de dos modelos que atienden solicitudes individuales. | Scripts desde la terminal. |
| [2. Integración continua](02-integracion-continua.md) | Ejecutar comprobaciones automáticas de la API al abrir o actualizar un PR. | Terminal y workflow de GitHub Actions. |
| [3. Despliegue continuo en EC2](03-despliegue-continuo.md) | Desplegar una revisión desde GitHub Actions, comprobarla y recuperar la revisión anterior. | GitHub Actions, SSH y Docker Compose. |
| [4. Drift y reentrenamiento](04-drift-reentrenamiento.md) | Detectar cambios en las entradas y evaluar un candidato cuando el flujo active el entrenamiento. | Terminal o [notebook de drift](../../../labs/starters/clase-24-laboratorios-mlops/04-drift-reentrenamiento/drift.ipynb). |
| [5. Explicabilidad con SHAP](05-explicabilidad-shap.md) | Comparar la importancia global de las variables y explicar una predicción. | Terminal o [notebook de explicabilidad](../../../labs/starters/clase-24-laboratorios-mlops/05-explicabilidad-shap/explicabilidad.ipynb). |

Cada guía incluye su preparación y comprobaciones. Consulten el [notebook de la clase](../../../modulo-03-produccion/clase-24-laboratorios-mlops.ipynb) para relacionar el laboratorio con el sistema que construyeron en el curso.

## Qué preparar

1. Un integrante crea **un repositorio nuevo y privado en GitHub para todo el equipo**, exclusivo de este laboratorio. Inicialícenlo con un README en la rama `main`. El repositorio del curso se usa como fuente de materiales, y el repositorio del proyecto final se usa para el proyecto.
2. La persona que creó el repositorio abre **Settings → Collaborators → Add people** e invita por su usuario de GitHub a **todos los demás integrantes del equipo y al profesor (`zapatacc`)**. Cada integrante acepta la invitación con su propia cuenta. Antes de entregar, comprueben en **Collaborators** que las invitaciones fueron aceptadas y que el profesor tiene acceso. [GitHub — Invitar colaboradores a un repositorio personal](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/inviting-collaborators-to-a-personal-repository)
3. Sigan la guía asignada y copien el starter correspondiente. Los scripts y la configuración de partida ya están escritos. El equipo prepara su ambiente, configura los accesos que requiere su laboratorio y ejecuta las comprobaciones. Mantengan las llaves y los tokens fuera de Git.
4. En `README.md`, expliquen qué hace el laboratorio, cómo preparar el ambiente, cómo ejecutarlo y cómo verificar el resultado. Respondan brevemente la pregunta **Qué explicar en el README** de su guía con evidencia de su ejecución. Incluyan los pasos de cierre cuando apliquen.
5. Guarden una captura por cada comprobación que pide su guía en `evidencia/`. Cada imagen debe mostrar la acción o comando y el resultado observable. Enlacen las capturas desde el README y oculten credenciales, direcciones e identificadores sensibles.
6. Integren el trabajo a `main`. Verifiquen que el README y sus enlaces abren desde GitHub.

Pueden consultar documentación y utilizar asistentes de IA. Comprueben que las sugerencias funcionan en su laboratorio. Dentro del equipo pueden repartirse la configuración, la ejecución y la preparación de evidencias. Cada equipo genera sus propios resultados.

**Extensiones opcionales.** Si una pregunta del laboratorio les da una idea, pueden investigarla y sumar una mejora, un experimento o una comprobación relacionada. Incluyan en el README qué investigaron, qué agregaron y qué observaron. Pueden obtener todo el puntaje con las comprobaciones de su guía.

## Copiar los archivos del laboratorio

En Git Bash, Zsh o Bash, sitúense en la **raíz del repositorio privado**. Asignen a `curso` la ruta absoluta de su clon del curso y a `laboratorio` el nombre de la carpeta enlazada en la guía. El ejemplo usa el laboratorio 1. Las comillas conservan rutas con espacios. `/.` al final del origen copia el contenido de la carpeta, incluidos archivos ocultos como `.gitignore` y `.python-version`.

```bash
curso="/ruta/a/tu/clon-del-curso"
laboratorio="01-rendimiento-api"
cp -R "$curso/labs/starters/clase-24-laboratorios-mlops/$laboratorio/." .
base="$curso/labs/starters/clase-10-experiment-tracking"
cp "$base/modelos.py" "$base/preparar_datos.py" .
git status --short
```

Copien los datos que indica su guía. Comprueben que `pyproject.toml` y `uv.lock` estén junto a su README. El primero declara las dependencias y el segundo fija las versiones instaladas por `uv sync --locked`. Registren ambos en Git y mantengan `.venv/` como ambiente local.

En CI y despliegue, la guía indica dónde instalar el YAML del workflow. En drift y SHAP, el starter incluye un notebook opcional con las celdas listas. El README del equipo sigue siendo el punto de entrada a los comandos, resultados y evidencias.

## Entrega y calificación

Cada integrante entrega en **Canvas la misma URL del repositorio privado del equipo**. La fecha y hora de entrega se consultan en Canvas. La demostración ante el grupo es opcional.

| Criterio | Evidencia para obtener el puntaje completo | Puntos |
|---|---|---:|
| Configuración e implementación | El equipo conserva los scripts requeridos y deja la estructura, el ambiente y la configuración del laboratorio listos para ejecutar el recorrido de la guía. | 40 |
| Resultado comprobable | Las capturas y salidas acreditan las comprobaciones principales de la guía, incluidos los casos de control, falla o recuperación que correspondan. | 40 |
| Reproducibilidad | El README documenta requisitos, configuración, ejecución, verificación y cierre cuando corresponda. La explicación solicitada se apoya en la evidencia enlazada. | 20 |
| **Total** | **Puntaje común al equipo.** | **100** |

Se asigna crédito parcial por los pasos que se puedan verificar. Si una conexión impide terminar una comprobación, documenten la última etapa que funcionó, el error observado y la comprobación que hicieron para identificar el problema.
