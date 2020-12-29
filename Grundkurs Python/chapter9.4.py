#!/usr/bin/env python3
#ggT nach Euklid

#klassisch, ohne Fehlerbehandlung
def ggT(a:int ,b:int) -> int:
    if isinstance(a, int) and isinstance(b, int):
        a = abs(a)
        b = abs(b)
        while a != b:
            if a<b:
                a,b=b,a
            c=a-b
            a=c
        return c
    else:
        return -1

# Division mit Rest, rekursiver Aufruf
def ggT2(a,b):
    if isinstance(a, int) and isinstance(b, int):
        c=a%b
        if c == 0:
            return b
        else:
            return ggT2(b,c)
    else:
        return -1

Teiler = [[-65, 143], [4,2], [13,44], [-20,8]]

for x in Teiler:
    print(x, ggT(x[0],x[1]), end=' ')
print()
for x in Teiler:
    print(x, ggT2(x[0],x[1]), end=' ')
print()
