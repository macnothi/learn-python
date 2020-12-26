#!/usr/bin/env python3

#W1: Drei Möglichkeiten eine Liste mit Vielfachen von 7, die kleiner 100 sind auszugeben
#1.1: map auf liste
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14] # zahlen 1..14, 1*7=1 .. 14*7=98
print(list(map(lambda x: x*7, lst))) # map funktion auf liste anwenden

#1.2: range objekt und modulo...
lst = list(range(1,101,1)) # Zahlen 1..100 mit Schrittweite 1
print([x for x in lst if x%7==0]) # Elemente der Liste, die ohne Rest durch 7 teilbar sind

#1.3: range objekt und range operator
lst = list(range(0,101,7)) # zahlen 0..100 mit Schrittweite 7
print(lst[1:]) # liste ohne 0 ...

#W2: Extrahieren Sie aus 'Hello, World!' alle Vokale und geben Sie diese als neue Zeichenkette aus
zeichenKette = 'Hello, World!'
vokale = ['a','e','i','o','u','A','E','I','O','U']
vokaleInKette = ''.join(filter(lambda x: x in vokale, list(zeichenKette)))
print('Vokale in \'{0}\':'.format(zeichenKette), vokaleInKette)

#W3: Welchen Datentyp verwenden Sie, um Lottozahlen zu speichern?
''' Grundsätzlich ist der Datentyp 'set' gut geeignet, da dieser keine doppelten Einträge zulässt (6 aus 49)
    Nachteil ist, das sich ein set nicht so einfach sortieren lässt. '''

#W3.1 Lottozahlen mit set
from random import randint

lottoSet = set() # leeres Set
while len(lottoSet) < 6:
    n  = randint(1,49) # Zufallszahl 1..49
    lottoSet.add(n) # add fügt Zahl nur an, wenn noch nicht enthalten... (theoretisch Endlosschleife!)
erg = sorted(list(lottoSet))
print('Lottozahlen:', ) # sortierte Ausgabe

'''
#W3.2 Lottozahlen mit liste
lottoList = [] # leere Liste
while len(lottoList) < 6:
    n  = randint(1,49) # Zufallszahl 1..49
    if not n in lottoList:
        lottoList.append(n) # Zahl nur anfügen, wenn noch nicht drin ...
lottoList.sort() # der Größe nach sortieren
print('Lottozahlen:', lottoList) # sortierte Ausgabe
'''

#W4: Welches sind die gemeinsamen Buchstaben der Zeichenketten "Python" und "Programmierung"?
# sets lassen sich gut mit & operator verknüpfen
zk1 = set('Python')
zk2 = set('Programmierung')
print('gemeinsame Buchstaben:', sorted(''.join(zk1 & zk2)))

#W5: Entfernen Sie Doppelgänger aus einer Liste von Zahlen, z.B. [1,2,3,2,7,3,9], Die Ausgabe soll geordnet sein
zahlListe = [8,1,2,-5,7,7,7,3,2,7,76,3,9,-5]
print("ungeordnet mit Doppelgängern:", zahlListe)
zahlSet = set(zahlListe)
erg = sorted(list(zahlSet))
print("geordnet ohne Doppelgänger  :", erg)

#W6: erstellen Sie ein kleines DE-EN Wörterbuch für Zahlen
numDict = {'eins':'one', 'zwei':'two', 'drei':'three', 'vier':'four', 'fünf':'five'}
#print(numDict['zwei'])
for x in numDict:
    print(x, numDict[x])

#W7: Ermitteln sie die maximale Wortlänge in der folgenden Zeichenkette
lorem = 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.'
'''
# Lösung aus Buch
# Zeichenkette aus Wörtern und Leerzeichen bilden (Zahlen, Satzzeichen etc. entfernen)
plain = ''.join(filter(lambda x: str.isalpha(x) or x == ' ',list(lorem)))
words = plain.split(' ')
sortedWords = sorted(words,key=len,reverse=True)
print('Maximale Wortlänge :',len(sortedWords[0]))
'''

# Jens' Variante mit for in ...
n=0
longestWord=0
for x in list(lorem):
    n=n+1
    if x == ' ' or x == ',' or x == '.' :
        if n>longestWord:
            longestWord=n-1 # eins zurück...
        n=0 
print('Die maximale Wortlänge ist {0} Zeichen:'.format(longestWord))
