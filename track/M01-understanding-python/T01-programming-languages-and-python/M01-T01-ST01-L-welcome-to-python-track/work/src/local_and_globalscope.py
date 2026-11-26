#local and global variables
a=100
def number():
    global b
    b=10
    print(b)
    print(a)
number()
print(b)
print(a)