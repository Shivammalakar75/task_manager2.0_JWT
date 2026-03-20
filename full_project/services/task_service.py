from models.task import Task


class TaskService:

    @staticmethod
    def add_task(user, title, description):
        task_id = len(user.tasks) + 1
        task = Task(task_id, title, description)
        user.tasks.append(task)
        print(f"Task '{title}' added successfully!")

    @staticmethod
    def get_tasks(user, status=None):
        if status:
            return [t for t in user.tasks if t.status == status]
        return user.tasks

    @staticmethod
    def print_tasks(tasks):
        if not tasks:
            print("No tasks found.")
            return
        print(f"\n{'ID':<5} {'Title':<20} {'Description':<35} {'Status':<12}")
        print("-" * 75)
        for task in tasks:
            print(f"{task.task_id:<5} {task.title:<20} {task.description:<35} {task.status:<12}")

    @staticmethod
    def update_task(user, task_id, new_description):
        for task in user.tasks:
            if task.task_id == task_id:
                task.description = new_description
                print("Task updated successfully!")
                return True
        return False

    @staticmethod
    def mark_completed(user, task_id):
        for task in user.tasks:
            if task.task_id == task_id:
                task.status = "Completed"
                print("Task marked as completed!")
                return True
        return False

    @staticmethod
    def delete_task(user, task_id):
        for task in user.tasks:
            if task.task_id == task_id:
                user.tasks.remove(task)
                print("Task deleted successfully!")
                return True
        print("Task not found!")
        return False
