import math
def truncateLtoR(n,li):
    m=str(n)
    while len(m)>1 and n!=0:
        revm=m[::-1]
        rn=(int(revm))/10
        revm2=(str(rn))[::-1]
        li.append(int(revm2))
        n=int(revm2)
        m=revm2
    return li

def truncateRtoL(n,li):
    m=str(n)
    while len(m)>1 and n!=0:
        n=n/10
        li.append(n)
        m=str(n)
    return li


def isPrime(n):
    flag=0
    for i in range(2,int(math.sqrt(int(n)))+1):
        if n%i==0:
            flag=1 #notPrime
    if flag==0:
        return 1
    else:
        return 0 #notPrime
def allPrime(li):
    flag=0
    for i in li:
        status=isPrime(i)
        if status == 0:
            flag=1 #notPrime
    if flag == 1:
        return 0 #all not prime
    else:
        return 1 #all prime

if __name__=="__main__":
    for i in range(9,1000000):
        li=[]
        li.append(i)
        li=truncateLtoR(i,li)
        li=truncateRtoL(i,li)
        status=allPrime(li)
        if status == 1 :
            print i,li
     
