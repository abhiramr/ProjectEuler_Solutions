#0.041 seconds #problem number 29
li=[]
for i in range(2,101):
    for j in range(2,101):
        li.append(i**j)
print len(set(li))
