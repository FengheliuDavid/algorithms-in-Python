# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 22:27:37 2022

@author: lfh
"""


class Node(object):
    def __init__(self, elem):
        self.elem=elem
        self.next=None
#node=Node(100)
        
class SingleCycleList(object):
    def __init__(self, node=None):
        self._head = node
        if node:
            node.next=node
    
    #检查是否为空                       #与单向列表一样
    def is_empty(self):
        return self._head==None
    
    #求长度
    def length(self):
        #cur游标用来移动遍历节点
        if self.is_empty():
            return 0
        cur=self._head
        count=1
        while cur.next!=self._head:
            count+=1
            cur=cur.next
        return count
    
    #遍历列表    
    def travel(self):
        if self.is_empty():
            return 
        else:
            cur=self._head
            while cur.next!=self._head:
                print(cur.elem, end=' ')
                cur=cur.next
            print(cur.elem)
    
    #表尾添加
    def append(self,item):
        node=Node(item)
        if self.is_empty():
            self._head=node
            node.next=node
        else:
            cur=self._head
            while cur.next !=self._head:
                cur=cur.next
            node.next=self._head
            cur.next=node
            
    #表头添加
    def add(self,item):
        node=Node(item)
        if self.is_empty():
            self._head=node
            node.next=node
        else:
            cur=self._head
            while cur.next!=self._head:
                cur=cur.next
            node.next=self._head
            self._head=node
            cur.next=self._head
    
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
        if self.is_empty():
            return False
        cur=self._head
        while cur.next!=self._head:
            if cur.elem==item:
                return True
            else:
                cur=cur.next
        #退出循环，cur指尾节点
        if cur.elem==item:
            return True
        return False
    
    #删除
    def remove(self,item):
        #为空
        if self.is_empty():
            return
        cur=self._head
        pre=None
        while cur != None:
            if cur.elem==item:
                #头节点
                if cur==self._head:
                    #要找尾节点
                    rear=self._head
                    while rear.next!=self._head:
                        rear=rear.next
                    self._head=cur.next
                    rear.next=self._head
                #中间
                else:
                    pre.next=cur.next
                return
            #没找到则两个游标移动
            else:
                pre=cur
                cur=cur.next
        #跳出循环，cur为尾节点
        if cur.elem==item:
            if cur==self._head:
                #链表只有一个节点
                self._head=None
            else:
                pre.next=cur.next
        
        

        
if __name__=="__main__":
    cl=SingleCycleList()
    print(cl.is_empty())    

    cl.append(1)
    cl.append(2)
    cl.append(3)
    print('len:',cl.length())
    print(cl.is_empty())
    print("遍历：")
    cl.travel()
    print('\n')
    cl.insert(-1,9)
    cl.insert(2,100)
    cl.insert(10,200)
    print('len:',cl.length())
    cl.travel()
    print('测试remove:')
    cl.remove(100)
    cl.remove(9)
    cl.remove(200)
    print('len:',cl.length())
    cl.travel()
        
    
        