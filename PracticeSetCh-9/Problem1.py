# Check if the twinkle is present in txt file or not

f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("The word twinkle is present in the content")

else:
      print("The word twinkle is not present in the content")

f.close()