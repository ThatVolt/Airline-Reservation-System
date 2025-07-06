# app/auth/signup.py

import mysql.connector
from app.db import get_connection
import hashlib


def signup():
    conn = get_connection()
    cursor = conn.cursor()

    username = input("Enter your name: ").strip()
    email = input("Enter your email: ").strip()
    password = input("Enter password: ").strip()
    role = "admin" if input("Sign up as admin? (y/n): ").lower() == "y" else "user"

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    try:
        cursor.execute(
            """
            INSERT INTO users (username, email, password, role)
            VALUES (%s, %s, %s, %s)
        """,
            (username, email, hashed_password, role),
        )

        conn.commit()
        print("\n✅ Signup successful! You can now login.\n")

    except mysql.connector.IntegrityError as e:
        if e.errno == 1062:
            print("\n❌ Signup failed. This email is already registered.\n")
        else:
            print("\n❌ Signup failed due to a database error:", e)

    finally:
        cursor.close()
        conn.close()
