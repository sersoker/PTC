import punto
import copy

class Contorno:
    lista=[]
    
    def __init__(self,puntos):
        if isinstance(puntos,punto.Punto):
            self.lista.append(puntos)
        else:
            self.lista=copy.copy(puntos)
        
    def __repr__(self):
        return str(self.lista)   
        
    def __str__(self):
        return str(self.lista)        
    
    def __len__(self):
        return (len(self.lista))

    def addPoint(self,punt):
        self.lista.append(punt)
    
    def insertPoint(self,position,punt):
        self.lista.insert(position,punt)
    
    def getPoint(self,index):
        return self.lista[index]

    def deletePoint(self,index):
        self.lista.remove(self.lista[index])

