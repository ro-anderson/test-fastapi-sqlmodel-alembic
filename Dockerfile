FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app/

# Install uv
COPY --from=ghcr.io/astral-sh/uv:0.5.11 /uv /uvx /bin/

# Create virtual environment with uv
RUN uv venv

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

# Compile bytecode
ENV UV_COMPILE_BYTECODE=1

# uv Cache
ENV UV_LINK_MODE=copy

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files
COPY pyproject.toml uv.lock alembic.ini ./

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project

# Set Python path
ENV PYTHONPATH=/app

# Copy application code
COPY . .

# Sync the project and ensure uvicorn is installed
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync && \
    uv pip install uvicorn

# Create startup script
RUN echo '#!/bin/bash\n\
alembic upgrade head\n\
uv run uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4' > /app/start.sh && \
chmod +x /app/start.sh

# Expose the port the app runs on
EXPOSE 8000

# Command to run the startup script
CMD ["/app/start.sh"] 