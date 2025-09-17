#!/usr/bin/python3
"""
2-rectangle module
Bu modul Rectangle sinifini təyin edir, eni və hündürlüyü olan düzbucaqlı.
Həmçinin sahə və perimetr hesablama metodlarına malikdir.
"""


class Rectangle:
    """
    Rectangle sinifi.
    Eni və hündürlüyü olan düzbucaqlını təmsil edir.
    Sahə və perimetr hesablamaq üçün metodlara malikdir.
    """

    def __init__(self, width=0, height=0):
        """
        Rectangle sinifinin konstruktoru.

        Args:
            width (int, optional): Düzbucaqlının eni. Default 0.
            height (int, optional): Düzbucaqlının hündürlüyü. Default 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width atributunun getter metodu"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        width atributunun setter metodu

        Args:
            value (int): Yeni en dəyəri

        Raises:
            TypeError: Əgər value integer deyilsə
            ValueError: Əgər value 0-dan kiçiksə
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height atributunun getter metodu"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        height atributunun setter metodu

        Args:
            value (int): Yeni hündürlük dəyəri

        Raises:
            TypeError: Əgər value integer deyilsə
            ValueError: Əgər value 0-dan kiçiksə
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Düzbucaqlının sahəsini hesablayır.

        Returns:
            int: Düzbucaqlının sahəsi (eni * hündürlük)
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Düzbucaqlının perimetrini hesablayır.

        Returns:
            int: Düzbucaqlının perimetri (2 * (eni + hündürlük))
            Əgər eni və ya hündürlüyü 0-dırsa, 0 qaytarır.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
