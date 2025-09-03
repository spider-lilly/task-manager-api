from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    username: str
    email: str
    password: str
    id: Optional[int] = None

    def validate(self):
        if not self.username or len(self.username) < 3:
            raise ValueError("Username must be at least 3 characters long")
        if not '@' in self.email:
            raise ValueError("Invalid email format")
        if len(self.password) < 6:
            raise ValueError("Password must be at least 6 characters long")