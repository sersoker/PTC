"""
Created on Tue Oct 11 09:45:43 2016
@author: Bryan Moreno Picaman
"""

def contar_letras(palabra,letra):
    cont=0;
    for c in palabra:
        if c==letra:
            cont+=1
    return cont
    
def eliminar_letras(palabra,letra):
    salida="";
    for c in palabra:
        if c!=letra:
            salida=salida+c
    return salida

def mayusculas_minusculas(cadena):
    salida="";
    for c in cadena:
        if(ord(c)>=65 and ord(c)<=90) or (ord(c)>=97 and ord(c)<=122) :
            if ord(c)>=97 and ord(c)<=122:
                salida=salida+chr(ord(c)-32)
            else: 
                salida=salida+chr(ord(c)+32)
        else:
             salida=salida+c
    return salida    

def buscaCorrespondencia(cadena,subcadena,indice):
   existe=True
   contador=0;   
   while contador<len(subcadena) and existe==True:
       if indice+contador<len(subcadena):
           if cadena[indice+contador]!=subcadena[contador]:
               existe=False
       contador+=1
   return existe   
    
def buscar(cadena,subcadena):
    salida=-1
    indice=0
    for c in cadena:
       if c==subcadena[0]:
           if buscaCorrespondencia(cadena,subcadena,indice)== True:
               return indice;
       indice+=1
    return salida    
    
def vocales(cadena):
    salida=""
    cadenaC="aeiouAEIOU"
    for c in cadena:
        if c in cadenaC:
            if not c in salida:
                salida=salida+c
    return salida


def es_inversa(cadena1,cadena2):
    salida=False
    inve=""
    if len(cadena1)==len(cadena2):
        for h in cadena2:
            inve = h + inve
        if buscar(cadena1,inve)==0:
            salida=True
    return salida

    
if __name__=="__main__":
    
    print("*** 1-Contador de letras ***")
    p=raw_input('Inserta palabra: ')
    l=raw_input('Inserta letra: ')
    contador=contar_letras(p,l)
    print ("Numero de letras encontradas:",contador)
    
    print("\n*** 2-Eliminador de letras ***")    
    p=raw_input('Inserta palabra: ')
    l=raw_input('Inserta letra: ')
    salida=eliminar_letras(p,l)
    print ("Palabra final:",salida)    
        
    print("\n*** 3-Swap MinusculasMayusculas ***")    
    p=raw_input('Inserta palabra: ')
    salida=mayusculas_minusculas(p)
    print ("Palabra final:",salida)    
    
    print("\n*** 4-Buscar subcadena***")    
    cadena=raw_input('Inserta Cadena: ')
    subcadena=raw_input('Inserta SubCadena: ')
    salida=buscar(cadena,subcadena)
    print ("Posicion:",salida)    
    
    print("\n*** 5-Buscar vocales ***")    
    cadena=raw_input('Inserta Cadena: ')
    salida=vocales(cadena)
    print ("Vocales existentes:",salida)    
     
     
    print("\n*** 6-Buscar vocales ***")    
    cadena1=raw_input('Inserta Cadena1: ')
    cadena2=raw_input('Inserta Cadena2: ')
    salida=es_inversa(cadena1,cadena2)
    if salida :
        print ("Es inversa:")   
    else:
        print ("No es inversa:")
        
