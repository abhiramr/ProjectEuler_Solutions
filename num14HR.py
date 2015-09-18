#PROBLEM NUMBER 14
#LONGEST COLLATZ SEQUENCE
import sys

def collatz(n):
	if n%2==0:
		return n/2
	else:
		return 3*n+1
bigcnt=0
bigi=0
tc=int(raw_input())
arr=[]
for i in range(tc):
	cnt=0
        num=int(raw_input())
	n=collatz(num)
	#print("i="+str(i)+" n="+str(n))
	while n!=1:
		n=collatz(n)
		#print("n for i="+str(i)+"="+str(n))
		if n == 1:
			if bigcnt<cnt:
				bigcnt=cnt+3
				bigi=i
			#print("i="+str(i)+" count="+str(cnt+3))
		cnt=cnt+1
        print(bigcnt,bigi)
