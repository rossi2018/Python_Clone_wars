pairs_1=[]
for num1 in range(0,2):
    for num2 in range(6,8):
        pairs_1.append((num1,num2))
print(pairs_1)

#How to do this with list comprehension 
pairs_2=[(num3,num4) for num3 in range(0,2) for num4 in range(6,8)]
print(pairs_2)


# How would a list comprehension that produces a list of the first character
#  of each string in doctor look like? Note that the list comprehension uses
#   doc as the iterator variable. What will the output be?

doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']
print([doc[0] for doc in doctor])

print("__" * 14)
#To create the list of lists, you simply have to supply the list comprehension as the output expression
#  of the overall list comprehension:

#[[output expression] for iterator variable in iterable]
#Note that here, the output expression is itself a list comprehension.

## Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(0,5)] for row in range(0,5)]
# Print the matrix
for row in matrix:
    print(row)

print('Conditional in list comprhension__________________________')
#conditional in comprehension
print([num ** 2 for num in range(10) if num% 2==0])


print('Dictioanry comprehension__________________________________')
pos_neg={num: --num for num in range(9)}
print(pos_neg)

