from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Task:
    user_id: int
    title: str
    description: str
    status: str
    due_date: datetime
    id: Optional[int] = None

    def validate(self):
        if not self.title:
            raise ValueError("Title cannot be empty")
        if not self.user_id:
            raise ValueError("Task must be assigned to a user")


