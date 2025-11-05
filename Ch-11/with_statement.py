# With statement helps to write the  function without closing it

# Without with function
f = open("file.txt")
print(f.read())
f.close()

# The same can be written using with statement like this:
with open("file.txt") as f:
   print(f.read())

# You dont have to explicitly close the file