
class Employee:
    language = "Python"  # This is a class attribute
    salary = 1200000

    def __init__(self): # dunder method which is automatically called
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    def greet(self):
        print("Good Morning")

alex = Employee()
alex.name = "Alex"
print(alex.name, alex.salary)


