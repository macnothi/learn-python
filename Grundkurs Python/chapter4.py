#!/usr/bin/env python3
'''
W1: Wie führen Sie eine ganzzahlige Division durch?
A1: Dazu nutze ich den Ganzzahl Division Operator '//'; Beispiel:  erg = 6 // 2 # erg = 3
'''
erg = 6 // 2
print(erg, type(erg))
'''
W2: Geben Sie den Oktalcode 750 binär aus.
A2: print(bin(0o750) # 0o750 ist die Entsprechung für Oktalcode 750, bin(<number>) wandelt den übergebenen Wert in binäre Entsprechung um 
'''
print(bin(0o750))
'''
W3: Wie erzeugen Sie Zufallszahlen zwischen 1 und 49
A3: Ganzzahlige ZUfallszahlen lassen sich mit randint() aus dem Modul random erzeugen
'''
import random
zufall = random.randint(1,49)
print(zufall)
'''
W4: Sie brauchen 2 Zufallszahlen zwischen 0,0 und 10,0. Schreiben Sie geeigneten Python Code.
A4: pseudo zufällige Fließkommazahlen können mit random() oder uniform() aus dem Modul random erzeugt werden.
'''
from random import random, uniform
zufallA = random()*10 # Zufallszahl zwischen 0..1 erzeugen und mit Wertebereich multiplizieren
zufallB = random()*10
print(zufallA, zufallB)

zufallA = uniform(0.0, 10.0) # Zufallszahl zwischen 0.0 und 10.0 erzeugen
zufallB = uniform(0.0, 10.0)
print(zufallA, zufallB)

'''
W5: Mit welchem Datentyp lassen sich Geldbeträge rundungsfrei verarbeiten?
A5: Dazu nutze ich den Datentyp Decimal. Dafür muss decimal importiert werden.
'''
from decimal import Decimal
vielGeld = Decimal('2000.45')
mehrGeld = Decimal('30000.00')
allesGeld = vielGeld + mehrGeld
print(allesGeld)
'''
W6: Welchem Zahlenwert ist True zugeordnet?
A6: True ist allen Zahlenwerten ungleich 0 zugeordnet. 
'''
n, m = 2.3, 0
if n:
    print('True')
if m:
    print('auch True')
