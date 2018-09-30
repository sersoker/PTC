import DID as DID
"""
@author: Bryan Moreno Picamán
"""
listaIdiomas=["spa","eng","de"]

listaDocumentos=[]
listaDocumentos.append(["spa1.txt","spa2.txt","spa3.txt"])
listaDocumentos.append(["eng1.txt","eng2.txt","eng3.txt"])
listaDocumentos.append(["de1.txt","de2.txt","de3.txt"])


pruebaDID=DID.DID(listaDocumentos,listaIdiomas)
print("Texto en Aleman")
print(pruebaDID.calculateFileLanguage("deText1.txt")) #Aleman
print("Texto en Ingles")
print(pruebaDID.calculateFileLanguage("enText1.txt")) #Ingles
print("Texto en Español")
print(pruebaDID.calculateFileLanguage("esText1.txt")) #Español
print("Texto en Español")
print(pruebaDID.calculateFileLanguage("guerra.txt")) #Español
print("Texto en Español")
print(pruebaDID.calculateFileLanguage("quijote.txt")) #Español


