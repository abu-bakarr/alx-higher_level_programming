#!/usr/bin/python3
"""A empty class Square that defines a square
This module provides a simple version of class
"""


class Square:
    """The class definition"""
    def __init__(self, size=0, position=(0, 0)):
        """init"""
        self.size = size
        self.position = position

    def __str__(self):
        return str(self.my_print())

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

    @property
    def position(self):
        """position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the size"""
        if type(value) is not tuple or len(value) < 2 or\
           (isinstance(value[1], int) is not True) or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """calculate the area"""
        return self.__size ** 2

    def my_print(self):
        """print the area"""
        if self.__size == 0:
            return ''
        for j in range(self.__position[1]):
            print()
        for i in range(self.__size - 1):
            print(' ' * self.__position[0], end='')
            print('#' * self.__size)
        print(' ' * self.__position[0], end='')
        print('#' * self.__size, end='')
        return ''
