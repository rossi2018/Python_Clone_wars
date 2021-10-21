class Shoe:
    #defines the initializer method
    def __init__(self,size,isOnSale,material,price):
       self.size=size
       self.isOnSale=isOnSale
       self.material=material
       self.price=price

    #Instantiate method
    def printInfo(self):
        return f"This pair of shoes are  size {self.material}, costs ${self.price}"


    #Instance method
    def putOnSale(self):
        self.isOnSale=True

sneakers=Shoe(11,"false","leather",81)

print(sneakers.printInfo())