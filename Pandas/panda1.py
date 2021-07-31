#!/usr/bin/env python3

import pandas as pd             # 
import locale                   # Lokalisierung
from datetime import datetime, timedelta   # Zeiten

# lokale Formatierung
locale.setlocale(locale.LC_ALL,'de_DE.UTF-8')
dt = datetime.now()    # aktuelles Datum + Zeit lesen
print(dt.strftime('%A, %d. %B %Y')) # Ausgabe Wochentag, Tag. Monat Jahr 
# iso Format
dt = datetime.now().isoformat() # aktuelles Datum + Zeit in ISO Format 
print(dt) # 2020-12-14T00:14:45.465216
# 
dt = datetime.now() # aktuelles Datum+Zeit 
print(dt) # 2020-12-14 00:14:45.465216
# Zeitstempel zusammenbauen
sta = datetime(year=2021, month=7, day=31, hour=20,minute=48,second=2,microsecond=1000)
print(sta)
stb = datetime(year=2021, month=7, day=31, hour=20,minute=48,second=27,microsecond=132000)
print(stb)
dif = stb-sta
print(dif)
