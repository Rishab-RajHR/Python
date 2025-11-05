# Instance attribute takes preference over class attribute

class Employee:
    language = "Python"  # This is a class attribute
    salary = 1200000

alex = Employee()
alex.language = "JavaScript"  # This is an instance(object) attribute
print(alex.language, alex.salary)

