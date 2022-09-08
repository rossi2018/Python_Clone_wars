#Function that check for the missing numbers 
#Given an array containing a range of numbers from 0 to n with a missing number, find the missing number in 
# the input array.

def findMissingNumbers(n):
    numbers=list(n)
    output=[]
    for i in range(n[0],n[-1]):
        if i not in numbers:
            output.append(i)
    return output

print(findMissingNumbers([0,3,4,8,10]))