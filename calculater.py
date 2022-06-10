from math import factorial
import numbers
from re import I


def add(a,b):
    answer=a+b
    return answer
def subtract(a,b):
      answer=a-b
      return answer

def multiplication(a,b):
      answer=a*b
      return answer


def division(a,b):
      answer=a/b
      return answer


def modulus(a,b):
      answer=a%b
      return answer     

def exponet(a,b):
      answer=a**b
      return answer

def int_divide(a,b):
      answer=a//b
      return answer

def square(a,b):
      answer=a*a

      return answer

def cube(a,b):
      answer=a*a*a
      return answer



def factorial(number):
    factor=1
    for i in range(1,number + 1):
        factor *=i
    return factor
 
