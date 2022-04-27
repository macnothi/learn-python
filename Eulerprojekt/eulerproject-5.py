#!/usr/bin/env python3 

'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

# berechnet Primfaktorzerlegung einer natürlichen Zahl
def primeFactors(n):        
    factors = []                # Ergebnisliste
    t = 2                       # starte mit 2 als Teiler
    while n > 1:                # solange n > 1
        if n % t == 0:          # n ohne Rest durch t teilbar?
            factors += [t]      # wenn ja, dann Primfaktor gefunden
            n=n/t               # n durch Primfaktor teilen für "neues" n
        else:
            t += 1              # wenn kein Primfaktor nächsten Teiler prüfen
    return factors

# berechnet Primfaktoren für eine übergebene Liste natürlicher Zahlen
def getFactors(num):
    primeFactorDict = {}
    for i in range(len(num)):
        primeFactorDict[num[i]] = primeFactors(num[i])
    return primeFactorDict

# erzeugt Dictionary mit den Primfaktoren und jeweils höchster Potenz des Auftretens 
# für ein Dictionary mit natürlichen Zahlen und ihren Primfaktoren
def getMaxPrimeFactorPotencies(primeFactorDict):
    primes = {}
    for _,v in primeFactorDict.items():
        m=0
        l=1
        for _,j in enumerate(v):    # für jede Primzahl
            if j==m:                # mehrfache Potenz? (gleiche Zahl wie vorher)
                l+=1                # Anzahl Potenz erhöhen
            else:
                m=j                 # neue Primzahl merken
                l=1                 # erstes Auftreten Potenz=1
            if m in primes:         # Primzahl schon in Dict?
                if l > primes[m]:
                    primes[m] = l # Key update, wenn Wert größer als zuletzt gemerkt
            else:
                primes[m] = l # Key anlegen 
    return primes

# kgV berechnen (Primzahl^Potenz*Primzahl^Potenz)
def getKgV(list):
    kgV=1
    pontencies = getMaxPrimeFactorPotencies(getFactors(list))
    for k,v in pontencies.items():
        kgV=kgV*k**v
    return kgV

# wenn als script aufgerufen
if __name__ == '__main__':
    print(getKgV([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))
