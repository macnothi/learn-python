# Fibonacci series:
# the sum of two elements defines the next

"""
a, b = 0, 1
while a < 1000:
    print(a, end=',')
    c = a
    a = b
    b = c+b
"""

# return list with fibonacci numbers up to n
def fibo(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

f10 = fibo(1000)
print(f10)
