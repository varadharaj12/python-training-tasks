
# Task 2: Abstraction
from abc import ABC, abstractmethod
from functools import reduce

# Abstract Base Class
class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass


# Base Class
class User(AbstractUser):
    def __init__(self, name, id):
        self.name = name
        self.id = id


# Task 1: super() usage

class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = int(fees)

    def get_details(self):
        return f"Student -> Name: {self.name}, ID: {self.id}, Dept: {self.dept}, Fees: {self.fees}"


class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = int(salary)

    def get_details(self):
        return f"Faculty -> Name: {self.name}, ID: {self.id}, Salary: {self.salary}"


class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

    def get_details(self):
        return f"TempFaculty -> Name: {self.name}, ID: {self.id}, Salary: {self.salary}, Duration: {self.duration}"


# -------------------------------
# 🧪 Final Challenge System
# -------------------------------

# Create objects
students = [
    Student("Arun", 1, "CSE", 60000),
    Student("Bala", 2, "ECE", 40000),
    Student("Kumar", 3, "IT", 80000)
]

faculty = [
    Faculty("Ravi", 101, 35000),
    Faculty("Suresh", 102, 25000),
    TempFaculty("Mani", 103, 30000, "6 months")
]


# ✅ Print all details
print("\n--- ALL DETAILS ---")
for user in students + faculty:
    print(user.get_details())


# -------------------------------
# Task 3: Sorting
# -------------------------------

students_sorted = sorted(students, key=lambda x: x.fees)
faculty_sorted = sorted(faculty, key=lambda x: x.salary)

print("\n--- SORTED STUDENTS (by fees) ---")
for s in students_sorted:
    print(s.get_details())

print("\n--- SORTED FACULTY (by salary) ---")
for f in faculty_sorted:
    print(f.get_details())


# -------------------------------
# Task 4: map()
# -------------------------------

student_names = list(map(lambda s: s.name, students))
print("\n--- STUDENT NAMES ---")
print(student_names)


# -------------------------------
# Task 5: filter()
# -------------------------------

high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))

print("\n--- HIGH FEE STUDENTS (>50000) ---")
for s in high_fee_students:
    print(s.get_details())

print("\n--- HIGH SALARY FACULTY (>30000) ---")
for f in high_salary_faculty:
    print(f.get_details())


# -------------------------------
# Task 6: reduce()
# -------------------------------

total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)

print("\n--- TOTAL FEES ---")
print(total_fees)

print("\n--- TOTAL SALARY ---")
print(total_salary)


# -------------------------------
# Task 7: Higher Order Function
# -------------------------------

def process_users(users, func):
    return list(map(func, users))


# Example usage
names = process_users(students, lambda x: x.name)
print("\n--- USING HIGHER ORDER FUNCTION ---")
print(names)