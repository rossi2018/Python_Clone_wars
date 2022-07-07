#List comprehensions can be built over iterables. They can replace a for loop in a single line of code.
#List comprehension looks like this: [output expression for iterator variable in iterable]

#create a list comprehesion: squares
squares=[i*i for i in range (0,10)]
print(squares)

print('Nested list comprehension ______________________' )
#Nested list comprehensions 
#In this exercise, we will be writing a list comprehension within another 
# list comprehension, or nested list comprehensions. It sounds a little tricky.
#  Let’s step aside for a while from strings. One of the ways in which lists can be 
# used are in representing multi-dimension objects such as matrices. Matrices can be represented
#  as a list of lists in Python. For example a 5 x 5 matrix with values 0 to 4 in each row can be written as:
#matrix = [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]

#Our task is to recreate this matrix by using nested listed comprehensions. Recall that we can create one of 
# the rows of the matrix with a single list comprehension. To create the list of lists, we simply have to supply 
# the list comprehension as the output expression of the overall list comprehension:
#[[output expression] for iterator variable in iterable]
#Note that here, the output expression is itself a list comprehension.

# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(0,5)] for row in range(0,5)]
# Print the matrix
for row in matrix:
    print(row)