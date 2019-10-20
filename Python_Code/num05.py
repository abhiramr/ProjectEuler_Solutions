from sympy import divisors, divisor_count

# Works for goal = 10
# Will hang for goal = 20

goal = int(input())
li = list(range(1,goal))
j = 2
while True:
    div = divisors(j)
    if set(li).issubset(set(div)):
        print(j)
        break
    j = j+1         

    