# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt
import itertools
def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite

def is_prime(n, _precision_for_huge_n=16):
    if n in _known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653:
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467:
        if n == 3215031751:
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s)
                   for a in _known_primes[:_precision_for_huge_n])

_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]


tc=int(raw_input())
ans=[]
ans2=[]
for i in range(tc):
    n=int(raw_input())
    sqrs=[]
    cubes=[]
    quads=[]
    for i in range(2,int(sqrt(n)+1)):
        if is_prime(i):
            sqrs.append(i**2)
            cubes.append(i**3)
            quads.append(i**4)
    li=[]
    li2=itertools.product(sqrs,cubes,quads)
    for i in li2:
        if sum(list(i))<=n:
            li.append(sum(list(i)))
#    for i in sqrs:
#        for j in cubes:
#            for k in quads:
#                if i+j+k<=n:
#                    li.append(i+j+k)
    ans2.append(len(li))
for i in ans2:
    print i
