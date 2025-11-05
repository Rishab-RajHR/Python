# Username length is less than 10 characters otherwise print all is well

username = input("Enter username: ")

if(len(username)<10):
   print("Your username contains less than 10 characters")
else:
   print("Your username contains more than or eqaul to 10 characters")