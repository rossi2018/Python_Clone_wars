class PlayerCharacter:
    membership=True #Class object atrribute (Its static)
    def __init__(self,name="Anonymous",age=0):
        if (age > 18):
            self.name=name  
            self.age=age #Attribute or class atrribute(Its dynamic)
        


    def run(self):      #Method
        print("run")
        return "done"
    
    def shout(self):
        print(f"my name is {self.name}")

    

         #Instantiate object
player1=PlayerCharacter("Tom",10)

print(player1.shout())



