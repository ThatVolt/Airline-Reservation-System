# app/admin/export_csv.py

import csv
from app.db import get_connection


def export_reservations_to_csv():
    """Export all reservations to a CSV file."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT 
            r.id AS reservation_id,
            u.username,
            u.email,
            f.flight_id,
            f.source,
            f.destination,
            f.date,
            f.status,
            r.seat_number,
            r.booking_date
        FROM reservations r
        JOIN users u ON r.user_id = u.id
        JOIN flights f ON r.flight_id = f.flight_id
        ORDER BY r.id
    """
    )
    rows = cursor.fetchall()

    filename = "reservations.csv"
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "Reservation ID",
                "Username",
                "Email",
                "Flight ID",
                "Source",
                "Destination",
                "Flight Date",
                "Flight Status",
                "Seat Number",
                "Booking Date",
            ]
        )
        writer.writerows(rows)

    print(f"\n✅ Reservations successfully exported to {filename}")

    cursor.close()
    conn.close()
