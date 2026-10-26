arr=[1,2,3,4,5]
num=int(input("Enter a number to search for:"))
for i in arr:
    if i==num:
        print("Number found")
        break
else:
    print("Number not found")