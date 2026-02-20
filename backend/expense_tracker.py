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

def monthly_summary():
    
    
    while True:
        try:
            month = int(input("Enter month (1-12): "))
            year = int(input("Enter year (e.g. 2026): "))
            if 1 <= month <= 12:
                break
            else:
                print("Please enter a valid month between 1 and 12")
        except ValueError:
            print("Please enter a valid number")

    
    data = load_data()

    
    filtered = []
    for record in data:
        parts = record["date"].split("-")
        record_year = int(parts[0])
        record_month = int(parts[1])
        if record_month == month and record_year == year:
            filtered.append(record)

    # Check if any records found
    if not filtered:
        print(f"\n No expenses found for {month}/{year}\n")
        return

    # Calculate total and count
    grand_total = 0
    item_count = 0
    for record in filtered:
        grand_total += sum(record["expenses"].values())
        item_count += len(record["expenses"])

    # Display the summary
    print("\n==============================")
    print(f"  MONTHLY SUMMARY - {month}/{year}")
    print("==============================")
    print(f"Number of expense items : {item_count}")
    print(f"Number of entries       : {len(filtered)}")
    print(f"Total spent             : {grand_total} rs")
    print("==============================\n")




def menu():
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. View Monthly Summary")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            print(" Goodbye!")
            break
        else:
            print(" Invalid choice")


menu()
