#WHat is recursion?
#The repeated application of the same procedure to a small problem

#Recursion lets us tackle complex problems by reducig the problem to a simpler one.
#In progrommmaning,recursion is a way of doing a repetitive task by having  a function call itself
#A recursive function call itself usually with a modified perimeter until it reaches a specific condition.
#  This condition is called the base case 

def factorial(n):
    print("Factorial called with " + str(n))
    if n < 2:   #This line is the base case 
        print("Returning 1")
        return 1
    result=n * factorial(n-1) #THis line is the recursive case
    print("Returning " + str(result) + " for factorial of" + str(n))
    return result

factorial(4)
