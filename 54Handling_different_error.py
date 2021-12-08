while True:
    try:
        age=int(input("What is your age? "))
        10/age       #when you inpute 0 in age, it will give you division by zero error
    except ValueError:        #This except bloc only accept valueError,any other error he does not care about
        print("Please enter a number")
    except ZeroDivisionError:
        print("please enter age higher than zero")
    else:
        print("Thank you")
        break