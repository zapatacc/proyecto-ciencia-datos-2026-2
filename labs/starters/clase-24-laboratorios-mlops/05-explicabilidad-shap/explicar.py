"""Explica predicciones del Random Forest de NYC Taxi con las variables originales."""

from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import shap
from modelos import construir_pipeline
from preparar_datos import (
    FEATURES,
    FEATURES_CATEGORICAS,
    FEATURES_NUMERICAS,
    TARGET,
    cargar_muestra,
)

DATOS = Path("datos")
SALIDA = Path("resultados")
matplotlib.use("Agg")


def grupos_columnas(preprocesador) -> dict[str, np.ndarray]:
    """Relaciona cada variable original con sus posiciones en la matriz transformada."""
    posiciones = preprocesador.output_indices_
    grupos = {
        feature: np.array([posiciones["numericas"].start + indice])
        for indice, feature in enumerate(FEATURES_NUMERICAS)
    }
    inicio = posiciones["categoricas"].start
    codificador = preprocesador.named_transformers_["categoricas"]
    for feature, categorias in zip(FEATURES_CATEGORICAS, codificador.categories_, strict=True):
        fin = inicio + len(categorias)
        grupos[feature] = np.arange(inicio, fin)
        inicio = fin
    assert inicio == posiciones["categoricas"].stop
    return grupos


def explicar() -> None:
    entrenamiento = cargar_muestra(DATOS / "green-taxi-train.csv")
    validacion = cargar_muestra(DATOS / "green-taxi-validation.csv")
    pipeline = construir_pipeline("random_forest")
    pipeline.fit(entrenamiento[FEATURES], entrenamiento[TARGET])
    preprocesador = pipeline.named_steps["preprocesamiento"]
    bosque = pipeline.named_steps["modelo"]
    muestra = validacion[FEATURES].sample(n=60, random_state=42)
    columnas = preprocesador.get_feature_names_out()
    matriz = preprocesador.transform(muestra)
    if hasattr(matriz, "toarray"):
        matriz = matriz.toarray()

    explicador = shap.TreeExplainer(
        bosque, feature_perturbation="tree_path_dependent", feature_names=list(columnas)
    )
    explicacion = explicador(matriz)
    grupos = grupos_columnas(preprocesador)
    contribuciones = np.column_stack(
        [explicacion.values[:, grupos[feature]].sum(axis=1) for feature in FEATURES]
    )
    predicciones = pipeline.predict(muestra)
    reconstruidas = explicacion.base_values + contribuciones.sum(axis=1)
    np.testing.assert_allclose(reconstruidas, predicciones, rtol=1e-5, atol=1e-6)

    ranking = pd.DataFrame(
        {
            "variable": FEATURES,
            "importancia_impureza": [
                bosque.feature_importances_[grupos[feature]].sum() for feature in FEATURES
            ],
            "media_shap_absoluto_min": np.abs(contribuciones).mean(axis=0),
        }
    ).set_index("variable")

    SALIDA.mkdir(exist_ok=True)
    ranking.to_csv(SALIDA / "importancias.csv")
    fig, ejes = plt.subplots(1, 2, figsize=(11, 4), layout="constrained")
    for eje, columna, titulo, unidad in [
        (ejes[0], "importancia_impureza", "Importancia del bosque", "Proporción total"),
        (ejes[1], "media_shap_absoluto_min", "Atribución SHAP media", "Minutos"),
    ]:
        ranking[columna].sort_values().plot.barh(ax=eje, title=titulo, xlabel=unidad)
    fig.savefig(SALIDA / "importancias.png", dpi=120)
    plt.close(fig)

    indice = 0
    viaje = shap.Explanation(
        values=contribuciones[indice],
        base_values=explicacion.base_values[indice],
        data=muestra.iloc[indice].to_numpy(),
        feature_names=FEATURES,
    )
    shap.plots.waterfall(viaje, show=False)
    plt.gcf().savefig(SALIDA / "explicacion-viaje.png", dpi=120, bbox_inches="tight")
    plt.close()
    print(ranking.round(3).to_string())
    print(f"Valor de referencia: {viaje.base_values:.2f} min")
    print(f"Duración estimada: {predicciones[indice]:.2f} min")
    print(f"Duración reconstruida con SHAP: {reconstruidas[indice]:.2f} min")


if __name__ == "__main__":
    explicar()
