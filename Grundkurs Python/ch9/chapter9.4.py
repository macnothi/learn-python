#!usr/bin/env python3

# Berechnung des Produkts aller übergebenen Faktoren
def prod(*factor):
    erg=factor[0] # 1. Faktor
    for x in factor[1:]: # Schleife über alle weiteren Faktoren
        erg *= x
    return erg

print(prod(1,2,3,-0.5), prod(0))