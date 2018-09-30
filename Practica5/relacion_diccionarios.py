import random
import math
import copy
"""
@author: Bryan Moreno Picaman
"""
datos={'A':'U','C':'G','T':'A','G':'C'}
def transcripcion_mRNA(cadena):
    aux=str.upper(cadena)
    salida=[]
    for i in range (0,len(cadena)):
        try:
            salida.append(datos[aux[i]])
        except:
            print("La cadena contiene caracteres no validos",aux[i])
    return salida    
    
def contar_letras(cadena):
    salida={}
    for i in range (0,len(cadena)):
        try:
            salida[cadena[i]]+=1
        except:
            salida[cadena[i]]=1
    return salida  

def contar_letras2(cadena):
    salida={}
    for i in range (0,len(cadena)):
        salida[cadena[i]]=cadena.count(cadena[i])
    return salida  

def invertir_diccionario(cadena):
    salida={}
    for key, value in cadena.iteritems():
        if(salida.has_key(value)):
            if(type(salida[value]) is not list):
                salida[value]=[salida[value],key]
            else:
                aux=salida[value]
                aux.append(key)
        else:
            salida[value]=key
    return salida  
    
def revertir_diccionario(cadena):
    salida={}
    for key, value in cadena.iteritems():
        if(type(cadena[key]) is list):
            for i in cadena[key]:
                salida[i]=key
        else:
                salida[value]=key
    return salida    
    
def imprimir_archivo(nombre):
    f=open(nombre, "r") 
    contenido = f.read()
    print contenido
    f.close()
        
if __name__=="__main__":

    print("*** 1-transcripcion_mRNA***")
    cadena=raw_input('Inserta codigo: ')
    print("Transcripcion_mRNA",transcripcion_mRNA(cadena))

    print("*** 2-Contar letras***")
    cadena=raw_input('Inserta codigo: ')
    print("Contar letras",contar_letras(cadena))

    print("*** 3-Contar letras Version2***")
    cadena=raw_input('Inserta codigo: ')
    print("Contar letras",contar_letras2(cadena))

    print("*** 4-Invertir Diccionario***")
    cadena={'A':'U','C':'G','T':'A','G':'C','T':'C','Q':'C'}
    print("invertir_diccionario",invertir_diccionario(cadena))   

    print("*** 5-Revertir Diccionario***")
    cadena={'A':'U','C':'G','T':'A','G':'C','T':'C','Q':'C'}
    print("invertir_diccionario",revertir_diccionario(invertir_diccionario(cadena)))

    print("*** 6-Imprimir archivo***")
    print("Imprimir",imprimir_archivo("archivo.txt"))
    
    
    
    
    
    