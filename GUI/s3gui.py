from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Sudoku Solver")

mainframe = ttk.Frame(root, padding="3 3 3 3")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

m = [[0 for x in range(9)] for y in range(9)]
for x in range(9):
    for y in range(9):
        m[x][y] = IntVar(value=0)

e = [[0 for x in range(9)] for y in range(9)]
for x in range(9):
    for y in range(9):
        e[x][y] = ttk.Entry(mainframe, width=1, textvariable=m[x][y], foreground='blue')
        e[x][y].grid(column=y, row=x, sticky=(W, E))
        e[x][y].grid_configure(padx=2, pady=2)

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
            if solveSudoku(m): # und rekursiv testen
                return True # gelöst...
            m[pos[0]][pos[1]] = 0 # Änderung rückgängig
    return False # noch keine gültige Lösung

# int matrix aus StringVar feld erzeugen
def createMatrix(m: list) -> list:
    matrix = [[0 for x in range(9)] for y in range(9)]
    for r in range(9):
        for c in range(9):
            matrix[r][c] = m[r][c].get()
    return matrix
    
# Matrix ausgeben 9x9
def printMatrix(m: list):
    for r in range(9):
        for c in range(9):
            print(m[r][c], end='')
        print()
    print()

printMatrix(createMatrix(m))

e[0][0].focus()
root.bind("<Return>", solveSudoku(createMatrix(m)))
root.mainloop()

printMatrix(createMatrix(m))
