# DevOps Capstone — FastAPI Portfolio Infrastructure

## Overview

This branch demonstrates the **DevOps evolution** of a working FastAPI application into a **reproducible and infrastructure-driven deployment**.

The focus is on:
- Containerization (Docker)
- Infrastructure as Code (Terraform)
- Cloud architecture design
- Deployment automation (planned)

---

## Project Philosophy

This project follows a real-world engineering progression:

**functional → reproducible → automated → optimized**

- `main` branch → working system (manual deployment)
- `devops-capstone` → DevOps transformation

---

## Architecture Overview

### Application Flow
User
↓
Nginx (HTTPS, reverse proxy)
↓
FastAPI (application service)
↓
PostgreSQL (database)


---

## DevOps Layers

| Layer | Tool | Purpose |
|------|------|--------|
| Application | FastAPI | Business logic |
| Containerization | Docker | Consistent runtime |
| Orchestration | Docker Compose | Multi-service setup |
| Infrastructure | Terraform | AWS resource provisioning |
| Configuration | Ansible *(planned)* | Server automation |
| CI/CD | GitHub Actions *(planned)* | Deployment automation |

---

## Docker Setup

### Purpose

- Ensure consistent development and runtime environment  
- Eliminate “works on my machine” issues  

### Services

| Service | Description |
|--------|-------------|
| backend | FastAPI app (Uvicorn) |
| postgres | PostgreSQL database |

---

### Run Locally
```bash
docker compose up --build
```

Access

- API Docs → http://localhost:8000/docs

### Terraform — Infrastructure as Code

Purpose

Provision AWS infrastructure in a reproducible and predictable way.

Resources defined

- EC2 instance (application server)
- Security Group:
	- SSH (22)
	- HTTP (80)
	- HTTPS (443)
- Elastic IP

Terraform workflow

```bash
terraform init
terraform validate
terraform plan
```

`terraform plan` previews infrastructure changes before applying them.

### Security Considerations

- Backend is not exposed directly (served via Nginx)
- PostgreSQL is not publicly accessible
- Only required ports are open (22, 80, 443)

### Deployment Strategy

#### Current State (Hybrid)

- Infrastructure defined using Terraform
- Application deployed manually

#### Target State (Fully Automated)

- Terraform provisions infrastructure
- Ansible configures the server
- Docker deploys the application
- CI/CD pipeline automates updates

### Planned Improvements

#### Ansible

Will automate:

- Docker installation
- Nginx configuration
- Application deployment

#### GitHub Actions (CI/CD)

Planned pipeline:

- Trigger on push to `main`
- Build Docker image
- Validate application
- Deploy to EC2 via SSH
- Restart services

### Future Architecture

```text
EC2 (Application Server)
├── Nginx
├── FastAPI (Docker)

EC2 (Database Server)
└── PostgreSQL
```

### Key Learning Outcomes

- Infrastructure as Code using Terraform
- Containerization with Docker
- Cloud deployment on AWS EC2
- Reverse proxy and SSL handling
- DevOps architecture design
- Understanding system evolution from manual → automated
Related Branch

Main application (manual deployment):
https://github.com/zsoltcsengeri/FastAPI-Portfolio/tree/main

Author

Zsolt Csengeri
Solution Engineer → DevOps / Cloud Engineer