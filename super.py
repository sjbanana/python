class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width 
        self.height = height

circle = Circle(color = "red", is_filled = True, radius = 5)
square = Square(color = "blue", is_filled = False, width = 4)
print(circle.color)
print(circle.is_filled)
print(circle.radius)

print(square.color)
print(square.is_filled)
print(square.width)