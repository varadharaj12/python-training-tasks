# task 1 encapsulation

class User:
    def __init__(self):
        self.__user_name = None
        self.__pwd = None

    def set_user(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd

    def get_user(self):
        return self.__user_name   # password hidden

    def register(self):
        print(f"Registering user: {self.__user_name}")

    def login(self):
        print(f"Logging in: {self.__user_name}")


# Test
u1 = User()
u1.set_user("john", "1234")
u1.register()
u1.login()

# task 2 inheritance

class User:
    def register(self):
        print("User registered")

    def login(self):
        print("User logged in")


class Student(User):
    def student_greet(self):
        print("Hello Student")


class Faculty(User):
    def faculty_greet(self):
        print("Hello Faculty")


class TempFaculty(Faculty):
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")


# Test
s = Student()
s.register()
s.login()
s.student_greet()

f = Faculty()
f.register()
f.faculty_greet()

t = TempFaculty()
t.login()
t.faculty_greet()
t.tempFaculty_greet()

# task 3 method overriding

class User:
    def greet(self):
        print("Welcome User")


class Student(User):
    def greet(self):
        print("Welcome Student")


class Faculty(User):
    def greet(self):
        print("Welcome Faculty")


# Test
s = Student()
f = Faculty()

s.greet()
f.greet()


# task 4 method chaining

class User:
    def register(self):
        print("registered")
        return self

    def login(self):
        print("logined")
        return self

    def greet(self):
        print("enjoy everyone")
        return self


# Test
user = User()
user.login().greet().register()


# task 5 combined real-time system 

class User:
    users_count = 0   # class variable

    def __init__(self, name, pwd):
        self.__name = name
        self.__pwd = pwd
        User.users_count += 1

    def login(self):
        print(f"{self.__name} logged in")
        return self

    def register(self):
        print(f"{self.__name} registered")
        return self

    def greet(self):
        print("Welcome User")
        return self


class Student(User):
    def greet(self):
        print("Welcome Student")
        return self


class Faculty(User):
    def greet(self):
        print("Welcome Faculty")
        return self


# Test
s1 = Student("john", "123")
f1 = Faculty("admin", "456")

s1.login().greet().register()
f1.login().greet().register()

print("Total Users:", User.users_count)