#!/usr/bin/python
import ClasificadorNum as c
from tkinter import *
from tkinter.ttk import * 
from tkinter.messagebox import *


def ejemploModoGrafico():
    Clasificador=c.Clasificador(True)

def ejemploModoTexto():
    imageList=[]
    imageList.append("num1.gif")
    imageList.append("num2.gif")
    imageList.append("num3.gif")
    Clasificador=c.Clasificador(False)
    Clasificador.processImageList(imageList)
    
    
if __name__ == "__main__":
    
    #Modo Grafico
    #ejemploModoGrafico()
    #Modo Texto
    ejemploModoTexto()