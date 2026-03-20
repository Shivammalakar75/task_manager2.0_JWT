import bcrypt                                   
from models.user import User
from auth.jwt_handler import generate_token    


def sign_up(users):

    print("\n--- SIGN UP ---")
    username = input("Enter username: ")

    if any(u.username == username for u in users):
        print("Username already exists!")
        return

    password = input("Enter password: ")

    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    new_user = User(username, hashed)
    users.append(new_user)

    from storage.file_manager import save_users
    save_users(users)
    print("Sign up successful!")


def log_in(users):
    
    print("\n--- LOG IN ---")
    username = input("Enter username: ")
    password = input("Enter password: ")

    for user in users:
        if user.username == username:
            if bcrypt.checkpw(password.encode(), user.password.encode()):
                print("Login successful!")

                token = generate_token(username)
                return user, token

    print("Invalid credentials!")
    return None, None  
