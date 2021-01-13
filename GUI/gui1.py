#!/usr/bin/env python3

import tkinter

# Klasse für Fenster
class Window(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.master = master
        self.pack(fill=tkinter.BOTH, expand=1)
        
        exitButton = tkinter.Button(self, text='Exit', command=self.clickExitButton, fg='blue')
        exitButton.place(x=0,y=0)

    def clickExitButton(self):
        exit()
      

# Tk starten
root = tkinter.Tk()
# Fenster anlegen
app = Window(root)
# titel setzen
root.wm_title('Sudoku Solver')
root.geometry('640x480')
# loop starten
root.mainloop()
