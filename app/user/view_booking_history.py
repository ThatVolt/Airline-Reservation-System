# app/user/view_booking_history.py
from app.db import get_connection
from app.auth.session import session
from tabulate import tabulate


def view_booking_history():
    if not session["user_id"]:
        print("You need to log in to view your booking history.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT r.id, f.flight_id, f.source, f.destination, f.date, r.seat_number
        FROM reservations r
        JOIN flights f ON r.flight_id = f.flight_id
        WHERE r.user_id = %s
        ORDER BY f.date DESC
    """,
        (session["user_id"],),
    )

    rows = cursor.fetchall()
    if not rows:
        print("\nYou have no bookings yet.\n")
    else:
        print("\n--- Your Booking History ---")
        print(
            tabulate(
                rows,
                headers=["Reservation ID", "Flight", "From", "To", "Date", "Seat"],
                tablefmt="grid",
            )
        )

    cursor.close()
    conn.close()
