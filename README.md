# 🧠 FastAPI Task Manager (Backend Only)

This project is a backend-only Task Manager API built using **FastAPI**, tested with **Postman**, and connected to a **MySQL** database. The project is structured for daily project-based learning from beginner to advanced levels.

---

## ✅ Day-by-Day Progress

### 🗓 Day 1: Project Setup
- Initialized FastAPI project
- Created folder structure (`app/`, `main.py`)
- Created `.gitignore` to ignore virtual env and system files
- Used GitHub Desktop for version control
- Set up virtual environment and installed dependencies

**Important Points:**
- Always use a virtual environment
- Commit regularly after every task
- Use `.gitignore` to keep the repo clean

---

### 🗓 Day 2: In-Memory CRUD API
- Implemented basic CRUD for tasks using a Python list
- Created Pydantic models for request & response validation

**Key Concepts:**
- `BaseModel` from Pydantic for validation
- HTTP methods: `POST`, `GET`, `PUT`, `DELETE`
- Use of `List[Task]` in response models

---

### 🗓 Day 3: Modular Routing
- Split routes into a separate file `task.py` under `routers/`
- Used FastAPI's `APIRouter` to keep code modular
- Introduced `UUID` for task IDs (later replaced by `int` for DB compatibility)

**Important Concepts:**
- `UUID` provides globally unique identifiers (used temporarily)
- `APIRouter` helps in route modularity and organization

---

### 🗓 Day 4: Database Integration (MySQL)
- Connected FastAPI with MySQL using SQLAlchemy
- Created `Task` model with auto-increment `id` (changed from UUID)
- Created `create_tables.py` to initialize tables
- Used `.env` file to store DB credentials securely
- Added `.env` to `.gitignore` so secrets don’t get pushed to GitHub

**Important Code Components:**
- `create_engine`: Connects to your MySQL database
- `SessionLocal`: Used to create DB sessions for querying and transactions
- `Base`: Base class for all models, used for table mapping

**Issue Faced & Solution:**
> ❌ Problem: Python was not recognizing `app` as a module  
> ✅ Fix: Use this command to run table creation:

python -m app.create_tables

### 🗓 Day 5: Full CRUD with SQLAlchemy + Bulk Support

- Fully implemented all database operations using SQLAlchemy:
  - ✅ **Create a Task** using `POST /tasks`
  - ✅ **Get All Tasks** using `GET /tasks`
  - ✅ **Get Task by ID** using `GET /tasks/{id}`
  - ✅ **Update Task** using `PUT /tasks/{id}`
  - ✅ **Delete Task** using `DELETE /tasks/{id}`
  - ✅ **Bulk Create Tasks** using `POST /tasks/bulk`

**Why It Was Done:**
- To replace in-memory task storage with real database persistence
- To follow RESTful API design using actual DB operations

**New Concepts Introduced:**
- `.add_all([...])`: Efficiently inserts multiple rows in one go
- `.refresh()`: Updates model instances with DB-generated fields like auto-ID
- `HTTPException`: Used to handle cases like "task not found"
- `response_model`: Used to validate and serialize response output via Pydantic

**Improvements Over Day 2:**
- Switched from Python list to SQLAlchemy DB model
- Implemented error handling with proper HTTP status codes
- Used a consistent response format (`{ "message": ..., "data": ... }`)

**Important Note:**
- The `GET /tasks` route must return a **list of tasks**, not a dict. Wrap additional metadata like messages outside of the endpoint's `response_model`.

```python
# ❌ This will break response_model = list[TaskResponse]
return { "message": "Fetched", "data": task_list }

# ✅ This works with response_model = list[TaskResponse]
return task_list

