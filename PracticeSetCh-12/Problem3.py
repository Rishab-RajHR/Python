# A list comprehension to print a list which contains the mutiplication table of a user entered number.

n = int(input("Enter a number: "))

table = [n*i for i in range(1, 11)]
print(table)