#!/usr/bin/env python3 

'''
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

'''
largest product of two 3-digit numbers is 999 * 999 = 998001
smallest product of two 3-digit numbers is  100 * 100 = 10000 

'''

# prüfen einer übergebenen Ganzzahl auf Palindrom    
def checkIfPalindrome(n):
    isPalindrome = True
    pali = str(n)  # Wandeln in String
    n = len(pali)
    i = 0
    while i < n/2:
        if pali[i] != pali[n-i-1]:
            isPalindrome = False
            break
        i+=1
    return isPalindrome

# Produkt berechnen und prüfen
def getLargestPalindrome():
    c=0                     # init c
    a=999                   # init outer loop
    while a > 99: # 3-digit number means >=100
        b=999     # (re-)init inner loop
        while b > 99: # 3-digit number means >=100
            c=a*b     # calculate product
            if checkIfPalindrome(c):   
                return c,a,b # return largest palindrome, a and b
            b-=1      # next b
        a-=1     # next a
    return -1,-1,-1         # we did not find a palindrome!

# wenn als script aufgerufen
if __name__ == '__main__':
    print(getLargestPalindrome())   # 3 digits palindrome (valid, if not -1)
