class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print(f"my name is {self.name}")

    @classmethod
    def adding_things(cls,num1, num2):
        return num1 + num2

    

playe1 = PlayerCharacter("Tom", 20)
print(playe1.shout())
print(playe1.adding_things(2, 3))

print(PlayerCharacter.adding_things(10,4))
