# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 11:50:15 2022

@author: Victor Valenzuela
"""

class Punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
class Linea:
    def __init__(self,p1=Punto(0,0),p2=Punto(0,0)):
        self.p1 = p1
        self.p2 = p2
    
    def getp1(self):
        return self.p1
    def getp2(self):
        return self.p2
    
    def setp1(self,p1):
        self.p1 = p1
    def setp2(self,p2):
        self.p2 = p2
    
    def md(self,cant):
        x1=self.getp1().x
        x2=self.getp2().x
        y1=self.getp1().y
        y2=self.getp2().y
        x1=x1+cant
        x2=x2+cant
        self.setp1(Punto(x1,y1))
        self.setp2(Punto(x2,y2))
        
    def mi(self,cant):
        x1=self.getp1().x
        x2=self.getp2().x
        y1=self.getp1().y
        y2=self.getp2().y
        x1=x1-cant
        x2=x2-cant
        self.setp1(Punto(x1,y1))
        self.setp2(Punto(x2,y2))
        
    def mar(self,cant):
         x1=self.getp1().x
         x2=self.getp2().x
         y1=self.getp1().y
         y2=self.getp2().y
         y1=y1+cant
         y2=y2+cant
         self.setp1(Punto(x1,y1))
         self.setp2(Punto(x2,y2))  
    
    def mab(self,cant):
        x1=self.getp1().x
        x2=self.getp2().x
        y1=self.getp1().y
        y2=self.getp2().y
        y1=y1-cant
        y2=y2-cant
        self.setp1(Punto(x1,y1))
        self.setp2(Punto(x2,y2))
        
    def imprimir(self):
        print("[("+str(self.getp1().x)+","+str(self.getp1().y)+"),("+str(self.getp2().x)+","+str(self.getp2().y)+")]")

p1=Punto(0,0)
p2=Punto(1,5)
p3=Punto(4,4)
p4=Punto(0,7)
l1=Linea(p1,p2)
l2=Linea(p3,p4)
l3=Linea()
l1.imprimir()
l1.mar(10)
l1.imprimir()
print()
l2.imprimir()
l2.mi(5)
l2.imprimir()
print()
l3.imprimir()
        
    
    