# app/auth/auth.py

from app.auth.login import login
from app.auth.signup import signup
from app.auth.session import session


def auth_menu():
    while True:
        print("\n--- Welcome to Airline Reservation System ---")
        print("1. Login")
        print("2. Sign Up")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            if login():
                break
        elif choice == "2":
            signup()
        elif choice == "3":
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")
