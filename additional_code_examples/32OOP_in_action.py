class Apple:
    def __init__(self,color,flavour):
        self.color=color
        self.flavour=flavour

    def __str__(self):  #We use the __str__ method when we want to print out string with print function and the object together
        return "This apple is {} and its flavour is {}" .format(self.color,self.flavour)

jonagold=Apple("Red","Sweet")
print(jonagold)