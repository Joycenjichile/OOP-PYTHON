import numbers
from ossaudiodev import SOUND_MIXER_ALTPCM
from unicodedata import name

 
def hello(name,age):
    year=2022-age
    print(f"Wellcome to AkiraChix ")

    return f"hello{name},you were born in {year}"


def my_country(country="Uganda",student="susan"):
        return f"hello{student} you are from {country}"
def my_country(country="Rwanda",student="Verite"):
       
#  def greet_multiple(*names):
#      print(names)
#      for name in names:
#          print(f"hello {name}") 
# #

 def greet_intergers(*numbers):
    sum=0
    for number in numbers:
        sum+=numbers
    return(sum)


def greet_multiple_name(**kwags):
    print(kwags)
    print(kwags. keys())
    print(kwags.values())

greet_multiple_name(name="Joyce")
greet_multiple_name(name="Joyce",age=20)
greet_multiple_name (name="Joyce",age=30,country="kenya")
(greet_multiple_name)


def greet_multiple_info(**kwags):
    keys=kwags.keys()
    if "country" in keys:
          print(f"hello {kwags['name']} you were born in {kwags['country']}")

    elif "age" in keys:
        year=2022-kwags["age"]
        print(f"hello {kwags['name']}")


def get_sum_add_greet(*args ,**kwargs):
    sum=0
    for num in args:
        sum+=num


        keys=kwargs.keys()
        if"name" in keys:
            print(f"hello {kwargs['name']} from {kwargs['country']} the anser is {sum}")
            
        elif"country" in keys:
            print(f"hello{kwargs['name']}from {kwargs['country']},the answer is{sum}")

    
    
    
    



        # write a function that accept any number of intergers and return the sum of all of them      