import random
import math
import copy
"""
Created on Tue Oct 11 09:45:43 2016
@author: Bryan Moreno Picaman
"""
def factores_primos(num):
    copia=copy.copy(num)
    salida=[]
    raiz=int(math.sqrt(num))+1
    i=2
    while(copia>=1 and i<raiz):
        if copia%i==0:
            salida.append(i)
            copia=copia/i
        else:
            i=i+1
    if copia>1:
        salida.append(copia)
    salida.append(1)
    return salida
    
    
def factores_primos2(num):
    copia=copy.copy(num)
    salida={}
    raiz=int(math.sqrt(num))+1
    i=2
    while(copia>=1 and i<raiz):
        if copia%i==0:
            if salida.get(i)== None: 
                salida[i]=1
            else:
                salida[i]=salida.get(i)+1
            copia=copia/i
        else:
            i=i+1
    if copia>1:
        salida[copia]=1
    salida[1]=1
    return salida    

def suma_acumulada(lista):
    salida=[0]*len(lista)
    for i in range(0,len(lista)):
        if not i==0:
            for j in range(0,i):
                salida[i]=salida[j]+lista[i]
        else:
            salida[i]=lista[i]

    return salida
    
    
    
def eliminar(l1,l2):
    salida=[]
    for i in range(0,len(l1)):
        if(l2.count(l1[i])==0):
            salida.append(l1[i])
    for i in range(0,len(l2)):
        if(l1.count(l2[i])==0):
            salida.append(l2[i])
    return salida

def contar_letras(cadena):
    salida={}
    for i in range (0,len(cadena)):
        salida[cadena[i]]=cadena.count(cadena[i])
    sorted(salida.keys())
    return salida    
    
    
    
if __name__=="__main__":
    """
    print("*** 1-Factores primos de un numero***")
    num=int(raw_input('Inserta codigo: '))
    print("Primos",factores_primos(num))
    
    print("*** 2-Factores primos de un numero***")
    num=int(raw_input('Inserta codigo: '))
    print("Primos",factores_primos2(num))

    print("*** 3-Suma acumulada***")
    lista=[1,3,6]
    print("Suma acumulada",suma_acumulada(lista))

    print("*** 4-Eliminar***")
    lista1=[1,5,3,8,4]    
    lista2=[5,8]
    print("Eliminar",eliminar(lista1,lista2))
    """ 
    print("*** 5-Contar letras***")
    cadena=raw_input('Inserta codigo: ')
    print("Contar letras",contar_letras(cadena))









    