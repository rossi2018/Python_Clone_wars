while True:
    try:
        age=int(input("What is your age? "))
        10/age
    except ValueError:
        print("Please enter a number")
    except ZeroDivisionError:
        print("Please enter a age higher than 0")
    else:
        print("Thank you! ")
        break
    finally:   #finally always runs last .Its important in a game server when you want to log the activities of the game
        print("Ok, i am finally done")