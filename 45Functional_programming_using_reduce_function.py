#Syntax: reduce(function, sequence[, initial]) -> value

#The reduce() function accepts a function and a sequence and returns a single value calculated as follows:

# Initially, the function is called with the first two items from the sequence and the result is returned.
# The function is then called again with the result obtained in step 1 and the next value in the sequence. 
# This process keeps repeating until there are items in the sequence.

from functools import reduce

my_list=[1,2,3]

def accumulator(acc,item):
    print(acc,item)
    return acc + item

print(reduce(accumulator,my_list,0 )) #can change the value of 0 to other numbers eg 10,20 to see how it work

#Another example of reduc function
def do_sum(x1,x2):
    return x1+x2

print(reduce(do_sum, [1,2,3,4]))
#the reduce () call perform the following operation like this: (((1+2)+3)+4) => 10