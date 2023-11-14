# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 23:26:32 2022

@author: lfh
"""
#编写二分搜索法启示：
#1.第一步为模拟一次程序，无论在脑海里还是画图
#比如：
#  I............I...I..I.I。I........I
#
#2.第二部为思考可行的控制结构，算法
#3.写出伪代码
#4.写代码

def binary_search(arr,low, high, find):
    mid=(low+high)//2
    if arr[mid]==find:
        return mid
    elif arr[mid]>find:
        high=mid-1
        return binary_search(arr,low,high,find)
    elif arr[mid]<find:
        low=mid+1
        return binary_search(arr,low,high,find)
    
arr=[1,2,3,5,7,8,9,11,13]
print(binary_search(arr,0,len(arr)-1,7))





#从升序列表A中找k元素的索引（共有n个元素）
def recur_dichosearch(A,n,k):
    m=n//2
    if A[m]==k:
        return m
    elif  A[m]>k:
        left=A[:m]
        return recur_dichosearch(left,len(left),k)
    elif A[m]<k:
        right=A[m:]
        #m=4,right=[7,8,9,11,13],4+[]=4+2+[9,11,13]=4+2+1+[11,13]=4+2+1=7
        return m+recur_dichosearch(right,len(right),k)
    
#print(recur_dichosearch([1,2,3,5,7,8,9,11,13],9,11))
