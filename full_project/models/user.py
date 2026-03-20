from models.task import Task


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.tasks = []

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "tasks": [task.to_dict() for task in self.tasks]
        }

    @staticmethod
    def from_dict(data):
        user = User(data["username"], data["password"])
        user.tasks = [Task.from_dict(t) for t in data.get("tasks", [])]
        return user
