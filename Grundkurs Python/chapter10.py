#!/usr/bin/env python3

try:
    #file = open('/Users/jens/Projects/learn python/Grundkurs Python/readme.txt')
    file = open('readme.txt')
    for line in file:
        print(line, end='') # CR schon in der Textdatei...
# alle Fehler abfangen (nicht so cool...)
except BaseException as err:
    print(err)
finally:
    if 'file' in locals() and file:
        file.close()

def fkt(x,y):
    if x<0 or y<0:
        raise ValueError('x,y > 0 expected')
    return x*y


try:
    print(fkt(-2,8))
    print(fkt(2,8)) # wird nicht mehr ausgeführt...
except ValueError as err:
    print(err)

try:
    print(fkt(2,8))
except ValueError as err:
    print(err)

# print(fkt(-2,8)) # nicht abgefangen, kompletter traceback ..., stoppt Programm

'''
# Ctrl-C abfangen
try:
    cnt=0
    while 1:
        cnt +=1
except KeyboardInterrupt as err:
    print('Zähler: ',cnt)
'''

#W3: Funktion kürzt Zeichenketten ...
def shrink(s: str, n: int) -> str:
    if not isinstance(s,str) or not s:
        raise TypeError('s erwartet String')
    if not isinstance(n,int):
        raise TypeError('n erwartet Integer')
    if n < 1:
        raise ValueError('n erwartet n > 0')
    if n > len(s):
        return s
    elif n <= 15:
        return s[:n] + ' ...'
    else:
        return s[:n-10] + ' ... ' + s[-5:]


# Testcases
#print(shrink('',8)) # s ist leerstring
#print(shrink(8,'abcdefghij')) # n und s vertauscht  (s kein string)
#print(shrink('abcdefghijklmnop',16.0)) # n nicht int
#print(shrink('abcdefghijklmnop',-2)) # n < 1

print(shrink('abcdefghij',5)) 
print(shrink('abcdefghij',99)) 
print(shrink('abcdefghijklmnop',16))

print('EOF')