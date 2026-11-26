# TUPLES -> ()

numbers=(1,2,3,4)
print(numbers, type(numbers))

# Tuples are ordered collection of Data

# Tuples are immutable
nums=(1,2,3,4)
# nums[0]=100 -> TypeError: 'tuple' object does not support item assignment ----> Soo tuples are immutable.
print(nums)

#Tuples can store multiple data type, be accessed by indexing and can support slicing. 
stu_info=('Mahadev',True,7.93,22)
print(stu_info)
print(stu_info[3])
print(stu_info[0:3])
print(stu_info[-2]) # negative indexing

name=("Ganesha",)
print(name)
print(name,type(name))
print(name*3) # repeat the tuple for more times

# Tuple Constructor
rgb=tuple("red")
print(rgb)
print(type(rgb))


""" We cannot add elements to a tuple due to its immutability
Inorder to add elements into a tuple, we need to convert the tuple into a list"""
x=(1,2,3)
z=(10,11,12)
y=list(x)

y.append(4)
print(y)

# Loop

loop=(10,11,12)
for i in range(len(z)):
    print(z[i])

#Tuple Methods
z=(10,11,12,10)
print(z.count(2))
print(z.index(10)) # First index of 10
print(z.index(10,2)) # Index of 10 from the 3rd position

# Unpacking of Tuples
emp=("Mahadev",100)
name,empid=emp
print(name)
print(empid)

# TUPLE b*
s=(2,4,6,8,10)
(a,*b)=s
print(a)
print(b)


# OTHER METHODS

t=(10,20,30,40,500)

print(len(t))
print(max(t))
print(min(t))
print(sum(t))
print(sorted(t))
print(any(t))
print(all(t))
print(10 in t)

t1=(1,2)
t2=(3,4)

print(1,2)
print(3,4)

del t