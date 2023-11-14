# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 22:19:24 2022

@author: lfh
"""

class Line:
    def __init__(self,A,B,C):
        self.A=A
        self.B=B
        self.C=C
    def distance(self):
        dist=abs(self.C)/((self.A**2+self.B**2)**0.5)
        return dist

line1=Line(2,3,5)
print(line1.distance())


