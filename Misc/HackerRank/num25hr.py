def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
count=0
n=1
t=0
si=int(raw_input())
fibs=[[0]*si]*2
while count <si:
    i=fib(n)
    fibs[0][t]=i
    fibs[1][t]=len(str(i))
    count=fibs[1][t]
    print fibs[0][t],fibs[1][t],count
    n=n+1
    t=t+1
iin=fibs[1].index(si)
#print fibs[0][iin]
