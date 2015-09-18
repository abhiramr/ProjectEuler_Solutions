# 2 minutes 3 seconds
import math
def getCircular(n):
    p=n
    l=[]
    m=str(n)
    for i in range(len(m)):
        t1=n%10
        t2=n/10
        t3=int(str(t1)+str(t2))
        l.append(t3)
        n=t3
    return l
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
    count=0
    for i in range(3,1000000,2):
        li=getCircular(int(i))
        net=allPrime(li)
        if net == 1:
      #  print "YES"
            count=count+1
            print li
        else:
            count=count
       # print "NO"
    print count
