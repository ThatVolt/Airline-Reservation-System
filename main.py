import os
from app.auth.auth import auth_menu
from app.auth.session import session
from app.user.book_flight import book_flight
from app.user.cancel_booking import cancel_booking
from app.user.show_flights import show_flights
from app.user.search_flights import search_flights
from app.user.view_booking_history import view_booking_history
from app.admin.admin_panel import admin_panel
from app.admin.dashboard import dashboard
from app.admin.generate_report import generate_report
from app.admin.flight_status import update_flight_status
from app.admin.export_csv import export_reservations_to_csv


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    auth_menu()

    while True:
        clear()
        print("\nAirline Reservation System")
        print(
            "Logged in as:",
            session["username"],
            "| Role:",
            session["role"].capitalize(),
        )

        if session["role"] == "admin":
            menu = {
                "1": ("Dashboard", dashboard),
                "2": ("Show All Flights", show_flights),
                "3": ("Manage Flights (Admin Panel)", admin_panel),
                "4": ("Flight Status Management", update_flight_status),
                "5": ("Generate Report", generate_report),
                "6": ("Export Reservations to CSV", export_reservations_to_csv),
                "7": ("Logout", None),
            }
        else:
            menu = {
                "1": ("Show Flights", show_flights),
                "2": ("Search Flights", search_flights),
                "3": ("Book Flight", book_flight),
                "4": ("Cancel Booking", cancel_booking),
                "5": ("My Booking History", view_booking_history),
                "6": ("Logout", None),
            }

        for key, (desc, _) in menu.items():
            print(f"{key}. {desc}")

        choice = input("\nChoose an option: ").strip()

        if session["role"] == "admin" and choice == "7":
            break
        elif session["role"] != "admin" and choice == "6":
            break

        action = menu.get(choice)
        if action:
            clear()
            action[1]()
        else:
            print("Invalid choice.")

        input("\nPress Enter to continue...")

    print("\nLogged out. Thank you for using Airline Reservation System!")


if __name__ == "__main__":
    main()
