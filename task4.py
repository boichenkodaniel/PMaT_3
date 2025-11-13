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

rect = Rectangle(5, 3)
print(f"Прямоугольник: площадь: {rect.area()}, периметр: {rect.perimeter()}")
