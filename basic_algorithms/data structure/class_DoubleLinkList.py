# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 18:05:01 2022

@author: lfh
"""


class Node(object):
    def __init__(self, elem):
        self.elem=elem
        self.next=None
        self.prev=None
#node=Node(100)
        
class DoubleLinkList(object):
    #重复的方法可以使用类的继承
    def __init__(self, node=None):  #与单链表相比没变化
        self._head = node
    
    #检查是否为空
    def is_empty(self):           #没变化
        return self._head==None
    
    #求长度
    def length(self):             #没变化
        #cur游标用来移动遍历节点
        cur=self._head
        count=0
        while cur!=None:
            count+=1
            cur=cur.next
        return count
    
    #遍历列表                     #没变化
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
            node.prev=cur
            
    #表头添加
    def add(self,item):
        node=Node(item)
        node.next=self._head
        self._head=node
        node.next.prev=node
    
    #插入        
    def insert(self, pos,item):
        if pos<=0:
            self.add(item)
        elif pos>(self.length()-1):
            self.append(item)
        else:    
            cur=self._head
            count=0
            while count< pos:
                count+=1
                cur=cur.next
            node=Node(item)
            node.next=cur
            node.prev=cur.prev
            cur.prev.next=node
            cur.prev=node


    #查找                          #没变化
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
        while cur != None:
            if cur.elem==item:
                #头节点
                if cur==self._head:
                    self._head=cur.next
                    if cur.next:
                    #判断链表是否仅有一个节点
                        cur.next.prev=None
                else:
                    cur.prev.next=cur.next
                    if cur.next:
                        cur.next.prev=cur.prev
                break
            else:
                cur=cur.next
                

        
if __name__=="__main__":
    dl=DoubleLinkList()
    print(dl.is_empty())    

    dl.append(1)
    dl.append(2)
    dl.append(3)
    print(dl.length())
    print(dl.is_empty())
    print("遍历：")
    dl.travel()
    print('\n')
    dl.insert(-1,9)
    dl.insert(0,0)
    dl.insert(2,100)
    dl.insert(10,200)
    dl.travel()
    print('\n')
    print('测试remove:')
    dl.remove(100)
    dl.remove(9)
    dl.remove(200)
    dl.travel()
        
    
        
        
        
        
        
    
        
        
    
        