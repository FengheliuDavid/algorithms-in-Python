# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 22:48:17 2022

@author: lfh
"""

from class_queue import Queue
from class_Graph import Graph

def bfs(s,g):  #s是节点的key，g是图
    q=Queue()   #先进先出
    visited={i:False for i in g.vertList.keys()} #装已访问过的元素
    q.enqueue(s)
    while q.size() !=0:  #有元素
        #出队
        a=q.dequeue()
        visited[a]=True
        print(a)
        
        #邻居入队
        visited_vertex=g.vertList[a]  #a是整数，visited_vertex是类
        for i in visited_vertex.getConnections(): #i是类
            if visited[i.getId()] == False:  #如果没有被访问才能入队
                q.enqueue(i.getId())
                visited[i.getId()]=True   #入队了的话下次就不能入队，
                                          #因为入队一定会出队，所以会重


if __name__== "__main__":
    g=Graph()
    for i in range(6):
        g.addVertex(i)
    g.addEdge(0,1,5)
    g.addEdge(0,5,2)
    g.addEdge(1,2,4)
    g.addEdge(2,3,9)
    g.addEdge(3,4,7)
    g.addEdge(3,5,3)
    g.addEdge(4,0,1)
    g.addEdge(5,4,8)
    g.addEdge(5,2,1)

    
    bfs(0,g)   
    
     


        
    
    
