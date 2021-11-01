#The filter() method filters the given sequence with the help of a function that tests each element in the sequence
#to be true or not
#syntax: filter(function,sequence)

my_list=[1,2,3]

def only_odd(item):
    return item % 2 !=0

print(list(filter(only_odd, my_list)))

#Secomd example of using filter function 

ages=[5,12,17,18,24,32] 

def myfunc(x):
    if x < 18:
        return False
    else:
        return True

adults=filter(myfunc,ages)

for x in adults:
    print(x)
    
#or uncomment the code snipppet below

# print(list(adults))