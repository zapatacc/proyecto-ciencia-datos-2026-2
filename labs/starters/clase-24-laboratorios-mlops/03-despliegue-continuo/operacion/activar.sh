#!/usr/bin/env bash
set -euo pipefail

raiz=$1
revision=$2
export LAB_PORT=$3
modo=$4
motor=(env)
python_local=(uv run --no-project --python 3.12 python)
if [[ ${LAB_DOCKER_SUDO:-0} == 1 ]]; then
    motor=(sudo -n env)
    python_local=(python3)
fi

if [[ ! $revision =~ ^[0-9a-f]{40}$ || ! -f $raiz/revisiones/$revision/compose.yaml ]]; then
    echo 'La revisión debe existir en revisiones/ y tener un SHA completo.' >&2
    exit 1
fi

# Compose identifica el mismo servicio aunque cambie el directorio de la revisión.
compose() {
    local id=$1
    shift
    "${motor[@]}" REVISION="$id" LAB_PORT="$LAB_PORT" docker compose -p green-taxi-lab03 \
        -f "$raiz/revisiones/$id/compose.yaml" "$@"
}

anterior=
if [[ -f $raiz/activa ]]; then
    anterior=$(cat "$raiz/activa")
fi

case "$modo" in
    desplegar)
        if ! "${motor[@]}" docker image inspect "nyc-taxi-api-image:$revision" >/dev/null 2>&1; then
            compose "$revision" build api
        fi
        ;;
    recuperar) "${motor[@]}" docker image inspect "nyc-taxi-api-image:$revision" >/dev/null ;;
    *) echo 'Usa desplegar o recuperar.' >&2; exit 1 ;;
esac

# Esta verificación sale del anfitrión y atraviesa el puerto publicado.
verificador="$raiz/revisiones/$revision/operacion/verificar.py"
if compose "$revision" up -d --no-build &&
   "${python_local[@]}" "$verificador" "http://127.0.0.1:$LAB_PORT" "$revision"; then
    printf '%s\n' "$revision" > "$raiz/activa.tmp"
    mv "$raiz/activa.tmp" "$raiz/activa"
    exit 0
fi

echo "La revisión $revision falló." >&2
if [[ -n $anterior && $anterior != "$revision" ]]; then
    echo "Recuperando $anterior." >&2
    compose "$anterior" up -d --no-build
    "${python_local[@]}" "$verificador" "http://127.0.0.1:$LAB_PORT" "$anterior"
elif [[ -z $anterior ]]; then
    compose "$revision" down
fi
exit 1
