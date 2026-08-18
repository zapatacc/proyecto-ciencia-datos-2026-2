# Preparación en macOS y Linux

## Herramientas

1. Instalar [Python 3.12](https://www.python.org/downloads/release/python-31210/) sin reemplazar el Python del sistema.
2. Instalar [Visual Studio Code](https://code.visualstudio.com/download) y la extensión oficial de Python.
3. Instalar o verificar [Git](https://git-scm.com/downloads/) y una shell compatible.

## Verificación

```bash
python3 --version
git --version
bash --version
code --version
```

## Carpeta local del curso

Se puede escoger cualquier ubicación local fácil de encontrar. Como organización sugerida, desde Finder o el administrador de archivos:

1. Crear una carpeta local llamada `cursos`.
2. Dentro, crear `proyecto-ciencia-datos`.
3. Dentro de esta última, crear `tareas` y `proyecto`.
4. Confirmar que no está dentro de OneDrive ni de otra carpeta sincronizada.

Los nombres y esta estructura son sólo un ejemplo. Abrir VS Code, elegir **Archivo > Abrir carpeta...** y seleccionar la carpeta local elegida para el curso. Abrir **Terminal > Nueva terminal** y clonar desde ahí el repositorio oficial donde el profesor publicará los notebooks y demás recursos:

```bash
git clone https://github.com/zapatacc/proyecto-ciencia-datos-2026-2.git
```

Al terminar, elegir nuevamente **Archivo > Abrir carpeta...** y seleccionar `proyecto-ciencia-datos-2026-2`. En una nueva terminal integrada ejecutar:

```bash
python3 labs/starters/clase-01-bienvenida/primeras_funciones.py
```

## Errores frecuentes

- La ruta contiene una carpeta sincronizada: mover la carpeta completa a una ruta local y volver a abrirla en VS Code.
- VS Code muestra la carpeta principal: usar **Archivo > Abrir carpeta...** y seleccionar la carpeta clonada.
- VS Code usa una versión distinta: elegir manualmente Python 3.12.
- Permiso denegado: no usar `sudo pip`; en la primera clase no se instalan paquetes.
