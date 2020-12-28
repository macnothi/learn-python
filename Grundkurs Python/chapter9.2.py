#!/usr/bin/env python3
import time

# palindrome testen
pali = ['Lagerregal', 'Trug Tim eine so helle Hose nie mit Gurt?', 'Anni mag Lehrer, Helga Minna.', 'Ein Seetier iss, oh Ossi, reite es nie.', 'Ne Biene, die bei den Eiben hastet – sah ’ne Biene die beiden Eiben?', 'Das ist kein Palindrom!']

'''
def isPalindrom(pali):
    paliStr = ''.join(filter(str.isalpha, list(pali)) # nur Buchstaben
    #paliLst = list(paliStr.lower())
    n=len(paliLst)
    isPalindrom = True
    i=0
    while i < n/2:
        if paliLst[i] != paliLst[n-1-i]: 
            isPalindrom = False
            break
        i += 1
    return isPalindrom

'''
def isPalindrom(s):
    plain = list(s.lower()) # nur kleine Buchstaben
    plain = ''.join(filter(str.isalpha,plain)) # nur noch Buchstaben
    return plain == plain[::-1]


timeStamp = time.process_time_ns()
for x in pali:
    print('\"{0}\"'.format(x) ,'Ist {0} Palindrom'.format('ein' if isPalindrom(x) else 'kein'))
timeStamp = time.process_time_ns() - timeStamp
print(timeStamp)
