marks=int(input("Enter your marks:"))
family_income=int(input("Enter your annual family income:"))
if marks>=85 and family_income<=300000:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")