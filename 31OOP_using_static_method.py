import csv

class Item:
    # Class Attribute
    pay_rate = 0.8  # The pay rate after 20% discount

    all=[]

    def __init__(self, name: str, price: float, quantity=0):
        # Run validationto the received arguments
        assert price >= 0, f"Price{price} is not greater than or equal to zero!"
        assert quantity >= 0, f" Quantity {quantity} is not greater than or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity


        #Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    @classmethod
    def instantiate_from_csv(cls):
        with open ("30Item.csv","r") as f:
            reader = csv.DictReader(f)
            items=list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )
     
    
    def __repr__(self):
        return f"Item ('{self.name}','{self.price}','{self.quantity}')"


    @staticmethod
    def is_integer(num):
        #we will count out the float that are point zero
        #For i.e: 5.0,10.0
        if isinstance(num, float):
            #count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False


print(Item.is_integer(7.0))