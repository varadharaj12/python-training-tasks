import mysql.connector
from functools import reduce

# ---------------- DATABASE CONNECTION ----------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Admin@100",
    database="expense_db"
)

cursor = conn.cursor()

print("✅ Connected to MySQL")


# ---------------- ADD USER ----------------
def add_user():
    name = input("Enter user name: ")

    query = "INSERT INTO users (name) VALUES (%s)"
    cursor.execute(query, (name,))
    conn.commit()

    print("✅ User added")


# ---------------- ADD EXPENSE ----------------
def add_expense():
    user_id = int(input("Enter user ID: "))
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food/Travel/etc): ")
    description = input("Enter description: ")
    date = input("Enter date (YYYY-MM-DD): ")

    query = """
    INSERT INTO expenses (user_id, amount, category, description, date)
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(query, (user_id, amount, category, description, date))
    conn.commit()

    print("✅ Expense added")


# ---------------- VIEW EXPENSES ----------------
def view_expenses():
    user_id = int(input("Enter user ID: "))

    query = """
    SELECT u.name, e.amount, e.category, e.description, e.date
    FROM users u
    JOIN expenses e ON u.user_id = e.user_id
    WHERE u.user_id = %s
    """

    cursor.execute(query, (user_id,))
    data = cursor.fetchall()

    print("\n--- Expenses ---")
    for row in data:
        print(row)

    return data


# ---------------- FILTER CATEGORY ----------------
def filter_by_category(data):
    category = input("Enter category: ")

    result = list(filter(lambda x: x[2] == category, data))

    print("\nFiltered (Category):")
    for r in result:
        print(r)


# ---------------- FILTER DATE ----------------
def filter_by_date(data):
    date = input("Enter date (YYYY-MM-DD): ")

    result = [x for x in data if str(x[4]) == date]

    print("\nFiltered (Date):")
    for r in result:
        print(r)


# ---------------- TOTAL EXPENSE ----------------
def total_expense(data):
    amounts = list(map(lambda x: x[1], data))
    total = reduce(lambda a, b: a + b, amounts, 0)

    print("\nTotal Expense:", total)


# ---------------- CATEGORY WISE ----------------
def category_wise(data):
    categories = {x[2] for x in data}

    result = {
        cat: sum(x[1] for x in data if x[2] == cat)
        for cat in categories
    }

    print("\nCategory-wise Spending:")
    for k, v in result.items():
        print(k, ":", v)


# ---------------- DELETE ----------------
def delete_expense():
    exp_id = int(input("Enter expense ID: "))

    cursor.execute("DELETE FROM expenses WHERE exp_id=%s", (exp_id,))
    conn.commit()

    print("🗑️ Deleted")


# ---------------- UPDATE ----------------
def update_expense():
    exp_id = int(input("Enter expense ID: "))
    amount = float(input("Enter new amount: "))

    cursor.execute("UPDATE expenses SET amount=%s WHERE exp_id=%s", (amount, exp_id))
    conn.commit()

    print("✏️ Updated")


# ---------------- HIGHEST EXPENSE ----------------
def highest_expense(data):
    if not data:
        print("⚠️ No data")
        return

    highest = reduce(lambda x, y: x if x[1] > y[1] else y, data)
    print("\nHighest Expense:", highest)


# ---------------- SMART INSIGHT ----------------
def smart_insight(data):
    if not data:
        print("⚠️ No data")
        return

    categories = {x[2] for x in data}

    result = {
        cat: sum(x[1] for x in data if x[2] == cat)
        for cat in categories
    }

    max_cat = max(result, key=result.get)

    print(f"\n⚠️ You are spending too much on {max_cat}")


# ---------------- MENU ----------------
data = []

while True:
    print("\n===== EXPENSE MANAGER =====")
    print("1. Add User")
    print("2. Add Expense")
    print("3. View Expenses")
    print("4. Filter by Category")
    print("5. Filter by Date")
    print("6. Total Expense")
    print("7. Category-wise")
    print("8. Delete Expense")
    print("9. Update Expense")
    print("10. Highest Expense")
    print("11. Smart Insight")
    print("12. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_user()

    elif choice == "2":
        add_expense()

    elif choice == "3":
        data = view_expenses()

    elif choice == "4":
        if data:
            filter_by_category(data)
        else:
            print("⚠️ First view expenses")

    elif choice == "5":
        if data:
            filter_by_date(data)
        else:
            print("⚠️ First view expenses")

    elif choice == "6":
        if data:
            total_expense(data)
        else:
            print("⚠️ First view expenses")

    elif choice == "7":
        if data:
            category_wise(data)
        else:
            print("⚠️ First view expenses")

    elif choice == "8":
        delete_expense()

    elif choice == "9":
        update_expense()

    elif choice == "10":
        if data:
            highest_expense(data)
        else:
            print("⚠️ First view expenses")

    elif choice == "11":
        if data:
            smart_insight(data)
        else:
            print("⚠️ First view expenses")

    elif choice == "12":
        print("Exiting...")
        break

    else:
        print("❌ Invalid choice")