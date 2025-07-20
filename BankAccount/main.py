class BankAccount:
    def __init__(self,int_rate=0.01,balance=0):
        self.int_rate=int_rate
        self.balance=balance
    def deposite(self,amount):
        self.balance+=amount
        return self
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance-=5
        return self
    def display_account(self):
        print(f"BankAccount-Interest Rate: {self.int_rate}, Balance:${self.balance}")
        return self
    def yield_interst(self):
        if self.balance>0:
            interest=self.balance*self.int_rate
            self.balance+=interest
        return self
    
BankAccount1=BankAccount(0.02,100)
BankAccount2=BankAccount(0.03,200)

BankAccount1.deposite(50).deposite(200).deposite(50).withdraw(70).yield_interst().display_account()
BankAccount2.deposite(30).deposite(50).withdraw(50).withdraw(100).withdraw(60).withdraw(20).yield_interst().display_account()