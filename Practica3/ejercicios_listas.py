import random
"""
Created on Tue Oct 11 09:45:43 2016
@author: Bryan Moreno Picaman
"""

def codigo_cesar(palabra,num):
    lista=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w","x","y","z"]    
    cont="";
    codigo=0    
    if num<0:
        codigo=num+pepelen(lista)
    else:
        codigo=num
        
    for c in palabra:
        cont=cont+lista[(lista.index(c)+codigo)%len(lista)]
    return cont

def suma_cifras(palabra):
    cont=0
    for c in palabra:
        if c.isdigit():
            cont+=int(c)
    return cont

def suma_num_lista(lista):
    suma=0
    for i in lista:
        suma+=i
    return suma
    
def numeros_pares(lista):
    salida=[]
    for i in lista:
        if i%2==0:
            salida.append(i)
    return salida

def numeros_impares(lista):
    salida=[]
    for i in lista:
        if not i%2==0:
            salida.append(i)
    return salida    

def combinar(lista1,lista2):
   salida=[]
   indice1=indice2=0
   while indice1<len(lista1) and indice2<len(lista2):
       if lista1[indice1]<=lista2[indice2]:
           salida.append(lista1[indice1])
           indice1+=1
       else:
           salida.append(lista2[indice2])
           indice2+=2
   return salida
   
def traspuesta(lista):
    salida=[]
    for i in range(len(lista)):
        listaParcial=[]
        for j in range(len(lista)):
            listaParcial.append(lista[j][i])
        salida.append(listaParcial)
    return salida

    
   
if __name__=="__main__":

    print("*** 1-Codigo cesar ***")
    p=raw_input('Inserta palabra: ')
    l=int(raw_input('Inserta codigo: '))
    contador=codigo_cesar(p,l)
    print ("Cesar:",p,contador)

    print("*** 2-Suma cifras ***")
    l=raw_input('Inserta cadena: ')
    contador=suma_cifras(l)
    print ("Suma cifras:",l,contador)
    
    print("*** 3-Suma lista ***")
    lista=[]
    for i in range(5623):     
        lista.append(random.random())
    print("Suma",suma_num_lista(lista))
    
    print("*** 4-Pares de una lista***")
    lista=[]
    for i in range(53):     
        lista.append(int(random.random()*100))
    print("Pares",numeros_pares(lista))
    
    print("*** 5-Impares de una lista***")
    lista=[]
    for i in range(53):     
        lista.append(int(random.random()*100))
    print("Pares",numeros_impares(lista))
    
    print("*** 6-Combinar listas***")
    lista1=[]
    lista2=[]
    for i in range(53):     
        lista1.append(int(random.random()*20))
        lista2.append(int(random.random()*20))
    lista1.sort()
    lista2.sort()
    print("Combinados",combinar(lista1,lista2))
    print("*** 6-Combinar listas***")
    lista=[[0,1,2],[3,4,5],[6,7,8]]
    print(lista)
    print("Traspuesta",traspuesta(lista1))
    