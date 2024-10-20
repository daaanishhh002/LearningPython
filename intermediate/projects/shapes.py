import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract class for creating other shapes.
    """    
    total_shapes_created = 0

    def __init__(self, name):
        self.name = name
        Shape.total_shapes_created += 1

    @abstractmethod
    def calculate_area(self):
        pass

    def get_name(self):
        return f"{self.name}"


class Circle(Shape):
    def __init__(self, radius):
        super().__init__('Circle')     # inits name to 'Circle'
        self.__radius = radius

    def calculate_area(self):
        return math.pi * self.__radius**2

    def get_radius(self):
        return self.__radius


class Square(Shape):
    def __init__(self, side):
        super().__init__('Square')     # inits name to 'Square'
        self.__side = side

    def calculate_area(self):
        return self.__side**2

    def get_side(self):
        return self.__side


class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__('Rectangle')  # inits name to 'Rectangle'
        self.__length = length
        self.__breadth = breadth

    def calculate_area(self):
        return self.__length * self.__breadth

    def get_sides(self):
        return self.__length, self.__breadth


if __name__ == '__main__':
    # prints results
    print(Shape.total_shapes_created)
    circle = Circle(22)
    square = Square(19)
    rectangle = Rectangle(15, 9)
    print(Shape.total_shapes_created)


    name = circle.get_name()
    print(name)

    side = square.get_side()
    print(side)

    area = rectangle.calculate_area()
    print(area)