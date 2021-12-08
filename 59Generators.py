#Generator allow us to generate a sequence of value over  time

def make_list(num):
    result=[]
    for i in range(num):
        result.append(i*2)
    return result

my_list=make_list(100)
print(list(range(1000000))) #This particular list consumes large amount of memory generated from range  