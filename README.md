# Proyecto en Ciencia de Datos — Otoño 2026

Material activo del curso **Proyecto en Ciencia de Datos**. El semestre recorre el camino desde fundamentos de desarrollo hasta desplegar y operar una aplicación de machine learning, usando NYC Taxi como caso conductor.

## Recorrido del curso

1. **Fundamentos para construir y compartir aplicaciones de datos** (`modulo-01-fundamentos/`).
2. **Del modelo al producto: diseño y trazabilidad MLOps** (`modulo-02-ciclo-mlops/`).
3. **De local a producción: contenedores, nube y operación** (`modulo-03-produccion/`).

La orientación principal para estudiantes está en [`docs/guia-de-aprendizaje.md`](docs/guia-de-aprendizaje.md). Las fechas viven en [`docs/calendario-2026.md`](docs/calendario-2026.md) y las políticas complementarias en [`docs/syllabus.md`](docs/syllabus.md).

## Primer contacto — clases 1 y 2

Para comenzar se requieren Git, Git Bash o una terminal, Visual Studio Code y Python 3.12. Si falta alguna herramienta, consulta la guía de [Windows](docs/setup/windows.md) o [macOS/Linux](docs/setup/macos-linux.md).

Se recomienda mantener todo el trabajo del curso en una carpeta local que no esté sincronizada con OneDrive. El repositorio contiene los notebooks y recursos que el profesor irá publicando; las tareas y el proyecto pueden guardarse en carpetas separadas.

Como ejemplo, desde el Explorador de archivos o Finder puedes crear `cursos/proyecto-ciencia-datos` y dentro las carpetas `tareas` y `proyecto`. Esta estructura es sólo una sugerencia: puedes elegir cualquier ubicación local y los nombres que prefieras. Abre en VS Code la carpeta que hayas elegido mediante **Archivo > Abrir carpeta...** y ejecuta en la terminal integrada:

```bash
git clone https://github.com/zapatacc/proyecto-ciencia-datos-2026-2.git
```

Cuando termine, abre manualmente `proyecto-ciencia-datos-2026-2` desde VS Code. En una nueva terminal integrada ejecuta:

```bash
python labs/starters/clase-01-bienvenida/primeras_funciones.py
```

En macOS o Linux puede ser necesario usar `python3` en lugar de `python`.

## Ambiente docente canónico

El mantenimiento y la validación reproducible del repositorio sí utilizan [uv](https://docs.astral.sh/uv/):

```bash
uv sync --locked
uv run jupyter lab
```

Para comprobar el material disponible:

```bash
uv run python tools/validation/validate_notebooks.py
uv run ruff check .
```

## Material disponible

- [`clase-01-bienvenida.ipynb`](modulo-01-fundamentos/clase-01-bienvenida.ipynb): bienvenida, socialización de la guía de aprendizaje y preparación del espacio local de trabajo.
- [`clase-02-python-vscode.ipynb`](modulo-01-fundamentos/clase-02-python-vscode.ipynb): repaso compacto de Python mediante una actividad de viajes.
- `labs/starters/`: archivos que modifica el estudiantado.
- `labs/solutions/`: soluciones de referencia; el docente decide cuándo publicarlas.
- `templates/` y `project/templates/`: plantillas para crear clases, laboratorios y asesorías posteriores.

## Estado de construcción

Este repositorio contiene únicamente las fases 0 y 1 del plan de implementación y los borradores de las dos primeras clases solicitadas. El ejemplo canónico de NYC Taxi aún no se implementa: corresponde a la fase 2.

La migración es curada. El material 2025 no se copia en bloque; su procedencia y decisiones están registradas en [`docs/source-map.md`](docs/source-map.md) y [`docs/origen-2025.md`](docs/origen-2025.md).

## Licencia

Código y materiales propios bajo [MIT](LICENSE), salvo que un recurso indique otra licencia.
