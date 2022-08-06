import random

max_val=6
min_val=1

roll_again="Yes"

while roll_again=="Yes" or roll_again=="y" or roll_again=="yes" or roll_again=="Y":
    print("Rolling the dicess.............")
    print("The values are :")

    print(random.randint(min_val,max_val))
    print(random.randint(min_val,max_val))

    roll_again=input("Do you want to roll again? ")