from ctypes import sizeof
import numbers
from typing import Sized


class Fruit:
    name="mango"
    color="green"
    sized="small"
    classification="vitamin"
    def __init__(self,name,color,classification,small):
        self.name=name
        self.color=color
        self.sized=Sized
        self.classification=classification


from bank import Account
acc1=Account(name="Joy",number=123)
acc2=Account(name="susan",number=324)
    # acc1.deposit(10000)
    # acc2.deposit(15000)
    # acc1(7500)
    # acc2(8000)


def deposit(self,amount):
    if amount<=0:
        return f"deposit amount must be greater than zero"
    else:
        self.balance+=amount
        return f""    
