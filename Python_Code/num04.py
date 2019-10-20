#PROBLEM NUMBER 04

def met1():
    li = []
    for i in range(100,1000):
        for j in range(100,1000):
            prod = str(i*j)
            prodr = prod[::-1]
            if prod == prodr:
                li.append((int(prod),i,j))
    return max(li)

def met2():
    pass

print(met1())
#print(met2())

