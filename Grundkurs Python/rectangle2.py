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

    # Overload ==
    def __eq__(self, other):
        return (self.h, self.w) == (other.h, other.w)

    # Overload <
    def __lt__(self, other):
        return self.getArea() < other.getArea()

    # Overload <=
    def __le__(self, other):
        return self.getArea() <= other.getArea()

    # Print Ausgabe
    def __str__(self):
        return 'Rechteck (h=%.2f, w=%.2f)' % (self.h, self.w)

    # Debug Ausgabe
    def __repr__(self):
        return 'Rectangle h=%f, w=%f' % (self.h, self.w)

    # hash Wert
    def __hash__(self):
        return hash((self.h, self.w)) # Tupel der Instanzvariablen

r1 = Rectangle(12, 13.546)
r2 = Rectangle(7.5, 11.2)
r3 = Rectangle(10,15)

r2.h = 11.3

for r in [r1, r2, r3]:
    print('++++++++++++++++++++++')
    print(r)
    print('Höhe   :', r.h)
    print('Breite :', r.w)
    print('Fläche : {0:.2f}'.format(r.getArea()))
    print('Umfang : {0:.2f}'.format(r.getPerimeter()))

# Ausgabe sortiert ...
print(sorted([r1, r2, r3])) # nutzt < operator
print(sorted([r1, r2, r3], key=lambda x: x.w)) # nach w sortiert
print(sorted([r1, r2, r3], key=lambda x: x.h)) # nach h sortiert
