FROM python:3.14-slim AS builder

WORKDIR /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.14-slim

WORKDIR /app
## appuser only for run gunicorn, no run shell
RUN useradd --no-create-home --shell /usr/sbin/nologin appuser

## system-wide package path, executable path
COPY --from=builder /usr/local/lib/python3.14/site-packages /usr/local/lib/python3.14/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY app.py .

## system path for shared package, while appuser for gunicorn run app.py
RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/healthz')" || exit 1


CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]


