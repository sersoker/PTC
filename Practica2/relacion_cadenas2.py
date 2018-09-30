"""
Created on Tue Oct 11 09:45:43 2016
@author: Bryan Moreno Picaman
"""

def comunes(palabra,palabra2):
    cont="";
    for c in palabra:
        if c in palabra2 and c not in cont:
            cont=cont+c
    for c in palabra2:
        if c not in palabra and c not in cont:
            cont=cont+c        
    return cont

def no_comunes(palabra,palabra2):
    cont="";
    for c in palabra:
        if c not in palabra2 and c not in cont:
            cont=cont+c
    for c in palabra2:
        if c not in palabra and c not in cont:
            cont=cont+c
    return cont
    
def eco_palabras(palabra):
    cont="";
    for c in palabra:
        cont+=palabra
    return cont
    
def palindromo(palabra):
    salida=True;
    comparar1=''.join(e for e in palabra if e.isalnum()).lower()
    comparar2=comparar1[::-1]
    
    for i,j in zip(comparar1,comparar2):
        if i!=j:
            salida=False;
    return salida
    
def orden_al(palabra):
    salida=True;
    cadena=palabra.lower()
    i=0
    if len(cadena)>=1:
        i=1;
    while(salida and i<len(cadena)):
        if cadena[i]<cadena[i-1]:
            salida=False
        else:
            i=i+1
    return salida

def trocear(palabra,num):
    listaSalida=[]
    i=0
    while i<len(palabra):
        listaSalida.append(palabra[i:(i+num)])
        i+=num
    
    return listaSalida
    
def anagrama(p1,p2):
    palabra=p1.lower()
    palabra2=p2.lower()
    salida=True;
    if len(palabra)==len(palabra2):
        for i in palabra:
            if salida:
                if i not in palabra2:
                    salida=False
                else:
                    palabra2.replace(i, "",1)
            else:
                break
    else:
        salida=False
    return salida


def pangrama(palabra):
    salida=True
    cadena="qwertyuiopasdfghjklzxcvbnm"

    for i in cadena:
        if i not in palabra:
            salida=False
            break
   
    return salida   

if __name__=="__main__":

    print("*** 1-Palabras comunes ***")
    p=raw_input('Inserta palabra: ')
    l=raw_input('Inserta palabra2: ')
    contador=comunes(p,l)
    print ("Letras Comunes:",contador)
    
    print("*** 2-Palabras no comunes ***")
    p=raw_input('Inserta palabra: ')
    l=raw_input('Inserta palabra2: ')
    contador=no_comunes(p,l)
    print ("Letras Comunes:",contador)
    
    print("*** 3-Eco Palabras ***")
    p=raw_input('Inserta palabra: ')
    contador=eco_palabras(p)
    print ("Eco:",contador)
    
    print("*** 4-Palindromo ***")
    p=raw_input('Inserta palabra: ')
    contador=palindromo(p)
    print ("Palindromo:",contador) 
 
    print("*** 5-Orden ***")
    p=raw_input('Inserta palabra: ')
    contador=orden_al(p)
    print ("Orden Al:",contador) 

    print("*** 6-Trozos ***")
    p=raw_input('Inserta palabra: ')
    l=int(raw_input('Inserta trozos: '))
    contador=trocear(p,l)
    for i in contador:
        print ("Trozo:",i)
 

    print("*** 7-Anagrama ***")
    p=raw_input('Inserta palabra: ')
    l=raw_input('Inserta palabra2: ')
    contador=anagrama(p,l)
    print ("Es anagrama:",contador)

    print("*** 8-Pangrama ***")
    p=raw_input('Inserta palabra: ')
    contador=pangrama(p)
    print ("Es pangrama:",contador)
    
    