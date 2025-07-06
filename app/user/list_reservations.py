from tabulate import tabulate
from app.db import get_connection


def list_reservations():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT reservation_id, name, email, flight_id, booking_date
        FROM reservations
    """
    )
    rows = cursor.fetchall()

    if not rows:
        print("\nNo reservations found.\n")
    else:
        headers = ["Reservation ID", "Name", "Email", "Flight", "Booking Date"]
        print("\n--- Current Reservations ---")
        print(
            tabulate(
                rows,
                headers=headers,
                tablefmt="grid",
                colalign=("center",) * len(headers),
            )
        )

    cursor.close()
    conn.close()
