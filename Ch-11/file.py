# If we want to store data we use files 
# Persist means save
# RAM(volatile) => data is for short time
# HDD(Non volatile) => data is until deleted

'''
a = "a very long string with emails"

emails = []
3 seconds
'''

f = open("file.txt", "r")  # By default it is read
data = f.read()
print(data)
f.close()  # It should be done after we have accessed the file
