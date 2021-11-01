
#Sqaure of the individual number in the list
my_list=[5,4,3]
new_list=list(map(lambda num: num**2,my_list))
print(new_list)

#List sorting of the second itme in the list of tuple item
a=[(0,2),(4,3),(9,9),(10,-1)]
a.sort(key=lambda x: x[1])
print(a)

