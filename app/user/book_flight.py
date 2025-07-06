import datetime
from app.db import get_connection
from app.user.show_flights import show_flights
from app.user.seat_selection import select_seat
from app.auth.session import session
from app.user.utils import is_valid_email, process_payment


def book_flight():
    show_flights()
    flight_id = input("Enter flight number to book: ").strip()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT seats, booked_seats, price FROM flights WHERE flight_id = %s",
        (flight_id,),
    )
    result = cursor.fetchone()

    if not result:
        print("❌ Invalid flight ID.\n")
        conn.close()
        return

    total_seats, booked_seats, price = result
    if booked_seats >= total_seats:
        print("❌ No seats available on this flight.\n")
        conn.close()
        return

    available_seats = total_seats - booked_seats
    selected_seat = select_seat(available_seats)
    if not selected_seat:
        print("❌ Seat selection cancelled.")
        conn.close()
        return

    if not process_payment(price):
        conn.close()
        return

    booking_date = datetime.date.today()

    try:
        cursor.execute(
            """
            INSERT INTO reservations (user_id, flight_id, seat_number, booking_date)
            VALUES (%s, %s, %s, %s)
            """,
            (session["user_id"], flight_id, selected_seat, booking_date),
        )

        cursor.execute(
            """
            UPDATE flights SET booked_seats = booked_seats + 1 WHERE flight_id = %s
            """,
            (flight_id,),
        )

        conn.commit()
        print("\n✅ Booking successful!")
        print(f"✈️  Flight: {flight_id}")
        print(f"🪑  Seat: {selected_seat}")
        print(f"📅  Date: {booking_date}")
    except Exception as e:
        print("❌ Failed to book flight:", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
