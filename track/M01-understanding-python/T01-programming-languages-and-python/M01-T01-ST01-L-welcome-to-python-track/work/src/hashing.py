print(hash(1))
print(hash("Hello"))
print(hash(5.0))

x="Python"
print(hash(x))

# Hashing in sets

s={1,"Python"}
# print(hash(s)) -> TypeError: unhashable type: 'set'

a=1
b=1.0
print(hash(a))
print(hash(b))
print(a==b)
print(a is b)


# Custom hashing in sets is done using __dunder__ meethods these are also called as magic methods
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def __eq__(self,other):
        return self.name==other.name and self.age==other.age
p1=Person("John",30)
p2=Person("John",30)
print(p1==p2)
