class Shape:
    def area(self):
        print("This is base class")

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

square = Square(4)
print("Square Area:", square.area())

triangle = Triangle(5, 10)
print("Triangle Area:", triangle.area())

