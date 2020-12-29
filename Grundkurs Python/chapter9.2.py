#!/usr/bin/env python3
from time import process_time_ns

# palindrome testen
pali = ['Lagerregal', 'Trug Tim eine so helle Hose nie mit Gurt?', 'Anni mag Lehrer, Helga Minna.', 'Ein Seetier iss, oh Ossi, reite es nie.', 'Ne Biene, die bei den Eiben hastet – sah ’ne Biene die beiden Eiben?', 'Das ist kein Palindrom!']

'''
def isPalindrom(pali):
    #paliLst = list(pali.lower())
    paliStr = ''.join(filter(str.isalpha, list(pali.lower()))) # nur Buchstaben
    n = len(paliStr)
    isPalindrom = True 
    i=0
    while i < n/2:
        if paliStr[i] != paliStr[n-1-i]: 
            isPalindrom = False
            break
        i += 1
    return isPalindrom

'''

def isPalindrom(s):
    plain = list(s.lower()) # nur kleine Buchstaben
    plain = ''.join(filter(str.isalpha,plain)) # nur noch Buchstaben
    return plain == plain[::-1] # vergleiche String mit inversem String
#'''

timeStamp = process_time_ns()
for x in pali:
    print('\"{0}\"'.format(x) ,'Ist {0} Palindrom'.format('ein' if isPalindrom(x) else 'kein'))
timeStamp = process_time_ns() - timeStamp
print(timeStamp)
