import random

class Coin:
    def __init__(self,rare=False,clean=True,heads=True, **Kwargs):
        for key,value in Kwargs.items():
            setattr(self,key,value)



        self.is_rare=rare
        self.is_clean=clean
        self.heads=heads

        if self.is_rare:
            self.value=self.original_value * 1.25
        else:
            self.value=self.original_value

        if self.is_clean:
            self.colour=self.clean_colour
        else:
            self.colour=self.rusty_colour

    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour=self.clean_colour


    def __del__(self):
        print("Coin spent!")

    def flip(self):
        head_option = [True, False]
        choice = random.choice(head_option)
        self.heads = choice


class Pound(Coin):
    def __init__(self):
        data = {
            "original_value":1.00,
            "clean_colour":"gold",
            "rusty_colour":"greenish",
            "num_edges":1,
            "diameter":22.5,
            "thickness":3.15,
            "mass":9.5
        }
        super().__init__( **data)

coin_obj=Pound()
coin_obj.rust()
print(coin_obj.colour)
