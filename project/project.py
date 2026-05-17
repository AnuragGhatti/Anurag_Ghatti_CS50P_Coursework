import json
from datetime import datetime

FILE = "data.json"


def load_data():
    """Load saved transactions."""
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_data(data):
    """Save transactions to file."""
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)


def add_transaction(data, t_type, category, amount, date=None):
    """Add income or expense."""
    if date is None:
        date = str(datetime.today().date())

    data.append({
        "type": t_type,
        "category": category,
        "amount": amount,
        "date": date
    })

    save_data(data)
    return data


def calculate_summary(data):
    """Calculate total income, expenses, and net balance."""
    income = 0
    expense = 0

    for t in data:
        if t["type"] == "income":
            income += t["amount"]
        elif t["type"] == "expense":
            expense += t["amount"]

    return income, expense, income - expense


def category_totals(data):
    """Calculate spending by category."""
    categories = {}

    for t in data:
        if t["type"] == "expense":
            categories[t["category"]] = categories.get(t["category"], 0) + t["amount"]

    return categories


def delete_transaction(data):
    """Delete a transaction by index."""
    if not data:
        print("No transactions to delete.")
        return data

    for i, t in enumerate(data):
        print(f"{i}: {t['date']} | {t['type']} | {t['category']} | ${t['amount']}")

    try:
        index = int(input("Enter index to delete: "))
        removed = data.pop(index)
        save_data(data)
        print("Deleted:", removed)
    except (ValueError, IndexError):
        print("Invalid selection.")

    return data


def reset_data(data):
    """Delete all data after confirmation."""
    confirm = input("Type RESET to confirm deleting all data: ")

    if confirm == "RESET":
        data.clear()
        save_data(data)
        print("All data has been reset.")
    else:
        print("Reset cancelled.")

    return data


def main():
    data = load_data()

    while True:
        print("\n--- FINANCE TRACKER ---")
        print("1. Add income")
        print("2. Add expense")
        print("3. View summary")
        print("4. View category breakdown")
        print("5. Delete transaction")
        print("6. Reset all data")
        print("7. Exit")

        choice = input("Choose: ")

        if choice == "1":
            category = input("Source: ")
            amount = float(input("Amount: "))
            add_transaction(data, "income", category, amount)

        elif choice == "2":
            category = input("Category: ")
            amount = float(input("Amount: "))
            add_transaction(data, "expense", category, amount)

        elif choice == "3":
            income, expense, net = calculate_summary(data)
            print("\n--- SUMMARY ---")
            print("Income:", income)
            print("Expenses:", expense)
            print("Net:", net)

        elif choice == "4":
            breakdown = category_totals(data)
            print("\n--- CATEGORY BREAKDOWN ---")
            for k, v in breakdown.items():
                print(k, ":", v)

        elif choice == "5":
            data = delete_transaction(data)

        elif choice == "6":
            data = reset_data(data)

        elif choice == "7":
            break


if __name__ == "__main__":
    main()
