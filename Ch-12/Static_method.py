
class Employee:
    language = "Python"  # This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet(): # Instead of self we use static method
        print("Good Morning")

alex = Employee()
alex.language = "JavaScript"  # This is an instance(object) attribute
alex.getInfo()
alex.greet()
# Employee.getInfo(alex)

