friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
print(friends)
friends.append("Alex")  # At the end of the list
print(friends)


# list of numbers
l1 = [1, 34, 62, 2, 6, 11]
# l1.sort()
l1.reverse()
print(l1)


# Insert operation at index 3
l2 = [1, 34, 62, 2, 6, 11]
l2.insert(3, 333)
print(l2)

# Pop method => deletes the number
l3 = [1, 34, 62, 2, 6, 11]
l3.pop(3) # index 3 is popped out
print(l3.pop(3))
print(l3)

l4 = [1, 34, 62, 2, 6, 11]
value = l4.pop(3)
print(value)
print(l4)