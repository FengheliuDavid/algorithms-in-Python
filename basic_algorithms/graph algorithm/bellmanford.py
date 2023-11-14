# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 22:43:11 2022

@author: lfh
"""

from class_Graph import Graph
from findnewstart_for_array import findnewstart

#未编写提前推出循环的代码，未编写处理负权环
def bellmanford(s,g):
    #change the vertexlist to s as first elem
    origin_list=list(g.vertList.keys())
    key_list=findnewstart(origin_list, origin_list.index(s))
    #initailize
    #unvisited=[i for i in key_list]
    shortest={i: float('inf') for i in key_list}
    previous={i:None for i in key_list}
    shortest[s]=0
    #n represent the time of loop, should be V-1
    n=1
    while n <= len(key_list)-1:
        for i in key_list:   #the visiting vertex is i
        #find the neighbor
            i_neighbor=g.vertList[i].getConnections()   #is a set of class
            neighbor_list=[v.getId() for v in list(i_neighbor)] #is a list of int
            #print(neighbor_list)
            for nbr_vtx in neighbor_list:
                #if new_path is shorter, then update the distance and previous vertex
                new_shortest=shortest[i] + g.distance(i,nbr_vtx)
                if new_shortest < shortest[nbr_vtx]:
                    shortest[nbr_vtx] = new_shortest
                    previous[nbr_vtx] = i
            #print('shortest:',shortest,'\n'+'previous:',previous,'\n')
        n+=1
    return previous
 
       
if __name__== "__main__":
    g=Graph()
    for i in ['S','A','B','C','D','E']:
        g.addVertex(i)
    g.addEdge('S','A',10)
    g.addEdge('S','E',8)
    g.addEdge('A','C',2)
    g.addEdge('E','D',1)
    g.addEdge('D','A',-4)
    g.addEdge('D','C',-1)
    g.addEdge('C','B',-2)
    g.addEdge('B','A',1)
    
  
    print(bellmanford('S',g))