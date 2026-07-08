# Kubernetes Cluster Setup

## Cluster

- Kubernetes: v1.31
- Kind Cluster
- 1 Control Plane
- 2 Worker Nodes

## Installed Components

- Metrics Server
- Monitoring Namespace

## Verification Commands

```bash
kubectl get nodes
kubectl get pods -A
kubectl top nodes
kubectl cluster-info
```

## Notes

Metrics Server is configured with:

--kubelet-insecure-tls

This is required for local Kind clusters.
