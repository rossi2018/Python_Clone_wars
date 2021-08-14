known_users=["Rossi","Sam","Joshua","Job","Henry","Rose","Ifeanyi","Wale"]


while True:
    print("Hi, My name is Travis am a robot")
    name=input("what is your name?:").strip().capitalize()

    if name in known_users:
        print("Hello {}".format(name))
        remove=input("Would you like to be removed from the system (y/n)?").lower()

        if remove == "y":
            known_users.remove(name)
        elif remove=="n":
            print("No problem, i didn't want you to leave anyway!")

            
    else:
        print("Hmmmm i dont think i have met you yet {}".format(name))
        add_me=input("Would you like to be added to the systme (y/n) ?:").strip().lower()
        if add_me=="y":
            known_users.append(name)
            
        elif add_me=="n":
            print("No worries, see you around!")