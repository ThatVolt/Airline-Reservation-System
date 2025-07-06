# app/admin/flight_status.py
from app.db import get_connection
from tabulate import tabulate


def update_flight_status():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT flight_id, source, destination, date, status FROM flights")
    rows = cursor.fetchall()

    print("\n--- All Flights & Status ---")
    print(
        tabulate(
            rows, headers=["Flight", "From", "To", "Date", "Status"], tablefmt="grid"
        )
    )

    flight_id = input("Enter Flight ID to update status: ").strip()
    new_status = (
        input("Enter new status (Scheduled / Delayed / Cancelled): ")
        .strip()
        .capitalize()
    )

    if new_status not in ["Scheduled", "Delayed", "Cancelled"]:
        print("Invalid status. Must be Scheduled, Delayed, or Cancelled.")
    else:
        cursor.execute(
            "UPDATE flights SET status = %s WHERE flight_id = %s",
            (new_status, flight_id),
        )
        conn.commit()
        print(f"Flight {flight_id} status updated to {new_status}.")

    cursor.close()
    conn.close()
