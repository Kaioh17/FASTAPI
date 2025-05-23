# FastAPI Learning Project

This project is a hands-on learning exercise for FastAPI, a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Purpose
I created this project to:
- Learn and practice FastAPI fundamentals
- Organize code using routers for authentication, users, and posts
- Understand how to structure a real-world API project
- Make it easy to access, modify, and extend all files as I learn

## Features
- User registration and authentication (JWT-based)
- CRUD operations for posts
- SQLAlchemy ORM integration
- Password hashing with passlib
- Modular code structure using routers

## Getting Started

### Requirements
- Python 3.10+
- PostgreSQL (or update the database URL in `app/database.py` for your DB)

### Setup
1. **Clone the repository**
2. **Create a virtual environment**
   ```cmd
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. **Install dependencies**
   ```cmd
   pip install fastapi[all] uvicorn sqlalchemy psycopg2 passlib[bcrypt] python-jose
   ```
   Or use the requirements in the README for password hashing:
   ```powershell
   pip install passlib[bcrypt] bcrypt==3.2.0
   ```
4. **Configure your database**
   - Update the connection string in `app/database.py` if needed.
   - Default is PostgreSQL with user `postgres` and password `1308`.

5. **Run the application**
   ```powershell
   uvicorn app.main:app --reload
   ```

6. **Access the API docs**
   - Open [http://localhost:8000/docs](http://localhost:8000/docs) in your browser.

## Project Structure
- `app/routers/` — Contains route logic for authentication, users, and posts
- `app/models.py` — SQLAlchemy models
- `app/schemas.py` — Pydantic schemas
- `app/database.py` — Database connection and session
- `app/oauth2.py` — JWT authentication logic
- `app/utils.py` — Utility functions (e.g., password hashing)
- `app/main.py` — FastAPI app entry point

## Notes
- This project is for learning purposes. Security and error handling are basic.
- You can easily add new features or endpoints as you learn more.
- All files are organized for easy access and modification.



---
