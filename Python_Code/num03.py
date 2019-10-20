#PROBLEM NUMBER 03

import math
from sympy.ntheory import factorint

def isprime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def trial_division(n):
    for i in range(3,n+1,2):
        if n % i == 0:
            print("{}".format(i))

def factorize(n): # trial division, pollard rho, p-1 algorithm
    return factorint(n,verbose=True)

def prime_factors(n):
    start = int(n/2)
    factor = 1
    for i in range(3,int(math.sqrt(n)),2):
        if n%i == 0:
            if isprime(i):
                print(i)


# trial_division(int(input()))
print(factorize(int(input())))
#prime_factors(int(input()))