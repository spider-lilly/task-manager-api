from app import mysql
from app.model.Task import Task
class task_repository:
    def __init__(self):
        pass
    def set(self, task: Task):

        self.user_id = task.user_id
        self.title = task.title
        self.description = task.description
        self.status = task.status
        self.due_date = task.due_date
    def show(self,user_id):
        cur= mysql.connection.cursor()
        cur.execute("SELECT * FROM tasks WHERE user_id = %s;", (user_id,))
        rows = cur.fetchall()
        cur.close()
        return rows
    def all(self):
        cur= mysql.connection.cursor()
        cur.execute("SELECT * FROM tasks;")
        rows = cur.fetchall()
        cur.close()
        return rows
    def save(self):
        cur= mysql.connection.cursor()
        cur.execute("INSERT INTO tasks (user_id, title, description, status, due_date) VALUES (%s, %s, %s, %s, %s);", (self.user_id, self.title, self.description, self.status,self.due_date))
        mysql.connection.commit()
        task_id = cur.lastrowid  
        cur.close()
        return {"message": "Task created successfully!","task_id": task_id}
    def update(self, task_id,updates: dict):
        if not updates:
            return {"message": "No updates provided!"}
        for key, value in updates.items():
            cur= mysql.connection.cursor()
            cur.execute(f"UPDATE tasks SET {key} = %s WHERE id = %s;", (value, task_id))
        mysql.connection.commit()
        cur.close()
        return {"message": "Task updated successfully!"}
    def delete(self, task_id):
        cur= mysql.connection.cursor()
        cur.execute("DELETE FROM tasks WHERE id = %s;", (task_id,))
        mysql.connection.commit()
        cur.close()
        return {"message": "Task deleted successfully!"}