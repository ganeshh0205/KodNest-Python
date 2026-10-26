num=int(input("Enter a number to find the factorial:"))
factorial=1
while num>=1:
    factorial*=num
    num-=1
print(f"The factorial of the number is {factorial}")