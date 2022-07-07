#A list comprehension produces a list as output, a generator produces a generator object.

def num_sequence(n):
    """ Generate values from 0 to n"""
    i=0
    while i < n:
        yield i
        i +=1

    
result=num_sequence(19)

for item in result:
    print(item)