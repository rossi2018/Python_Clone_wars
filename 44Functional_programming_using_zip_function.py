#Zip function in python

#The zip() function returns a zip object, which is an iterator of tuples where the first item in each 
# passed iterator is paired together, and then the second item in each passed iterator are paired together etc.

my_list=[1,2,3]
your_list=[10,20,30]
their_list=(5,4,3)

print(list(zip(my_list, your_list)))
print(list(zip(my_list,your_list,their_list)))

#if one tuple contains more items, these items are ignored
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b)
print(list(x))