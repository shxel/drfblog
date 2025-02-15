

# **DRF Blog API** 
A modern, scalable **Blog API** built with Django REST Framework (DRF), featuring secure authentication, customizable user profiles, and robust CRUD operations for posts and comments. Designed for production with Docker, PostgreSQL, and automated testing.

---

## **Key Features** 
- **🔒 Authentication & Authorization**  
  - JWT-based token authentication for secure user access .
  - Custom user model with email/phone verification and OTP support .
  - Granular permissions: Users can **edit/delete only their posts and profiles** .
- **📝 Blog Management**  
  - Create, retrieve, update, and delete blog posts.
  - Nested comments with threaded replies.
  - Advanced filtering and search for posts (e.g., by tags, author, date).
- **⚙️ Production-Ready Setup**  
  - Dockerized environment with multi-stage configurations (dev, staging, production) .
  - PostgreSQL database for scalability .
  - NGINX and Gunicorn for optimized static file serving .
- **📊 Automated Workflows**  
  - GitHub Actions for CI/CD (automated testing and deployment) .
  - Load testing via Locust for performance optimization .
- **📚 Interactive API Documentation**  
  - OpenAPI 3.0 schema with **drf-spectacular** .
  - Swagger UI and ReDoc for endpoint exploration .

---

## **Technologies Used**
- **Backend**: Django 3.2+, DRF 3.12+
- **Database**: PostgreSQL
- **Auth**: JWT, OTP (via Simple JWT and cache)
- **Infrastructure**: Docker, NGINX, Gunicorn
- **Tools**: Black, Flake8 (linting), Pytest (testing) 

---

## **Installation**
### **Prerequisites**
- Docker and Docker Compose 
```bash
git clone https://github.com/nader-chan/drfblog.git
cd drfblog
```

### **Setup Environment Variables**
1. Create `.env` and `.env.db` files (see `.env.example` for reference) .
2. Configure secrets for `SECRET_KEY`, `DB_NAME`, `DB_USER`, etc.

### **Run with Docker**
```bash
# Build and start containers
docker-compose -f docker-compose.prod.yml up --build -d

# Create superuser
docker-compose exec web python manage.py createsuperuser
```

---

## **API Endpoints** 
Explore endpoints interactively:
- **Swagger UI**: `http://localhost:8000/api/docs/swagger/`
- **ReDoc**: `http://localhost:8000/api/docs/redoc/`

Example endpoints:
- `POST /api/auth/login/`: JWT token generation.
- `GET /api/posts/`: List all published posts.
- `POST /api/posts/`: Create a new post (authenticated users only).

---

## **Testing & Linting** 
```bash
# Run tests
docker-compose exec backend pytest .

# Format code
docker-compose exec backend sh -c "black -l 77 . && flake8 ."
```

---

## **License**
MIT License. See `LICENSE` for details.

---

**Contribute**: Feel free to submit issues or PRs!  
**Questions?** Reach out via [GitHub Discussions](https://github.com/nader-chan/drfblog/discussions).

---