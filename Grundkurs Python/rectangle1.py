#!/usr/bin/env/ python3

class Rectangle():
    # Konstruktor mit Höhe, Breite
    def __init__(self, heigth, width):
        self.h = heigth
        self.w = width

    # Flächeninhalt
    def getArea(self):
        return self.h * self.w

    # Umfang
    def getPerimeter(self):
        return 2 * (self.h + self.w)

r1 = Rectangle(12.0, 15)
r2 = Rectangle(7.5, 11.2)

for r in [r1, r2]:
    print('++++++++++++++++++++++')
    print('Höhe   :', r.h)
    print('Breite :', r.w)
    print('Fläche :', r.getArea())
    print('Umfang :', r.getPerimeter())
