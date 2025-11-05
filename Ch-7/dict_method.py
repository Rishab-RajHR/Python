marks = {
    "Alex" : 100,
    "Shubham" : 56,
    "Rohan" : 23,
    0 : "Alex"
}

print(marks.items()) #It will return list of tuples
print(marks.keys()) #It will return list of keys
print(marks.values()) #It will return list of values
marks.update({"Rohan" : 45}) #It will update the value of Rohan
print(marks)
print(marks.get("Alex"))

print(marks.get("Alex2")) # None
print(marks["Alex2"]) # Error