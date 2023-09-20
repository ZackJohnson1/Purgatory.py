# Initializing lists to store income and expenses

income_entries = []
expense_entries = []

def add_income(description, amount):
    income_entries.append({"description": description, "amount": amount})

def add_expense(description, amount):
    expense_entries.append({"description": description, "amount": amount})

def view_ledger():
    print("Income:")
    for entry in income_entries:
        print(f"{entry['description']}: ${entry['amount']}")

    print("\nExpenses:")
    for entry in expense_entries:
        print(f"{entry['description']}: -${entry['amount']}")

def view_balance():
    total_income = sum(entry['amount'] for entry in income_entries)
    total_expense = sum(entry['amount'] for entry in expense_entries)
    balance = total_income - total_expense
    print(f"Total Income: ${total_income}")
    print(f"Total Expense: ${total_expense}")
    print(f"Current Balance: ${balance}")

while True:
    print("\n--- Expense Tracker ---")
    print("1: Add Income")
    print("2: Add Expense")
    print("3: View Ledger")
    print("4: View Balance")
    print("5: Exit")

    choice = input("Select an option: ")

    if choice == '1':
        description = input("Enter income description: ")
        while True:
            try:
                amount = float(input("Enter amount: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numerical value.")
        add_income(description, amount)

    elif choice == '2':
        description = input("Enter expense description: ")
        while True:
            try:
                amount = float(input("Enter amount: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numerical value.")
        add_expense(description, amount)

    elif choice == '3':
        view_ledger()

    elif choice == '4':
        view_balance()

    elif choice == '5':
        break

    else:
        print("Invalid option. Please try again.")
