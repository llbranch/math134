# Made by Liam Branch
# 11/27/2022

import math
import numpy as np

n=118901509
q=3*11*29*89*349
k=2


primelist = [2,3,5,7,11]
fixedlist = (x for x in primelist if np.gcd(x,n)==1)
for a in fixedlist:
    print("Checking a =",a)
    for i in range(0,k):
        check = pow(a,pow(2,i)*q,mod=n)
        print(a, "^(", pow(2,i)* q, ") mod", n, "=", check)
        if(check==(n-1)):
            print(a,"is not a witness")
            break
        elif(i==k):
            print(a, "is a witness to the compositeness of", n)