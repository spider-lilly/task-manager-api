from flask import Blueprint, jsonify
from app import mysql
from flask import request
from app.service.services import srv
from app.repository.user_repository import user_repository
from app.repository.task_repository import task_repository
bp = Blueprint("main", __name__)



@bp.route("/")
def home():
    return jsonify({"message": "Flask + MySQL app is running!"})
#get functions
@bp.route("/users")
def get_users():
    ur= user_repository()
    try:
        rows=ur.all()
        return jsonify(rows)
    except Exception as e:
        return jsonify({"error": "An error occurred while fetching users."}), 500
@bp.route("/tasks")
def get_tasks():
    tr= task_repository()
    try:
        rows=tr.all()
        return jsonify(rows)
    except Exception as e:
        return jsonify({"error": "An error occurred while fetching tasks."}), 500
@bp.route("/user/<int:user_id>/tasks")
def get_user_tasks(user_id):
    tr= task_repository()
    try:
        rows=tr.show(user_id)
        return jsonify(rows)
    except Exception as e:
        return jsonify({"error": f"An error occurred while fetching tasks for the user:{user_id}"}), 500
@bp.route("/user/<int:user_id>")
def get_user_by_id(user_id):
    ur= user_repository()
    try:
        row=ur.find_by_id(user_id)
        return jsonify(row)
    except Exception as e:
        return jsonify({"error": f"An error occurred while fetching the user:{user_id}"}), 500
@bp.route("/user/username/<string:username>")
def get_user_by_username(username):
    ur= user_repository()
    try:
        row=ur.find_by_username(username)
        return jsonify(row)
    except Exception as e:
        return jsonify({"error": f"An error occurred while fetching the user:{username}"}), 500
#post functions
@bp.route("/create/user", methods=["POST"])
def create_user():
    svc= srv()
    try:
        data = request.json
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        if not all([username, email, password]):
            return jsonify({"error": "Missing required fields"}), 400
        result = svc.create_user(username,email,password)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": "An error occurred while creating the user."}), 500
@bp.route("/create/task", methods=["POST"])
def create_task():
    svc= srv()
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        title = data.get('title')
        description = data.get('description')
        status = data.get('status')
        due_date = data.get('due_date')
        result = svc.create_task(user_id,title,description,status,due_date)
        return jsonify(result) 
    except Exception as e:
        return jsonify({"error": "An error occurred while creating the task."}), 500 
#put functions
@bp.route("/task/update/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    tr= task_repository()
    updates = request.get_json()
    result = tr.update(task_id, updates)
    return jsonify(result)  
#delete functions
