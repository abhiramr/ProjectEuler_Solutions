#PROBLEM NUMBER 01
#Solution copied and edited
sum_by_me <- 0 
for(i in 1:999)
{
  if(i%%3==0||i%%5==0)
  {
    sum_by_me <- sum_by_me+i
  }
}

print(sum_by_me)
