#Creating lists
one2ten = {0: '',
 1: 'one',
 2: 'two',
 3: 'three',
 4: 'four',
 5: 'five',
 6: 'six',
 7: 'seven',
 8: 'eight',
 9: 'nine'}

tens = {0: '',
 2: 'twenty',
 3: 'thirty',
 4: 'forty',
 5: 'fifty',
 6: 'sixty',
 7: 'seventy',
 8: 'eighty',
 9: 'ninety'}

ele2twenty={10: 'ten',
 11: 'eleven',
 12: 'twelve',
 13: 'thirteen',
 14: 'fourteen',
 15: 'fifteen',
 16: 'sixteen',
 17: 'seventeen',
 18: 'eighteen',
 19: 'nineteen'}

longrange=list(range(111,120))+list(range(211,220))+list(range(311,320))+list(range(411,420))+list(range(511,520))+list(range(611,620))+list(range(711,720))+list(range(811,820))+list(range(911,920))
longrange=longrange+[110,210,310,410,510,610,710,810,910]


sums1=0
sums2=0
sums3=0
sums4=0
sums5=0
sums6=0
sums7=0

#SUMMATION OF 1-9
for i in one2ten.iterkeys():
    sums1=sums1+len(one2ten.get(i))

#SUMMATION OF 20-99
for i in range(20,100):
    key1=str(i)[0:1]
    key2=str(i)[1:]
    key1i=int(key1)
    key2i=int(key2)
    if key1i in tens.iterkeys() and key2i in one2ten.iterkeys():
#        print len(tens.get(key1i)),len(one2ten.get(key2i)),i
        lenstens=len(tens.get(key1i))
        lensones=len(one2ten.get(key2i))
        sums2=sums2+lensones+lenstens
    else:
#        print 0
        sums2=sums2
#print sums

#SUMMATION OF 11-20
for i in ele2twenty:
    sums3=sums3+len(ele2twenty.get(i))

#SUMMATION OF 100-999 WITHOUT 'HUNDRED AND' & SKIPPING 110..119,210..219 etc
for i in range(100,1000):
    key2=str(i)[1:2]
    key1=str(i)[2:]
    key3=str(i)[0:1]
    key1i=int(key1)
    key2i=int(key2)
    key0i=int(key3)
    if key0i in one2ten.iterkeys() and key1i in one2ten.iterkeys() and key2i in tens.iterkeys():
#        print len(one2ten.get(key0i)),len(tens.get(key2i)),len(one2ten.get(key1i)),i
        lenshundy=len(one2ten.get(key0i))
        lenstens=len(tens.get(key2i))
        lensones=len(one2ten.get(key1i))
        sums4=sums4+lensones+lenstens+lenshundy
    else:
#        print 0
        sums4=sums4
#print sums

#CALCULATION OF "HUNDRED AND"
hund_and=(7+3)*(999-100+1)

#SKIPPING "AND" for 100,200,300 etc
hund_and_final=hund_and-(9*3)

sums5=hund_and_final

#SUMMATION OF 110-119,210-219...910-919
for i in longrange:
    key1=str(i)[0:1]
    key2=str(i)[1:]
    key1i=int(key1)
    key2i=int(key2)
    if key1i in one2ten.iterkeys() and key2i in ele2twenty.iterkeys():
#        print len(one2ten.get(key1i)),len(ele2twenty.get(key2i)),i
        sums6=sums6+len(one2ten.get(key1i))+len(ele2twenty.get(key2i))

sums7=len("onethousand")

print sums1+sums2+sums3+sums4+sums5+sums6+sums7
