# Preparación en Windows

## Herramientas

1. Instalar [Python 3.12](https://www.python.org/downloads/release/python-31210/) y habilitar `Add Python to PATH`.
2. Instalar [Visual Studio Code](https://code.visualstudio.com/download) y la extensión oficial de Python.
3. Instalar [Git for Windows](https://git-scm.com/downloads/win); Git Bash será la terminal común del curso.

## Verificación en Git Bash

```bash
python --version
git --version
bash --version
code --version
```

## Carpeta local del curso

No usar OneDrive para este repositorio. Se puede escoger cualquier ubicación local fácil de encontrar. Como organización sugerida, desde el Explorador de archivos:

1. Crear una carpeta local llamada `cursos`.
2. Dentro, crear `proyecto-ciencia-datos`.
3. Dentro de esta última, crear `tareas` y `proyecto`.
4. Confirmar en la barra de dirección que la ruta no contiene `OneDrive`.

Los nombres y esta estructura son sólo un ejemplo. Abrir VS Code, elegir **Archivo > Abrir carpeta...** y seleccionar la carpeta local elegida para el curso. Abrir **Terminal > Nueva terminal** y elegir Git Bash como perfil. Clonar desde esa terminal el repositorio oficial donde el profesor publicará los notebooks y demás recursos:

```bash
git clone https://github.com/zapatacc/proyecto-ciencia-datos-2026-2.git
```

Al terminar, elegir nuevamente **Archivo > Abrir carpeta...** y seleccionar `proyecto-ciencia-datos-2026-2`. En una nueva terminal integrada ejecutar:

```bash
python labs/starters/clase-01-bienvenida/primeras_funciones.py
```

## Errores frecuentes

- `python: command not found`: reabrir Git Bash y revisar PATH.
- Se abre Microsoft Store: desactivar los alias de ejecución de `python.exe` en Windows.
- La ruta contiene `OneDrive`: mover la carpeta completa a una ruta local y volver a abrirla en VS Code.
- VS Code muestra la carpeta principal: usar **Archivo > Abrir carpeta...** y seleccionar la carpeta clonada.
- VS Code usa otro Python: ejecutar `Python: Select Interpreter` y elegir Python 3.12.
- La política institucional bloquea instalaciones: registrar el error y usar el ambiente alternativo indicado por el docente.
