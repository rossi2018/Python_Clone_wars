#map, filter, zip, and reduce 
def multiple_by2(li):
    new_list=[]
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiple_by2([1,2,3]))

#Using map function ,we can reduce the code 
#Note: map function is map(function, iterables )

def multiple_by3(item):
    return item*2

print(list(map(multiple_by3, [1,2,3])))

#Another example of map function
#Calculate the length of each word in the tuple:
def myfunc(n):
    return len(n)

x=map(myfunc, ("apple","banana","cherry"))
print(list(x))

#The third example of map function 
#Make new fruits by sending two iterable objects into the function:
def myfuncn(a,b):
    return a + b

s=map(myfuncn, ("apple","banana","cherry"),("orange","lemon","pineapple"))
print(list(s))