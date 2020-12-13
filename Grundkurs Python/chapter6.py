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
