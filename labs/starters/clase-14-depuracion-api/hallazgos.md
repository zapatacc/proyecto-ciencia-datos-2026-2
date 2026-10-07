# Hallazgos de la depuración

## Integrantes

- Nombre:
- Nombre:

## Ciclo de trabajo

Por cada error: ejecuta, observa, registra la evidencia, formula una hipótesis,
realiza un solo cambio y vuelve a ejecutar.

| Iteración | Evidencia observada | Hipótesis | Cambio realizado | Resultado al volver a ejecutar |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |

## Verificación final

- [ ] El servidor inicia sin traceback.
- [ ] `GET /health` responde `200` con `{"status": "ok"}`.
- [ ] Una solicitud válida a `POST /api/v1/predicciones` responde `200`.
- [ ] La respuesta válida contiene `duracion_estimada_minutos`.
- [ ] Una solicitud con `hora_recoleccion` igual a `24` responde `422`.
- [ ] Los cinco cambios se justifican con evidencia, no sólo con el resultado.

## Explicación para compartir

Elige uno de los cinco errores y explica:

1. qué observaste;
2. qué evidencia fue útil;
3. qué hipótesis formulaste;
4. cuál fue el cambio mínimo;
5. cómo comprobaste la corrección.
