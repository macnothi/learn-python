#!/usr/bin/env python3

# Übung
def f(a,b, **c):
    print(len(c))
    print(a, b)
    for k in c:
        print(k,"=",c[k], end=' ')
    print()

dict = {'a':1, 'b':2, 'x':3, 'y':4, 'z':5}
f(**dict)


#W1: Funktion, die min und max aus Liste ermittelt
# Lösung ohne Fehlerbehandlung ...
def minmax(lst):
    min, max = lst[0], lst[0] 
    for x in lst:
        if x < min:
            min = x
        elif x > max:
            max = x
    return min, max

zahlen = [1,6,-4,8,0,12,33,-4.98,5,9.87]
erg = minmax(zahlen)
print(erg)
