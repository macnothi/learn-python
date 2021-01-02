#!usr/bin/env python3

#Funktion, die eine Zeichenkette auf Vorkommen einer anderen Zeichenkette untersucht und  die Startpositionen als Liste zurückgibt
def findAll(s: str, f: str) -> list:
    erg = []
    i = s.find(f)
    while i != -1:
        erg += [i]
        i = s.find(f,i+1) 
    return erg

text = 'abcdefabcghiabcjklabc'
subtext = 'abc'

print(findAll(text, subtext))