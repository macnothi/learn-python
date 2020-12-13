#!/usr/bin/env python3
import locale, platform #modules to handle localization & platfrom specific tasks

print(platform.system())

# set localization format
if platform.system() == 'Darwin':
    print('Mac, gute Wahl!')
    locale.setlocale(locale.LC_ALL,'de_DE.UTF-8')
elif platform.system() == 'Linux':
    print('Linux, Hacker oder was?')
    locale.setlocale(locale.LC_ALL,'de_DE.utf8')
else:
    print('Windows, ach du Sch...')
    locale.setlocale(locale.LC_ALL,'german')

x = locale.atof('2,7') # string in float from local expression
x *= 2.0 
print(x) # print (expected output 5.4)
print(locale.format_string('%.2f',x)) # expected output 5,40

#W1:  Zeichenkette, die selbst ' oder " enthält
s = 'Das ist eine Zeichenkette, die selbst \' oder \" enthält'
print(s)

#W2: Zeichenketten bilden, die das Zeichen \ enthalten
s = 'Das ist eine Zeichenkette, die \'\\\' enthält'
print(s)

#W3: Das Tag zwischen den eckigen Klammern extrahieren
s = 'bla bla [wichtiger Text] noch mehr bla'
print(s.find('['), s.find(']')) # 8, 23
print(s[s.find('[')],s[s.find(']')] ) # [ ]
print(s[s.find('['):s.find(']')]) # [wichtiger Text

s = s[s.find('[')+1:s.find(']')] 
print(s) # wichtiger Text
