#TASK1

# Task 1

def create_user(name, age, role):
    return {
        "name": name.title(),
        "age": age,
        "role": role
    }

users = []

users.append(create_user("Alice", 30, "Developer"))
users.append(create_user("Bob", 25, "Tester"))

print("All users:")
for user in users:
    print(user)

#TASK2

    def calculate_total(*numbers):
        total = sum(numbers)
        avg = total / len(numbers) if numbers else 0
        return total, avg
    
    total, average = calculate_total(10, 20, 30)
    print("\nTotal:", total)
    print("Average:", average)

#TASK3

def system_config(**settings):
    print("\nSystem Config:")
    for key, value in settings.items():
        print(f"{key}: {value}")

system_config(mode="debug", version="1.0")

#task4

def factorial(n):
    if n < 0:
        return "Error: Negative number"
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("\nFactorial of 5:", factorial(5))
print("Factorial of -1:", factorial(-1))

#task5

def square_generator(n):
    for i in range(n):
        yield i * i

# Normal list
square_list = [i*i for i in range(5)]
print("\nList:", square_list)
print("Type of list:", type(square_list))

# Generator
gen = square_generator(5)
print("Generator:", list(gen))
print("Type of generator:", type(square_generator(5)))

#task6

try:
    num = int(input("\nEnter numerator: "))
    den = int(input("Enter denominator: "))
    result = num / den
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Invalid input")

finally:
    print("Program Completed")


    #task7

with open("team_data.txt", "w") as file:
    for user in users:
        file.write(str(user) + "\n")


with open("team_data.txt", "r") as file:
    print("\nFile Content:")
    print(file.read())
    print("File closed?", file.closed)


