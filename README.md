# 🚀 Autonomous Self-Healing AIOps Platform

> A production-inspired Kubernetes platform that automatically detects application failures and performs GitOps-based self-healing using Argo CD, Prometheus, Alertmanager, and an AIOps decision engine.

---

## 📌 Project Overview

This project demonstrates how to build an **Autonomous Self-Healing Platform** on Kubernetes using modern DevOps and GitOps practices.

The platform continuously monitors application health, detects abnormal error rates, and automatically restores the last healthy application version through **Argo CD Rollback**.

This project is designed as a **production-ready DevOps portfolio project** covering:

- Kubernetes
- GitOps
- Observability
- Monitoring
- Automation
- Self-Healing Infrastructure
- CI/CD

---

# 🎯 Project Objectives

- Deploy applications on Kubernetes
- Implement GitOps using Argo CD
- Monitor application health using Prometheus
- Visualize metrics with Grafana
- Generate alerts using Alertmanager
- Build an AIOps decision engine
- Automatically rollback unhealthy deployments
- Build a production-ready DevOps project

---

# 🏗️ High-Level Architecture

```text
                     Developer
                         │
                         ▼
                  GitHub Repository
                         │
                         ▼
                      Argo CD
                         │
                         ▼
                 Kubernetes Cluster
                         │
         ┌───────────────┼───────────────┐
         │                               │
         ▼                               ▼
   Flask Application              Monitoring Stack
                                         │
                 ┌───────────────────────┴──────────────────────┐
                 ▼                                              ▼
            Prometheus                                      Grafana
                 │
                 ▼
           Alertmanager
                 │
                 ▼
         AIOps Decision Engine
                 │
                 ▼
      Automatic Argo CD Rollback
```

---

# ⚙️ Technology Stack

| Category | Technology |
|-----------|------------|
| Operating System | Ubuntu 26.04 LTS |
| Version Control | Git & GitHub |
| Container Runtime | Docker |
| Container Orchestration | Kubernetes (Kind) |
| GitOps | Argo CD |
| Monitoring | Prometheus |
| Visualization | Grafana |
| Alerting | Alertmanager |
| Metrics | Metrics Server |
| Backend | Python Flask |
| WSGI Server | Gunicorn |
| Configuration Management | Kustomize *(Upcoming)* |
| Automation | Python |
| CI/CD | GitHub Actions *(Upcoming)* |

---

# 📂 Repository Structure

```text
autonomous-self-healing-aiops/
│
├── app/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── src/
│       └── app.py
│
├── kubernetes/
│   ├── base/
│   └── overlays/
│
├── kind/
│   └── kind-config.yaml
│
├── argocd/
├── monitoring/
├── alertmanager/
├── aiops/
├── docker/
├── scripts/
├── diagrams/
│
├── docs/
│   ├── application/
│   └── kubernetes/
│
├── README.md
└── LICENSE
```

---

# ✨ Features

## ✅ Completed

- Multi-node Kubernetes Cluster
- Metrics Server
- Dockerized Flask Application
- Gunicorn Production Server
- Health Endpoint
- Readiness Endpoint
- Version Endpoint
- Prometheus Metrics Endpoint
- Error Simulation Endpoint
- Kubernetes Deployment
- Kubernetes Service
- Production Folder Structure
- Documentation

---

## 🚧 Upcoming

- Argo CD GitOps
- Prometheus Monitoring
- Grafana Dashboard
- Alertmanager
- AIOps Decision Engine
- Automatic Rollback
- Self-Healing
- GitHub Actions CI/CD
- Production Documentation

---

# 🌐 Application Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | Main Application |
| `/health` | Kubernetes Liveness Probe |
| `/ready` | Kubernetes Readiness Probe |
| `/metrics` | Prometheus Metrics |
| `/version` | Application Version |
| `/error` | Enable Failure Simulation |
| `/reset-errors` | Disable Failure Simulation |

---

# 📊 Current Project Progress

| Phase | Status |
|--------|--------|
| ✅ Repository Foundation | Completed |
| ✅ Kubernetes Foundation | Completed |
| ✅ Application Platform | Completed |
| ⏳ GitOps with Argo CD | In Progress |
| ⏳ Monitoring Stack | Pending |
| ⏳ Alerting | Pending |
| ⏳ AIOps Engine | Pending |
| ⏳ Autonomous Self-Healing | Pending |
| ⏳ CI/CD | Pending |
| ⏳ Documentation | Pending |

---

# 📋 Completed Milestones

## ✅ Phase 1 — Repository Foundation

- Repository Initialization
- Professional Folder Structure
- GitHub Repository
- README
- MIT License

---

## ✅ Phase 2 — Kubernetes Foundation

- Multi-node Kind Cluster
- Metrics Server
- Monitoring Namespace
- Cluster Verification

---

## ✅ Phase 3 — Application Platform

- Flask Application
- Docker Image
- Gunicorn
- Kubernetes Deployment
- Kubernetes Service
- Health Checks
- Prometheus Metrics
- Error Simulation

---

# 🚀 Current Deployment Flow

```text
Developer
     │
     ▼
Docker Image
     │
     ▼
Kind Kubernetes Cluster
     │
     ▼
Deployment
     │
     ▼
ReplicaSet
     │
     ▼
Pods (2 Replicas)
     │
     ▼
ClusterIP Service
```

---

# 📖 Documentation

| Document | Description |
|-----------|-------------|
| docs/kubernetes/cluster-setup.md | Kubernetes Cluster Setup |
| docs/application/deployment.md | Application Deployment |

More documentation will be added throughout the project.

---

# 📦 Current Version

```text
v1.0.0
```

---

# 🛣️ Roadmap

- [x] Repository Initialization
- [x] Kubernetes Cluster
- [x] Metrics Server
- [x] Flask Application
- [x] Docker Image
- [x] Kubernetes Deployment
- [ ] Argo CD Installation
- [ ] GitOps Deployment
- [ ] Prometheus
- [ ] Grafana
- [ ] Alertmanager
- [ ] AIOps Engine
- [ ] Automatic Rollback
- [ ] Self-Healing
- [ ] GitHub Actions
- [ ] Final Documentation

---

# 🎓 Learning Outcomes

This project demonstrates practical experience with:

- Docker
- Kubernetes
- GitOps
- Argo CD
- Prometheus
- Grafana
- Alertmanager
- Python
- DevOps Automation
- CI/CD
- Kubernetes Monitoring
- Self-Healing Infrastructure

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Saifudheen PV**

Cloud & DevOps Engineer

GitHub: https://github.com/Saifudheenpv