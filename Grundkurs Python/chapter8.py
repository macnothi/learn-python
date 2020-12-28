#!/usr/bin/env python3

#W1: erweitern des Schaltjahr scripts um die Anzahl der Tage des Monats
jahr = 2020
monat = 2

monate = ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember']

# Schaltjahr ermitteln
if jahr % 400 == 0:
    schaltjahr = True
elif jahr % 100 == 0:
    schaltjahr = False
elif jahr % 4 == 0:
    schaltjahr = True
else:
    schaltjahr = False

# Anzahl Tage im Monat ermitteln
if monat in (1,3,5,7,8,10,12):
    tage = 31
elif monat in (4,6,9,11):
    tage = 30
elif monat == 2:
    tage = 29 if schaltjahr else 28
else:
    tage = 0 # ungültiger Monat

# Ergebnis ausgeben
if tage > 0 and jahr > 0:
    print('Der {0} im Jahr {1} hat {2} Tage.'.format(monate[monat-1], jahr, tage))
else:
    print('ungültiger Monat: 1 - Januar, 12 - Februar oder ungültiges Jahr z.B. 2017')

#W2: Berechnen Sie die Fakultät der Zahlen 1 bis 20 (nicht rekursiv...)
fakul=1
for x in range(1,21):
    fakul=fakul * x
print(fakul)

#W3: Berechnen Sie die Summe der Funktion 1/(x*x) der Zahlen 2 bis 30
summe=0
for x in range(2,31):
    summe += 1/(x*x)
print(summe)

#W4: was wird hier ausgegeben?
'''
for i in range(1,3):
    for j in range(i):
        print(i+j)

# Ausgabe:
1  # i=1, j=0 (j range(0,1))
2  # i=2, j=0 (j range(0,2))
3  # i=2, j=1 (j range(0,2))
'''

#W5: was wird hier ausgegeben?
'''
i=0
j=9
while i < j:
    print(i, j)
    if i >= 3:
        break
    i+=1
    j-=1

# Ausgabe:
0 9    # i=0, j=9
1 8    # i=1, j=8
2 7    # i=2, j=7
3 6    # i=3, j=6 --> führt zu Abbruch in Zeile 66...
'''

#W6: while Schleife, die in 5er Schritten von 100 bis 0 zählt
n=100
while n >= 0:
    print(n, end=' ')
    n -= 5
print()

#W7: Schleife, die den Wertebereich 125 .. 160 in 11 Schritten durchläuft, Ausgabe aller 11 Zahlen 125.0 .. 160.0
max=160
min=125
n=11
dif = (max - min) / (n-1)
summe = min
while summe <= max:
    print('{0:.1f}'.format(summe), end=' ')
    summe += dif
print()

#W8: Liste mit 50 Zufallszahlen 0..10 generieren, Summe berechnen, Anzahl Auftreten '0' und erste Position '0' ausgeben
from random import randint

lst = []
for _ in range(50):
    lst.append(randint(0,10))

countZero = 0
posZero = 0
summe = 0
for x in lst:
    summe +=x
    if x == 0:
        countZero += 1
    if countZero < 1:
        posZero += 1

print('Liste der Zufallszahlen ',lst)
print('Summe : {0:.4f}'.format(summe))
if countZero:
    print('Anzahl auftreten von \'0\' :', countZero)
    print('Erstes Auftreten von \'0\' :', posZero)
else:
    print('keine \'0\'...')

# in Python style (und auch am effektivsten...)
lst = [randint(0,10) for _ in list(range(50))]
print('Liste der Zufallszahlen :',lst)
print('Summe : {0}'.format(sum(lst)))
n=lst.count(0)
if n:
    print('Anzahl auftreten von \'0\' :', n)
    print('Erstes Auftreten von \'0\' :', lst.index(0))
else:
    print('keine \'0\'...')
