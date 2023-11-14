# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 12:20:16 2022

@author: lfh
"""

class Queue(object):
    
    def __init__(self):
        self.__list=[]
    
    def __str__(self):
        return str(self.__list)
    
    def enqueue(self,item):
        self.__list.append(item)
        
    def dequeue(self):
        return self.__list.pop(0)
        
    def is_empty(self):
        return self.__list==[]
        #return not self.__list
        
    def size(self):
        return len(self.__list)
    
if __name__== "__main__":
    s=Queue()
    s.enqueue(1)
    s.enqueue(2)
    print(s.dequeue())
    print(s.dequeue())