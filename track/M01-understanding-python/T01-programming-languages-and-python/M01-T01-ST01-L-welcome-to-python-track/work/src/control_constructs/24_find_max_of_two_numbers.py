a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
def greater(a,b):
    if a>b:
        return a
    else:
        return b
print(greater(a,b))