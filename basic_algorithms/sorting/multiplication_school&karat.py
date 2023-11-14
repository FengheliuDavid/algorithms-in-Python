# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 22:30:56 2022

@author: lfh
"""

#三年级乘法课算法
def school_multi(a,b):
    b=[int(i) for i in str(b)]
    temp=[]
    for i in range(len(b)-1,-1,-1):
        t=b[i]*a*10**(len(b)-1-i)
        temp.append(t)
    print(temp)
    return sum(temp)
'''
a=1234
b=5678
print(school_multi(a,b))
print(a*b)
'''

#karatsuba算法
#A,B必须位数相同，且为2的整数次幂,注意：递归中每一步都要满足这个要求（当心Z不满足，加起来为奇数位）
def karatsuba_multi(A,B):
    A=[i for i in str(A)]
    B=[i for i in str(B)]
    n=len(A)
    if n>1:
        plist=A[:n//2]
        qlist=A[n//2:]
        rlist=B[:n//2]
        slist=B[n//2:]
        p=int(''.join(plist))
        q=int(''.join(qlist))
        r=int(''.join(rlist))
        s=int(''.join(slist))
        
        z=karatsuba_multi(p+q,r+s)
        p_r=karatsuba_multi(p,r)
        q_s=karatsuba_multi(q,s)
        return (10**n)*p_r + q*s + (10**(n/2))*(z- p_r- q_s)
    if n==1:
        return int(A[0])*int(B[0])

a=1234
b=5212
print(karatsuba_multi(a,b))
print(a*b)    

    
    

    
    
      
        