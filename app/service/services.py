from app.repository.user_repository import user_repository
from app.repository.task_repository import task_repository
from app.model.Task import Task
from app.model.User import User
class srv:
    def __init__(self):
        self.ur= user_repository()
        self.tr= task_repository()
    def create_user(self,username,email,password):
        try:
            user= User(username=username,email=email,password=password)
            user.validate()
            self.ur.set(user)
            result = self.ur.save()
            return result
        except ValueError as ve:
            return {"error": str(ve)}
        except Exception as e:
            print(e)
            return {"error": "An error occurred while creating the user..."}
    def create_task(self,user_id,title,description,status,due_date):
        try:
            task= Task(user_id=user_id,title=title,description=description,status=status,due_date=due_date)
            task.validate()
            self.tr.set(task)
            result = self.tr.save()
            return result
        except ValueError as ve:
            return {"error": str(ve)}
        except Exception as e:
            return {"error": "An error occurred while creating the task."}

