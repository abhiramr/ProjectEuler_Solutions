#PROBLEM NUMBER 02

q0 <- 0
q1 <- 1
fibo <- c()
while (q0 < 4000000){
     q0 <- q0 + q1
     q1 <- q0 + q1
     fibo = c(fibo, q0, q1)
 }

sum(fibo[fibo %% 2 == 0 & fibo < 4000000])