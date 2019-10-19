count = 0
for i in range(1,1000):
    for j in range(1,1000):
        if len(str(i**j)) == j:
            count = count+1
print(count)
