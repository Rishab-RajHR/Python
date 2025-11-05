f = open("file.txt")

# lines = f.readlines()
# print(lines, type(lines))

# With the help of while loop
line = f.readline()
while(line != ""):
   print(line)
   line = f.readline()

f.close()