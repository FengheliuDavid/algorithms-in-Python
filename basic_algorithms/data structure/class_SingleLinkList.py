# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 11:07:10 2022

@author: lfh
"""

class Node(object):
    def __init__(self, elem):
        self.elem=elem
        self.next=None
#node=Node(100)
        
class SingleLinkList(object):
    def __init__(self, node=None):
        self._head = node
    
    #检查是否为空
    def is_empty(self):
        return self._head==None
    
    #求长度
    def length(self):
        #cur游标用来移动遍历节点
        cur=self._head
        count=0
        while cur!=None:
            count+=1
            cur=cur.next
        return count
    
    #遍历列表    
    def travel(self):
        cur=self._head
        while cur!=None:
            print(cur.elem,end=' ')
            cur=cur.next
    
    #表尾添加
    def append(self,item):
        node=Node(item)
        if self.is_empty():
            self._head=node
        else:
            cur=self._head
            while cur.next !=None:
                cur=cur.next
            cur.next=node
            
    #表头添加
    def add(self,item):
        node=Node(item)
        node.next=self._head
        self._head=node
    
    #插入        
    def insert(self, pos,item):
        if pos<=0:
            self.add(item)
        elif pos>(self.length()-1):
            self.append(item)
        else:    
            pre=self._head
            count=0
            while count< (pos-1):
                count+=1
                pre=pre.next
            node=Node(item)
            node.next=pre.next
            pre.next=node
    
    #查找
    def search(self, item):
        cur=self._head
        while cur!=None:
            if cur.elem==item:
                return True
            else:
                cur=cur.next
        return False
    
    #删除
    def remove(self,item):
        cur=self._head
        pre=None
        while cur != None:
            if cur.elem==item:
                #头节点
                if cur==self._head:
                    self._head=cur.next
                else:
                    pre.next=cur.next
                break
            else:
                pre=cur
                cur=cur.next
        
            
     
        
        
if __name__=="__main__":
    ll=SingleLinkList()
    print(ll.is_empty())    

    ll.append(1)
    ll.append(2)
    ll.append(3)
    print(ll.length())
    print(ll.is_empty())
    print("遍历：")
    ll.travel()
    print('\n')
    ll.insert(-1,9)
    ll.insert(2,100)
    ll.insert(10,200)
    ll.travel()
    ll.add(-100)
    print('测试remove')
    ll.remove(100)
    ll.remove(9)
    ll.remove(200)
    ll.travel()
        
    
        
        
        
        
        
    
        
        
    