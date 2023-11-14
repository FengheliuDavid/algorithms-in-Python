# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 23:56:25 2022

@author: lfh
"""

def naive_fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return naive_fibo(n-1)+naive_fibo(n-2)

print(naive_fibo(20))

def btmup_fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        i=2
        f1=0
        f2=1
        while i<=n:
            f3=f1+f2
            temp=f2
            f2=f3
            f1=temp
            i+=1
        return f3

print(btmup_fibo(20))


def recur_sqr_fibo(n):
    import numpy as np
    import power
    
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        m=np.matrix([[1,1],[1,0]])
        f=power.powernumber(m,n)
        return f[0,1]



print(recur_sqr_fibo(20))
        
        
    
    
            
    