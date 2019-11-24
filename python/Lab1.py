from math import *

def e1(x,n):
    element = 1.0*((-1)**n*x**n)/factorial(n) 
    return element
def e2(x,n):
    element = 1.0*x**n/factorial(n)
    return element

truevalue = 6.737947*10**(-3)
n = 0
x = 5
result1 = 0
sup2 = 0
result2 = 0

for n in range(20):
    print("-------------------------------------------")
    print("Time",n+1)
    result1 = result1 + e1(x,n)
    trueError = abs(result1 - truevalue)
    relativeError = trueError/truevalue
    print("Formular 1:\n",result1)
    print("true error: ",trueError)
    print("relative error: ",relativeError)

    print("-------------------------------------------")

    
    sup2 = sup2 + e2(x,n)
    result2 = 1/sup2
    trueError = abs(result2 - truevalue)
    relativeError = trueError/truevalue
    print("Formular 2:\n",result2)
    print("true error: ",trueError)
    print("relative error: ",relativeError)
