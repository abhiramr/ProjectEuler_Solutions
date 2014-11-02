#Problem 15 - Lattice paths
#Can only move right or down

#SOLUTION - 
#essentially a combinatorics problem - Catalan Numbers - wherein the number of ways is C(x+y,x) or C(x+y,y) 
#where x is the number of ways you can move right
#and y is the number of ways you can move down

#This reduces to one module - a factorial. and ZERO if you used the built in math function

#Objective is 20*20. Making it generic. Meh

import math
import sys

x=int(input("Enter the number of paces you can move right:"))
y=int(input("Enter the number of paces you can move down:"))
num=math.factorial(x+y)
deno=math.factorial(x)*math.factorial(y)
print("The total number of ways ="+str(num/deno))


