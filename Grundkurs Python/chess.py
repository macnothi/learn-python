#!/usr/bin/env python3

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
            return 'ABCDEFGH'[col] + '12345678'[row]

############ Springer ##############
class Knight(Figure):

    def __init__(self, pos):
        super().__init__(pos)

    def __str__(self):
        return 'Knight@' + Figure.position(self.col, self.row)


fig = Knight('C4')

print(fig)

