#!/usr/bin/env python3
'''
class MyClass():
    def __init__(self, a, b):
        self.a = a
        self.b = b

obj = MyClass(3,4)
# print(MyClass.a) # Fehler, es gibt keine Attribut (Methode, Variable) "a" der Klasse MyClass 
print(obj.a) # Ausgabe 3

# der folgende Code ist zulässig, da zur Laufzeit Attribute hinzugefügt werden können
obj.c = 7
print(obj.c) # Ausgabe 7
'''

class Konto():
    # Konstruktor, defualt leeres Konto
    def __init__(self, name, balance = 0, credit = 0):
        if not isinstance(name, str) or len(name) < 2:
            raise ValueError('Name als String >= 3 erwartet')
        self.name = name
        self.balance = balance
        self.credit = credit

    def einzahlen(self, money):
        if not isinstance(money, (float, int)) or money<0:
            raise ValueError('Einzahlung > 0 erwartet')
        self.balance += money
    
    def auszahlen(self, money):
        if not isinstance(money, (float, int)) or money<0:
            raise ValueError('Auszahlung > 0 erwartet')        
        if (self.balance + self.credit) > money:
            self.balance -= money
            return True
        else:
            print('Nicht genug Geld auf dem Konto')
            return False
    
    # Print Ausgabe
    def __str__(self):
        return 'Konto von {0}:\n  Guthaben:{1:.2f}\n  Kredit:{2:.2f}'.format(self.name, self.balance, self.credit)

k1=Konto('Michael',200,0)
k2=Konto('Maria')
k3=Konto('Peter',1000,500)

k1.einzahlen(100)
if k2.auszahlen(100):
    print('Geld von Konto 2 abgehoben')
if k3.auszahlen(1200):
    print('Geld von Konto 3 abgehoben')
for k in [k1,k2,k3]:
    print(k)
