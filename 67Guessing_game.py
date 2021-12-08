from random import randint
import sys

#generate number from 1 to 10 
answer=randint(int(sys.argv[1]),int(sys.argv[2]))

#input from user?


#check that input is a number 1 to 10 
while True:
    try:
        guess=int(input("Guess a number 1~10:  "))
        if 0 < guess < 11:
            if guess == answer:
                print("you are a genious! ")
                break
        else:
            print("hey bozo, i said 1~10 ")
    except ValueError:
        print("Please enter a number")
        continue

#check if number is the right guess. Otherwise ask again.

#----------------------------------instruction on using this program
#playing this game use the terminal by typing this in the terminal like this:
#python3 67Guessing_game.py 1 2



#once you guess the number correctly,it will display:
#you are genious! 