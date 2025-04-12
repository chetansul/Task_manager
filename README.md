# 🧠 FastAPI Task Manager API

This is a backend-only project built with **FastAPI**, designed to learn API development from basic to advanced — one day, one milestone at a time. The project focuses on building a **task management API** and testing endpoints using **Postman**, without a frontend.

We are using **MySQL** (coming up), and tracking everything on GitHub using branches for each day.

---

## 📅 Daily Progress Overview

| Day | Topics / Milestone                           | Status   |
|-----|-----------------------------------------------|----------|
| 1   | Project Setup + Hello World                   | ✅ Done   |
| 2   | Task CRUD with In-Memory Storage              | ✅ Done   |
| 3   | Refactor Code with UUIDs & Modular Structure  | ✅ Done   |
| 4+  | MySQL Integration, Auth, Filtering, etc.      | 🔜 Coming Soon

---

## 📘 Day 1 – Project Setup & First Endpoint

### ✅ What Was Done
- Created virtual environment (`env`)
- Installed FastAPI and Uvicorn
- Created `main.py` with a simple `"Hello World"` endpoint
- Tested endpoint using Postman and browser
- Generated `requirements.txt`
- Initialized Git repo and pushed to GitHub

### 💡 Why It Was Done
- Setting up the dev environment is the first step in any project
- FastAPI gives automatic Swagger UI for testing
- Virtual environment helps isolate dependencies
- GitHub tracks changes and enables version control

---

## 📘 Day 2 – Task CRUD with In-Memory Storage

### ✅ What Was Done
- Created a `Task` model using Pydantic
- Built API endpoints:
  - `POST /tasks` – Create a task
  - `GET /tasks` – List all tasks
  - `GET /tasks/{id}` – Get task by ID
  - `PUT /tasks/{id}` – Update task
  - `DELETE /tasks/{id}` – Delete task
- Stored tasks in a Python list (in-memory)
- Tested everything with Postman
- Pushed to a separate branch (`day-2-task-crud`)

### 💡 Why It Was Done
- CRUD (Create, Read, Update, Delete) is the core of any backend
- In-memory storage is fast for learning and testing without DB setup
- Pydantic helps validate and serialize input data automatically

---

## 📘 Day 3 – Refactor with UUIDs & Modular Routing

### ✅ What Was Done
- Replaced numeric IDs with auto-generated `UUIDs`
- Separated logic into:
  - `models.py` – Pydantic models
  - `routes/tasks.py` – All task-related routes
  - `main.py` – App entry point with router include
- Cleaned up the project structure for scalability

### 💡 Why It Was Done

#### ✅ UUIDs
- Universally unique, non-sequential identifiers (e.g. `e91d...-a20d`)
- Prevents ID collisions
- More secure and production-ready than integers
- Easily generated using `uuid4()` from Python’s `uuid` module

#### ✅ Routers (`APIRouter`)
- Lets you break your app into logical modules
- Easier to scale as features grow (e.g., add users, auth, etc.)
- Keeps code organized and clean

## 🧠 Important to Remember (Day 1 - Day 3)

---

### 📅 Day 1 – Setup & First Endpoint
- Always activate your virtual environment before coding.
- Use `uvicorn app.main:app --reload` for hot-reload development.
- FastAPI auto-generates Swagger UI at `http://127.0.0.1:8000/docs`.
- Track dependencies using `pip freeze > requirements.txt`.
- Use `.gitignore` to avoid pushing folders like `env/`, `__pycache__/`.

---

### 📅 Day 2 – CRUD with In-Memory Storage
- Use **Pydantic models** for clean, validated input/output.
- In-memory list storage is temporary and resets on server restart.
- Always test each CRUD operation using Postman.
- Return clear status codes and messages using FastAPI's `HTTPException`.

---

### 📅 Day 3 – UUIDs & Modular Routing
- Use `uuid4()` from Python to generate unique task IDs.
- UUIDs are better than integers for production-level identification.
- Use `APIRouter()` to split logic into route modules.
- Organize code into:
  - `models.py` for data models
  - `routes/` for endpoint logic
  - `main.py` for app startup and router includes

---

### ✅ Bonus Best Practices (So Far)
- Keep each Python file focused on a single job (separation of concerns).
- Write meaningful commit messages like `Day 2: CRUD with in-memory`.
- Create a new branch for each day to keep code clean and trackable.
- Use `.gitignore` to exclude `__pycache__`, `env`, `.idea`, `.vscode`, etc.
