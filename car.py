from atexit import register
from turtle import color


class Car:
    name="prado"
    color="black"
    range="40km"
    registeration="kbl"
    # def__init__(self,name,color,range,registeration):
    #        self.name=name
    #        self.color=color
    #        self.range=range
    #        self.registtration=registeration


    
#  Add a new attribute to the class Account called deposits which by default is an empty list.
# Add another attribute to the class Account called withdrawals which by default is an empty list.
# Modify the deposit method to append each successful deposit to self.deposits
# Modify the withdrawal method to append each successful withdrawal to self.withdrawals
# Add a new method called deposits_statement which using a for loop prints each deposit in a new line
# Add a new method called withdrawals_statement which using a for loop prints each withdrawal in a new line
# Modify the withdrawal method to include a transaction fee of 100 per transaction.
# Add a method to show the current balance.
        
        
# Add these methods to class student - full_name, year_of_birth, initials. Create two instances and verify the work as expected
# Add these methods to class Account - deposit, withdraw. Create two instances of account and verify they work as expected.
    
# condition for withdrawal to be seccessful
# reguested amount must be greater than current balance
# //         //                      //       zero
from locale import currency
from typing_extensions import Self
from unicodedata import name

from fruit import deposit
class Account:
    def __init__(self,account_name,account_number):
        self.account_name= account_name
        self.account_number=account_number
        self.balance=0
        self.deposits=[]
        self.withdrawals=[]
        self.transaction_cost=100

    def deposit(self,amount):
        if amount<=0:
            return f"deposit amount must be greater than zero"
        else:
            self.balance+=amount
            return f"{self.balance}"
            self.deposits.append(amount)
            return f"you have deposited{amount}your new balance is{self.balance},self.deposits"
       
    def withdraw(self,amount):
        if amount >self.balance:
            return f"sinsuficient fund"
        elif amount<=0:
            return f"amount must be greater than zero"
        else:
            self.withdrawals-=amount 
            return f"hello {self.account_number} you have withdrawn {amount} your balance is {self.balance}"
            self.withdrawals.append (amount)
            return f"you have withdraw {amount}your new balance is {self.balance},self.withrawals" 

    def deposit_statement(self):
        for deposit in self.deposit:
            print(f"your deposit is {deposit}")
        # print(*self.deposits,sep="\n")

    def withdraw_statement(self):
        # print(*self.deposits,self="\n")
        for withdrawals in self.withdrawals:
            print(f"your withdrawals is {withdrawals}")

    def withdrawals(self,amount):
        withdrawals_balance=self.transaction_cost
        if amount>withdrawals_balance:
            return "insufficiate funds" 
    # method to show current balance
    def current_balance():
        print(f"hello{Self.name},your current balance is{self.balance}")
          




       
    def __init__(self,first_name,last_name,age,country):
           self.first_name=first_name
           self.self_name=last_name
           self.age=age
           self.country=country
    def greeting(self):
         return f"hello {self.first_name} from {self.country} welcome to {self.school}"
    def full_name(self):
        return f"my name is {self.first_name} {self.last_name}"
    def year_of_birth(self):
        return 2022-self.age
    def initials(self):
        return f"my initials{self.first_name[0]} {self.last_name[0]}"

#  Add a new attribute to the class Account called deposits which by default is an empty list.
# Add another attribute to the class Account called withdrawals which by default is an empty list.
# Modify the deposit method to append each successful deposit to self.deposits
# Modify the withdrawal method to append each successful withdrawal to self.withdrawals
# Add a new method called deposits_statement which using a for loop prints each deposit in a new line
# Add a new method called withdrawals_statement which using a for loop prints each withdrawal in a new line
# Modify the withdrawal method to include a transaction fee of 100 per transaction.
# Add a method to show the current balance.
        
        
# Add these methods to class student - full_name, year_of_birth, initials. Create two instances and verify the work as expected
# Add these methods to class Account - deposit, withdraw. Create two instances of account and verify they work as expected.
    
# condition for withdrawal to be seccessful
# reguested amount must be greater than current balance
# //         //                      //       zero
    


