# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 11:58:00 2022

@author: Victor Valenzuela
"""
import random

class Jugador():
    def __init__(self,nombre,vida,estado):
        self.__nombre = nombre
        self.__vida = vida
        self.__estado = estado
    
    def getnombre(self):
        return self.__nombre
    def getvida(self):
        return self.__vida
    def getestado(self):
        return self.__estado
    def setnombre(self,nombre):
        self.__nombre = nombre
    def setvida(self,vida):
        self.__vida = vida
    def setestado(self,estado):
        self.__estado = estado
    
    
    
    def info(self):
      if self.getestado() == True:
          texto="vivo"
      else:
          texto="muerto"
      print(self.getnombre(),"tiene",self.getvida(),"de vida, está",texto)
      
      return self.getestado()
  
    def dmg(self,x):
      if self.getestado() == True:
          self.setvida(self.getvida()-x)
          if self.getvida() <=0:
              self.setvida(0)
              self.setestado(False)
          self.info()
      else:
          print("el jugador ya está muerto...")  
  
    def shoot(self,jugador):
        print(self.getnombre(),"está disparando a", jugador.getnombre())
        jugador.dmg(random.randint(50,100))
    
    
    
    def heal(self,x):
        if self.getestado() == True:
            self.setvida(self.getvida() + x)
            if self.getvida() >100:
                self.setvida(100)
        else:
            print("el jugador está muerto... no puede helear")
    
    
a=Jugador("goku",100,True)  
b=Jugador("vegeta",100,True)

a.shoot(b)   
b.shoot(a)
a.heal(50)
b.heal(50)  
a.info()
b.info()
        
    
        