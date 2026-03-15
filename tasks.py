# Task 1 – Print Formatting
print("Hello", "World", "Welcome", "Python", sep=" ", end="\n")
print("Laptop", "Mouse", "Keyboard", sep=" | ")

# Task 2 – Variables
name = "Ravi"
age = 22
city = "Chennai"
print(name, age, city, sep="-")

# Task 3 – Multiple Assignment
name, age, student = "Meena", 20, True
print(name, age, student)

# Task 4 – Indexing
word = "Python"
print("First letter:", word[0])
print("Third letter:", word[2])
print("Last letter:", word[-1])
# -----------------------------
# Bitwise Operator Tasks
# -----------------------------

# 1
a = 10
b = 6
print("1:", a & b)

# 2
x = 12
y = 5
print("2:", x | y)

# 3
num = 8
print("3:", ~num)

# 4
a = 15
b = 9
print("4:", a ^ b)

# 5
num = 7
print("5:", num << 2)

# 6
num = 20
print("6:", num >> 1)

# 7
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("7 AND result:", a & b)

# 8
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("8 XOR result:", a ^ b)


# -----------------------------
# String Tasks
# -----------------------------

# 9
s = "hi"
print("9:", s * 4)

# 10
s = "python"
print("10:", s * 3)

# 11
a = "super"
b = "man"
print("11:", a + b)

# 12
a = "hello"
b = " "
c = "world"
print("12:", a + b + c)

# 13
name = input("Enter your name: ")
print("13:", name * 5)

# 14
a = input("Enter first string: ")
b = input("Enter second string: ")
print("14:", a + b)


# -----------------------------
# Input & Type Casting
# -----------------------------

# 15
name = input("Enter name: ")
print("15 type:", type(name))

# 16
age = int(input("Enter age: "))
print("16 age:", age)

# 17
a = int(input("Enter number1: "))
b = int(input("Enter number2: "))
print("17 sum:", a + b)

# 18
m1 = int(input("Enter mark1: "))
m2 = int(input("Enter mark2: "))
print("18 average:", (m1 + m2) / 2)

# 19
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("19 result:", 3 * a * 2 + b - 2)

# 20
num = input("Enter number: ")
print("20 before:", type(num))
num = int(num)
print("20 after:", type(num))


# -----------------------------
# Unit Digit Tasks
# -----------------------------

# 21
num = input("Enter number: ")
print("21 last digit:", num[-1])

# 22
num = int(input("Enter number: "))
print("22 unit digit:", num % 10)

# 23
num = int(input("Enter number: "))
print("23 remove last digit:", num // 10)

# 24
num = int(input("Enter number: "))
print("24 second last digit:", (num // 10) % 10)

# 25
num = int(input("Enter 5 digit number: "))
print("25 last digit:", num % 10)


# -----------------------------
# If Statement Tasks
# -----------------------------

# 26
if 10 >= 5:
    print("26: 10 is greater than or equal to 5")

# 27
num = int(input("Enter number: "))
if num > 50:
    print("27 greater than 50")

# 28
age = int(input("Enter age: "))
if age >= 18:
    print("28 eligible")

# 29
num = int(input("Enter number: "))
if num > 100:
    print("29 greater than 100")

# 30
num = int(input("Enter number: "))
if num >= 0:
    print("30 positive")


# -----------------------------
# If Else Tasks
# -----------------------------

# 31
num = int(input("Enter number: "))
if num % 2 == 0:
    print("31 Even")
else:
    print("31 Odd")

# 32
marks = int(input("Enter marks: "))
if marks >= 35:
    print("32 Pass")
else:
    print("32 Fail")

# 33
num = int(input("Enter number: "))
if num > 0:
    print("33 Positive")
else:
    print("33 Negative")

# 34
num = int(input("Enter number: "))
if num > 10:
    print("34 greater than 10")
else:
    print("34 not greater than 10")


# -----------------------------
# Nested If Tasks
# -----------------------------

# 35 Job eligibility
age = int(input("Enter age: "))
height = int(input("Enter height: "))
weight = int(input("Enter weight: "))

if age >= 18:
    if height >= 160:
        if weight >= 60:
            print("35 Selected")
        else:
            print("35 Rejected")
    else:
        print("35 Rejected")
else:
    print("35 Rejected")


# 36 College admission
marks = int(input("Enter marks: "))
age = int(input("Enter age: "))

if marks >= 60:
    if age >= 17:
        print("36 Admission Granted")
    else:
        print("36 Age not eligible")
else:
    print("36 Marks not eligible")


# 37 Sports selection
age = int(input("Enter age: "))
height = int(input("Enter height: "))
weight = int(input("Enter weight: "))

if age >= 16:
    if height >= 150:
        if weight >= 50:
            print("37 Selected")
        else:
            print("37 Rejected")
    else:
        print("37 Rejected")
else:
    print("37 Rejected")


# -----------------------------
# Match Statement Tasks
# -----------------------------

# 38 Day name
num = int(input("Enter number (1-7): "))

match num:
    case 1: print("Monday")
    case 2: print("Tuesday")
    case 3: print("Wednesday")
    case 4: print("Thursday")
    case 5: print("Friday")
    case 6: print("Saturday")
    case 7: print("Sunday")
    case _: print("Invalid")


# 39 Colors
num = int(input("Enter number (1-3): "))

match num:
    case 1: print("Red")
    case 2: print("Blue")
    case 3: print("Green")
    case _: print("Invalid")


# 40 Fruits
num = int(input("Enter number (1-4): "))

match num:
    case 1: print("Apple")
    case 2: print("Mango")
    case 3: print("Orange")
    case 4: print("Banana")
    case _: print("Invalid")

# Task 5 – Arithmetic Operators
print(25 + 10)
print(50 - 20)
print(8 * 5)
print(100 / 10)
print(10 % 3)
print(2 ** 4)
print(20 // 3)

# Task 6 – BODMAS Expression
print(3 + 2 * 5 ** 2)

# Task 7 – Assignment Operator
num = 50
num += 25
print(num)

num = 100
num /= 10
print(num)

# Task 8 – Comparison Operators
print(10 > 5)
print(20 < 15)
print(5 == 5)
print(10 != 8)
print(7 >= 7)
print(6 <= 2)

# Task 9 – String Comparison
a = "apple"
b = "Apple"
print(a == b)

# Task 10 – Logical Operators
print(10 > 5 and 5 == 5)
print(5 > 10 or 10 == 10)
print(not(5 > 2))

# Task 11 – Membership Operator
numbers = [10,20,30,40,50]
print(20 in numbers)
print(60 in numbers)
print(30 not in numbers)

# Task 12 – Swap Variables
a = 10
b = 20
a, b = b, a
print("a =", a)
print("b =", b)

# Task 13 – Bitwise XOR
a = 6
b = 3
print(a ^ b)
