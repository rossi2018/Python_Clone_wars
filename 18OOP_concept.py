#OOP

class PlayerCharacter:
    def __init__(self,name,age):
        self.name=name  #Attribute or properties
        self.age=age


    def run(self):      #Method
        print("run")
        return "done"

         #Instantiate object
player1=PlayerCharacter("Daniel",25)
player2=PlayerCharacter("James",22)

print(player1.name) 
print(player2.run())