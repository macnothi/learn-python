#!/usr/bin/env python3
def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)

# wenn als script aufgerufen
if __name__ == '__main__':
    print(fact(20))