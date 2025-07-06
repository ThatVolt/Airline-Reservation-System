# app/user/seat_selection.py


def display_seat_map(booked_seats, total_seats=30):
    print("Seat Map (X = booked):")
    for seat_num in range(1, total_seats + 1):
        if seat_num in booked_seats:
            print("[X]", end=" ")
        else:
            print(f"[{seat_num}]", end=" ")
        if seat_num % 6 == 0: 
            print()
    print()


def select_seat(available):
    print(f"\nAvailable seats: {available}")
    seat_number = input("Choose your seat number: ").strip()
    if seat_number == "":
        return None
    return seat_number
