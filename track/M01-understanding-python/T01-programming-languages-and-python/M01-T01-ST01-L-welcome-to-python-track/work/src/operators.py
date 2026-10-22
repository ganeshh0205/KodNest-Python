# Arithmetic Operators
print(3+3) # 6
print(3-3) # 0
print(3*3) # 9
print(3/3) # 1.0
print(3%3) # 0
print(10%30) # 10
print(100%30) # 10
print(3**3) # 27
print(3//3) # 1
print(10//30) # 0
print(100//30) # 3

# Comparison Operators
print(11 == 11) # True
print(11==10) # False
print(11 != 10) # True
print(11 > 10) # True
print(11 < 10) # False
print(11 >= 10) # True
print(11 <= 10) # False

# Assignment Operators
a=10
print(a)
a+=10 #a=a+10
print(a) # 20
a-=10 #a=a-10
print(a) # 10
a*=10 #a=a*10
print(a) # 100
a/=10 #a=a/10
print(a) # 10.0
a%=10 #a=a%10
print(a) # 0
a**=10 #a=a**10
print(a) # 0
a//=10 #a=a//10
print(a) # 0

# Logical Operators (True or False Case)
a=True
b=False
print(a and b) # False
print(a or b) # True
print(not a) # False

# Logical Operators (Non-zero Case)
a=10
b=20
print(a and b) # 20
print(a or b) # 10
print(not a) # False

# Logical Operations (Zero Case)
a=0
b=20
print(a and b) # 20
print(a or b) # 10
print(not a) # False

'''Identity Operators'''
# Number case
a=10
b=20

print(a is b) # False
print(a is not b) # True
print(a == b) # False
print(a != b) # True

# String Case
a="Python"
b="Python"

print(a is b) # False
print(a is not b) # True
print(a == b) # False
print(a != b) # True

'''Membership Operators'''
a=[1,2,3,4,5]
print(1 in a) # True
print(10 in a) # False
print(1 not in a) # False
print(10 not in a) # True

'''Bitwise Operators'''
a=2
b=3
# And
print(a & b) # 0
print(a | b) # 3
print(a^b) # 1
a=5
print(~a) # -6
print(a<<b) # 40
print(a>>b) # 0

print(~3) # -4
print(4^6) # 
print(3>>2)
print(3<<2)