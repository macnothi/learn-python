# https://projecteuler.net/problem=1
# 23.4.22 JNO
# results sum35(10) == 23, sum35(1000) == 233168 
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

#!/usr/bin/env python3

def sum35(r):
    if r < 1:
        raise ValueError("range > 0 required")

    sum = 0
    for n in range(1,r): # range is 1 .. 999 by definition
        if n % 3 == 0 or n % 5 == 0:  # check if n divides by 3 or 5 without rest
            sum += n    # add up
    return sum


# return result if called as script
if __name__ == '__main__':
    print(sum35(1000))
