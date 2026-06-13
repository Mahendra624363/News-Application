# 📰 News Application (Django REST Framework Backend)

A backend-only News Application built using Django REST Framework. It provides secure authentication using JWT and manages news content through RESTful APIs with a modular architecture.

---

## 🚀 Tech Stack

- Python
- Django
- Django REST Framework
- SimpleJWT (JWT Authentication)
- SQLite / MySQL
- Postman (API Testing)

---

## 🏗️ Project Structure

This project contains two main apps:

- accounts → Handles user authentication and profile management  
- news → Handles CRUD operations for news articles  
- config → Project settings and URL routing  

---

## 🔐 Authentication System (JWT)

This project uses JWT (JSON Web Token) for authentication.

### Flow:
- User registers
- User logs in and receives access & refresh tokens
- Token is sent in request headers for protected APIs

### Authorization Header:
Authorization: Bearer <access_token>

---

## 🔑 Authentication APIs

POST /accounts/register/ → Register new user  
POST /accounts/login/ → Get JWT tokens  
POST /accounts/refresh/ → Refresh access token  
POST /accounts/logout/ → Logout user  
GET /accounts/profile/ → Get user profile  

---

## 📰 News APIs (ViewSet + Router)

GET /news/ → List all news articles  
POST /news/ → Create a news article  
GET /news/<id>/ → Retrieve a single article  
PUT /news/<id>/ → Update a news article  
DELETE /news/<id>/ → Delete a news article  

---

## ⚙️ Features

- JWT-based authentication system  
- User registration, login, logout, profile APIs  
- Full CRUD operations for news  
- RESTful API architecture  
- Router-based URL management  
- Modular Django project structure  

---

## 🧠 Key Implementations

- Django REST Framework ViewSets for CRUD operations  
- DefaultRouter for automatic API routing  
- SimpleJWT for authentication  
- Custom API views (Register, Login, Logout, Profile)  
- Modular app separation (accounts + news)  

---

## 🧪 Tools Used

- Postman → API testing  
- Django Admin Panel → Database management  
- Git & GitHub → Version control  

---

## ▶️ How to Run Locally

1. Clone repository  
git clone <repo-url>  
cd News-Application  

2. Create virtual environment  
python -m venv venv  

3. Activate environment  
Windows: venv\Scripts\activate  
Mac/Linux: source venv/bin/activate  

4. Install dependencies  
pip install -r requirements.txt  

5. Run migrations  
python manage.py makemigrations  
python manage.py migrate  

6. Create superuser (optional)  
python manage.py createsuperuser  

7. Run server  
python manage.py runserver  

---

## 📌 API Testing Example

Login API:  
POST http://127.0.0.1:8000/accounts/login/  

For protected APIs use:  
Authorization: Bearer <access_token>  

---

## 📂 Project Highlights

- Secure JWT authentication  
- Modular Django architecture  
- REST API using ViewSets and Routers  
- Backend-only scalable design  
- Fully testable via Postman  

---

## 🎯 Learning Outcomes

- Django REST Framework development  
- JWT authentication implementation  
- REST API design principles  
- Backend architecture design  
- Real-world API development workflow  

---

## 📄 Note

This project is developed for learning backend development, API design, and authentication systems using Django REST Framework.
