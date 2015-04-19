fh=open("/Users/aramesh/Desktop/names.txt")
red=fh.read()
redl=red.split(",")
redl.sort()
redl2=[]
sum2=0
for i in redl:
    k=i.replace('"','')
    redl2.append(k)
for i in range(len(redl2)):
    sum=0
    for j in redl2[i]:
        sum=sum+(ord(j)-64)
    sum2=sum2+((i+1)*sum)
print sum2
