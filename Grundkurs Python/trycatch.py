#!/usr/bin/env python3

try:
    f = open('/Users/jens/Projects/learn python/Grundkurs Python/readme.txt')
    for line in f:
        print(line, end='') # CR schon in der Textdatei...
# alle Fehler abfangen (nicht so cool...)
except BaseException as err:
    print('unerwartet:',err)
finally:
    if 'f' in locals() and f:
        f.close()
