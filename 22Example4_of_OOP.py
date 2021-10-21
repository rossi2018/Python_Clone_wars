class Car:
    def __init__(self,name,mileage):
        self.name=name
        self.mileage=mileage

    def max_speed(self,speed):
        return f" The {self.name} runs at the maximum spped of {speed} km/hr"

Honda=Car("Honda city", 21.4)
print(Honda.max_speed(150))

Skoda=Car("Skoda Octavia",13)
print(Skoda.max_speed(210))
