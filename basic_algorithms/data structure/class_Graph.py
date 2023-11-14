# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 17:47:14 2022

@author: 
https://blog.csdn.net/weixin_30646505/article/details/95615234?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1-95615234-blog-124361758.pc_relevant_multi_platform_whitelistv3&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1-95615234-blog-124361758.pc_relevant_multi_platform_whitelistv3&utm_relevant_index=1
"""


class Vertex:
    def __init__(self,key):
        self.id = key            #相当于node class里的self.elem=elem
        self.connectedTo = {}    #相当于self.next=None
 
    def addNeighbor(self,nbr,weight=0):  #把邻居顶点链接到connectedTo,nbr是类
        self.connectedTo[nbr] = weight
 
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo]) 
        #此处的x是类所以能使用x.id
        #为何connectedTo字典里键是类呢，因为connectedTo里的元素只能通过addNeighbor添加
        #addNeighbor的参数是类，因为addEdge是唯一调用addNeighbor的，而其参数为类  
    
    def getConnections(self):
        return self.connectedTo.keys()
 
    def getId(self):  #也可以直接调用属性v.id
        return self.id
 
    def getWeight(self,nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}  #注意：vertlist本身也是字典
        self.numVertices = 0
 
    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex  #键是key，值是Vertex类
        return newVertex     #就像是list.pop()返回弹出元素，此处返回添加进的类
 
    def getVertex(self,key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None
 
    def __contains__(self,key):
        return key in self.vertList
 
    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost) #vertList[f]是一个Vertex
 
    def getVertices(self):
        return self.vertList.keys()
 
    def __iter__(self):
        return iter(self.vertList.values())
    
    def findnei(self, key):
        return list(self.vertList[key].connectedTo.keys())
    
    def distance(self, v1,v2):                     #v2是整数
        for key in self.vertList[v1].connectedTo:  #key是类
            if key.getId()==v2:
                return self.vertList[v1].connectedTo[key]


    
'''   
v=Vertex(3)
print(v.id, v.getId())   #属性
v.addNeighbor(4,1)
v.addNeighbor(5,1)
print(v.connectedTo)  #属性
#print(v)
print(v.getConnections())  #不是属性，所以调用时加括号
print("find the weight of neighbor 4: weight=", v.getWeight(4))
'''

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
    
    
    for k in g.vertList.values(): 
        for n in k.connectedTo.keys():
            print((k.getId(),n.getId()))
    
    print(len(g.vertList))
    print(g.findnei(0))
    
    
    a=[]
    neighbors=g.vertList[0].getConnections() #neighbors是类
    for i in list(neighbors)[::-1]:
        a.append(i.getId())
    print(a)
    
    print(g.distance(0,5))

