# addition function
def add():
    a=int(input("Enter a value for addition: "))
    b=int(input("Enter b value for addition: "))
    print(a+b)
add()

# Square Function
def square():
    a=int(input("Enter a value for square: "))
    print(a*a)
square()

# Function for finding out largest of 3 numbers
def largest_of_three_numbers():
    a=int(input("Enter a value for largest of three numbers: "))
    b=int(input("Enter b value for largest of three numbers: "))
    c=int(input("Enter c value for largest of three numbers: "))
    if a>b and a>c:
        print(a)
    elif b>a and b>c:
        print(b)
    else:
        print(c)
largest_of_three_numbers()

# function to find whether a number is even or not
def even():
    a=int(input("Enter a value for even or not: "))
    if a%2==0:
        print("Even")
    else:
        print("Odd")
even()

#function to greet user with name
def greet():
    name=input("Enter your name: ")
    print("Good Morning",name)
greet()


''' Types of Functions '''
#1. No paramaters no return type
def square():
    n=5*5
    print(n)
square()

#2. No parameters but has a return type
def square():
    n=5*5
    return n
print(square())

#3. has parameters but no return type
def square(n):
    print(n*n)
square(5)

#4. has parameters and has a return type
def square(n):
    return n*n
print(square(5))

# Write the 4 types of functions for checking even or odd using functions.

# 1. No parameters no return type
def even():
    a=int(input("Enter a value for even or not: "))
    if a%2==0:
        print("Even")
    else:
        print("Odd")
even()

#2. No parameters but has a return type
def even():
    a=int(input("Enter a value for even or not: "))
    if a%2==0:
        print("Even")
    else:
        print("Odd")
even()

#3. has parameters but no return type
def even(n):
    if n%2==0:
        print("Even")
    else:
        print("Odd")
even(5)

#4. has parameters and has a return type
def even(n):
    return n%2==0
print(even(5))