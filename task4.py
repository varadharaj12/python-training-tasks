# mini project 1
employees = []

def add_employee():
    name = input("Name: ")
    age = int(input("Age: "))
    role = input("Role: ")
    salary = float(input("Salary: "))
    employees.append({"name": name, "age": age, "role": role, "salary": salary})

def display():
    for emp in employees:
        print(emp)

def update_employee():
    name = input("Enter name to update: ")
    for emp in employees:
        if emp["name"] == name:
            emp["salary"] = float(input("New salary: "))

def delete_employee():
    name = input("Enter name to delete: ")
    for emp in employees:
        if emp["name"] == name:
            employees.remove(emp)

# Test
add_employee()
display()


# mini project 2

def report():
    name = input("Name: ")
    m1 = int(input("Mark1: "))
    m2 = int(input("Mark2: "))
    m3 = int(input("Mark3: "))
    
    total = m1 + m2 + m3
    avg = total / 3

    grade = "A" if avg >= 90 else "B" if avg >= 70 else "C"

    print(f"\nReport Card\nName: {name}\nTotal: {total}\nAverage: {avg}\nGrade: {grade}")

report()


# mini project 3

cart = []

def add_item():
    name = input("Product: ")
    price = float(input("Price: "))
    qty = int(input("Quantity: "))
    cart.append({"name": name, "price": price, "qty": qty})

def total_bill():
    total = 0
    for item in cart:
        total += item["price"] * item["qty"]
    print("Total Bill:", total)

def display():
    for item in cart:
        print(item)

add_item()
display()
total_bill()


#mini project 4
users = {"admin": "1234", "user": "pass"}

username = input("Username: ")
password = input("Password: ")

if username in users and users[username] == password:
    print("Login Successful")
else:
    print("Login Failed")

    # mini project 5

    visitors = set()

for _ in range(5):
    name = input("Visitor name: ")
    visitors.add(name)

print("Unique Visitors:", len(visitors))
print(visitors)

#mini project 6

name = input("Name: ")
product = input("Product: ")

print(f"{name} bought {product}")
print(name.ljust(10))
print(name.rjust(10))
print(name.center(10))

# mini project 7

account = {"name": "Arun", "balance": 1000}

def deposit(amount):
    account["balance"] += amount

def withdraw(amount):
    if amount <= account["balance"]:
        account["balance"] -= amount
    else:
        print("Insufficient balance")

def check():
    print(account)

deposit(500)
withdraw(200)
check()

#mini project 8

votes = {"A": 0, "B": 0, "C": 0}

for _ in range(5):
    v = input("Vote (A/B/C): ")
    if v in votes:
        votes[v] += 1

winner = max(votes, key=votes.get)
print("Winner:", winner)
print(votes)


#mini project 9

students = {}

def add_student():
    name = input("Student: ")
    courses = input("Courses (comma): ").split(",")
    students[name] = courses

def display():
    print(students)

add_student()
display()


#mini project 10

num = int(input("Enter number: "))

print("Binary:", bin(num))
print("Octal:", oct(num))
print("Hex:", hex(num))

print("With commas:", f"{num:,}")
print("Scientific:", f"{num:e}")


