class User:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def make_deposit(self,amount):
        self.balance+=amount
        return self
    def make_withdraw(self,amount):
        self.balance-=amount
        return self
    def display_userBalance(self):
        print(f"User:{self.name},Balance:${self.balance}")
        return self
    def transfer_money(self,other_user,amount):
        self.make_withdraw(amount)
        other_user.make_deposit(amount)
        print(f"{self.name} transfered ${amount} to {other_user.name}")
        return self
    
user1=User("Qasem Aboalia")
user2=User("Mohammad")
user3=User("Khaled")

#First user make 3 deposite and 1 withdraw
user1.make_deposit(100)
user1.make_deposit(200)
user1.make_deposit(50)
user1.make_withdraw(75)
user1.display_userBalance()
#Second user make 2 deposite and 2 withdraw
user2.make_deposit(300)
user2.make_deposit(150)
user2.make_withdraw(100)
user2.make_withdraw(50)
user2.display_userBalance()
#Third user make1 deposite and 3 withdraw
user3.make_deposit(500)
user3.make_withdraw(100)
user3.make_withdraw(50)
user3.make_withdraw(75)
user3.display_userBalance()
#Transfer money from user1 to user3
user1.transfer_money(user3,50)

user1.display_userBalance()
user3.display_userBalance()
