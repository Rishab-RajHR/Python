# Using functions avoids code writing repetition. We define a function once and call it multiple times.

# Function definition
def avg():
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))

    average = (a + b + c) / 3
    print(average)

# function call
avg()
print("Thank you")
avg()
print("Thank you")
avg()
avg()   # We can call the function as many times we want.