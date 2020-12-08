#!/usr/bin/env python3
# Hello Name (Python, Der Grundkurs M. Kofler)
import time, locale

# Eingabe, Leerstring führt zu Laufzeitfehler
name = input('Geben Sie bite Ihren Namen ein: ')
print('Hallo ', name, '!')

# Datum und Zeit in lokalem Format ausgeben
locale.setlocale(locale.LC_ALL, '')
print(time.strftime('Heute ist %A, der %d. %B %Y.'))
print(time.strftime('Es ist jetzt %H:%M'), 'Uhr.')
