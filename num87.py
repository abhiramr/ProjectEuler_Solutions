#105 seconds
#Problem number 87
from math import sqrt
import sys
import itertools
sys.path.insert(0,"./Misc/MathUtils/")
import miller_rabin_prime
def is_prime(n):
    for i in range(2,int(sqrt(n)+1)):
        if n%i ==0:
            return 0
    return 1
tc=int(raw_input())
ans=[]
for i in range(tc):
    n=int(raw_input())
    sqrs=[]
    cubes=[]
    quads=[]
    for i in range(2,int(sqrt(n)+1)):
        if miller_rabin_prime.is_prime(i):
            sqrs.append(i**2)
            cubes.append(i**3)
            quads.append(i**4)
    li=[]
    for i in sqrs:
        for j in cubes:
            for k in quads:
                if i+j+k<=n:
                    li.append(i+j+k)
    ans.append(len(list(set(li))))
for i in ans:
    print i
