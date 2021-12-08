#Using generator make it  use less resources in fibonacci series 

def fib(number):
    a=0
    b=1
    for i in range(number):
        yield a
        temp=a
        a=b
        b=temp+b

for x in fib(20):
    print(x)

#Doing the fibonacci series with list.Using this list method keeps it in memory therby using much resources
def fib2(number):
    a=0
    b=1
    result=[]
    for i in range(number):
        result.append(a)
        temp=a
        a=b
        b=temp+b
    return result

print(fib2(20))