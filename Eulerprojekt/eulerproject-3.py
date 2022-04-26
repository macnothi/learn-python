#!/usr/bin/env python3 

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

# wenn als script aufgerufen
if __name__ == '__main__':
    print(primeFactors(600851475143))   # 600851475143 -> [71, 839, 1471, 6857]