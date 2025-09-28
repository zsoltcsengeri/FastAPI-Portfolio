# PK-Work – CV Website with FastAPI Contact Form

This project contains my personal CV website, originally hosted on GitHub Pages.  
The `fastapi-contact-form` branch extends the project by adding a **backend** with **FastAPI** and a **PostgreSQL database** to handle the contact form submissions.

---

## 📂 Project Structure

PK-Work/
│
├── backend/ # FastAPI backend
│ ├── main.py # FastAPI app (entry point)
│ ├── models.py # Database models
│ ├── database.py # DB connection
│ └── requirements.txt # Python dependencies
│
├── frontend/ # Website files
│ ├── CV/ # Resume
│ │ └── Zsolt_Resume.pdf
│ ├── images/ # Images
│ ├── index.html # Main CV site
│ ├── script.js # JS logic for contact form
│ ├── style.css # Main styling
│ ├── terms_conditions.html
│ └── terms_style.css
│
├── LICENSE
└── README.md


---

## 🚀 Running the Backend Locally

### 1. Install dependencies
Create a virtual environment (recommended):
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate     # On Windows
pip install -r requirements.txt

2. Set up PostgreSQL

Make sure you have PostgreSQL running locally.
Create a database (example):

CREATE DATABASE cv_site;


Update the connection settings in backend/database.py:

DB_USER = "postgres"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "cv_site"

3. Run the server

From the root folder:

uvicorn backend.main:app --reload


FastAPI will start at:

API docs → http://127.0.0.1:8000/docs

Contact endpoint → POST /contact

🖥️ Frontend

All website files are in the frontend/ folder.

script.js collects form input and sends it to the backend (/contact) using JavaScript fetch().

On deployment, Nginx will serve these static files and proxy API requests to FastAPI.

🌍 Deployment Plan

The final deployment will be on a Linux cloud server (DigitalOcean or AWS):

Nginx → serves static files (frontend) + reverse proxy for FastAPI backend.

FastAPI (Uvicorn/Gunicorn) → runs backend app.

PostgreSQL → stores contact form submissions.

Namecheap domain → zsolt-csengeri.com will point to the server’s IP.

Certbot → enables HTTPS with Let’s Encrypt.

📌 Branches

main → static version of my CV site (GitHub Pages).

fastapi-contact-form → development branch with FastAPI + PostgreSQL backend.

✨ Future Improvements

Email notification on new contact form submission.

Admin panel to view messages.

Dockerize backend for easier deployment.