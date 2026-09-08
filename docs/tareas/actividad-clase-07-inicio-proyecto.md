# Actividad en clase 2 — Inicio del proyecto en equipo

## Propósito

Crear el repositorio privado del proyecto, preparar su estructura inicial y
registrar el avance que el equipo alcance durante la Clase 7. Esta actividad
permite comenzar el informe y la selección de datos sin exigir que la primera
entrega del proyecto quede terminada durante la sesión.

## Recursos

- [Clase 7 — Inicio del proyecto en equipo](../../modulo-01-fundamentos/clase-07-integracion.ipynb).
- [Flujo de trabajo y entrega de tareas](../flujo-tareas.md).
- [Plantilla de pull request](../plantillas/pull-request-tarea.md).
- La fuente y documentación del dataset que el equipo esté considerando.

## Entregable

**Repositorio:** repositorio privado del proyecto en equipo, separado de
`pcd-entregas-2026`.

**Rama obligatoria:** `docs/trabajo-clase-07`

**Evidencia principal:** un pull request hacia `main` con el avance real del
equipo durante la sesión.

Antes de terminar la clase, el equipo debe:

1. crear el repositorio privado y agregar a todas las personas integrantes;
2. agregar como colaborador al usuario de GitHub `zapatacc`;
3. preparar la estructura inicial indicada en el notebook;
4. avanzar en la selección del dataset, el README o las primeras secciones del
   informe;
5. documentar con claridad qué quedó listo y qué continuará en la tarea;
6. abrir, revisar y fusionar el pull request.

No es necesario completar durante la clase todos los apartados de la primera
entrega. El PR debe mostrar trabajo sustantivo realizado por el equipo y no
solamente archivos vacíos.

## Commits

Utilicen mensajes que describan el avance real. Por ejemplo:

```text
chore(proyecto): prepara estructura inicial
docs(proyecto): agrega contexto y fuentes de datos
docs(proyecto): registra pendientes de la primera entrega
```

No realicen commits vacíos ni trabajen directamente sobre `main`.

## Verificación

Antes de abrir el PR, comprueben:

```bash
git status --short
git diff
```

Revisen que el repositorio no incluya `.venv/`, `.env`, datos descargados,
credenciales, rutas personales ni artefactos generados. En la descripción del
PR indiquen qué archivos revisaron y qué avance contiene cada uno.

## Pull request y cierre obligatorio

El PR debe apuntar a `main`. Para preparar su descripción:

1. abran la [plantilla del curso](../plantillas/pull-request-tarea.md);
2. copien todo su contenido y péguenlo en **Write**;
3. adapten el resumen, la verificación y la lista de requisitos al trabajo de
   la clase;
4. comprueben el resultado con **Preview**;
5. agreguen como reviewers a las demás personas del equipo;
6. revisen **Files changed** y atiendan cualquier observación;
7. fusionen mediante **Create a merge commit**.

Antes de entregar, el PR debe aparecer como **Merged** y cerrado. Cerrar sin
merge no completa la actividad.

## Entrega en Canvas

Entreguen la URL del PR cerrado y fusionado en la
actividad correspondiente de Canvas. La fecha y hora límite se publican en
Canvas.

## Uso de herramientas y colaboración

El trabajo se realiza en equipo. Pueden consultar el material del curso,
documentación oficial y herramientas de IA como apoyo. El equipo debe revisar
toda sugerencia, citar las fuentes utilizadas y poder explicar el contenido y
las decisiones del repositorio. Una respuesta generada por IA no sustituye el
avance verificable ni la interpretación propia.

## Criterio de cumplimiento

Esta actividad no utiliza una rúbrica analítica. Se registra como completa
cuando el equipo entrega un PR con avance sustantivo, revisado, fusionado y
cerrado. No se evalúa cuántos apartados de la primera entrega alcanzaron a
terminar durante la sesión.
