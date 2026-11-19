FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:0.12.5 /uv /bin/uv
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev
COPY entrenar.py api.py modelos.py preparar_datos.py ./
COPY datos/green-taxi-train.csv datos/
RUN .venv/bin/python entrenar.py
CMD [".venv/bin/uvicorn", "api:app", "--host", "0.0.0.0"]
