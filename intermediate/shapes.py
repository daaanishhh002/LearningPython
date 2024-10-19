import math
from abc import ABC, abstractmethod


class Shape(ABC):
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
        super().__init__('Circle')
        self.__radius = radius

    def calculate_area(self):
        return math.pi * self.__radius**2

    def get_radius(self):
        return self.__radius


class Square(Shape):
    def __init__(self, side):
        super().__init__('Square')
        self.__side = side

    def calculate_area(self):
        return self.__side**2

    def get_side(self):
        return self.__side


class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__('Rectangle')
        self.__length = length
        self.__breadth = breadth

    def calculate_area(self):
        return self.__length * self.__breadth

    def get_sides(self):
        return self.__length, self.__breadth
