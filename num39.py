#1 min 43 seconds
#Problem number 39
import itertools

li=range(1,1001)
cnt=0
for i in itertools.combinations(li,3):
    cnt=cnt+1
li2=[0]*cnt
li3=[0]*1001
for i in itertools.combinations(li,3):
    t=sum(i)
    if (((i[0]**2)+(i[1]**2))==(i[2]**2)):
        li2[t]=li2[t]+1

for i in range(0,1001):
    li3[i]=li2[i]

m1=max(li3)
mi=li3.index(m1)
print mi
