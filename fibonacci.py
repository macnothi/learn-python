# Fibonacci series:
# the sum of two elements defines the next

# return list with fibonacci numbers up to n
def fibo(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

# first class functions
f10 = fibo(1000)
print(f10)
