import re


class Account:
    def __init__(self,balance,accountnumber):
        self.balance=balance
        self.accountnumber=accountnumber
    def deposit(self,amount):
        self.amount=amount
        self.balance+=amount
        return self.balance
        return f"my deposit is{amount} on the account {self.account_number}. The balance is{self.balance} "
    def withdraw(self,amount):
        self.amount=amount
        self.withdraw-=amount
        return self.amount
        return f"my withdraw is{amount} on the account {self.account_number}.The balance is{self.balance}"
        
    

    
