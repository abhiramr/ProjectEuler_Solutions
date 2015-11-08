# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(raw_input())
arr=[]
arr2=[]
for i in range(n):
    arr.append(raw_input())
m=int(raw_input())
for i in range(m):
    arr2.append(raw_input())
sums=[]
arr.sort()
for i in range(len(arr)):
    sum1=0
    for j in arr[i]:
        sum1=sum1+(ord(j)-64)
    sums.append(sum1*(i+1))
for p in range(m):
    print sums[arr.index(arr2[p])]
