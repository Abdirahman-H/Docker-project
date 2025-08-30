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

yaml
Copy code

---

## 🛠️ Local Development

### 1️⃣ Clone Repository
```bash
git clone https://github.com/<your-username>/flask-postgres-app.git
cd flask-postgres-app
2️⃣ Build & Run with Docker Compose
bash
Copy code
docker-compose up --build
3️⃣ Initialize PostgreSQL
Access the DB container:

bash
Copy code
docker exec -it <db_container_id> psql -U flaskuser -d flaskdb
Create a table:

sql
Copy code
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);
4️⃣ Test the API
Add item

bash
Copy code
curl -X POST http://localhost:5000/items \
-H "Content-Type: application/json" \
-d '{"name":"Docker Flask"}'
Fetch items

bash
Copy code
curl http://localhost:5000/items
☁️ Push to AWS ECR
Authenticate Docker with ECR

bash
Copy code
aws ecr get-login-password --region <region> | \
docker login --username AWS --password-stdin <account_id>.dkr.ecr.<region>.amazonaws.com
Build & Tag Image

bash
Copy code
docker build -t flask-postgres-app ./backend
docker tag flask-postgres-app:latest <account_id>.dkr.ecr.<region>.amazonaws.com/flask-postgres-app:latest
Push Image

bash
Copy code
docker push <account_id>.dkr.ecr.<region>.amazonaws.com/flask-postgres-app:latest
🔮 Future Improvements
Add JWT authentication

Deploy with AWS ECS Fargate

API documentation with Swagger/OpenAPI

CI/CD pipeline using GitHub Actions

📸 Screenshots
image.png

📜 License
MIT License © 2025