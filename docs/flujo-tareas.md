# Flujo de trabajo y entrega de tareas

Este documento define el flujo obligatorio para las tareas individuales del curso. Las instrucciones particulares de cada tarea pueden agregar requisitos, pero no reemplazan estas reglas.

## Repositorio individual del semestre

Cada estudiante mantendrá **un repositorio privado individual** para sus tareas y para las actividades que indiquen explícitamente un flujo Git. El nombre recomendado es:

```text
pcd-entregas-2026
```

Se recomienda clonar ambos repositorios al mismo nivel dentro de la estructura propuesta en la clase 1. La ubicación y los nombres de las carpetas superiores son sólo una sugerencia; pueden cambiarse, siempre que se utilice una ruta local fuera de OneDrive:

```text
cursos/
└── proyecto-ciencia-datos/
    ├── proyecto-ciencia-datos-2026-2/   # repositorio público del curso
    │   └── labs/trabajo-local/          # prácticas no calificables, ignoradas
    ├── pcd-entregas-2026/               # repositorio privado individual
    │   ├── actividades/                 # sólo cuando la clase indique usar Git
    │   └── tareas/
    └── proyecto/                        # proyecto en equipo, cuando se indique
```

El repositorio individual debe dar acceso al profesor como colaborador y usar internamente una estructura como ésta:

```text
actividades/                              # sólo actividades con flujo Git explícito
└── clase-02/
tareas/
├── tarea-01-lecturas/
└── tarea-02-nombre/
README.md
```

El proyecto en equipo vivirá en un repositorio privado separado. No se crea un repositorio nuevo para cada tarea, salvo que las instrucciones indiquen explícitamente una excepción.

## Actividades no calificables

El repositorio público del curso se actualiza con `git pull`; no se utiliza para hacer commits o push. Para una actividad no calificable, conserva los archivos publicados en `labs/starters/` sin modificaciones y copia únicamente lo necesario a:

```text
labs/trabajo-local/clase-XX/
```

`labs/trabajo-local/` está ignorada por Git. Su contenido no requiere rama, commit, push, pull request ni entrega en Canvas. Es una copia de trabajo local, no un respaldo.

No edites directamente el starter o notebook publicado: aunque no hagas commit, un cambio local sobre un archivo rastreado puede bloquear un `git pull` cuando el profesor publique una corrección. Si una clase tiene como objetivo practicar Git, sus instrucciones indicarán explícitamente que la actividad debe copiarse a `pcd-entregas-2026` y completar el flujo correspondiente.

## Una rama y un pull request por tarea

No se trabaja directamente sobre `main`. Cada tarea evaluada debe completar este ciclo:

1. Cambiar a `main` y obtener su versión más reciente.
2. Crear desde `main` la rama indicada en las instrucciones.
3. Trabajar únicamente en la carpeta de la tarea correspondiente.
4. Crear commits pequeños y comprensibles.
5. Publicar la rama en GitHub.
6. Abrir un pull request hacia `main` y completar su descripción con la plantilla del curso.
7. Revisar **Files changed** y corregir archivos accidentales o requisitos faltantes.
8. Hacer merge del pull request a `main`.
9. Confirmar en GitHub que el pull request aparece como **Merged** y está cerrado.
10. Entregar en Canvas únicamente la URL de ese pull request cerrado y fusionado.

Una tarea **no está terminada** si el pull request permanece abierto, fue cerrado sin merge o los archivos sólo existen en la rama. Siempre debe quedar como evidencia un pull request cerrado y fusionado a `main`.

Secuencia base, sustituyendo el nombre y la ruta de cada tarea:

```bash
git switch main
git pull
git switch -c <tipo>/NN-slug
mkdir -p tareas/tarea-NN-slug
# desarrollar y verificar el entregable
git status
git diff
git add tareas/tarea-NN-slug
git diff --staged
git commit -m "<tipo>(tarea-NN): describe el cambio"
git push -u origin <tipo>/NN-slug
```

Después del merge, se actualiza la copia local:

```bash
git switch main
git pull
```

La rama ya fusionada puede eliminarse. Las correcciones posteriores a la entrega se realizan en otra rama y otro pull request; no se reescribe silenciosamente la evidencia original.

## Convenciones de nombres

### Ramas

La convención de ramas del curso es:

```text
<tipo>/<numero-y-descripcion-en-kebab-case>
```

El tipo comunica la naturaleza principal del trabajo:

- `feat`: agrega una funcionalidad o capacidad nueva;
- `fix`: corrige un error de comportamiento;
- `docs`: crea o modifica principalmente documentación, análisis o texto;
- `test`: agrega o corrige verificaciones;
- `refactor`: reorganiza código sin cambiar su comportamiento;
- `chore`: realiza mantenimiento que no encaja en los anteriores.

