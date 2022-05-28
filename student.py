# class Student:
#       name="Effence"
#       country="kenya"
#       age=20
#       school="Akirachix"
class Student:
    school="Akirachix"
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
        



    

