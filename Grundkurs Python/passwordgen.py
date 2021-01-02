#!/usr/bin/env python3
# Passwortgenerator nach Beispiel in Kapitel 9
import string
from random import randint
#from random import choices
from random import shuffle

def pwgen(n):
    '''
    def pwgen(n: int) -> str
    Minimum 8 Zeichen
    Passwortgenerator, einfach, Übung zu Funktionen
    '''
    if n<8:
        n=8
    else:
        lower = 'abcdefghijklmnopqrstuvwxyz'
        upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        digit = '1234567890'
        other = '.,;:#§$%?!'
        
        pwlst = [lower[randint(0,len(lower)-1)] for _ in range(n-3)]
        pwlst += [upper[randint(0,len(upper)-1)]]
        pwlst += [digit[randint(0,len(digit)-1)]]
        pwlst += [other[randint(0,len(other)-1)]]
        shuffle(pwlst)
        
        return ''.join(pwlst)

def pwgen2():
    '''
    def pwgen2() -> str
    generiert ein Passwort in der Form 'aaaa-bbbb-cccc-dddd'
    Passwortgenerator, einfach, Übung zu Funktionen
    '''
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digit = '1234567890'
    #other = '.,;:#§$%?!'
        
    pWord = []
    n=3 # Anzahl Abschnitte
    l=5 # Anzahl Zeichen pro Abschnitt

    for i in range(n):
        pwlst = [lower[randint(0,len(lower)-1)] for _ in range(l-2)]
        pwlst += [upper[randint(0,len(upper)-1)]]
        pwlst += [digit[randint(0,len(digit)-1)]]
       # pwlst += [other[randint(0,len(other)-1)]]
        shuffle(pwlst)
        if i < n-1:
            pwlst += '-' # nicht nach letzem Durchlauf
        pWord += pwlst
        
    return ''.join(pWord)
    

for _ in range(5):
    print(pwgen(8))

for _ in range(5):
    print(pwgen2())
