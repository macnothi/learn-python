#!/usr/bin/env python3

############ Basisklasse, Figur ##############
class Figure():
    
    def __init__(self, pos):
        if len(pos) != 2:
            raise ValueError('invalid position')
        c = pos[0].lower()
        r = pos[1]
        if (not c in 'abcdefgh') or (not r in '12345678'):
            raise ValueError('invalid position') 
        self.__col = 'abcdefgh'.find(c)
        self.__row = '12345678'.find(r)

    # get, set methoden 
    @property
    def col(self):
        return self.__col

    @property
    def row(self):
        return self.__row

    def __str__(self):
        return Figure.position(self.col, self.row)

    @staticmethod
    # prüfen, ob gültige Position und Rückgabe in Schach Notation
    def position(col, row):
        if col<0 or col>7 or row<0 or row>7:
            return ''
        else:
            return 'abcdefgh'[col] + '12345678'[row]

############ Springer / Knight ##############
class Knight(Figure):

    def __init__(self, pos):
        super().__init__(pos)

    def __str__(self):
        return 'Knight@' + Figure.position(self.col, self.row)

    def moves(self):
        # offset (col, row) alle mögliche Züge inkremental
        offsets = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,2),(1,-2),(2,-1),(2,1)]
        positions = []
        for coff, roff in offsets:
            # mögliche Positionen suf Spielfeld bestimmen
            pos = Figure.position(self.col + coff, self.row + roff)
            if pos:
                positions += [pos]
        return positions

############ Läufer / Bishop ##############
class Bishop(Figure):

    def __init__(self, pos):
        super().__init__(pos)

    def __str__(self):
        return 'Bishop@' + Figure.position(self.col, self.row)

    def moves(self):
        positions = []
        for off in range(-7,8):
                if off == 0:
                    continue
                # mögliche Positionen suf Spielfeld bestimmen
                # links unten nach rechts oben
                pos = Figure.position(self.col + off, self.row + off)
                if pos:
                    positions += [pos]
                # links oben, nach rechts unten
                pos= Figure.position(self.col + off, self.row - off)
                if pos:
                    positions += [pos]
        return positions

############ Turm / Rook ##############
class Rook(Figure):

    def __init__(self, pos):
        super().__init__(pos)

    def __str__(self):
        return 'Rook@' + Figure.position(self.col, self.row)

    def moves(self):
        positions = []
        for off in range(-7,8):
                if off == 0:
                    continue
                # mögliche Positionen suf Spielfeld bestimmen
                # links nach rechts 
                pos = Figure.position(self.col + off, self.row)
                if pos:
                    positions += [pos]
                # oben nach unten
                pos= Figure.position(self.col, self.row + off)
                if pos:
                    positions += [pos]
        return positions

############ Dame / Queen ##############
class Queen(Figure):

    def __init__(self, pos):
        super().__init__(pos)

    def __str__(self):
        return 'Queen@' + Figure.position(self.col, self.row)

    def moves(self):
        positions = []
        for off in range(-7,8):
                if off == 0:
                    continue
                # mögliche Positionen suf Spielfeld bestimmen
                # links nach rechts 
                pos = Figure.position(self.col + off, self.row)
                if pos:
                    positions += [pos]
                # oben nach unten
                pos= Figure.position(self.col, self.row + off)
                if pos:
                    positions += [pos]
                # mögliche Positionen suf Spielfeld bestimmen
                # links unten nach rechts oben
                pos = Figure.position(self.col + off, self.row + off)
                if pos:
                    positions += [pos]
                # links oben, nach rechts unten
                pos= Figure.position(self.col + off, self.row - off)
                if pos:
                    positions += [pos]
        return positions

fig = Queen('f3')

print(fig, sorted(fig.moves()))

