# Demo Mesh Predictor

### Instructions

Install project dependencies
```bash
uv sync
```

Run test server
```bash
JOB_MAX_RETRIES=1 \
UPLOAD_STORAGE_DIR="/tmp/collections" \
COLLECTIONS_API_ENABLED=True \
ASYNC_ALLOW=True \
REDIS_PORT=6379 \
REDIS_PASSWORD="" \
python src/main.py
```