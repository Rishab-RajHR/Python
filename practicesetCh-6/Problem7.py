# Given post is talking about "Alex" or not.

post = input("Enter the post: ")

if("Alex".lower() in post.lower()):
   print(("This post is talking about Alex"))

else:
   print(("This post is not talking about Alex"))