FROM ghcr.io/astral-sh/uv:0.13.6 AS uv
FROM python:3.13-slim-bookworm

WORKDIR /app

# The environment lives outside /app so mounting the project over /app
# (see docker-compose.yaml) does not hide the installed packages.
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PROJECT_ENVIRONMENT=/opt/venv \
    PATH="/opt/venv/bin:$PATH"

COPY --from=uv /uv /uvx /bin/
# Install dependencies before copying the notebooks, so notebook changes
# reuse this layer.
COPY pyproject.toml uv.lock .python-version ./
RUN uv sync --locked --no-install-project --group notebook

COPY . .

# Run as an unprivileged user instead of root.
RUN useradd --create-home appuser && chown -R appuser /app
USER appuser

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--ServerApp.root_dir=/app"]
