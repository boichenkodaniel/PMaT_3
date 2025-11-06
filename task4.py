import math
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius * self.radius
    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    def perimeter(self):
        return self.a + self.b + self.c

rect = Rectangle(5, 3)
circle = Circle(2)
triangle = Triangle(5, 3, 4)
print(f"Прямоугольник: площадь: {rect.area()}, периметр: {rect.perimeter()}")
print(f"Круг: площадь: {circle.area():.3f}, периметр: {circle.perimeter():.3f}")
print(f"Треугольник: площадь: {triangle.area()}, периметр: {triangle.perimeter()}")