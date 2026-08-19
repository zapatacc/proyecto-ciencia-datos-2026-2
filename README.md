# Proyecto en Ciencia de Datos — Otoño 2026

Material activo del curso **Proyecto en Ciencia de Datos**. El semestre recorre el camino desde fundamentos de desarrollo hasta desplegar y operar una aplicación de machine learning, usando NYC Taxi como caso conductor.

## Recorrido del curso

1. **Fundamentos para construir y compartir aplicaciones de datos** (`modulo-01-fundamentos/`).
2. **Del modelo al producto: diseño y trazabilidad MLOps** (`modulo-02-ciclo-mlops/`).
3. **De local a producción: contenedores, nube y operación** (`modulo-03-produccion/`).

La orientación principal para estudiantes está en [`docs/guia-de-aprendizaje.md`](docs/guia-de-aprendizaje.md). Las fechas viven en [`docs/calendario-2026.md`](docs/calendario-2026.md), el procedimiento de entrega en [`docs/flujo-tareas.md`](docs/flujo-tareas.md) y las políticas complementarias en [`docs/syllabus.md`](docs/syllabus.md).

## Cómo utilizar este repositorio

El profesor publicará aquí notebooks, lecturas, starters y recursos del curso. Para comenzar se requieren Git, Git Bash en Windows o una terminal compatible en macOS/Linux, Visual Studio Code y Python 3.12. Las guías de instalación están disponibles para [Windows](docs/setup/windows.md) y [macOS/Linux](docs/setup/macos-linux.md).

Clona el repositorio en una ruta local fuera de OneDrive u otras carpetas sincronizadas:

```bash
git clone https://github.com/zapatacc/proyecto-ciencia-datos-2026-2.git
```

Antes de cada clase, abre una terminal dentro del repositorio y obtén el material más reciente con `git pull`. No hagas commits ni push desde este repositorio.

## Espacios de trabajo

Durante el semestre se utilizan tres espacios con propósitos diferentes:

1. `proyecto-ciencia-datos-2026-2`: repositorio público con el material publicado por el profesor.
2. `pcd-entregas-2026`: repositorio privado individual para tareas y actividades que indiquen explícitamente un flujo Git.
3. `proyecto`: repositorio privado del equipo para el proyecto integrador, cuando se indique.

Se recomienda mantenerlos al mismo nivel dentro de una ruta local. La estructura siguiente es sólo un ejemplo:

```text
cursos/
└── proyecto-ciencia-datos/
    ├── proyecto-ciencia-datos-2026-2/
    ├── pcd-entregas-2026/
    └── proyecto/
```

### Prácticas no calificables

Los archivos publicados en `labs/starters/` se conservan como originales de referencia. Cuando una práctica no calificable requiera modificaciones, copia el starter indicado a `labs/trabajo-local/clase-XX/`. Esta carpeta está ignorada por Git: no requiere rama, commit, push, pull request ni entrega en Canvas.

### Tareas

Cada tarea vive en su propia carpeta y rama dentro de `pcd-entregas-2026`. El flujo termina con un pull request revisado, fusionado a `main` y cerrado; la entrega oficial se realiza mediante Canvas. Consulta el [flujo completo de tareas](docs/flujo-tareas.md) y las instrucciones particulares publicadas en `docs/tareas/`.

## Organización del repositorio

```text
modulo-01-fundamentos/   # construcción y colaboración inicial
modulo-02-ciclo-mlops/   # diseño, trazabilidad y ciclo de ML
modulo-03-produccion/    # despliegue y operación
labs/
├── starters/            # archivos iniciales publicados
└── trabajo-local/       # copias locales ignoradas por Git
assets/                  # recursos visuales organizados por módulo y clase
docs/                    # calendario, políticas, guías y tareas
```

Los notebooks y materiales disponibles se enlazan progresivamente desde el [calendario del curso](docs/calendario-2026.md) y los README de cada módulo.

## Licencia

Código y materiales propios bajo [MIT](LICENSE), salvo que un recurso indique otra licencia.
