# Banking system using OOP

# Parents class: user
# Holds details about a user
# Has a function to show user details

# Child class: Bank
# Stores details about account balance
# stores details about the account
# Allows for deposits,withdraw,view_balance


class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal details")
        print("")
        print("Name", self.name)
        print("Age ", self.age)
        print("Gender ", self.gender)


class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account balance has been updated by adding up deposite : #", self.balance)


    def withdraw(self,amount):
        self.amount=amount
        if (self.amount> self.balance):
            print("Insufficient Funds | Balance available: #", self.balance)
        else:
            self.balance=self.balance-self.amount
            print("Account balance has been updated: #", self.balance)

    def view_balance(self):
        self.show_details()
        print("Account balance  : #", self.balance)



jp=Bank("Rossi",20,"Male")
jp.deposit(10000)
jp.withdraw(1000)
jp.view_balance()