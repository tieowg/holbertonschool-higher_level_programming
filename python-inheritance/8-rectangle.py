#!/usr/bin/python3
'''salam'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry
'''salam'''


class Rectangle(BaseGeometry):
    '''salam'''
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height


if __name__ == "__main__":
    print(issubclass(Rectangle, BaseGeometry))
