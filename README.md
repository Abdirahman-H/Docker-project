# Flask + PostgreSQL API (Dockerized & Pushed to AWS ECR)

This project is a **Flask web application** with a **PostgreSQL database**, containerized using **Docker**, styled with **HTML/CSS**, and pushed to **AWS Elastic Container Registry (ECR)** for deployment.  

---

## 🚀 Features
- REST API built with **Flask**  
- **PostgreSQL** integration for persistent storage  
- Styled **HTML/CSS frontend** for better UI  
- Fully **Dockerized** with `Dockerfile` and `docker-compose.yml`  
- Pushed to **AWS ECR** for cloud deployment  

---

## 📂 Project Structure

flask-postgres-app/
│── backend/
│ ├── app.py # Flask app with routes
│ ├── requirements.txt # Python dependencies
│ ├── Dockerfile # Backend Dockerfile
│ ├── templates/ # HTML templates
│ ├── static/ # CSS files
│── docker-compose.yml # Local dev setup