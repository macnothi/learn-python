#!/usr/bin/env python3
import locale   # Lokalisierung
from datetime import datetime # Zeiten

# lokale Formatierung
locale.setlocale(locale.LC_ALL,'de_DE.UTF-8')
dt = datetime.now()    # aktuelles Datum + Zeit lesen
print(dt.strftime('%A, %d. %B %Y')) # Ausgabe Wochentag, Tag. Monat Jahr 
# iso Format
dt = datetime.now().isoformat() # aktuelles Dateum+ Zeit in ISO Format 
print(dt) # 2020-12-14T00:14:45.465216

#W1: Geben sie das heutige Datum inklusive Wochentag aber ohne Jahreszahl aus
locale.setlocale(locale.LC_ALL,'de_DE.UTF-8')
dt = datetime.now()    # aktuelles Datum + Zeit lesen
print(dt.strftime('%A, %d. %B')) # Ausgabe Wochentag, Tag. Monat Jahr 

#W2: Ein Kinofilm beginnt um 19:30Uhr und dauert 132 Minuten. Wann ist dieser zu Ende?
from datetime import datetime, timedelta
startTime = datetime(1970, 1, 1, hour=19,minute=30) # nur mit time() lässt sich nicht rechnen
endTime = startTime + timedelta(minutes=132)
print(endTime.time())

#W3: Wieviele Sekunden sind seit Mitternacht vergangen?
from datetime import time, datetime, timedelta
locale.setlocale(locale.LC_ALL,'de_DE.UTF-8')
now = datetime.now()
secondsSinceMidnight = 60 * (now.hour * 60 + now.minute) + now.second 
print(now.time())
print(secondsSinceMidnight)
