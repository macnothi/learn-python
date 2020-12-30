#!/usr/bin/env python3
# Hello Name (Python, Der Grundkurs M. Kofler)
import time, locale

# Eingabe
name = input('Geben Sie bite Ihren Namen ein: ')
# print('Hallo ', name, '!')
print('Hallo, {0}!'.format(name)) # bessere Lösung finde ich

# Datum und Zeit in lokalem Format ausgeben
locale.setlocale(locale.LC_ALL,'de_DE.UTF-8') 
print(time.strftime('Heute ist %A, der %d. %B %Y.'))
print(time.strftime('Es ist jetzt %H:%M'), 'Uhr.')

n = 22.7
msg = 'Die Temperatur beträgt ' + str(n) + ' Grad Celsius'
msg = 'Die Temperatur beträgt {0:.2f}°C'.format(n)

print(msg)