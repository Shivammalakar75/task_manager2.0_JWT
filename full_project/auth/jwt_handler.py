
import jwt
import datetime


JWT_SECRET = "task_manager_secret_key_change_in_prod"
JWT_ALGORITHM = "HS256"
JWT_EXPIRY_HOURS = 2          
JWT_EXPIRY_MINUTES = 10


def generate_token(username: str) -> str:
    
    payload = {
        "username": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=JWT_EXPIRY_MINUTES),
        "iat": datetime.datetime.utcnow(),
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token


def verify_token(token: str) -> str | None:

    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload["username"]
    except jwt.ExpiredSignatureError:
        print("[Session expired. Please log in again.]")
        return None
    except jwt.InvalidTokenError:
        print("[Invalid session token. Please log in again.]")
        return None
