# Lists are mutable ,ordered, and allows duplicates and can be accessed using index,[]
# General list storing using []
gen_list=[1,2,3,"Hello",3.14]

# creating List using list() constructor
list_constructor=list((1,2,3,4,5,6))
# List is ordered, they return in the way we give the elements
nums=[1,2,3,4,5]
print(nums)
print(type(nums))


#List is duplicatable - It supports duplicate values
numbers=[1,2,3,4,5,4,3,2,1]
print(numbers)

#List is mutable-  After creating, we can change its value
names=["Alice","Bob","Charlie"]
names[1]="David"
print(names)
print(type(names))


# Basic List Methods
names=["Alice","Bob","Charlie"]
names.append("Ram")
names.insert(2,"Sita")
names.pop()
names.remove("Sita")


n1=[5,7,4,1,2]
print(n1.sort())




# List Aliasing
student_info=["Ram",23]
stu=student_info
print(stu)
print(student_info)
print(stu is student_info)

x=[1,2,3]
y=[1,2,3]
print(x,y)
print(x==y)
print(x is y)