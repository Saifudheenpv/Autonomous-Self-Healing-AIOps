# Application Deployment

## Image

autonomous-self-healing-aiops:v1.0.0

## Components

- Deployment
- Service
- 2 Replicas

## Endpoints

| Endpoint | Purpose |
|----------|---------|
| / | Main application |
| /health | Liveness |
| /ready | Readiness |
| /metrics | Prometheus metrics |
| /version | Version information |
| /error | Simulate failures |
| /reset-errors | Reset failure simulation |

## Verification

```bash
kubectl get deployments
kubectl get pods
kubectl get svc
kubectl port-forward svc/aiops-service 8080:80
curl http://localhost:8080/
```
