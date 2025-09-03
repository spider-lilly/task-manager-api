from app import mysql
from app.model.User import User
class user_repository:
    def __init__(self):
        pass
    def set(self, user: User):
        self.username = user.username
        self.email = user.email
        self.password = user.password
    def all(self):
        cur= mysql.connection.cursor()
        cur.execute("SELECT * FROM users;")
        rows = cur.fetchall()
        cur.close()
        return rows
    def find_by_id(self,id):
        cur= mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE id = %s;", (id,))
        row = cur.fetchone()
        cur.close()
        if row is None:
            return {"message": "User not found"}
        return row
    def find_by_username(self,username):
        cur= mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s;", (username,))
        row = cur.fetchone()
        cur.close()
        if row is None:
            return {"message": "User not found"}
        return row
    def save(self):
        cur= mysql.connection.cursor()
        cur.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s);", (self.username, self.email, self.password))
        mysql.connection.commit()
        user_id = cur.lastrowid  
        cur.close()
        return {"message": "User created successfully!","user_id": user_id}
    def delete(self, user_id,password):
        check=self.find_by_id(user_id)
        if "message" in check:
            return check
        if check['password'] != password:
            return {"error": "Incorrect password."}
        cur= mysql.connection.cursor()
        cur.execute("DELETE FROM users WHERE id = %s;", (user_id,))
        cur.execute("DELETE FROM tasks WHERE user_id = %s;", (user_id,))
        mysql.connection.commit()
        cur.close()
        return {"message": "User deleted successfully!"}