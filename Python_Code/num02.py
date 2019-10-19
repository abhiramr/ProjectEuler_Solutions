#PROBLEM NUMBER 02

q0,q1 = (1,2)

even_sum_ = q1

i = 0

while True:
    q_int = q0+q1
    if q1%2 !=0:
        even_sum_ = even_sum_+q1
    q0 = q1
    q1 = q_int
    if q_int > 4000000:
        break
    i = i+1

print(even_sum_)