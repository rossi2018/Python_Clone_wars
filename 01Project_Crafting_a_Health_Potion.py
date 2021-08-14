import random 


health=50

difficulty=2  #Make the player to get less and less health with more difficulty by changing the number from 1 to 3
portion_health=int(random.randint(25,50)/difficulty)  #this code snipet will generate a single random number from 25 and 50
health=health + portion_health

print(health)