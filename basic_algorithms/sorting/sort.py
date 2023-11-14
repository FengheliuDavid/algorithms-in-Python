# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 11:53:06 2022

@author: lfh

import random

#选择排序法，这里仅降序排序，时间复杂度O(n^2)，空间复杂度O(1)
def select_sort(a,ascending):
    if ascending==False:        #降序
        for i in range(len(a)-1):
            
            MAX=i                       #内层循环找往后的最大最小值
            for j in range(i,len(a)): 
                if a[j]>a[MAX]:
                    MAX=j
        
            if a[i]<a[MAX]:
                a[i],a[MAX]=a[MAX],a[i]
        return a
        
    
    elif ascending==True:      #升序
        for i in range(len(a)-1):
            
            MIN=i
            for j in range(i,len(a)):
                if a[j]<a[MIN]:
                    MIN=j
            
            if a[i]>a[MIN]:
                a[i],a[MIN]=a[MIN],a[i]
        return a
        
            

#print(select_sort([11,3,2,4,5,8,5,1,6]))


#冒泡排序法，这里仅降序排序，两两比较，反序则交换，时间复杂度为O(n^2),空间复杂度O(1)
def bubble_sort(a,ascending):
    n=list(range((len(a)-1)))
    n.reverse()
    for k in n:
        
        if ascending==False:                         #外层循环
            changelist_d=[]
            for i in range(0,k+1):           #内层循环
                if a[i+1]>a[i]:
                    changelist_d.append(1)
                    a[i],a[i+1]=a[i+1],a[i]
                else:
                    changelist_d.append(0)
            if 1 not in changelist_d:
                break
        
        
        elif ascending==True:
            changelist_a=[]
            for i in range(0,k+1):
                if a[i+1]<a[i]:
                    changelist_a.append(1)
                    a[i],a[i+1]=a[i+1],a[i]
                else:
                    changelist_a.append(0)
            if 1 not in changelist_a:
                break
    
    return a


#插入排序法，创建一个有序数组，将原序列中的值与有序数组比较决定插入位置,时间复杂度为O(n^2),空间复杂度O(1)
def bad_insert_sort(a,ascending):
    a0=a.pop(0)
    s_a=[a0]
    s_d=[a0]
    if ascending==True:
        for i in range(len(a)):
            
            inser_a=0
            for j in range(len(s_a)):
                if a[i]>s_a[j]:
                    inser_a=j+1
            
            s_a.insert(inser_a,a[i])
        return s_a
    
    if ascending==False:
        for i in range(len(a)):
            
            inser_d=0 
            for j in range(len(s_d)):
                if a[i]<s_d[j]:
                    inser_d=j+1
                    
            s_d.insert(inser_d,a[i])
        return s_d


#print(bad_insert_sort([11,3,2,4,5,8,5,1,6],ascending=True))


#插入排序，in place，升序
def insertion_sort1(a):
    for i in range(1,len(a)):    #2，3，5，11，4
        for j in range(i): 
            if a[i]<a[j]:
                a[i],a[j]=a[j],a[i]
    return a

#print(insertion_sort([11,3,2,4,5,8,5,1,6]))              

def insertionSort2(arr): 
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key
    return arr          
        


#是对插入排序的改进版
def shell_sort(a):
    pass
    

    


#归并排序（这里仅适用于n=2k）   
# A[1,2,...,n]
# 1.if n=1,done
# 2.recursively sort lefthalf and righthalf,要在此步调用自身
# 3.merge 2 sorted list，此步要用子程序
# O(nlgn)
def merge_sort(c):
    if len(c)<=1:
        return c
    else:
        n=int(len(c)/2)
        a=merge_sort(c[:n])
        b=merge_sort(c[n:])
        return merge(a,b)
def merge(a,b):
    A=0        
    B=0
    p=[]
    while A<=len(a)-1 and B<=len(b)-1:
        if a[A]<b[B]:
            p.append(a[A])
            A+=1
        elif a[A]>=b[B]:
            p.append(b[B])
            B+=1
    p.extend(a[A:]+b[B:])
    return p

    
#c=[1,3,4,5,7,11,6,7,2,3]
#print(merge_sort(c))

"""
#快速排序法，从小到大，取pivot，小于的放左边，大于的放右边，把左右边分别quicksort
#要保证in place，不额外占用空间,partition函数时间复杂度theta(n)
#随机快排
import random
def partition(a,p,q):
    #在quicksort的基础上：在partition开始前，把a[0]和随机元素交换
    #必须把pivot放在a[0]
    r=random.randint(p,q)
    a[p],a[r]=a[r],a[p]
    X=p
    i=p
    j=i+1
    while j<=q:
        if a[j]<a[X]:
            i+=1
            a[i],a[j]=a[j],a[i] 
        j+=1
    a[X],a[i]=a[i],a[X]
    return i

def quicksort(a,p,q):
    if p<q:
        m=partition(a,p,q)  #[3,4,...6...7,11,7]
        quicksort(a,p,m-1)   #[3,4,...] to [...x...6...7,11,7]  
        quicksort(a,m+1,q)   #[...7,11,7] to [...x...6...y...]
    return a
         
quicksort([0,2,1],0,2)       



c=[6,3,4,5,7,11,7,2,3]  #[3, 3, 4, 5, 2, 6, 7, 7, 11]
print(quicksort(c,0,len(c)-1))

        
    







            
        
