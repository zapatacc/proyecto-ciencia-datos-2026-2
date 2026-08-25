# Starter — Clase 3

Este starter contiene únicamente la actividad. Cópialo a tu repositorio privado
individual dentro de:

```text
actividades/clase-03-uv/
```

Durante la primera parte de la clase usarás este mismo script para aprender el flujo
manual con una sola carpeta `.venv/`, `pip`, `pip freeze`, un archivo de requisitos y
`pipreqs`. Ese ambiente se elimina después de demostrar que puede reconstruirse, y `uv`
crea nuevamente la misma carpeta `.venv/` para el flujo recomendado. Nada de ello se
versiona.

Después convertirás la raíz de `pcd-entregas-2026` en el proyecto `uv` recomendado. El
proyecto no se inicializa dentro de esta carpeta; en la raíz se crearán o actualizarán:

```text
pcd-entregas-2026/
├── .gitignore
├── .python-version
├── pyproject.toml
├── uv.lock
└── actividades/
    └── clase-03-uv/
        └── src/
            └── verificar_ambiente.py
```

El archivo `verificar_ambiente.py` usa `requests` para preparar una URL sin acceder a
internet. Sigue el notebook: ahí se explica cómo comprobar el intérprete activo, cómo
reconstruir un ambiente manual y por qué `uv run python` usa el Python de `.venv/` sin
activar el ambiente en la terminal.

La práctica termina cuando funciona:

```bash
uv sync --locked
uv run --locked python actividades/clase-03-uv/src/verificar_ambiente.py
```

Es una actividad no calificable y no se entrega en Canvas.
