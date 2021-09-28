#!/usr/bin/python3
"""A class Square that defines a square
This module provides a simple version of class
"""


class Square:
    """The class definition"""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
