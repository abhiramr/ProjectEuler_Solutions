from enum import Enum
from string import maketrans
alphabets=Enum('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
f=open('/Users/aramesh/Desktop/wordsz.txt','r')
li=[]
for l in f.readlines():
    li.append(l.strip().split(","))

li2=li[0]
li3=[]
abhi="\""
abhi4=" "
abhi3=maketrans(abhi,abhi4)
for i in li2:
    li3.append((i.translate(abhi3)).strip())

mama=26*26
momo=1
momos=[]
while momo<=mama:
    momos.append((momo)*(momo+1)/2)
    momo=momo+1

dicc={}
for i in alphabets:
    dicc[i.key]=i.index+1

sums=[]
for la in li3:
    sum1=0
    for lo in la:
        sum1=sum1+dicc[lo]
    sums.append(sum1)

counter=0

for i in sums:
    if i in momos:
        counter=counter+1

print counter
