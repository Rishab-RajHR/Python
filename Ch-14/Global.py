# Global => accessible everywhere
# Local => particular area

a = 89

def fun():
    global a  
    a = 3
    print(a)

fun()
print(a) # Without global a = 89 will be printed but with global a = 3 will be printed

