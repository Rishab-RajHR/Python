# Attribute that belongs to the class 

class Employee:
    language = "Python"  # This is a class attribute
    salary = 1200000

alex = Employee()
alex.name = "Alex"  # This is an instance(object) attribute
print(alex.name, alex.language, alex.salary)

basil = Employee()
basil.name = "Basil"
print(basil.name, basil.language, basil.salary)

# Here name is instance(object) attribute and salary and language are class attributes as they directly belong to the class