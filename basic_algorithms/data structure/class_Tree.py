# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 10:07:44 2022

@author: lfh
"""

class Node(object):
    def __init__(self,item):
        self.elem=item
        self.lchild=None
        self.rchild=None
        
class Tree(object):
    def __init__(self):
        self.root=None
        
    def add(self,item):
        node=Node(item)
        if self.root is None:
            self.root=node
            return
        queue=[self.root]
        while queue: #即不为空
            cur_node=queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild=node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild=node
                return
            else:
                queue.append(cur_node.rchild)
                    
    def breadth_travel(self):
        if self.root is None:
            return
        queue=[self.root]
        while queue:
            cur_node=queue.pop(0)
            print(cur_node.elem, end=' ')
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild) 
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)  
    
    #先序遍历，根左右
    def preorder(self,rootnode):
        if rootnode is None:
            return 
        print(rootnode.elem,end=' ')
        self.preorder(rootnode.lchild)
        self.preorder(rootnode.rchild)
        
    #中序遍历，左根右
    def inorder(self,rootnode):
        if rootnode is None:
            return 
        self.inorder(rootnode.lchild)
        print(rootnode.elem,end=' ')
        self.inorder(rootnode.rchild)
        
    #后序遍历，左右根
    def postorder(self,rootnode):
        if rootnode is None:
            return 
        self.postorder(rootnode.lchild)
        self.postorder(rootnode.rchild)
        print(rootnode.elem,end=' ')
        
        

if __name__=="__main__":
    tree=Tree()
    for i in range(10):
        tree.add(i)
    tree.breadth_travel()
    print('\n')
    tree.preorder(tree.root)
    print('\n')
    tree.inorder(tree.root)
    print('\n')
    tree.postorder(tree.root)
                    
            
                
            
        
        
        
        
    