#2.67 seconds
import sys
import itertools
sys.path.insert(0,"../Misc/MathUtils/")
import miller_rabin_prime

def include(filename):
    if os.path.exists(filename): 
        execfile(filename)

list1=[]
list2=[]

def generate_combinations(a):
    count=0
    for i in itertools.permutations(a,len(a)):
        count=count+1
        list1.append(''.join(list(i)))
    return list1

def generate_primes(li5):
    for i in li5:
        if miller_rabin_prime.is_prime(int(i))==1:
            list2.append(int(i))
    return list2

a1="123456789"
a2="12345678"
a3="1234567"
a4="123456"

list1=[]
listA1=generate_combinations(a1)
list1=[]
listA2=generate_combinations(a2)
list1=[]
listA3=generate_combinations(a3)
list1=[]
listA4=generate_combinations(a4)

list2=[]
listB1=generate_primes(listA1)
list2=[]
listB2=generate_primes(listA2)
list2=[]
listB3=generate_primes(listA3)
list2=[]
listB4=generate_primes(listA4)

listF=listB1+listB2+listB3+listB4
print(max(listF))
