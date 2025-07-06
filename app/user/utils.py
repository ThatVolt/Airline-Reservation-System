import re


def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@(gmail\.com|yahoo\.com|outlook\.com|hotmail\.com)$"
    return re.match(pattern, email)


def process_payment(amount):
    print("\n--- Payment Gateway ---")
    print(f"Total amount to pay: ₹{amount:.2f}")
    confirm = input("Confirm payment? (y/n): ").strip().lower()
    if confirm == "y":
        print("✅ Payment Successful!")
        return True
    else:
        print("❌ Payment Cancelled.")
        return False
