# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 22:41:57 2022

@author: lfh
"""

def powernumber(x,n):
    if n==0:
        return 1
    elif n==1:
        return x
    elif n%2==0:
        p=powernumber(x,n/2)
        return p*p
    elif n%2!=0:
        p=powernumber(x,(n-1)/2)
        return p*p*x
    