Una tarea no es automáticamente una `feat`. El tipo depende del entregable. La Tarea 1 es una lectura y un resumen en Markdown, por eso su rama es `docs/01-lecturas`. Una tarea que implemente una función nueva podría usar `feat/02-nombre`; una corrección podría usar `fix/03-nombre`. Las instrucciones de cada tarea indicarán el nombre exacto.

Los nombres van en minúsculas, sin espacios ni acentos. La parte descriptiva utiliza *kebab-case*: palabras separadas por guiones.

### Commits

Los mensajes siguen la especificación oficial de [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/):

```text
<tipo>(alcance-opcional): descripcion breve
```

Usaremos inicialmente los mismos tipos descritos para las ramas. El alcance entre paréntesis es opcional y ubica el área afectada. La descripción se escribe después de `: ` y explica el cambio concreto.

```text
feat(viajes): agrega calculo de duracion
test(viajes): verifica distancias invalidas
docs(tarea-01): compara definiciones de mlops
fix(tarea-01): corrige enlaces de las fuentes
```

La especificación reserva un significado especial para `feat` y `fix`, pero permite otros tipos. También admite `!` o un pie `BREAKING CHANGE:` para cambios incompatibles; los reconoceremos, aunque no serán necesarios en las primeras tareas.

El mensaje debe completar la idea “este commit...”. Se evitan mensajes vagos como `cambios`, `tarea`, `final`, `ahora si` o `version 2`.

Conventional Commits define **mensajes de commit**. La regla `<tipo>/...` para nombres de rama es una convención adicional del curso: ambas usan el mismo tipo para que el historial sea fácil de interpretar.

## Contenido mínimo del pull request

Todo pull request de tarea debe indicar:

- número y nombre de la tarea;
- ruta del entregable;
- qué se realizó;
- cómo se verificó;
- checklist de requisitos.

Antes de fusionar, la persona autora debe revisar la pestaña **Files changed**. No se fusiona un PR que incluya archivos de otra tarea, credenciales, datos privados, soluciones ajenas o cambios accidentales.

### Cómo utilizar la plantilla de PR

La plantilla canónica está en [`docs/plantillas/pull-request-tarea.md`](plantillas/pull-request-tarea.md) dentro del **repositorio público del curso**. No está instalada en `.github/` dentro del repositorio privado y, por lo tanto, GitHub no la insertará automáticamente.

Para utilizarla en cada tarea:

1. abre `docs/plantillas/pull-request-tarea.md` en el repositorio público, desde VS Code o desde GitHub;
2. copia **todo** el contenido del archivo;
3. abre el PR del repositorio privado y confirma **base: main** y **compare: rama-de-la-tarea**;
4. pega la plantilla en la pestaña **Write** del cuadro de descripción;
5. sustituye las indicaciones por información específica de tu trabajo, sin borrar las secciones obligatorias;
6. marca una casilla cambiando `- [ ]` por `- [x]`, o haciendo clic en ella cuando GitHub lo permita;
7. selecciona **Preview** para comprobar cómo se renderizan los encabezados, el código y la checklist;
8. crea el PR, revisa **Files changed**, corrige lo necesario y sólo entonces realiza el merge.

La plantilla es texto en [Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax): `##` crea encabezados, los acentos graves marcan código y `- [ ]` crea casillas. **Write** permite editar el texto; **Preview** muestra cómo lo verá otra persona. El archivo publicado permanece en `docs/plantillas/` para que siempre exista una copia limpia disponible para futuras tareas.

## Entrega oficial en Canvas

Canvas es el único medio oficial de entrega. En el espacio correspondiente se entrega:

1. la URL del pull request cerrado y fusionado;
2. cualquier evidencia adicional indicada expresamente en la tarea.

Un enlace enviado por correo, Teams o mensaje privado no sustituye la entrega en Canvas. Las políticas de retraso de la guía de aprendizaje se aplican a la hora registrada por Canvas.

Cada tarea publicada debe incluir una rúbrica cuya suma sea 100 puntos. La rúbrica describe evidencias observables del contenido, la verificación, el historial de Git y el cierre del PR. La política de retrasos se aplica después de obtener el resultado de la rúbrica; no sustituye sus criterios.

## Checklist final

- [ ] Trabajé en la rama indicada, no directamente en `main`.
- [ ] El entregable está en la carpeta indicada.
- [ ] Mis commits tienen mensajes descriptivos.
- [ ] Copié y completé la plantilla del curso en la descripción del PR.
- [ ] Revisé todos los archivos en **Files changed**.
- [ ] El PR apunta a `main`.
- [ ] El PR fue fusionado y aparece como **Merged** y cerrado.
- [ ] Actualicé mi `main` local después del merge.
- [ ] Entregué en Canvas la URL del PR.
