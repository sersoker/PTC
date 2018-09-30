import MDT as MDT
"""
Created on Sun Jan  1 19:07:28 2017

@author: Bryan Moreno Picamán
"""
print("Prueba implementación MDT, Bryan Moreno Picamán")
listaDocumentos=[]
listaDocumentos.append("lore.txt")
listaDocumentos.append("quijote.txt")
listaDocumentos.append("guerra.txt")

pruebaMDT=MDT.MDT(listaDocumentos,"palabras_vacias.txt")
print(pruebaMDT.countTerm("pero"))
print(pruebaMDT.countTerm2("Ahora no"))
print("Total de documentos:",pruebaMDT.num_documentos())
print("Listado de documentos",pruebaMDT.list_documentos())

pruebaMDT.savetofile("PruebaBasico.txt")
pruebaMDT.savetofile2("Prueba2Grama.txt")

print ("Termino mas grande: "+str(pruebaMDT.max_longitud()))
print(pruebaMDT.terminos_freq_sup(500))    
print(pruebaMDT.terminos_freq_min_max(700,900))

print(pruebaMDT.terminos_asociados("profesor"))

pruebaMDT.savetofile("uno.txt")
print("Reduciendo")
print("Tamanio inicial: "+str(pruebaMDT.numero_palabras()))
pruebaMDT.reducir(1)
print("Tamanio Final: "+str(pruebaMDT.numero_palabras()))

pruebaMDT.savetofile("dos.txt")

print("Cálculo de N-Gramas, se hacen directamente, los documentos grandes pueden dar problemas de memoria")
print(pruebaMDT.ngramas(None,0,5))
print(pruebaMDT.ngramas(listaDocumentos,0,5))