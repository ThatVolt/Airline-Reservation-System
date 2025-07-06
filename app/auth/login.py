import hashlib
from app.db import get_connection
from app.auth.session import session


def login():
    email = input("Email: ").strip()
    password = input("Password: ").strip()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, username, role FROM users WHERE email = %s AND password = %s",
        (email, hashed_password),
    )
    user = cursor.fetchone()

    if user:
        session["user_id"] = user[0]
        session["username"] = user[1]
        session["role"] = user[2]
        print(f"Welcome, {user[1]}! Logged in as {user[2]}.")
        return True
    else:
        print("Invalid credentials.")
        return False
