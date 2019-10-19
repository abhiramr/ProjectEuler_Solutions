#PROJECT EULER PROBLEM NUMBER 30
sums=[]

#4 digit numbers
for i in range(1,10):
    for j in range(0,10):
        for k in range(0,10):
            for l in range(0,10):
                t=(i**5)+(j**5)+(k**5)+(l**5) 
                if str(t)==(str(i)+str(j)+str(k)+str(l)):
                    sums.append(t)
#5 digit numbers
for i in range(1,10):
    for j in range(0,10):
        for k in range(0,10):
            for l in range(0,10):
                for m in range(0,10): 
                    t=(i**5)+(j**5)+(k**5)+(l**5)+(m**5)
                    if str(t)==(str(i)+str(j)+str(k)+str(l)+str(m)):
                        sums.append(t)
#6 digit numbers
for i in range(1,10):
    for j in range(0,10):
        for k in range(0,10):
            for l in range(0,10):
                for m in range(0,10):
                    for n in range(0,10):
                        t=(i**5)+(j**5)+(k**5)+(l**5)+(m**5)+(n**5)
                        if str(t)==(str(i)+str(j)+str(k)+str(l)+str(m)+str(n)):
                            sums.append(t)
print sum(sums)
