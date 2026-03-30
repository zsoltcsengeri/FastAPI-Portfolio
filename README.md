# Zsolt Csengeri — Full Stack FastAPI Deployment

## Live Demo
| Environment | URL |
|--------------|-----|
| **Frontend** | https://zsolt-csengeri.com |
| **Backend API** | https://api.zsolt-csengeri.com/contacts |

---

## Overview

This is a **production-ready full-stack web application** demonstrating how to design, deploy, and operate a backend service on a cloud server.

The system includes:
- FastAPI backend
- PostgreSQL database
- Nginx reverse proxy with HTTPS
- Deployment on AWS EC2

This project represents the **first stage** of a DevOps journey:

**functional → reproducible → automated → optimized**

---

## Architecture


User
↓
Nginx (HTTPS + SSL termination)
↓
FastAPI (Uvicorn, localhost:8000)
↓
PostgreSQL


### Key Design Decisions
- Backend is not publicly exposed
- Nginx handles SSL and routing
- Database runs securely on the server
- API is separated via subdomain

---

## Project Structure


```text
/fastapi-app
├── backend/
├── frontend/
└── venv/
```

---

## Tech Stack

| Layer | Technology |
|--------|-------------|
| Frontend | HTML, CSS, JavaScript |
| Backend | FastAPI, Uvicorn |
| Database | PostgreSQL |
| Web Server | Nginx |
| Hosting | AWS EC2 |
| SSL | Let’s Encrypt |

---

## Deployment Approach

The application is deployed manually to fully understand the system:

- EC2 instance provisioning
- PostgreSQL setup
- FastAPI application setup
- Nginx reverse proxy configuration
- SSL certificate installation

This provides a strong foundation before introducing automation.

---

## Next Step: DevOps Transformation

This project is extended in the **devops-capstone branch**, where:

- Docker is introduced for containerization
- Terraform is used for infrastructure as code
- CI/CD pipeline is planned

See: `devops-capstone` branch

---

## Features

- Contact form submission → stored in PostgreSQL
- REST API with FastAPI
- HTTPS secured with SSL certificates
- Reverse proxy architecture
- Production-ready deployment

---

## Validation

- Frontend loads successfully
- API endpoint responds correctly
- Data persists in PostgreSQL
- SSL certificates valid and auto-renewed

---

## Author

**Zsolt Csengeri**  
Solution Engineer → DevOps / Cloud Engineer