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

class User:
    def __init__(self, name,email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate= 0.01, balance=0)

    def user_info(self):
        print(f"Name: {self.name}")
        print(f"email: {self.email}")
        self.account.display_account()
        return self
    
Qasem = User("Qasem Abualia", "Qasem.abualia@Axsos-academy")

Qasem.account.deposite(500).deposite(200).withdraw(3350)
Qasem.user_info()
