#!/usr/bin/env python3

# qualität von passwörtern

def passQuali(s):
    points = 0
    lst=list(s)
    if len(s) > 7:
        points +=1
        if len(set(s)) > 6:
            points +=1
        if ''.join(filter(str.islower, lst)) and ''.join(filter(str.isupper, lst)):
            points+=1
        if ''.join(filter(str.isdigit, lst)):
            points+=1
        if ''.join(filter(lambda x: not str.isalnum(x), lst)):
            points+=1
    return points


passLst = ['abc', 'abcdefghij', 'ab1122$$', 'abcd1234$', 'Abcd1234$']
for x in passLst:
    print(x, passQuali(x))