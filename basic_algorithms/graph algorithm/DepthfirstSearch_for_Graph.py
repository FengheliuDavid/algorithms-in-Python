# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 12:15:48 2022

@author: lfh
"""


from class_Stack import Stack
from class_Graph import Graph

def dfs(start,g):
    visited={i:False for i in g.vertList.keys()}
    s=Stack()
    s.push(start)
    while s.size() !=0:
        p=s.pop()
        print(p)
        visited[p]=True
        
        #look for neighbors of p
        neighbors=g.vertList[p].getConnections() #neighbors是类
        for i in list(neighbors)[::-1]:
            if visited[i.getId()] == False:
                s.push(i.getId())
                visited[i.getId()]=True

            
if __name__== "__main__":
    g=Graph()
    for i in range(1,9):
        g.addVertex(i)
    g.addEdge(1,2,1)
    g.addEdge(1,3,1)
    g.addEdge(2,4,1)
    g.addEdge(2,5,1)
    g.addEdge(4,8,1)
    g.addEdge(5,8,1)
    g.addEdge(3,6,1)
    g.addEdge(3,7,1)


    
    dfs(1,g)         