# list => are the containers to store a set values of any data type

friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]

print(friends)
print(friends[0])
print(friends[4])

friends[0] = "Guava"
print(friends[0]) # Unlike strings list are mutable
print(friends[1:4]) # slicing in list