# Laboratorio 3 — Despliegue continuo en EC2

## Resultado

Despliega la API de duración de viajes Green Taxi desde GitHub Actions. Comprueba qué revisión y qué artefacto sirven las predicciones. Recupera una versión anterior ya comprobada.

Cada integración en `main` que modifica la aplicación inicia un trabajo de **despliegue continuo**. Un *runner* ejecuta ese trabajo en nombre de tu repositorio. En esta práctica prepara el código, se autentica por SSH y lo transfiere a EC2. EC2 construye la imagen con el modelo, arranca la API y prueba una predicción en el puerto local. Ese resultado indica si se puede conservar la revisión activa. Revisa el [recorrido de SSH y Docker de la Clase 20](../../../modulo-03-produccion/clase-20-aws-ec2-compose.ipynb) y la [consigna común](README.md).

## 1. Preparar el proyecto

Actualiza el repositorio público del curso mediante `git status` y `git pull` desde `main`. Crea y clona el repositorio nuevo y privado siguiendo la [consigna común](README.md). Desde la raíz del clon del equipo, ejecuta `git switch -c feat/despliegue-continuo` para abrir la rama de trabajo.

1. Copia el contenido del [starter de este laboratorio](../../../labs/starters/clase-24-laboratorios-mlops/03-despliegue-continuo) a la raíz del repositorio del equipo. Conserva las carpetas y los archivos ocultos. La [consigna común](README.md#copiar-los-archivos-del-laboratorio) incluye el comando de copia.
2. Copia `modelos.py` y `preparar_datos.py` del [starter de Clase 10](../../../labs/starters/clase-10-experiment-tracking/README.md) a la raíz. Copia `green-taxi-train.csv` de la Clase 10 a `datos/`. El Dockerfile lee esa ruta durante la construcción.
3. Prepara el ambiente desde el repositorio del equipo. `uv sync --locked` instala las versiones del `uv.lock` que viene con el starter.

```bash
uv sync --locked
uv run --locked python --version
```

**Comprueba** con `git status --short` que estás en el repositorio del equipo y que llegaron los archivos del starter. La terminal debe mostrar Python 3.12.

## 2. Comprobar el entrenamiento local

`entrenar.py` reutiliza el preprocesamiento y la regresión lineal de la Clase 10. Al ejecutarlo genera `modelo.pkl`. En el despliegue, la imagen vuelve a entrenar y conserva el artefacto que sirve esa revisión.

```bash
uv run --locked python entrenar.py
```

**Comprueba** que existe `modelo.pkl`. Carga sólo el artefacto generado por tu laboratorio. La API devuelve tanto la revisión de Git como el SHA-256 de los bytes del modelo. Si sólo cambia el código, la revisión puede cambiar aunque el hash del modelo coincida.

## 3. Leer la configuración de despliegue

| Archivo | Convención que debes reconocer |
|---|---|
| `Dockerfile` y `.dockerignore` | El Dockerfile define cómo se construye la imagen. `.dockerignore` limita qué archivos llegan al contexto de construcción. |
| `compose.yaml` | Usa la revisión como etiqueta de imagen y publica el puerto únicamente en la dirección local del anfitrión. `LAB_PORT` es el puerto del anfitrión y 8000 es el puerto interno. |
| `operacion/activar.sh` | Construye o recupera la imagen, inicia el contenedor y cambia la marca `activa` después de comprobar una predicción. |
| `operacion/verificar.py` | Envía una solicitud real y comprueba que la respuesta corresponde a la revisión esperada. |
| `.gitignore` | Excluye del repositorio llaves, configuración privada, archivos locales y el modelo generado. |

## 4. Prepara EC2 y las credenciales

1. Desde la consola de AWS en `us-east-1`, identifica una **instancia aislada de práctica** asignada al equipo. Comprueba que el grupo de seguridad que editarás sólo se aplica a esa práctica. Si usas una nueva instancia autorizada por el curso, sigue la instalación de Docker y Compose de la [Clase 20](../../../modulo-03-produccion/clase-20-aws-ec2-compose.ipynb). Antes de arrancarla, revisa con el responsable del equipo la autorización de coste y comprueba qué recursos seguirán generando cargos después de detenerla.
2. Con TCP 22 limitado a **Mi IP**, entra como `ubuntu` con la llave inicial de EC2. En la terminal remota, `sudo -n env docker compose version` debe mostrar una versión sin solicitar contraseña, como ocurrirá desde el workflow. `python3 --version` debe confirmar que existe el Python de sistema para la verificación HTTP. Comprueba con `sudo -n docker ps -a --filter name=nyc-taxi-api-container` que la instancia no aloja otro contenedor con el mismo nombre. El filtro sólo muestra nombres coincidentes.
3. En tu computadora crea una **llave de despliegue dedicada**, fuera del repositorio. `-t ed25519` selecciona el algoritmo, `-f` fija el archivo, `-C` agrega un comentario para localizar su parte pública al limpiar y `-N ""` usa una frase vacía para el trabajo no interactivo de Actions. Elige una ruta nueva y cancela si el comando pregunta si debe sobrescribir otra llave.

```bash
ssh-keygen -t ed25519 -f "$HOME/.ssh/green-taxi-lab03" -C "green-taxi-lab03" -N ""
```

4. Copia la **línea pública** de `green-taxi-lab03.pub`. En la sesión remota que ya verificaste, agrégala como una línea nueva en `~/.ssh/authorized_keys` con `nano` y conserva las demás entradas. Prueba desde tu computadora que SSH abre esa misma instancia con la llave dedicada.
5. En la sesión remota verificada, ejecuta `cat /etc/ssh/ssh_host_ed25519_key.pub`. Este archivo contiene la **llave pública del servidor**, diferente de la llave del equipo. Construye una sola línea con la dirección exacta que usarás, un espacio y los primeros dos campos de esa salida. El formato es `DIRECCION_EC2 ssh-ed25519 LLAVE_PUBLICA_DEL_SERVIDOR`. Actions comprobará esa identidad antes de transferir archivos. Si la IP pública cambia al volver a arrancar EC2, actualiza la dirección y la línea con la llave del servidor validada por la sesión de administración.
6. En el repositorio privado, abre **Settings → Secrets and variables → Actions**. Crea los secrets `EC2_SSH_KEY` con el contenido completo de la llave privada **dedicada**, y `EC2_KNOWN_HOSTS` con la línea de identidad del servidor. Crea las variables `EC2_HOST` con la dirección pública y `LAB_PORT` con el puerto local, por ejemplo `18003`. Comprueba que dicho puerto esté libre en EC2 antes de usarlo. [Secrets de GitHub Actions](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets)

El runner de GitHub aloja una sesión distinta de tu computadora. Si la política de la cuenta permite la excepción de demostración y el grupo pertenece sólo a la instancia aislada, agrega justo antes de ejecutar el flujo una regla temporal de entrada para SSH, TCP 22, con origen IPv4 `0.0.0.0/0`. Ese origen permite que cualquier dirección IPv4 intente conectarse durante la demostración. Mantén la autenticación por llave y conserva la regla de administración **Mi IP** para poder retirar sólo la temporal. Si la política impide agregar la regla, sigue la comprobación local de la sección 7. [Conexión SSH en EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-linux-inst-ssh.html) · [Direcciones de los runners de GitHub](https://docs.github.com/en/actions/reference/runners/github-hosted-runners#ip-addresses)

## 5. Automatiza el despliegue

Desde la raíz del repositorio del equipo, mueve la plantilla a la ruta estándar de GitHub Actions.

```bash
mkdir -p .github/workflows
mv configuracion/desplegar.yml .github/workflows/desplegar.yml
git status --short
```

GitHub descubre los archivos `.yml` o `.yaml` en `.github/workflows/` de la raíz del repositorio. Incluye el archivo en el commit. El evento `push` del workflow está limitado a `main` y a las rutas indicadas en `paths`. Un cambio exclusivo del README queda fuera de ese filtro. Las variables identifican el destino y puerto, y los secrets suministran la llave del equipo y el registro de identidad del servidor. El runner transfiere el código de la revisión y EC2 lo construye. [GitHub — Sintaxis de workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)

1. Revisa los archivos preparados con `git status`. Haz push a la rama del equipo, abre un PR, revisa y fusiona hacia `main`. Confirma que aparece una ejecución en **Actions**.
2. Abre el paso **Transferir y verificar revisión**. El log debe incluir la solicitud POST y un HTTP 200 con la revisión y el hash del modelo.
3. Actualiza tu copia de `main`, crea una segunda rama y realiza un cambio pequeño en `api.py`, por ejemplo en la descripción de la API. Revisa y fusiona el segundo PR. Confirma que la nueva ejecución devuelve el nuevo SHA completo de Git. Conserva los dos SHA para probar recuperación. El hash del modelo puede coincidir cuando se conservan el entrenamiento y los datos.

## 6. Recupera y cierra

Espera a que finalicen los trabajos de despliegue. En la terminal EC2 abierta desde tu computadora, define el SHA de la primera revisión exitosa y el puerto que configuraste en el repositorio. Ejecuta el script de esa revisión en modo `recuperar` desde el directorio personal.

```bash
REVISION_ANTERIOR=PEGA_AQUI_EL_SHA_COMPLETO
LAB_PORT=18003
LAB_DOCKER_SUDO=1 bash "green-taxi-lab03/revisiones/$REVISION_ANTERIOR/operacion/activar.sh" \
  green-taxi-lab03 "$REVISION_ANTERIOR" "$LAB_PORT" recuperar
```

**Comprobación.** La predicción recuperada devuelve el SHA anterior. El modelo corresponde al artefacto de esa imagen ya construida.

Al terminar, retira en la consola la regla temporal de SSH y comprueba que queda **Mi IP**. Si el despliegue falla, retira la regla temporal antes de continuar el diagnóstico. Desde la sesión de administración detén únicamente el servicio de la práctica. `cat` lee el SHA de `activa` y `down` retira el contenedor de ese proyecto.

```bash
REVISION_ACTIVA=$(cat green-taxi-lab03/activa)
sudo -n env REVISION="$REVISION_ACTIVA" LAB_PORT="$LAB_PORT" docker compose \
  -p green-taxi-lab03 -f "green-taxi-lab03/revisiones/$REVISION_ACTIVA/compose.yaml" down
```

Si no llegó a existir `activa`, revisa `sudo -n docker ps -a` y elimina sólo los recursos del proyecto que verificaste. Retira la línea marcada `green-taxi-lab03` de `authorized_keys`, borra el secret de la llave dedicada y detén la instancia desde la consola de AWS. El disco y otros recursos contratados pueden seguir generando cargos. [Detener una instancia EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Stop_Start.html)

## 7. Diagnostica o completa la comprobación local

| Resultado | Comprobación |
|---|---|
| `Connection timed out` | Comprueba que la instancia está en ejecución, que `EC2_HOST` coincide con la dirección pública y que el origen está permitido para TCP 22. |
| Fallo de identidad del servidor | Desde la sesión de administración verificada, confirma la llave pública y actualiza el registro de `EC2_KNOWN_HOSTS` para esa dirección. |
| `Permission denied (publickey)` | Confirma que la llave pública dedicada está en `authorized_keys` de `ubuntu` y corresponde al secret. |
| El contenedor falla o devuelve otra revisión | Comprueba el puerto local, los logs de Compose y el SHA indicado por la API. Si el flujo restaura la versión anterior, el trabajo seguirá marcado como fallido. |

Si la cuenta o la conexión bloquea el recorrido remoto, registra el error y la comprobación que realizaste. En una terminal local con Docker y Git Bash, Zsh o Bash, reproduce las dos revisiones confirmadas en Git. `git archive HEAD` empaqueta la revisión actual. `git rev-parse HEAD` muestra su SHA. `raiz` es una carpeta nueva fuera del repositorio, junto a su directorio. Usa un puerto libre y una máquina sin otro contenedor de NYC Taxi en uso.

```bash
raiz=../green-taxi-lab03-local
revision=$(git rev-parse HEAD)
LAB_PORT=18003
mkdir -p "$raiz/revisiones/$revision"
git archive HEAD | tar -xf - -C "$raiz/revisiones/$revision"
bash operacion/activar.sh "$raiz" "$revision" "$LAB_PORT" desplegar
```

Guarda el primer SHA, confirma el segundo cambio y repite el bloque. Después ejecuta `bash operacion/activar.sh "$raiz" "$revision_anterior" "$LAB_PORT" recuperar` con el primer SHA. Para detener sólo el servicio de este laboratorio, consulta el SHA en `"$raiz/activa"` y ejecuta `REVISION="$revision_activa" LAB_PORT="$LAB_PORT" docker compose -p green-taxi-lab03 -f "$raiz/revisiones/$revision_activa/compose.yaml" down`. En este recorrido el script usa `uv` para seleccionar Python 3.12, que sólo necesita su biblioteca estándar.

## Entrega y evidencias

Guarda en `evidencia/` una captura de cada predicción verificada después del despliegue inicial, la actualización y la recuperación. Guarda también el resultado de cierre de la regla y el estado de la instancia. Para la contingencia local adjunta el diagnóstico de la conexión y las comprobaciones locales alcanzadas. Oculta datos de cuenta, direcciones y credenciales.

El README explica cómo repetir la preparación y relaciona las revisiones con sus ejecuciones de Actions. Revisa la [rúbrica y la entrega en Canvas](README.md).

**Qué explicar en el README.** ¿Qué cambio dispara este workflow y cómo distinguiste la revisión desplegada del artefacto del modelo? Indica qué operación devolvió el servicio a la versión anterior.
