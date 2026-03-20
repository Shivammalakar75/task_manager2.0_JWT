# Task Manager 2.0 — with JWT Authentication

A Python CLI-based Task Manager with JWT session authentication.

## Project Structure

```
task_manager2.0/
├── main.py                    # Entry point (JWT-integrated)
├── requirements.txt
├── data/
│   └── users.json             # Persistent user + task storage (auto-created)
├── models/
│   ├── user.py                # User model
│   └── task.py                # Task model
├── auth/
│   ├── authentication.py      # sign_up / log_in (JWT token generated on login)
│   └── jwt_handler.py         # [NEW] JWT generate + verify utilities
├── services/
│   └── task_service.py        # Task CRUD operations
└── storage/
    └── file_manager.py        # JSON load/save helpers
```

## Setup

```bash
pip install -r requirements.txt
python main.py
```

## JWT Changes Summary

| File | Change |
|------|--------|
| `auth/jwt_handler.py` | **NEW** — `generate_token()` and `verify_token()` |
| `auth/authentication.py` | `log_in()` now returns `(user, token)` |
| `main.py` | Added `SESSION_TOKEN`, `require_valid_token()` guard on all task ops |

The CLI menus and workflow are **completely unchanged**.
