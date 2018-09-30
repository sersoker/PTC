#!/usr/bin/env python
import codecs
import re 
import copy 
class MDT:
    documentNameList=[]    
    stopWordsList=[]
    listaTerminos=[]
    listaTerminos2=[]
    listaDiccionarios=[]
    listaDiccionarios2=[]
    wordcount=0

    #Constructor MDT se le pasa como parametro una lista de documentos (rutas de archivos)
    #ademas de asi como el nombre del archivo con las palabras vacias.
    def __init__(self,documentNameList, stopWordsFile):
        if len(documentNameList)>0:
            self.documentNameList=copy.copy(documentNameList)
            self.__processStopWords(stopWordsFile)
            self.__processDocuments()
    
    #Método que se llama desde el constructor, encargado de procesar y almacenar la información referente a los documentos que se le pasan al constructor.
    #Además de esto inicializa las estructuras necesarias para poder almacenar toda la información a procesar de los documentos (reserva de espacio y declaración de estructuras), tanto para palabras normales como para los 2-gramas.
    def __processDocuments(self):
        print("Procesando Documentos")
        #Creamos un espacio de almacenamiento por cada documento, tanto para las palabras normales como para los 2-grama
        for i in range(len(self.documentNameList)):
            self.listaDiccionarios.append({})
            self.listaDiccionarios2.append({})
        #Procesamos el documento
        for i in range(len(self.documentNameList)):
            f = codecs.open(self.documentNameList[i], "r")
            self.__processUnit(f,i)
        #print(self.listaDiccionarios2)
        return 1
        
    #Método que procesa y almacena la información referente a las “palabras vacias” que se proporcionan en el constructor.
    def __processStopWords(self,stopWordsFile):
        print("Procesando Palabras Vacias")
        f = codecs.open(stopWordsFile, "r")
        content = f.read().split()
        #No se comprueba que esten por que la lista se supone que tiene apariciones unicas.
        for i in content:
            self.stopWordsList.append(i)
        #print(self.stopWordsList)
        return 1   
    
    #Función auxiliary utilizada para procesar un documento especifico, de forma que se llama una vez por cada uno de los documentos.
    #Se le debe indicar en qué posición de la matriz de documentos/términos/ocurrencias va a ser almacenada.
    def __processUnit(self,f,pos):
        primeraPalabra=True;
        palabraAnterior="nada"
        #Leemos el contenido y lo separamos
        decod=f.read().split()
        for i in decod:
            #Añadimos los valores sin caracteres especiales a la lista de terminos y ademas a un diccionario(independiente por cada documento)
            value=re.sub('[^A-Za-z0-9áÁéÉíÍóÓúÚÑññÑàÀèÈìÌòÒùÙ]+',"", str(i))
            value=value.lower()
            #Original Funcionando
            #value=re.sub('[^A-Za-z0-9]+', '', i)
            if(self.stopWordsList.count(value)<=0):
                self.wordcount=self.wordcount+1
                if(not primeraPalabra):
                    self.__insertNewValue(pos,value)
                    self.__insertNewValue2(pos,palabraAnterior,value)
                    palabraAnterior=value
                else:
                    primeraPalabra=False
                    self.__insertNewValue(pos,value)
                    palabraAnterior=value

    """
    Función auxiliar utilizada por processUnit, esta recibe una palabra, un índice (de diccionario) y para ese diccionario y todos los demás del sistema hace varias comprobaciones:
    -	Si el sistema había registrado ya esta palabra, aumente el número de ocurrencias donde corresponde, el resto no se altera.
    -	Si no se había registrado:
    o	Se genera una entrada en cada uno de los diccionarios a 0 y añade 1 al contador del diccionario indicado
    o	Se registra la palabra dentro de la lista de temimos para futuras comprobaciones.
    
    """        
    def __insertNewValue(self,index,palabraActual):
        value=palabraActual.lower()
        for i in range(self.num_documentos()):
            if(i!=index):
                try:
                    self.listaDiccionarios[i][value]+=0
                except:
                    self.listaDiccionarios[i][value]=0
            else:
                try:
                    self.listaDiccionarios[i][value]+=1
                except:
                    self.listaDiccionarios[i][value]=1
                    self.listaTerminos.append(value)
                    
    #Funcion complementaria de __insertNewValue utilizada para los 2-gramas
    def __insertNewValue2(self,index,palabraAnterior,palabraActual):
        value=palabraAnterior+" "+palabraActual
        value=value.lower()
        for i in range(self.num_documentos()):
            if(i!=index):
                try:
                    self.listaDiccionarios2[i][value]+=0
                except:
                    self.listaDiccionarios2[i][value]=0
            else:
                try:
                    self.listaDiccionarios2[i][value]+=1
                except:
                    self.listaDiccionarios2[i][value]=1
                    self.listaTerminos2.append(value)

        
    #Devuelve el número de términos existentes en el MDT, coincide con la cantidad de elementos de la lista de términos.
    def num_terminos(self):
        return len(self.listaTerminos)
    
    #Al igual que el método anterior, pero relacionado con los 2-gramas del sistema.
    def num_terminos2(self):
        return len(self.listaTerminos2)
        
    #Devuelve el número de documentos que hay en el sistema y han sido procesados.
    def num_documentos(self):
        return len(self.documentNameList)
    
    #Devuelve una lista de documentos (nombres de archivo) que han sido procesados por el sistema, coincide con la lista que se le pasa inicialmente.
    def list_documentos(self):
        return self.documentNameList   
    
    #Devuelve el término de mayor longitud del MDT, en caso de existir varios, el primero (para términos normales) 
    def max_longitud(self):
        longAct=0;
        terminoAct=""
        for i in self.listaTerminos:
            if len(i)>longAct:
                longAct=len(i)
                terminoAct=i
        return terminoAct
        
    #Devuelve el 2-grama de mayor longitud del MDT, en caso de existir varios, el primero (para 2-gramas)
    def max_longitud2(self):
        longAct=0;
        terminoAct=""
        for i in self.listaTerminos2:
            if len(i)>longAct:
                longAct=len(i)
                terminoAct=i
        return terminoAct
  
    #Devuelve una lista de palabras que aparezcan n o más veces.      
    def terminos_freq_sup(self,n):
        salida=[]
        for i in self.listaTerminos:
            nometido=True;
            for j in self.listaDiccionarios:
                if j[i]>=n and nometido:
                    salida.append(i)
                    nometido=False
        return salida
    
    #Devuelve una lista de palabras que aparezcan entre min y max veces
    def terminos_freq_min_max(self,min,max):
        salida=[]
        for i in self.listaTerminos:
            for j in self.listaDiccionarios:
                if j[i]>=min and j[i]<=max:
                    if(salida.count(i)==0):
                        salida.append(i)
        return salida
        
    #Dado una palabra, devuelve una lista de términos asociados a la misma.
    def terminos_asociados(self,termino):
        salida=[]
        for key in self.listaDiccionarios2[0]:
            if key.startswith(termino):
                salida.append(key)
        return salida

    #Reducir el MDT eliminando el porcentaje indicado (Eliminar 1-porcentaje del total)
    def reducir(self,porcentaje):
        #Calculamos la cantidad a reducir
        areducir=int(self.wordcount*(1-porcentaje))
        #El valor inicial de los que se reducen, empieza en 1
        valorInicial=1;
        #Mientras queden valores por recudir (usando la variable como contador), iteramos los contenedores y llamamos a una función que borra un elemento
        while(areducir>0):
            for i in range(len(self.documentNameList)):
                if areducir>0:
                    if(self.__popword(i,valorInicial)): #El primera valor para el indice del diccionario, el segundo para el valor que busca en el mismo
                        areducir=areducir-1
                        valorInicial=1
                        eliminado=True
            #Si se ha eliminado, no aumentamos el valor a buscar, ya que puede existir otra entrada que tenga el mismo valor.
            if(not eliminado):
                valorInicial=valorInicial+1
            else:
                eliminado=False


        self.wordcount=self.wordcount-int(self.wordcount/100*porcentaje)
        return 1
    
    #Dado un índice de diccionario y un valor, reduce en 1 la primera entrada del mismo que tenga ese valor. Es una función auxiliar utilizada por reducir.
    def __popword(self,ndict,valorInicial):
        actualdict=self.listaDiccionarios[ndict]
        for k,v in actualdict.items():
            if v == valorInicial:
                actualdict[k]=valorInicial-1
                return True
        return False
        
    #Dada una palabra devuelve el numero de ocurrencias para cada uno de los documentos.
    def countTerm(self,palabra):
        termino=palabra.lower()
        salida=[]
        for i in range(len(self.listaDiccionarios)):
            try:
                salida.append("Aparece en "+str(self.documentNameList[i])+", "+str(self.listaDiccionarios[i][termino])+" veces.")
            except:
                salida.append("Aparece en "+str(self.documentNameList[i])+", 0 veces.")

        return salida   
    
    #Dada una palabra devuelve el numero de ocurrencias para cada uno de los documentos. (para los 2-gramas)
    def countTerm2(self,palabra):
        termino=palabra.lower()
        salida=[]
        for i in range(len(self.listaDiccionarios2)):
            try:
                salida.append("Aparece en "+str(self.documentNameList[i])+", "+str(self.listaDiccionarios2[i][termino])+" veces.")
            except:
                salida.append("Aparece en "+str(self.documentNameList[i])+", 0 veces.")
        return salida
        
    #Indica el número de palabras contabilizadas en la estructura.
    def numero_palabras(self):
        return self.wordcount
    
    """
    Calcula los ngramas sobre los documentos del sistema o sobre los que se le pasen en el parámetro docs.
    N indica que documentos se usan, si es -1 se realiza en todos los documentos, si es mayor a este valor, solo en el documento que corresponda a este índice.
    Num_gramas indica cuantas palabras se cogerán para realizar el n-Grama.
    Esta función se realiza sin almacenar nada en las estructuras por lo que el uso de documentos muy grandes puede ocasionar problemas de estabilidad o memoria.
    """
    def ngramas(self,docs,n,num_ngramas):
        documentosAUsar=[]
        #Elegimos que lista de documentos será usada
        if(docs is None):
            print("Usando documentos almacenados")
            documentosAUsar=self.documentNameList;
        else:
            print("Usando documentos proporcionados")
            documentosAUsar=docs;
 
        salida=[]
        if(n<len(documentosAUsar)):
            #Elegimos la cantidad de documentos que serán procesados
            if(n>=0):
                salida=self.calculaGrama(documentosAUsar[n],num_ngramas)
            else:
                for i in range(len(documentosAUsar)):
                    salida=list(set(salida)|set(self.calculaGrama(documentosAUsar[i],num_ngramas)))
        return salida
    
    #Función que realiza el cálculo individual de un n-grama sobre un documento, devuelve una lista con los ngramas.
    def calculaGrama(self,document,num_ngramas):
        salida=[]
        indiceActual=0;
        print("Procesando documento: "+document)
        #Abriendo archivo y separando contenido
        file = codecs.open(document, "r")
        content = file.read().split()
        #No se comprueba que esten por que la lista se supone que tiene apariciones unicas.
        parcial=[]
        for i in range(len(content)):
            value=re.sub('[^A-Za-z0-9áÁéÉíÍóÓúÚÑññÑàÀèÈìÌòÒùÙ]+',"", str(content[i]))
            if(self.stopWordsList.count(value)<=0):
                if(indiceActual<num_ngramas):
                    parcial.append(value)
                    indiceActual=indiceActual+1
                else:                
                    salida.append(self.__toTerm(parcial))
                    parcial.pop(0)
                    parcial.append(value)
        #Añadimos el ultimo n-grama      
        salida.append(self.__toTerm(parcial))
        return salida;
        
    #Función auxiliar utilizada para pasar de una lista de varios términos a un string con formato  (palabra(espacio)palabra(espacio)…)   Se utiliza en el calculo de los nGramas para unificar formatos.
    def __toTerm(self,listaTerminos):
        salida=""
        for i in listaTerminos:
            salida=salida+" "+str(i)
        return salida
    
    #Guarda en un archivo con el nombre indicado en el parámetro, un volcado de los datos almacenados en las estructuras del MDT, solo para los términos simples.
    def savetofile(self,name):
        file_ = open(name, 'w')
        file_.write("NUM_TERMINOS:"+str(len(self.listaTerminos)))
        file_.write('\n')
        file_.write(', '.join(self.listaTerminos))
        file_.write('\n')
        for i in self.listaDiccionarios:
            file_.write("NUM_TERMINOS:"+str(len(i)))
            file_.write('\n')
            file_.write(' , '.join('{}{}'.format(key, val) for key, val in i.items()))
            file_.write('\n')

        file_.close()
        
    #Guarda en un archivo con el nombre indicado en el parámetro, un volcado de los datos almacenados en las estructuras del MDT, solo para los 2-gramas.
    def savetofile2(self,name):
        file_ = open(name, 'w')
        file_.write("NUM_TERMINOS:"+str(len(self.listaTerminos2)))
        file_.write('\n')
        file_.write(', '.join(self.listaTerminos2))
        file_.write('\n')
        for i in self.listaDiccionarios2:
            file_.write("NUM_TERMINOS:"+str(len(i)))
            file_.write('\n')
            file_.write(','.join('{}{}'.format(key, val) for key, val in i.items()))
            file_.write('\n')

        file_.close()


