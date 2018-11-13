import datetime

class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self,amount):
        self.balance += amount
        now = datetime.datetime.now()
        print("Last Transaction €{} Cr".format(amount)+" "+now.strftime("%d/%m/%Y %H:%M:%S"))

    def withdraw(self,amount):
        if self.balance - amount >= self.min_balance:
            self.balance = self.balance - amount
            now = datetime.datetime.now()
            print("Last Transaction €{} Dr".format(amount)+" "+now.strftime("%d/%m/%Y %H:%M:%S"))
        else:
            print("Sorry, not enough funds!")

    def statement(self):
        print("Account Balance: € {}".format(self.balance))

class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = -1000)

    def __str__(self):
        return "{}'s Current Account : Balance €{}".format(self.name,self.balance)

class Savings(Account):
    def __init__(self,name, balance):
        super().__init__(name,balance,min_balance=0)

    def __str__(self):
        return "{}'s Savings Account : Balance €{}".format(self.name,self.balance)
        
