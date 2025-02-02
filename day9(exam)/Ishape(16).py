from abc import ABC,abstractmethod
class IShape(ABC):
    @abstractmethod
    def cal_area(self):
        pass

class Rectangle(IShape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def cal_area(self):
        return self.width*self.height

class Circle(IShape):
    def __init__(self, radius):
        self.radius = radius

    def cal_area(self):
        return 3.14*self.radius*self.radius
n1=float(input("Enter width of rectangle: "))
n2=float(input("Enter height of rectangle: "))
rectangle = Rectangle(n1,n2)
print("Rectangle Area:", rectangle.cal_area())

n3=float(input("Enter radius of circle: "))
circle = Circle(n3)
print("Circle Area:", circle.cal_area())