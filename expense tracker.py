import csv
from datetime import datetime

FILENAME = 'expenses.csv'

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open(FILENAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])
    print("Expense added.")

def view_expenses():
    total = 0
    print("\nDate\t\t\tCategory\tAmount")
    print("-" * 40)
    try:
        with open(FILENAME, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"{row[0]}\t{row[1]}\t{row[2]}")
                total += float(row[2])
    except FileNotFoundError:
        print("No expenses recorded yet.")
    print(f"\nTotal Spent: ₹{total:.2f}")

while True:
    print("\n1. Add Expense\n2. View Expenses\n3. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        break
    else:
        print("Invalid choice.")
