#11th problem in Project Euler
import numpy
p=numpy.recfromtxt("./numbers.txt")
a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
g=[]
h=[]
#HORIZONTAL
for i in range(20):
    for j in range(17):
        a.append(p[i][j]*p[i][j+1]*p[i][j+2]*p[i][j+3])
        b.append(p[i][j])

#VERTICAL
for i in range(17):
    for j in range(20):
        c.append(p[i][j]*p[i+1][j]*p[i+2][j]*p[i+3][j])
        d.append(p[i][j])

#DIAGONAL
for i in range(17):
    for j in range(17):
        e.append(p[i][j]*p[i+1][j+1]*p[i+2][j+2]*p[i+3][j+3])
        f.append(p[i][j])

#REVERSE DIAGONAL
for i in range(17):
    for j in range(19,2,-1):
        g.append(p[i][j]*p[i+1][j-1]*p[i+2][j-2]*p[i+3][j-3])
        h.append(p[i][j])

maxes=[]
maxes.append(max(a))
maxes.append(max(c))
maxes.append(max(e))
maxes.append(max(g))
print max(maxes)
