import os
from app.db import get_connection


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def admin_panel():
    conn = get_connection()
    cursor = conn.cursor()

    while True:
        clear()
        print("\n--- Admin Panel ---")
        print("1. Add Flight")
        print("2. Modify Flight")
        print("3. Delete Flight")
        print("4. Exit Admin Panel")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            flight_id = input("Enter flight number: ").strip()
            source = input("Enter source: ").strip()
            destination = input("Enter destination: ").strip()
            seats = int(input("Enter total seats: "))
            date = input("Enter flight date (YYYY-MM-DD): ").strip()
            price = float(input("Enter ticket price: "))

            cursor.execute(
                """
                INSERT INTO flights (flight_id, source, destination, seats, booked_seats, date, price)
                VALUES (%s, %s, %s, %s, 0, %s, %s)
            """,
                (flight_id, source, destination, seats, date, price),
            )

            conn.commit()
            print(f"Flight {flight_id} added successfully!\n")
            input("Press Enter to continue...")

        elif choice == "2":
            flight_id = input("Enter flight number to modify: ").strip()
            cursor.execute("SELECT * FROM flights WHERE flight_id = %s", (flight_id,))
            result = cursor.fetchone()

            if not result:
                print("Flight not found.\n")
                input("Press Enter to continue...")
                continue

            print("Leave blank to keep current value.")
            source = input(f"Source ({result[1]}): ").strip() or result[1]
            destination = input(f"Destination ({result[2]}): ").strip() or result[2]
            seats = input(f"Seats ({result[3]}): ").strip()
            date = input(f"Date ({result[5]}): ").strip() or result[5]
            price = input(f"Price ({result[6]}): ").strip()

            cursor.execute(
                """
                UPDATE flights SET
                    source = %s,
                    destination = %s,
                    seats = %s,
                    date = %s,
                    price = %s
                WHERE flight_id = %s
            """,
                (
                    source,
                    destination,
                    int(seats) if seats else result[3],
                    date,
                    float(price) if price else result[6],
                    flight_id,
                ),
            )

            conn.commit()
            print(f"Flight {flight_id} updated successfully!\n")
            input("Press Enter to continue...")

        elif choice == "3":
            flight_id = input("Enter flight number to delete: ").strip()
            cursor.execute("DELETE FROM flights WHERE flight_id = %s", (flight_id,))
            conn.commit()
            print(f"Flight {flight_id} deleted successfully!\n")
            input("Press Enter to continue...")

        elif choice == "4":
            break

        else:
            print("Invalid choice.\n")
            input("Press Enter to continue...")

    cursor.close()
    conn.close()
