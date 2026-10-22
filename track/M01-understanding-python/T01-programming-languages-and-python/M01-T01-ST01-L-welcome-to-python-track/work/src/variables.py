name = "Ganesh"
age=21
print(id(name))
print(type(name))

print("Hello Python", end="--")
print("Thank you Python")

print("Hello Python \nThank you Python")

# My name is Ganesh and age is 21
print("My name is " + name + " and age is " , age)
print("My name is "+ name +" age is "+ str(age))
print("My name is", name, "and age is", age)
#String Formatting (f Strings)
print(f"My name is{name} and age is{age}")


# Single - line comments
""" Multi - Line comments
Hello
Hi
Thank you
"""

a=10
b=20
c=30
# a, b, c = 10,20,30
# print(a+b+c)
a=b=c=10
print(a+b+c)

a,b,c="Abhi", "Ram", "Sai"
print(b)
print(a+b+c)

x, y, z=30,4,8
print(x+z)
# print(a+x) #TypeError
print(a+str(x)) #=Abhi30
print(b+c) #=RamSai
print(a,x) #=Abhi 30
