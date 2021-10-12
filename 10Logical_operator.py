#You can check the behaviour of the code by changinh the boolean value to True or False
is_magician=True
is_expert=False

if is_magician and is_expert:
    print("You are a master magician")

elif is_magician and not is_expert:
    print("At least your'r getting there")

elif not is_magician:
    print("You need magic powers")