#When a return statement is executed, the function exits, so that the code that follows doesn't get executed
#The return is used basically inside the if statement which function as the else statment as well

def is_even(number):
    if number % 2 == 0:
        return True
    return False

print(is_even(10))
print(is_even(11))

