User
↓
Nginx (HTTPS, reverse proxy)
↓
FastAPI (containerized / service)
↓
PostgreSQL


---

## ⚙️ DevOps Layers

| Layer | Tool | Purpose |
|------|------|--------|
| Application | FastAPI | Business logic |
| Containerization | Docker | Consistent runtime |
| Orchestration | Docker Compose | Multi-service setup |
| Infrastructure | Terraform | AWS resource provisioning |
| Configuration | Ansible *(planned)* | Server automation |
| CI/CD | GitHub Actions *(planned)* | Deployment automation |

---

## 🐳 Docker Setup

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

Access:

API → http://localhost:8000/docs
☁️ Terraform — Infrastructure as Code
Purpose

Provision AWS infrastructure in a reproducible way.

Resources Defined
EC2 instance (application server)
Security Group:
SSH (22)
HTTP (80)
HTTPS (443)
Elastic IP
Terraform Workflow
terraform init
terraform validate
terraform plan

👉 terraform plan previews infrastructure changes without applying them.

🔐 Security Considerations
Backend not exposed directly (served via reverse proxy)
PostgreSQL not publicly accessible
Only required ports are open (22, 80, 443)
🔄 Deployment Strategy (Current vs Target)
Current (Hybrid)
Infrastructure defined via Terraform
Application deployed manually
Target (Fully Automated)
Terraform provisions infrastructure
Ansible configures server
Docker deploys application
CI/CD pipeline automates updates
🔧 Planned Improvements
🔹 Ansible

Will automate:

Docker installation
Nginx configuration
Application deployment
🔹 GitHub Actions (CI/CD)

Planned pipeline:

Trigger on push to main
Build Docker image
Validate application
Deploy to EC2 via SSH
Restart services
🧠 Future Architecture
EC2 (App Server)
 ├── Nginx
 ├── FastAPI (Docker)

EC2 (Database Server)
 └── PostgreSQL
🎯 Key Learning Outcomes
Infrastructure as Code using Terraform
Containerization with Docker
Cloud deployment on AWS EC2
Reverse proxy and SSL handling
Designing DevOps pipelines
Understanding system evolution from manual → automated
📂 Related Branch

👉 Main application (manual deployment):
https://github.com/zsoltcsengeri/FastAPI-Portfolio/tree/main

👤 Author

Zsolt Csengeri
Solution Engineer → DevOps / Cloud Engineer



