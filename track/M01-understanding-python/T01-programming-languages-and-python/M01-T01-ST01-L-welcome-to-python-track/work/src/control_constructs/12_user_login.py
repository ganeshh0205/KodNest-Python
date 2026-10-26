user_name=str(input("Enter username:"))
password=str(input("Enter your password"))
if user_name=="admin" and password=="password":
    print("Login successful")
else:
    print("Invalid credentials")