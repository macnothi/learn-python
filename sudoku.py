#!/usr/env/bin python3

# Sudoku in string format, '0' für leeres Feld
s = '700600984582901000400300021065219000000830156041000390004096803000052709179000000'

# string in Matrix "füllen"
def strToMatrix(s: str) -> list:
    # matrix anlegen
    m = [[0 for x in range(9)] for y in range(9)]
    for r in range(9):
        for c in range(9):
            m[r][c] = int(s[r*9+c])
    return m

# Matrix in String ausgeben
def matrixToString(m: list) -> str:
    s=''
    for r in range(9):
        for c in range(9):
            s += str(m[r][c])
    return s

# Matrix ausgeben 9x9
def printMatrix(m: list):
    for r in range(9):
        for c in range(9):
            print(m[r][c], end='')
        print()
    print()

# erstes leeres Feld finden
def findEmptyField(m: list) -> (int, int):
    for r in range(9):
        for c in range(9):
            if m[r][c] == 0: # erstes Feld mit 0?
                return r,c
    return -1,-1

# prüfen, ob Zahl in Zeile, Spalte und Submatrix vorhanden
def checkField(m: list, pos: (int,int), num: int) -> bool:
    r,c = pos
    row = m[r]
    #print(row)
    if row.count(num) != 0:
        return False # num in Zeile
    col = [m[x][c] for x in range(9)]
    #print(col)
    if col.count(num) != 0:
        return False # num in Spalte
    sub = [m[r-r%3+i][c-c%3+k] for i in range(3) for k in range(3)] 
    #print(sub)
    if sub.count(num) != 0:
        return False # num in submatrix 3x3
    return True # frei

# rekursives backtracking
def solveSudoku(m: list) -> bool:
    pos = findEmptyField(m) # erstes leeres Feld mit '0' suchen
    if pos == (-1,-1):
        return True # fertig, keine 0 mehr im Sudoku
    for num in range(1,10):
        if checkField(m,pos,num):
            m[pos[0]][pos[1]] = num # mögliche Lösung einsetzen
            if solveSudoku(m): # und testen
                return True # gelöst...
            m[pos[0]][pos[1]] = 0 # Änderungen rückgängig
    return False # noch keine gültige Lösung
 
m = strToMatrix(s)
print('Sudoku:')
printMatrix(m)

if solveSudoku(m):
    print('Solution:')
    printMatrix(m)
else:
    print('no solution ...')