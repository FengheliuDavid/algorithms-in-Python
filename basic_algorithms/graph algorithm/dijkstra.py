# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 21:40:51 2022

@author: lfh
"""

from class_Graph import Graph

def dijkstra(s,g):
    unvisited=[i for i in g.vertList.keys()]
    shortest={i: float('inf') for i in g.vertList.keys()}
    previous={i:None for i in g.vertList.keys()}
    shortest[s]=0
    while len(unvisited) !=0:
        #find the unvisited vertex that has the shortest path from start
        #for min func, the first parameter is an iterable,dict iters keys, 
        #the second parameter dispose the iterable and then compare
        a=min(shortest, key=lambda x: shortest[x])
        #print('visiting:',a)
        
        #find the neighbor of vertex a that is unvisited
        a_neighbor=g.vertList[a].getConnections()   #is a set of class
        neighbor_list=[i.getId() for i in list(a_neighbor) if i.getId() in unvisited] 
        #neighbor_list is a list of int
        #print('neighbor_list:',neighbor_list)
        for i in neighbor_list:  #i is an int
            #if new_path is shorter, then update the distance and previous vertex
            new_shortest=shortest[a] + g.distance(a,i)
            if new_shortest < shortest[i]:
                shortest[i] = new_shortest
                previous[i] = a
        #print('shortest:',shortest,'\n'+'previous:',previous,'\n')
        
        #a is visited
        unvisited.remove(a)
        del shortest[a]
        
    return previous

            
if __name__== "__main__":
    g=Graph()
    for i in ['A','B','C','D','E']:
        g.addVertex(i)
    g.addEdge('A','B',6)
    g.addEdge('A','D',1)
    g.addEdge('D','B',2)
    g.addEdge('D','E',1)
    g.addEdge('B','E',2)
    g.addEdge('E','C',5)
    g.addEdge('B','C',5)
  
    
    
    print(dijkstra('A',g))
    
    
        
                
            

        
        
        
    
    