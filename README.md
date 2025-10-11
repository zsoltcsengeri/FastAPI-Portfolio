PK-Work – CV Website with FastAPI Contact Form
A full-stack personal CV website featuring a contact form with FastAPI backend and PostgreSQL database integration. Originally hosted as a static site on GitHub Pages, this project has been enhanced with a complete backend infrastructure.
Live Demo: zsolt-csengeri.com (coming soon)

🛠️ Tech Stack
Frontend:

HTML5, CSS3 (Vanilla - no frameworks)
JavaScript (ES6+)
Responsive design

Backend:

FastAPI (Python)
SQLAlchemy ORM
Pydantic for data validation
Uvicorn ASGI server

Database:

PostgreSQL

Deployment:

Nginx (reverse proxy & static file serving)
Systemd (service management)
Let's Encrypt SSL/TLS (Certbot)
Cloud hosting: Digital Ocean / AWS


📂 Project Structure
PK-Work/
│
├── backend/                    # FastAPI backend
│   ├── main.py                 # FastAPI app (entry point)
│   ├── models.py               # SQLAlchemy database models
│   ├── database.py             # Database connection & session
│   ├── .env                    # Environment variables (not in repo)
│   └── requirements.txt        # Python dependencies
│
├── frontend/                   # Static website files
│   ├── CV/
│   │   └── Zsolt_Resume.pdf
│   ├── images/
│   ├── index.html              # Main CV page
│   ├── script.js               # Contact form JS logic
│   ├── style.css               # Main styling
│   ├── terms_conditions.html
│   └── terms_style.css
│
├── .gitignore
├── LICENSE
└── README.md

🚀 Running Locally
Prerequisites

Python 3.10+
PostgreSQL 14+
Git

1. Clone the Repository
bashgit clone https://github.com/zsoltcsengeri/PK-Work.git
cd PK-Work
git checkout fastapi-contact-form
2. Set Up Backend
Install Python Dependencies
bashcd backend
python -m venv venv
source venv/bin/activate  # On Linux/Mac
# venv\Scripts\activate   # On Windows

pip install -r requirements.txt
Configure Database
Create PostgreSQL database and user:
sqlCREATE DATABASE cv_site;
CREATE USER cv_app_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE cv_site TO cv_app_user;
GRANT ALL PRIVILEGES ON SCHEMA public TO cv_app_user;
Set Environment Variables
Create a .env file in the backend/ directory:
envDB_HOST=localhost
DB_PORT=5432
DB_NAME=cv_site
DB_USER=cv_app_user
DB_PASSWORD=your_secure_password
Run FastAPI Server
From the project root:
bashuvicorn backend.main:app --reload
Server will start at http://127.0.0.1:8000

API Documentation: http://127.0.0.1:8000/docs
Contact Endpoint: POST /contact

3. Serve Frontend
Open frontend/index.html in a browser, or use a local server:
bash# Using Python
cd frontend
python -m http.server 5500

# Using VS Code Live Server extension (recommended)
4. Test the Contact Form

Open http://127.0.0.1:5500 in your browser
Scroll to the contact form
Fill out and submit
Check database: psql -U cv_app_user -d cv_site -c "SELECT * FROM contacts;"


🌐 API Endpoints
POST /contact
Creates a new contact form submission.
Request Body:
json{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "+44 1234 567890",
  "website": "https://example.com",
  "message": "Hello, I'd like to get in touch!"
}
Response:
json{
  "status": "ok",
  "id": 1
}
GET /contact/{contact_id}
Retrieves a specific contact by ID.
Response:
json{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com"
}

🚢 Production Deployment
Architecture
User Browser
    ↓
Nginx (443) ← SSL/TLS (Let's Encrypt)
    ↓
    ├─→ Static Files (HTML/CSS/JS)
    └─→ Reverse Proxy → FastAPI (8000) → PostgreSQL (5432)
Deployment Steps
1. Server Setup (Ubuntu 22.04)
bash# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install python3-pip python3-venv postgresql nginx certbot python3-certbot-nginx -y
2. PostgreSQL Configuration
bashsudo -u postgres psql
# Create database and user (as shown above)
3. Deploy Application
bash# Clone repository
git clone https://github.com/zsoltcsengeri/PK-Work.git
cd PK-Work/backend

# Set up Python environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Configure .env file
nano .env  # Add production database credentials
4. Create Systemd Service
bashsudo nano /etc/systemd/system/fastapi-cv.service
ini[Unit]
Description=FastAPI CV Contact Form
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/path/to/PK-Work
Environment="PATH=/path/to/PK-Work/backend/venv/bin"
ExecStart=/path/to/PK-Work/backend/venv/bin/uvicorn backend.main:app --host 127.0.0.1 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
bashsudo systemctl daemon-reload
sudo systemctl enable fastapi-cv
sudo systemctl start fastapi-cv
5. Configure Nginx
bashsudo nano /etc/nginx/sites-available/zsolt-csengeri.com
nginxserver {
    listen 80;
    server_name zsolt-csengeri.com www.zsolt-csengeri.com;

    # Static files
    location / {
        root /path/to/PK-Work/frontend;
        index index.html;
        try_files $uri $uri/ =404;
    }

    # API proxy
    location /contact {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
bashsudo ln -s /etc/nginx/sites-available/zsolt-csengeri.com /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
6. Enable HTTPS
bashsudo certbot --nginx -d zsolt-csengeri.com -d www.zsolt-csengeri.com
7. Configure DNS (Namecheap)

Add A record: @ → [Your Server IP]
Add A record: www → [Your Server IP]


🔒 Security Considerations

✅ Environment variables for sensitive data (not committed to Git)
✅ HTTPS/TLS encryption via Let's Encrypt
✅ CORS properly configured for production domain
✅ SQL injection prevention via SQLAlchemy ORM
✅ Input validation using Pydantic models
✅ PostgreSQL user with minimal required privileges
✅ Firewall configured (UFW): only ports 22, 80, 443 open


📌 Git Branches

main → Static CV website (GitHub Pages compatible)
fastapi-contact-form → Full-stack version with backend (current)


🎯 Learning Outcomes
This project demonstrates:

Full-stack web development (frontend + backend + database)
RESTful API design and implementation
Database design and ORM usage
Production deployment on Linux servers
DevOps fundamentals (Nginx, systemd, SSL/TLS)
DNS configuration and domain management
Security best practices


✨ Future Enhancements

 Email notifications on form submission (SMTP integration)
 Admin dashboard to view/manage submissions
 Rate limiting to prevent spam
 Dockerize application for easier deployment
 CI/CD pipeline (GitHub Actions)
 Monitoring and logging (ELK stack or similar)
 Database backup automation


📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

👤 Author
Zsolt Csengeri

Website: zsolt-csengeri.com
LinkedIn: linkedin.com/in/zsolt-csengeri
GitHub: @zsoltcsengeri


🙏 Acknowledgments
This project was developed as part of my continuous learning journey in DevOps and full-stack development, currently undertaking a comprehensive DevOps training course covering:

Linux system administration
Cloud technologies (AWS)
Configuration management (Ansible)
Containerization (Docker)
CI/CD pipelines (Jenkins, GitLab)
Monitoring (ELK Stack, Grafana, Prometheus)


Note: The backend is currently in development. The production deployment will be completed by [target date].
