#Problem number 31
count = 0
for x in range(0,201):
    for y in range(0,101):
        for z in range(0,41):
            for a in range(0,21):
                for b in range(0,11):
                    for c in range(0,5):
                        for d in range(0,3):
                            for e in range(0,1):
                                if (x+(2*y)+(5*z)+(10*a)+(20*b)+(50*c)+(100*d)+(200*e)) == 200:
                                    count = count +1
print count

#73681

#Answer = 73682
