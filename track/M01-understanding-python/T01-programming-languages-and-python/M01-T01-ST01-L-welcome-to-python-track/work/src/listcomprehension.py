# Write a python program to find squares of a list of numbers using list comprehension

nums=[1,2,3,4,5]
sq_nums=[i*i for i in nums]
print(sq_nums)

# Write a python program to find even numbers in a list of numbers using list comprehension
nums=[1,2,3,4,5,6]
even_odd=[i for i in nums if i%2==0]
print(even_odd)

# Write a python program to find odd numbers in a range of 1 to 10 using list comprehension
odd=[i for i in range(1,11) if i%2!=0]
print(odd)

# Write a python program to convert a list of names into uppercase using list comprehension
names=["Ram","Sita","Lakshman","Hanuman"]
upper_list=[n.upper() for n in names]
print(upper_list)

# Write a python program to find length of each item in a list using list comprehension
len_lst=[len(n) for n in names]
print(len_lst)

# Write a python program to find even or odd numbers in list using if and else at the same time using list comprehension
num=[1,2,3,4,5,6]
result=["Even" if n%2==0 else "odd" for n in num]
print(result)

## Write a python program to find a number greater than 5 in list of numbers using list comprehension
gt_num=[n for n in num if n>5]

# Write a python program to extract each character of a word and store it as a list using list comprehension
word="Python"
char_list=[ch for ch in word]
print(char_list)

# # Write a python program to convert a matrix into a single list using list comprehension
matrix=[[1,2],[3,4],[5,6],[7,8]]
matrix_list=[n for row in matrix for n in row ]
print(matrix_list)

#  Write a python program to create multiplication pairs and store them in a single list using list comprehension
mul_pairs=[(i,j) for i in range(1,3) for j in range(1,4)]
print(mul_pairs)