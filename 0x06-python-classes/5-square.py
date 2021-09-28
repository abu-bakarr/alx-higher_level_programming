#!/usr/bin/python3
"""A empty class Square that defines a square
This module provides a simple version of class
"""


class Square:
    """The class definition"""
    def __init__(self, size=0):
        """init"""
        self.size = size

    @property
    def size(self):
        """size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """calculate the area"""
        return self.__size ** 2

    def my_print(self):
        """print the area"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print('#' * self.__size)
