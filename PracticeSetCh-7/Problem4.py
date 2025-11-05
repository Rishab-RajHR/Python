# Number is prime or not using for loop (Prime => number 1 and itself)

n = int(input("Enter a number : "))

for i in range(2, n):
    if(n%i) == 0:
        print("The number is not prime")
        break
else:
    print("Number is prime")

