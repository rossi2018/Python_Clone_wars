class Item:
    # Class Attribute
    pay_rate = 0.8  # The pay rate after 20% discount

    def __init__(self, name: str, price: float, quantity=0):
        # Run validationto the received arguments
        assert price >= 0, f"Price{price} is not greater than or equal to zero!"
        assert quantity >= 0, f" Quantity {quantity} is not greater than or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate


item1 = Item("Phone", 100, 1)


item2 = Item("Laptop", 1000, 3)
item1.apply_discount()
print(item1.price)

item2=Item("Laptop",1000,3)
item2.pay_rate=0.7
item2.apply_discount()
print(item2.price)

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())

# print(Item.pay_rate)
# print(item1.pay_rate)
# print(item2.pay_rate)

# #To check all the attribute that belong to a specific object use this built in method(__dict__)
# print(Item.__dict__)  #All the attributes for class level
# print(item1.__dict__) #All the attribute for instance level
