import json
from datetime import date

FILE_NAME = "expenses.json"


def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def add_expense():
    expenses = {}
    today = str(date.today())

    while True:
        category = input("Enter category: ").strip()

        while True:
            try:
                amount = int(input("Enter amount: "))
                break
            except ValueError:
                print(" Please enter a valid number")

        expenses[category] = amount

        if input("Add another item? (yes/no): ").lower() == "no":
            break

    note = ""
    if input("Add a note? (yes/no): ").lower() == "yes":
        note = input("Type your note: ")

    record = {
        "date": today,
        "expenses": expenses,
        "note": note
    }

    data = load_data()
    data.append(record)
    save_data(data)

    print("Expense added successfully\n")


def view_expenses():
    data = load_data()

    if not data:
        print(" No expenses found\n")
        return

    for entry in data:
        print("\n------------------------------")
        print("DATE:", entry["date"])

        for cat, amt in entry["expenses"].items():
            print(f"{cat.ljust(10)} : {str(amt).rjust(6)} rs")

        total = sum(entry["expenses"].values())
        print("-" * 30)
        print(f"TOTAL{' ' * 6}: {total} rs")

        if entry["note"]:
            print(f"NOTE: {entry['note']}")

        print("------------------------------")


def menu():
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print(" Goodbye!")
            break
        else:
            print(" Invalid choice")


menu()
