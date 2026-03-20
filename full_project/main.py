

from storage.file_manager import load_users, save_users
from auth.authentication import sign_up, log_in
from services.task_service import TaskService
from auth.jwt_handler import verify_token          

CURRENT_USER = None
SESSION_TOKEN = None    


def require_valid_token() -> bool:
    
    username = verify_token(SESSION_TOKEN)
    if username is None:
        return False
    return True


def task_menu(users):
    global CURRENT_USER, SESSION_TOKEN

    while CURRENT_USER:

        print(f"\n{f'WELCOME {CURRENT_USER.username.upper()}':^75}")
        print("=" * 75)
        print("1. ADD TASK")
        print("2. VIEW TASKS")
        print("3. VIEW PENDING TASKS")
        print("4. VIEW COMPLETED TASKS")
        print("5. UPDATE TASK")
        print("6. MARK TASK AS COMPLETED")
        print("7. DELETE TASK")
        print("8. LOG OUT")
        choice = input("Enter choice: ")

        match choice:
            case "1":
                if not require_valid_token():  
                    CURRENT_USER = None
                    SESSION_TOKEN = None
                    break
                title = input("Title: ")
                desc = input("Description: ")
                TaskService.add_task(CURRENT_USER, title, desc)
                save_users(users)

            case "2":
                if not require_valid_token():   
                    CURRENT_USER = None
                    SESSION_TOKEN = None
                    break
                TaskService.print_tasks(
                    TaskService.get_tasks(CURRENT_USER)
                )

            case "3":
                if not require_valid_token():   
                    CURRENT_USER = None
                    SESSION_TOKEN = None
                    break
                TaskService.print_tasks(
                    TaskService.get_tasks(CURRENT_USER, "Pending")
                )

            case "4":
                if not require_valid_token():   
                    CURRENT_USER = None
                    SESSION_TOKEN = None
                    break
                TaskService.print_tasks(
                    TaskService.get_tasks(CURRENT_USER, "Completed")
                )

            case "5":
                if not require_valid_token():   
                    CURRENT_USER = None
                    SESSION_TOKEN = None
                    break
                tid = int(input("Task ID: "))
                new_desc = input("New description: ")
                if TaskService.update_task(CURRENT_USER, tid, new_desc):
                    save_users(users)
                else:
                    print("Task not found!")

            case "6":
                if not require_valid_token():  
                    CURRENT_USER = None
                    SESSION_TOKEN = None
                    break
                tid = int(input("Task ID: "))
                if TaskService.mark_completed(CURRENT_USER, tid):
                    save_users(users)
                else:
                    print("Task not found!")

            case "7":
                if not require_valid_token():   
                    CURRENT_USER = None
                    SESSION_TOKEN = None
                    break
                tid = int(input("Task ID: "))
                TaskService.delete_task(CURRENT_USER, tid)
                save_users(users)

            case "8":
                CURRENT_USER = None
                SESSION_TOKEN = None    
                print("Logged out!")

            case _:
                print("Invalid choice!")


def main_menu():
    global CURRENT_USER, SESSION_TOKEN

    users = load_users()

    while True:
        print("\nTASK MANAGEMENT SYSTEM")
        print("1. SIGN UP")
        print("2. LOG IN")
        print("3. EXIT")
        choice = input("Enter choice: ")

        match choice:
            case "1":
                sign_up(users)

            case "2":
                CURRENT_USER, SESSION_TOKEN = log_in(users)
                if CURRENT_USER:
                    task_menu(users)

            case "3":
                print("Goodbye!")
                break

            case _:
                print("Invalid choice!")


if __name__ == "__main__":
    main_menu()
