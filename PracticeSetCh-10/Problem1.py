# Class "Programmer" for storing information of few programmers working at microsoft

class Programmer:
   company = "Microsoft"
   def __init__(self, name, salary, pin):
      self.name = name
      self.salary = salary
      self.pin = pin

p = Programmer("Alex", 120000, 254400)
print(p.name, p.salary, p.company)

r = Programmer("Robin", 120000, 254408)
print(r.name, r.salary, r.company)
