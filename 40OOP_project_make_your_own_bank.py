class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance=balance
        self.min_balance = min_balance

    def deposite(self, amount):
        self.balance += amount

    def withdraw(self, amonut):
        if self.balance - amonut >= self.min_balance:
            self.balance -= amonut
        else:
            print("Sorry, not enough funds! ")

    def statement(self):
        print("Account balance: #{}".format(self.balance))


class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=-1000)


    def __str__ (self):
        return "{}'s Current Acount: Balance # {}".format(self.name, self.balance)

class Savings(Account):
    def __init__ (self,name,balance):
        super().__init__(name,balance,min_balance=0)

    def __str__ (self):
        return "{}'s Savings Acount: Balance # {}".format(self.name, self.balance)


x = Current("Rossi", 500)
x.deposite(300)
print(x.statement())
x.withdraw(1000)
x.statement()
print(x.withdraw(800))
x.withdraw(800)
print(x.statement())

print(x.withdraw(1))
print(x)

tom=Savings("Tommy",300)
print(tom)
tom.deposite(5000)
print(tom)
tom.withdraw(4000)
print(tom)
print(tom.statement())
tom.withdraw(1500)
print(tom)