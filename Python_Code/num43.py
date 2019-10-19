
# 18 seconds
import itertools

a="0123456789"
li=[]
def combi():
    count=0
    for i in itertools.permutations(a,10):
        count=count+1
        li.append(''.join(list(i)))
combi()
li2=[]
for i in range(len(li)):
    a=int(li[i][1:4])
    b=int(li[i][2:5])
    c=int(li[i][3:6])
    d=int(li[i][4:7])
    e=int(li[i][5:8])
    f=int(li[i][6:9])
    g=int(li[i][7:10])
    if a%2==0 and b%3==0 and c%5==0 and d%7==0 and e%11==0 and f%13==0 and g%17==0:
        li2.append(int(li[i]))
sums=sum(list(set(li2)))
print(sums)
