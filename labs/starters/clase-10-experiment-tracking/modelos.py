"""Pipelines comparables para la práctica de experiment tracking."""

from preparar_datos import FEATURES_CATEGORICAS, FEATURES_NUMERICAS
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


def construir_pipeline(nombre_modelo: str) -> Pipeline:
    """Construye el mismo preprocesamiento y cambia sólo el estimador."""
    preprocesamiento = ColumnTransformer(
        [
            ("numericas", "passthrough", FEATURES_NUMERICAS),
            (
                "categoricas",
                OneHotEncoder(handle_unknown="ignore"),
                FEATURES_CATEGORICAS,
            ),
        ]
    )

    if nombre_modelo == "linear_regression":
        estimador = LinearRegression()
    elif nombre_modelo == "random_forest":
        estimador = RandomForestRegressor(
            n_estimators=100,
            max_depth=12,
            min_samples_leaf=5,
            n_jobs=-1,
            random_state=42,
        )
    else:
        raise ValueError(f"Modelo no reconocido: {nombre_modelo}")

    return Pipeline(
        [("preprocesamiento", preprocesamiento), ("modelo", estimador)]
    )
