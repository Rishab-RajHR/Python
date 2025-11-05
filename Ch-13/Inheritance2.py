class Employee:
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

# Inheritance
class Programmer(Employee):
    company = "ITC Infotech"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

a = Employee()
b = Programmer()

print(a.company, b.company)