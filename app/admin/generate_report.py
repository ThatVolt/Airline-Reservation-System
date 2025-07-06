from app.db import get_connection
from tabulate import tabulate


def generate_report():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            flight_id,
            source,
            destination,
            date,
            booked_seats,
            FORMAT(booked_seats * price, 2) AS revenue
        FROM flights
    """
    )
    rows = cursor.fetchall()

    if rows:
        headers = [
            "Flight Number",
            "Source",
            "Destination",
            "Date",
            "Bookings",
            "Revenue",
        ]
        print("\n--- Flight Report ---")
        print(
            tabulate(
                rows,
                headers=headers,
                tablefmt="grid",
                colalign=("center",) * len(headers),
            )
        )
    else:
        print("No flight data available.")

    # Totals
    cursor.execute("SELECT SUM(booked_seats), SUM(booked_seats * price) FROM flights")
    total_bookings, total_revenue = cursor.fetchone()

    print(f"\nTotal Bookings: {total_bookings or 0}")
    print(f"Total Revenue: ${total_revenue or 0:.2f}\n")

    cursor.close()
    conn.close()
