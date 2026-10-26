units=int(input("Enter the number of units consumed:"))
if units>500:
    print("High")
elif units>=301 and units<=500:
    print("Medium")
elif units>=101 and units<=300:
    print("Low")
elif units>=0 and units<=100:
    print("Very Low")