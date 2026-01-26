# Demo Mesh Predictor

### Setup

Install redis locally then install project dependencies
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


## Deploy

Install redis on cluster using helm charts see [here](https://github.com/bitnami/charts/tree/main/bitnami/redis)

Get redis password and update `REDIS_PASSWORD` in values.yaml
```bash
kubectl get secret --namespace redis redis -o jsonpath="{.data.redis-password}" | base64 -d
```

Deploy app with helmfile to cluster

```bash
helmfile -f charts/helmfile.yaml apply
```

Port forward service to test locally
```bash
# redis name of default namespace
oc port-forward -n redis svc/demo-mesh-predictor 8080:80
```

## Testing

Example inference request to this service
```bash
curl -X POST 'localhost:8080/service' \
  --header 'Content-Type: application/json' \
  --data '{
  "service_type": "get_mesh_property",
  "service_name": "get mesh test",
  "parameters": {
    "property_type": ["DemoMeshPredictor"],
	"algorithm_version": "v1",
    "test_delay": 1
  },
	"async": true,
	"file_keys": ["test/dec.vtk"]
}'
```

> the `file_keys` items refrences a uploaded file. Use the script helper from [openad_service_utils](https://github.com/acceleratedscience/openad_service_utils/blob/mesh_domain/tests/integration/upload_client.py) to test an upload a file to server.