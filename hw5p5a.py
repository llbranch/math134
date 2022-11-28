# Made by Liam Branch
# 11/27/2022
import numpy as np
from math import gcd

n = 11247661
e = 268729
m = e*7169 - 1
print(m)
looking = True
mprime = m #set mprime up
primelist = [2,3,5,7,11,13,17,19]
while(looking):
    mprime = mprime//2 #m -> m' and m' -> m''
    count = 0 # reset congruency counter
    i = 0 # reset primelist counter
    while(i < 7): # check condition
        tocheck = pow(primelist[i],mprime, mod=n)
        if(tocheck == 1): 
            print(primelist[i],"^",mprime, "is congruent to 1!")
            count+=1
        else: 
            print(primelist[i],"^",mprime, "is not congruent to 1 but", tocheck)
        i+=1
        print("gcd is", gcd(tocheck-1,n))
    if(count > 3): 
        looking = False