s = '700600984582901000400300021065219000000830156041000390004096803000052709179000000'

def getRowColumn(s: str, i: int, n:int) -> str:
    r=i//9 # Zeile (row)
    c=i%9 # Spalte (column)
    o=(c//3)*3 + (r//3)*3*9 # offset für substring
    
    row = s[r*9:r*9+9]  # Zeile fängt immer bei i//9*9 an 0..8
    col = ''
    for n in range(0,9):
        col += s[c+n*9]  # Spalte immer um 9 Zeichen versetzt...
    sub = ''
    for n in range(0,3):
        sub += s[o+n*9:o+n*9+3]
    
    return i, s[i], row, col, sub, c,r,o

def checkField(s: str, i: int, k:int) -> bool:
    r=i//9 # Zeile (row)
    c=i%9 # Spalte (column)
    o=(c//3)*3 + (r//3)*3*9 # offset für substring
    
    row = s[r*9:r*9+9]  # Zeile fängt immer bei i//9*9 an 0..8
    col = ''
    for n in range(0,9):
        col += s[c+n*9]  # Spalte immer um 9 Zeichen versetzt...
    sub = ''
    for n in range(0,3):
        sub += s[o+n*9:o+n*9+3]

    sub = sub + row + col 
    if sub.find(str(k)) == -1:
        return True # Zahl noch nicht in Zeile, Spalte und Submatrix
    else:
        return False # Zahl schon vorhanden 

def printMatrix(s: str):
    for r in range(0,9):
        for c in range(0,9):
            print(s[r*9+c],end='')
        print()

def solveSudoku(s: str) -> bool:
    field = s.find('0') # finde erstes leeres Feld 
    if field == -1:
        return True # alle Felder ausgefüllt
    for num in range(1,10):
        if checkField(s, field, num): # wenn Feld frei
            s[field] = str(num) # Zahl auf Feld schreiben
            if solveSudoku(s):
                return True # gelöst
            s[field] = '0'
    return False 

if solveSudoku(s):
    printMatrix(s)
else:
    print('no solution ...')