# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 22:51:57 2022

@author: lfh
"""

#为列表找一个新起点
#findnewstart([1,2,3,4],1) -> [2,3,4,1]
def findnewstart(l,k):
    new=[]
    for i in l[k:]+l[:k]:
        new.append(i)
    return new



    