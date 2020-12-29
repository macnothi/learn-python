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

# Division mit Rest
def ggT2(a,b):
    if isinstance(a, int) and isinstance(b, int):
        c=a%b
        while c != 0:
            a,b = b,c
            c=a%b
        return b
    else:
        return -1

Teiler = [[-65, 143.2], [2,4], [13,44], [-20,8]]

for x in Teiler:
    print(x, ggT(x[0],x[1]), end=' ')
print()
for x in Teiler:
    print(x, ggT2(x[0],x[1]), end=' ')
print()
