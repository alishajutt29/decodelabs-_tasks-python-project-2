# Project 2 - Expense Tracker
# Simple program to keep adding expenses and show the total at the end.

def get_expense():
    entry = input("Enter expense amount (or type 'done' to stop): ")

    if entry.lower() == "done":
        return None

    try:
        amount = float(entry)
    except ValueError:
        print("That's not a valid number, try again.")
        return get_expense()   # ask again if input was wrong

    if amount < 0:
        print("Expense can't be negative.")
        return get_expense()

    return amount


def main():
    total = 0
    expense_list = []

    print("Expense Tracker")
    print("---------------")

    while True:
        expense = get_expense()

        if expense is None:
            break

        total += expense
        expense_list.append(expense)
        print(f"Added Rs.{expense}. Current total: Rs.{total}")

    print("\n---------------")
    print("All your expenses:")
    for i in range(len(expense_list)):
        print(f"{i+1}. Rs.{expense_list[i]}")

    print(f"\nTotal Spent: Rs.{total}")

    if len(expense_list) > 0:
        print(f"Average expense: Rs.{total/len(expense_list):.2f}")


main()
