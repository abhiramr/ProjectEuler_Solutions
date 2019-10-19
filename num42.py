from enum import Enum
from string import maketrans

alpha_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alphabets = [ord(char) - 65 for char in alpha_list]

f=open('./Data/wordsz.txt','r')
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
for i in alpha_list:
    dicc[i]=alphabets[i]+1

print(dicc)
sums=[]
for la in li3:
    sum1=0
    for lo in la:
        print lo, dicc[lo]
        sum1=sum1+dicc[lo]
    sums.append(sum1)

counter=0

for i in sums:
    if i in momos:
        counter=counter+1

print counter
