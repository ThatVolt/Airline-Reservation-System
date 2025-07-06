from app.db import get_connection
from tabulate import tabulate


def show_flights():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT flight_id, source, destination, date, seats, booked_seats, price FROM flights"
    )
    rows = cursor.fetchall()

    if not rows:
        print("No flights available.\n")
        return

    table = []
    for flight_id, source, dest, date, seats, booked, price in rows:
        available = seats - booked
        table.append([flight_id, source, dest, date, available, f"${price:.2f}"])

    headers = ["Flight Number", "Source", "Destination", "Date", "Seats Left", "Price"]
    print("\n--- Available Flights ---")
    print(
        tabulate(
            table, headers=headers, tablefmt="grid", colalign=("center",) * len(headers)
        )
    )
    print()
    cursor.close()
    conn.close()
