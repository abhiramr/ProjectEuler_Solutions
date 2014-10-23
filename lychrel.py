#PROBLEM NUMBER 55
#NUMBER OF LYCHREL NUMBERS < 10000
import sys

#a=int(input())
count=0
for i in range(1,10000):
	iter=0	
        flag=0
	a=str(i)
	b=(str(i))[::-1]
	while iter < 50:
            summ=int(a)+int(b)
	    if str(summ) == (str(summ))[::-1]:
                flag=1
	    else:
	        a=int(a)+int(b)
                b=(str(a))[::-1]
            iter=iter+1
	if flag == 0:
            count = count +1
print(count)		
