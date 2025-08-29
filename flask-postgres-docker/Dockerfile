# ===== build stage =====
FROM python:3.12-slim AS builder
WORKDIR /src
COPY app/requirements.txt .
RUN pip install --upgrade pip && pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt

# ===== runtime stage =====
FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# (optional) add a non-root user
RUN useradd -m appuser
WORKDIR /app
COPY --from=builder /wheels /wheels
RUN pip install --no-cache /wheels/*
COPY app/ /app/

# basic healthcheck (Flask will listen on 8000 via gunicorn)
HEALTHCHECK --interval=30s --timeout=3s --start-period=20s \
  CMD python -c "import socket; s=socket.socket(); s.settimeout(2); s.connect(('127.0.0.1', 8000))" || exit 1

USER appuser
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]

