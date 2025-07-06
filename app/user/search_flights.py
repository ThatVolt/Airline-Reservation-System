from app.db import get_connection
from tabulate import tabulate


def search_flights():
    source = input("Enter source location: ").strip().lower()
    destination = input("Enter destination location: ").strip().lower()
    travel_date = input(
        "Enter travel date (YYYY-MM-DD or leave blank to skip): "
    ).strip()

    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT flight_id, date, (seats - booked_seats) AS seats_left, price
        FROM flights
        WHERE LOWER(source) = %s AND LOWER(destination) = %s
    """
    params = [source, destination]

    if travel_date:
        query += " AND date = %s"
        params.append(travel_date)

    cursor.execute(query, tuple(params))
    rows = cursor.fetchall()

    if rows:
        headers = ["Flight Number", "Date", "Seats Left", "Price"]
        print(f"\n--- Flights from {source.title()} to {destination.title()} ---")
        print(
            tabulate(
                rows,
                headers=headers,
                tablefmt="grid",
                colalign=("center",) * len(headers),
            )
        )
    else:
        print("No flights found matching your search criteria.\n")

    cursor.close()
    conn.close()
