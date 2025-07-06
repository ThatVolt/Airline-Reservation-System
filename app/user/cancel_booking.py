from app.db import get_connection


def cancel_booking():
    res_id = input("Enter reservation ID to cancel: ").strip()
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT flight_id FROM reservations WHERE id = %s", (res_id,))

    result = cursor.fetchone()
    if not result:
        print("Reservation not found.\n")
        conn.close()
        return

    flight_id = result[0]
    cursor.execute("DELETE FROM reservations WHERE id = %s", (res_id,))

    cursor.execute(
        "UPDATE flights SET booked_seats = booked_seats - 1 WHERE flight_id = %s",
        (flight_id,),
    )

    conn.commit()
    print(f"Reservation {res_id} cancelled successfully.\n")

    cursor.close()
    conn.close()
