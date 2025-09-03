# 📝 Task Manager API

A simple **Flask + MySQL REST API** that provides CRUD operations for **Users** and **Tasks**.
Built using the Flask Application Factory pattern with a layered architecture (**config → model → repository → service → controller**).

---

## 🚀 Features

* ✅ User Management (create, fetch, find by ID/username, delete)
* ✅ Task Management (create, fetch, update, delete, get user’s tasks)
* ✅ MySQL Database Integration with `Flask-MySQLdb`
* ✅ Environment-based configuration (`.env`)
* ✅ Clean modular project structure

---

## 📂 Project Structure

```
app/
 ├── config/
 │    └── settings.py        # Config (MySQL, dotenv, secret key)
 │
 ├── controller/
 │    └── main.py            # API routes (users & tasks CRUD)
 │
 ├── model/
 │    ├── Task.py            # Task model (data structure)
 │    └── User.py            # User model (data structure)
 │
 ├── repository/
 │    ├── task_repository.py # DB queries for tasks
 │    └── user_repository.py # DB queries for users
 │
 ├── service/
 │    └── services.py        # Business logic (task/user handling)
 │
 ├── __init__.py             # App factory (create_app)
 │
run.py                       # Entry point
requirements.txt             # Dependencies
.env                         # Environment variables (ignored in git)
```

---

## ⚙️ Installation

### 1️⃣ Clone the repo

```bash
git clone https://github.com/your-username/task-manager-api.git
cd task-manager-api
```

### 2️⃣ Setup virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Setup `.env` file

Create a `.env` file in the root directory:

```ini
MYSQL_USER=your_mysql_user
MYSQL_PASSWORD=your_mysql_password
MYSQL_DB=your_database
SECRET_KEY=your_secret_key
```

### 5️⃣ Run the app

```bash
python run.py
```

The API will be available at:
👉 **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

## 📡 API Endpoints

### 🔹 Root

* `GET /` → Health check

---

### 🔹 Users

* `GET /users` → Get all users
* `GET /user/<id>` → Get user by ID
* `GET /user/username/<username>` → Get user by username
* `POST /create/user` → Create new user
* `DELETE /user/delete` → Delete user (requires `user_id` & `password`)

#### Example: Create User

**Request**

```http
POST /create/user
Content-Type: application/json
```

```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "securepass123"
}
```

**Response**

```json
{
  "message": "User created successfully",
  "user_id": 1
}
```

---

### 🔹 Tasks

* `GET /tasks` → Get all tasks
* `GET /user/<id>/tasks` → Get tasks for a user
* `POST /create/task` → Create new task
* `PUT /task/update/<id>` → Update task
* `DELETE /task/delete/<id>` → Delete task

#### Example: Create Task

**Request**

```http
POST /create/task
Content-Type: application/json
```

```json
{
  "user_id": 1,
  "title": "Finish project",
  "description": "Complete the Flask-MySQL API project",
  "status": "pending",
  "due_date": "2025-09-10"
}
```

**Response**

```json
{
  "message": "Task created successfully",
}
```

---

## 🛠️ Tech Stack

* **Backend:** Flask 3.1.2
* **Database:** MySQL (`mysqlclient`, `Flask-MySQLdb`)
* **Environment:** python-dotenv
* **Others:** Jinja2, Werkzeug

---

## 📜 License

This project is licensed under the **MIT License**.
You are free to use, modify, and distribute this software, provided that the original license is included in any copies or substantial portions of the software.
