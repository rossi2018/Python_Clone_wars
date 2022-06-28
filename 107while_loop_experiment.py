#The while loop will never stop running, because offset will be further decreased on every run. offset != 0 will never become False and the while loop continues forever.
#Note this first piece of code block is infinit loop

# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    offset = offset - 1
    print(offset)


#Fix things by putting an if-else statement inside the while loop(correct code)
offset=-6
while offset != 0:
    print("correcting....")
    if offset > 0:
        offset=offset -1

    else:
        offset=offset+1
    print(offset)