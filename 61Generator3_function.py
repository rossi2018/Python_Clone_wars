#Iterable
#Iteraation
#Generator

def generator_function(num):
    for i in range(num):
        yield i

for item in generator_function(1000):
    print(item)