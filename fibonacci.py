#!/usr/bin/env python3 
# Fibonacci series:
# the sum of two elements defines the next

# return list with fibonacci numbers up to n
def fibo(n):
    result = [] # leere Liste erzeugen
    a, b = 0, 1
    #while a < n:
    for _ in range(n):
        result.append(a) # an Liste anhängen result += [a]
        a, b = b, a+b
    return result

# return fibonacci generator
def fibogen(n):
    a, b = 0, 1
    #while a < n: 
    for _ in range(n):
        yield a # Zwischenergebnis 
        a, b = b, a+b

# wenn als script aufgerufen
if __name__ == '__main__':
    print(fibo(10))
    print(fibogen(10)) # Liefert nur Zeiger auf den Generator!
    print(list(fibogen(10))) # Ausgabe als Liste ...
