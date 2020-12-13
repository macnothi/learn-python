#!/usr/bin/env python3
result = 225 / 17   # float division 13.235 ..
whole = 225 // 17   # ganzzahliger Teil = 13
remainder = 225 % 17 # Rest der Division = 4

print(result, whole, remainder)

'''
W1: Sie wollen den Rest der Division 225 / 17 ermitteln. Wie gehen sie vor?
A1: Zum Ermitteln des Rest benutze ich die Modulodivision 225 % 17. Der Rest ist 4.

W2: Was ist die Short-Circuit-Evaluation? Nennen Sie ein Beispiel.
A2: Als SCE wird der Abbruch von Auswertungen mit and bzw, or bezeichnet, wenn das Ergebnis feststeht.
    Ein solcher Ausdruck wird dann also nicht komplett ausgewertet.
    Beispiel:

    C=12
    if C>10 or C<5:   
        # das Ergebnis (True) steht nach Auswertung von C>10 fest, C<5 wird nicht mehr ausgewertet
        print(C)

W3: Welchen Wert haben a und b?  a = 1 + 2 * 3 ** 4 ; b = 100 < a < 200
A3: Berechnung a nach Operatorreihenfolge ** vor * vor +  
    3 ** 4 = 81
    2 * 81 = 162
    1 + 162 = 163

    a = 163 ; b = True , weil gilt 100 < 163 < 200
'''


    