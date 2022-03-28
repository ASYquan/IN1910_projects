from numpy import pi, sqrt

def add(x,y):
    ans = x+y
    return ans

def divide(x,y):
    ans = x/y
    return ans

def factorial(n):
    factorial = 1
    if n >= 0:
        for i in range(1,n+1):
            factorial *= i 
    elif n < 0:
        raise ValueError
    elif n == float:
        raise TypeError

    return factorial

def sin(x, N=20):
    s = 0
    for n in range(N): 
        val = (2*n+1)
        a = factorial(val)
        s += (((-1)**n) * x**(2*n+1)) / a
    return s

