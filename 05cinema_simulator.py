#Program to check if a user is old enogh to watche a film 
#and wether they are enough seat left, the system update itself when
#someone book a seat and also reduce the seat by one when soemone purcahse
# a ticket 

films={
    "Finding Dory": [3,5],  #in the dictionary the first number is age and the second number is ticket 
    "Bourne":[18,2],
    "Tarzan":[15,5],
    "Ghost Busters":[12,5]
}

while True:
    choice=input("What film would you like to watch?: ").strip().title()

    if choice in films:
        age=int(input("How old are you?: ").strip())

        # check user age 
        if age>=films[choice][0]:
            # check enough seats
            num_seats=films[choice][1]
            if num_seats>0:
                print("Enjoy the film!")
                films[choice][1]=films[choice][1]-1
            else:
                print("Sorry, we are sold out! ")
                
        else:
            print("Your are too young to see that film")

    else:
        print("We dont have that film.......")