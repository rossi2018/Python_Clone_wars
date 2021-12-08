#Error handling
#Error handling allow the script to keep running even if they is an  error 



while True:
    try:
        age=int(input("What is your age? "))
        print(age)
    except:
        print("Please enter a number")
    else:
        print("Thank you")
        break
