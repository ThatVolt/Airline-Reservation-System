from app.db import get_connection
from tabulate import tabulate


def dashboard():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM flights")
    total_flights = cursor.fetchone()[0]

    cursor.execute(
        "SELECT SUM(seats), SUM(booked_seats), SUM(booked_seats * price) FROM flights"
    )
    total_seats, total_booked, total_revenue = cursor.fetchone()

    available_seats = (total_seats or 0) - (total_booked or 0)

    data = [
        ["Total Flights", total_flights],
        ["Total Bookings", total_booked or 0],
        ["Available Seats", available_seats],
        ["Total Revenue", f"${total_revenue or 0:.2f}"],
    ]

    print("\n--- Dashboard ---")
    print(
        tabulate(
            data,
            headers=["Metric", "Value"],
            tablefmt="grid",
            colalign=("center", "center"),
        )
    )

    cursor.close()
    conn.close()
