# Autonomous Self-Healing AIOps Platform

## Project Overview

This project demonstrates a production-inspired Autonomous Self-Healing Kubernetes platform that detects application failures through monitoring and automatically rolls back unhealthy deployments using GitOps principles.

## Objectives

- Deploy applications on Kubernetes
- Implement GitOps using ArgoCD
- Monitor workloads with Prometheus and Grafana
- Detect failures using Alertmanager
- Build an AIOps decision engine
- Automatically trigger rollback when error thresholds are exceeded

---

## Technology Stack

- Ubuntu 24.04
- Docker
- Kubernetes (Kind)
- ArgoCD
- Prometheus
- Grafana
- Alertmanager
- Python
- GitHub Actions

---

## Repository Structure

```text
app/
docker/
kubernetes/
argocd/
monitoring/
alertmanager/
aiops/
scripts/
docs/
diagrams/
.github/
```

---

## Project Status

- [x] Repository Initialized
- [ ] Kubernetes Cluster
- [ ] Application Deployment
- [ ] GitOps
- [ ] Monitoring
- [ ] Alerting
- [ ] AIOps Engine
- [ ] Self-Healing
- [ ] CI/CD
- [ ] Documentation

---

## Completed Milestones

### ✅ Phase 1 – Repository Foundation

- Repository initialized
- Professional folder structure
- README created
- MIT License added
- GitHub repository configured

### ✅ Phase 2 – Kubernetes Foundation

- Multi-node Kind cluster
- Kubernetes v1.31
- Metrics Server installed
- Monitoring namespace created
- Cluster health verified

### ✅ Phase 3 – Application Platform

- Flask application
- Health & readiness endpoints
- Prometheus metrics endpoint
- Error simulation endpoint
- Dockerized with Gunicorn
- Deployed to Kubernetes
- 2-replica Deployment
- ClusterIP Service

## Architecture

> Architecture diagram will be added during the project.

---

## License

MIT