#Pruebas MDT        
if __name__=="__main__":
    listaDocumentos=[]
    listaDocumentos.append("lore.txt")
    #listaDocumentos.append("quijote.txt")
    listaDocumentos.append("guerra.txt")
    
    pruebaMDT=MDT(listaDocumentos,"palabras_vacias.txt")
    print(pruebaMDT.countTerm("pero"))
    print(pruebaMDT.countTerm2("Ahora no"))

#   print("Total de documentos:",pruebaMDT.num_documentos())
#   print("Listado de documentos",pruebaMDT.list_documentos())
#    
#   pruebaMDT.savetofile("PruebaBasico.txt")
#   pruebaMDT.savetofile2("Prueba2Grama.txt")
#
#   print ("Termino mas grande: "+str(pruebaMDT.max_longitud()))
#   #print(pruebaMDT.terminos_freq_sup(1))    
#   #print(pruebaMDT.terminos_freq_min_max(2,2))
#    
#   print(pruebaMDT.terminos_asociados("profesor"))
#   pruebaMDT.savetofile("uno.txt")
#
    #print("Tamanio inicial: "+str(pruebaMDT.numero_palabras()))
    #pruebaMDT.reducir(1)
    #print("Tamanio Final: "+str(pruebaMDT.numero_palabras()))
#
#   pruebaMDT.savetofile("dos.txt")

    
    #print(pruebaMDT.ngramas(None,0,5))
   # print(pruebaMDT.ngramas(listaDocumentos,0,5))




        