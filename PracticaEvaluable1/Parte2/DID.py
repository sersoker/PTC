"""
@author: Bryan Moreno Picamán
"""
import copy
import codecs 
import re

class DID:
    languajeList=[]
    documentNameList=[]
    listaDiccionarios=[]

    #El constructor recibe una lista de listas de documentos, cada lista es para un idioma. El nombre de los idiomas se le pasa en un listado separado.
    def __init__(self,documentNameList,languajeList):
        if len(documentNameList)>0:
            self.documentNameList=copy.copy(documentNameList) #Guardamos la lista de los documentos
            self.languajeList=copy.copy(languajeList) #Guardamos la lista de los idiomas
            for i in range(len(languajeList)): #Generamos el espacio para cada uno de los idiomas
                self.listaDiccionarios.append({})
                
            for i in range(len(documentNameList)): #Procesamos cada uno de los idiomas
                self.__processLanDocuments(i,documentNameList)
   
    #Método que se llama desde el constructor, encargado de procesar y almacenar la información referente a los documentos que se le pasan al constructor.
    #Además de esto inicializa las estructuras necesarias para poder almacenar toda la información a procesar de los documentos (reserva de espacio y declaración de estructuras).
    def __processLanDocuments(self,lanIndex,documentList):
        print("Procesando textos en: "+self.languajeList[lanIndex])
        for i in documentList[lanIndex]:
            self.__processUnit(i,lanIndex)

    
        
    #Función auxiliar utilizada para procesar un documento especifico, de forma que se llama una vez por cada uno de los documentos.
    #Se le debe indicar en qué posición de la matriz de documentos/términos/ocurrencias va a ser almacenada.
    def __processUnit(self,documentName,lanIndex):
        file=codecs.open(documentName, "r")
        decod=file.read().split("ç")
        value=re.sub('[^A-Za-záÁéÉíÍóÓúÚÑññÑàÀèÈìÌòÒùÙäÄöÖüÜß]+',"", str(decod))
        value=value.lower()
        for i in range(0, len(value), 4):
            self.__insertNewValue(lanIndex,value[i:i+4])

    """
    Función auxiliar utilizada por processUnit, esta recibe una palabra, un índice (de diccionario) y para ese diccionario y todos los demás del sistema hace varias comprobaciones:
    -	Si el sistema había registrado ya esta palabra, aumente el número de ocurrencias donde corresponde, el resto no se altera.
    -	Si no se había registrado:
    o	Se genera una entrada en cada uno de los diccionarios a 0 y añade 1 al contador del diccionario indicado
    
    """        
    def __insertNewValue(self,index,palabraActual):
        value=palabraActual.lower()
        for i in range(len(self.languajeList)):
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
                    
	#Función  que dado un documento devuelve una lista con los porcentajes de coincidencia para cada idioma (suma de todos es del 100%).
    def calculateFileLanguage(self,fileName):
        calculatedProb=[]
        total=0;
        file=codecs.open(fileName, "r")
        decod=file.read().split("ç")
        value=re.sub('[^A-Za-záÁéÉíÍóÓúÚÑññÑàÀèÈìÌòÒùÙäÄöÖüÜß]+',"", str(decod))
        value=value.lower()
        for i in range(len(self.languajeList)):
            eVal=self.__valueForLanguaje(value,i)
            calculatedProb.append(eVal)
            total+=eVal

        #print(self.languajeList,calculatedProb)
        returnValue=[]
        for i in range(len(calculatedProb)):
            returnValue.append(str(round(calculatedProb[i]*100/total,4))+"% , "+str(self.languajeList[i]))
        return returnValue
    
	#Dado un idioma y los valores leídos de un archivo, calcula el valor numérico (usando lo explicado anteriormente) o puntuación que le corresponde para el mismo. El valor que se devuelve es usado para elegir qué idioma se adapta más al documento en calculateFileLanguage().
    def __valueForLanguaje(self,value,index):
        #Se inicializa a 1000 para permitir hasta 100 fallos, esto se hace para compensar el posible mal aprendizaje.
        returnValue=1000;
        for i in range(0, len(value), 4):
            try:
                returnValue+=self.listaDiccionarios[index][value[i:i+4]]*100
            except:
                returnValue=returnValue-10
        #Si ha fallado tantas veces que el valor ha sido negativo (ha fallado mas de 100 y/o no encontrado ninguna coincidencia), se devuelve 0 directamente.
        if(returnValue<0):
            returnValue=0
        
        return returnValue
        
    #Guarda en un archivo con el nombre indicado en el parámetro, un volcado de los datos almacenados en las estructuras del DID.
    def savetofile(self,name):
        file_ = open(name, 'w')
        for i in self.listaDiccionarios:
            file_.write("NUM_TERMINOS:"+str(len(i)))
            file_.write('\n')
            file_.write(' , '.join('{}{}'.format(key, val) for key, val in i.items()))
            file_.write('\n')

        file_.close()
        
if __name__=="__main__":
    listaIdiomas=["spa","eng","de"]
    
    listaDocumentos=[]
    listaDocumentos.append(["spa1.txt","spa2.txt","spa3.txt"])
    listaDocumentos.append(["eng1.txt","eng2.txt","eng3.txt"])
    listaDocumentos.append(["de1.txt","de2.txt","de3.txt"])

    
    pruebaDID=DID(listaDocumentos,listaIdiomas)
    print(pruebaDID.calculateFileLanguage("deText1.txt"))
    print(pruebaDID.calculateFileLanguage("guerra.txt"))
    print(pruebaDID.calculateFileLanguage("lore.txt"))

    #pruebaDID.savetofile("prueba.txt")
