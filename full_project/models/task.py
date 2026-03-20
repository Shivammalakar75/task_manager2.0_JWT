class Task:
    def __init__(self, task_id, title, description, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        return Task(
            data["task_id"],
            data["title"],
            data["description"],
            data.get("status", "Pending")
        )
