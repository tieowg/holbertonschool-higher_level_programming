#!/usr/bin/python3
"""Module that defines class Rectangle which inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

# class BaseGeometry:
#     def area(self):
#         raise Exception("area() is not implemented")
#
#     def integer_validator(self, name, value):
#         if not isinstance(value, int):
#             raise TypeError(f"{name} must be an integer")
#         if value <= 0:
#             raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height


if __name__ == "__main__":
    print(issubclass(Rectangle, BaseGeometry))
