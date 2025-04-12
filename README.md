# 🧠 FastAPI Task Manager Backend

A learning-based backend project using **FastAPI** and **MySQL** (coming soon) — designed to go from basic to advanced features by building a real-world task manager API.  
Tested via **Postman**, no frontend involved.

---

## ✅ Project Progress

| Day | Topics Covered                        | Status   |
|-----|----------------------------------------|----------|
| 1   | Project setup, virtual env, FastAPI basics | ✅ Done    |
| 2   | Task CRUD using in-memory storage      | ✅ Done    |
| 3+  | Coming soon...                         | 🔜        |

---

## 📅 Day 1 – Project Setup & Hello World

### ✅ What I Did
- Created project folder and initialized FastAPI app
- Set up virtual environment
- Installed dependencies: `fastapi`, `uvicorn`
- Created first endpoint: `GET /` returning a Hello message
- Ran the server and tested with browser/Postman
- Committed project to GitHub

### 📘 Topics Covered
- Virtual environments
- FastAPI basics: `FastAPI()`, decorators (`@app.get`)
- Running app using `uvicorn`
- Basic routing and response structure
- Python package management (`requirements.txt`)
- GitHub project flow

### 📌 Important to Remember
- Always activate your virtual environment before running the app
- `uvicorn app.main:app --reload` auto-reloads on changes
- FastAPI provides automatic Swagger docs at `/docs`
- Use `pip freeze > requirements.txt` to track dependencies

---

## 📅 Day 2 – Task CRUD (In-Memory Storage)

### ✅ What I Did
- Created new route endpoints for Task management
- Used `Pydantic` models for request validation
- Implemented full CRUD: Create, Read All, Read by ID, Update, Delete
- Stored tasks in an in-memory Python list
- Tested each route with Postman
- Committed and pushed from a feature branch

### 📘 Topics Covered
- Creating API endpoints using `@app.get`, `@app.post`, etc.
- Path parameters and request bodies
- Pydantic models (`BaseModel`) for defining schemas
- Using `List` from `typing` module
- HTTPException for error handling
- Basic Git branching and merging via GitHub Desktop

### 📌 Important to Remember
- In-memory data is lost when server restarts (useful for testing only)
- FastAPI automatically validates and documents request/response schemas
- Response models make your API cleaner and safer
- `HTTPException(status_code=404)` is the correct way to handle missing resources
- Keep your logic readable and modular as it grows

---

## 🚧 Coming Up
- Day 3: Improved structure, UUIDs instead of manual IDs
- Day 4+: MySQL DB integration using SQLAlchemy
- JWT Auth, User accounts, Task filtering, etc.

---

## 💻 How to Run

```bash
# Step 1: Activate virtual environment
source env/bin/activate   # macOS/Linux
env\Scripts\activate      # Windows

# Step 2: Install requirements
pip install -r requirements.txt

# Step 3: Run the server
uvicorn app.main:app --reload
