#!/usr/bin/env/ python3

class Rectangle():
    # Konstruktor mit Höhe, Breite
    def __init__(self, height, width):
        if height <= 0 or width <= 0:
            raise ValueError('height > 0 , width > 0 expected')
        self.__h = height
        self.__w = width

    # get, set methoden 
    @property
    def w(self):
        return self.__w

    @w.setter
    def w(self, width):
        if width > 0:
            self.__w = width
        else:
            raise ValueError('width > 0 expected')

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, height):
        if height > 0:
            self.__h = height
        else:
            raise ValueError('height > 0 expected')

    # Flächeninhalt
    def getArea(self):
        return self.__h * self.__w

    # Umfang
    def getPerimeter(self):
        return 2 * (self.__h + self.__w)

r1 = Rectangle(12.0, 15)
r2 = Rectangle(7.5, 11.2)

r2.h = 11.2

for r in [r1, r2]:
    print('++++++++++++++++++++++')
    print('Höhe   :', r.h)
    print('Breite :', r.w)
    print('Fläche :', r.getArea())
    print('Umfang :', r.getPerimeter())
