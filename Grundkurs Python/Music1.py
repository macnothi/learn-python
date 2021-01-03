#!/usr/bin/env python3
from dataclasses import dataclass
from datetime import timedelta

### Track speichert Daten eines Tracks
@dataclass()
class Track():
    title: str
    length: timedelta
    mp3: str = None   # optionaler Parameter
    bought: str = None # zweiter optionaler Parameter

    # Print Ausgabe
    def __str__(self):
        msg = f'Titel: {self.title}\nLänge: {self.length:}'
        if self.mp3:
            msg += f'\nDatei: {self.mp3}'
        if self.bought:
            msg += f'\ngekauft: {self.bought}'
        return msg
   

### Album speichert Daten eines Albums
@dataclass()
class Album():
    # Instanzvariablen 
    title: str
    artist: str
    tracks: list[Track]

    # Track hinzufügen
    def addTrack(self, *tracks : list[Track]):
        for track in tracks:
            self.tracks += track
    
    # Zeit aller Tracks berechnen
    def getTotalTime(self) -> timedelta:
        totalTime = timedelta()
        for track in self.tracks:
            totalTime += track.length
        return totalTime

    # Ausgabe der Daten in strukturierter Form
    def printInfo(self):
        print('Album: ',self.title)
        print('von  : ',self.artist)
        print('Länge: ',self.getTotalTime())
        print()
        i=0
        for track in self.tracks:
            i+=1
            print(f'Track {i}: {track.title} [{track.length}]')

# Tracklist anlegen
tr1 = Track('Speak to Me',timedelta(minutes=3,seconds=57), 'speaktome.mp3', 'iTunes')
tr2 = Track('On the Run',timedelta(minutes=3,seconds=34), bought='amazon.com')
tr3 = Track('Time',timedelta(minutes=7,seconds=5))

# Album anlegen 
al1 = Album('The Dark Side of the Moon','Pink Floyd',[tr1, tr2, tr3])

# Trackliste, andere Form
tr = [
      Track('The Great Gig in the Sky',timedelta(minutes=4,seconds=47)),
      Track('Money',timedelta(minutes=6,seconds=23))
      ]

# Tracks hinzufügen
al1.addTrack(tr)

# Info ansehen
al1.printInfo()
