import codecs
import re
"""
@author: Bryan Moreno Picaman
"""

def sumar_archivo(nombre):
    f=open(nombre, "r")
    suma=0
    for line in f:
        print(line.strip())
        try:                
            suma+=float(line.strip())
        except:
            print("Bad Value")            
    f.close()
    return suma

def coordenada_media(nombre):
    f=open(nombre, "r")
    sumax=sumay=0
    cont=0
    for line in f:
        try:
            #sumax+=line.split(" ")
            s=line.split()           
            sumax+=float(s[0].split(":")[1])    
            sumay+=float(s[1].split(":")[1])    
            cont+=1
        except:
            print("Bad Value")            
    f.close()
    return sumax/cont,sumay/cont

def contar_palabras(nombre,palabra):
    f=codecs.open(nombre, "r","utf-8")
    suma=0
    for line in f:
        s=line.lower().split()
        suma+=s.count(palabra.lower())

    f.close()
    return suma
    
    
def contar_palabras(nombre):
    f=codecs.open(nombre, "r","utf-8")
    salida={}
    for line in f:
        s=re.split("\w",line)                    
        for i in s:
            #print(i)
            try:
                salida[i]+=1
            except:
                salida[i]=1
    f.close()
    return salida

        
if __name__=="__main__":
    """
    print("*** 1-Sumar un fichero de numeros ***")
    print("Imprimir",sumar_archivo("numeros.txt"))
    
    print("*** 2-Coordenadas de un fichero ***")
    print("Imprimir",coordenada_media("coordenadas.txt"))
    
    print("*** 3-Contar palabras ***")
    print("Imprimir",contar_palabras("pg2000.txt","Sancho"))
    """
            
    print("*** 3-Contar palabras ***")
    print("Imprimir",contar_palabras("pg2000.txt"))
    
    
    
    