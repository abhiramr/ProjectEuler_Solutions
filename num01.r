benchmark(
  "lm" ={sum_ <- 0 
  for(i in 1:999)
  {
    if(i%%3==0||i%%5==0)
    {
      sum_ <- sum_+i
    }
  }
  },replications = 1000,
  columns = c("test", "replications", "elapsed","relative", "user.self", "sys.self"))
print(sum_)
