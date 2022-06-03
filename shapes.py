from math import pi
class Circle:
    def __init__(self,r):
        self.radius =r
    

    def area(self):
        a= 3.14*self.radius*self.radius
        return f"The area of the circle is {a} "


    def calculate_circumference(self):
        calclate_circumference=2*3.14*self.radius
        return f"The circumference of a cirle is {calclate_circumference}"

circle1  = Circle(14)
print(circle1.area())
print(circle1.calculate_circumference())



class Square:
    def __init__(self,a):
         self.side=a
    

    def area(self):
         area= 3.14*self.side*self.side
         return f"The area of the square is{area}"


    def calculate_perimeter(self):
        calcule_perimeter=4*self.side
        return f"The perimeter of a square is{calcule_perimeter}"


Square1 = Square(7)
print(Square1.area())
print(Square1.calculate_perimeter())





class Rectangle:
    def __init__(self,w,l):
         self.side_w=w
         self.side_l=l
    

    def area(self):
         area= self.side_w*self.side_l
         return f"The area of the rectangle is{area}"


    def calculate_perimeter(self):
        calcu_perimeter=2*self.side_l*self.side_w
        return f"The perimeter of a rectangle is{calcu_perimeter}"


rectangle1  = Rectangle(28,6)
print(rectangle1.area())
print(rectangle1.calculate_perimeter())




class Sphere:
    def __init__(self,r):
         self.radiuss=r
    

    def surface_area(self):
         surfac_area= self.radiuss*self.radiuss
         return f"surface area of the Sphere is{surfac_area}"
         
    def calculate_volume(self):
        calculate_volume=4/3*22/7*self.radiuss**3
        return f"The volume of a Sphere is{calculate_volume}"


Sphere1  = Sphere(r=4.5)
print(Sphere1.surface_area())
print(Sphere1.calculate_volume())



