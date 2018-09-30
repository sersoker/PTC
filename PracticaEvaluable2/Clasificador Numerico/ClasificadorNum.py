# -*- coding: utf-8 -*-
"""
Autor Bryan Moreno Picamán
Clasificador asignatura PTC 2016-2017
"""
from tkinter import *
from tkinter.ttk import * 
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
import tkinter as tk
from PIL import Image
import PIL.ImageOps
import numpy
from PIL import ImageGrab
# Standard scientific Python imports
import matplotlib.pyplot as plt
# Import datasets, classifiers and performance metrics
from sklearn import datasets, svm, metrics

#Clase que define e implementa un clasificador númerico con una interfaz gráfica.
class Clasificador:
    #Constructor de la clase, encargado de inicializar variables y generar y organizar el entorno gráfico
    def __init__(self,gMode):
        #Inicializar y entrenar clasificador
        self.initClas()
        
        #Inicialización de variables
        self.selectArea=None
        self.vectorProcessData=[]
        self.imagenes=[]
        self.frameInferior=None
        self.frameBotonesGrid=None
        self.filename=None
        self.gridMode=False
        if gMode:
            #Init de variables y pantalla principal
            self.fullScreenStatus=False
            self.master=tk.Tk()

            
            self.master.title("Clasificador Bryan Moreno Picamán")
            self.master.minsize(width=500, height=500)
            
            #Añadiendo menus   
            self.createMenu();
            self.master.config(menu=self.menu)
            
            #Añadiendo botones
            self.frameBotones=Frame(self.master)
            self.frameBotones.pack()
            self.botonGuardar=Button(self.frameBotones,text="Guardar seleccionado",command=self.processClicReleaseSave)
            self.botonProcesar=Button(self.frameBotones,text="Procesar seleccionado",command=self.processClicRelease)
            self.botonTerminar=Button(self.frameBotones,text="Terminar",command=self.processList)
            self.botonGuardar.pack( side = LEFT)
            self.botonProcesar.pack( side = LEFT)
            self.botonTerminar.pack( side = LEFT)
    
            #Posición del cursor
            self.frameInferior2=Frame(self.master)
            self.frameInferior2.pack(side=BOTTOM)
            self.position=Label(self.frameInferior2,text="x,y")
            self.position.pack(side=RIGHT)
            
    
            
            #Controladores de teclado
            self.master.bind('<Escape>',self.enableFullScreen)
            self.master.mainloop()
        
    #Función auxiliar que permite añadir el canvas de mostrado y recorte de imágenes, es el encargado de borrar el canvas de cuadricula si es que existe.
    def __addCanvas__(self):
        self.frameInferior=Frame(self.master)
        self.frameInferior.pack(side=TOP,fill=BOTH)
        
        #Añadiendo canvas
        self.can = Canvas(self.frameInferior)
        self.can.pack(side=TOP,fill=BOTH)

        #Manejadores de raton
        self.can.bind("<Motion>",self.mouseEntered)
        self.can.bind("<Button-1>",self.clicImage)
        self.can.bind("<ButtonRelease-1>",self.releaseImage)
        self.can.bind("<B1-Motion>",self.motionImage)

	#Función que pinta en la cuadricula, está unida a el evento “motion” del ratón dentro del canvas.	
    def paint(self,event ):
       color = "#000000"
       x1, y1 = ( event.x - 2 ), ( event.y - 2 )
       x2, y2 = ( event.x + 2 ), ( event.y + 2 )
       self.can.create_oval( x1, y1, x2, y2, fill = color )
       st="["+str(event.x)+"]["+str(event.y)+"]"
    
	#Cuando se termina de pintar en la cuadricula procesa el contenido y genera una imagen.
    def paintEnd(self,event):
       x=self.frameBotonesGrid.winfo_rootx()+self.can.winfo_x()
       y=self.frameBotonesGrid.winfo_rooty()+self.can.winfo_y()
       x1=x+self.can.winfo_width()
       y1=y+self.can.winfo_height()
       self.gridimg=ImageGrab.grab().crop((x,y,x1,y1))
       self.gridimg=self.gridimg.convert('L')
    #Función auxiliar que permite añadir el canvas de cuadricula, es el encargado de borra el canvas de mostrado y recorte de imágenes si existe.    
    def __addButtonGrid__(self):
        #Añadiendo canvas
        self.frameBotonesGrid=Frame(self.master)
        self.frameBotonesGrid.pack(side=TOP,fill=BOTH)
        
        self.can = Canvas(self.frameBotonesGrid, width=80, height=80, bg='white')
        self.can.pack(expand = NO)
        self.can.bind( "<B1-Motion>", self.paint )
        self.can.bind( "<ButtonRelease-1>", self.paintEnd )

	#Manejador del evento de ratón entrando en el canvas de mostrado y recorte de imágenes, actualiza el label de posición del cursor dentro de la ventana gráfica.		
    def mouseEntered(self,event):
        st="["+str(event.x)+"]["+str(event.y)+"]"
        self.position.config(text=st)
        
	#Actualiza los valores internos de clic de ratón utilizados para el recorte de imágenes	
    def clicImage(self,event):
        if(event.x<0):
            self.clicX=0
        elif(event.x>self.img.width()):
            self.clicX=self.img.width()
        else:
            self.clicX=event.x
            
        if(event.y<0):
            self.clicY=0
        elif(event.y>self.img.height()):
            self.clicY=self.img.height()
        else:
            self.clicY=event.y

    #Conforme el ratón se mueve dentro del canvas de imagen después de hacer clic en la misma, actualiza la posición final del mismo, generando un cuadrado negro en la selección indicada entre la posición actual y la que se obtiene del clicImage.    
    def motionImage(self,event):
        if(event.x<0):
            self.clicrX=0
        elif(event.x>self.img.width()):
            self.clicrX=self.img.width()
        else:
            self.clicrX=event.x
            
        if(event.y<0):
            self.clicrY=0
        elif(event.y>self.img.height()):
            self.clicrY=self.img.height()
        else:
            self.clicrY=event.y
            
        if(self.selectArea!=None):
            self.can.delete(self.selectArea)
        self.selectArea=self.can.create_rectangle(self.clicX,self.clicY, self.clicrX,self.clicrY,outline="#000")

    #Actualiza la última posición de recorte al soltar el botón del ratón.
    def releaseImage(self,event):
        if(event.x>self.img.width()):
            self.clicrX=self.img.width()
        else:
            self.clicrX=event.x

        if(event.x>self.img.height()):
            self.clicrY=self.img.height()
        else:
            self.clicrY=event.y   

	#Procesa la lista completa de recortes y cuadriculas obtenidas de pasos anteriores y los pasa por el clasificador previamente declarado.	
    def processList(self):
        vector=numpy.array(self.vectorProcessData)
        n_samples2 = len(vector)
        data2 = vector.reshape(n_samples2,64)
        predicted = self.classifier.predict(data2)
        images_and_predictions = list(zip(self.imagenes, predicted))
        for index, (image, prediction) in enumerate(images_and_predictions[:len(self.imagenes)]):
            plt.subplot(2, 4, 5)
            plt.axis('off')
            plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
            plt.title('Prediction: %i' % prediction)
            plt.show()

    #Función que procesa el recorte de la imagen o la cuadricula completa y permite guardarla en la ruta que se indica a través de una ventana gráfica. Los elementos guardados no son añadidos a la lista de elementos que se procesarán más tarde.    
    def processClicReleaseSave(self):        
        if self.gridMode:
            try:
                nombre = tk.filedialog.asksaveasfilename()
                croped = self.gridimg
                croped.save(nombre)
                if(self.selectArea!=None):
                    self.can.delete(self.selectArea)
            except:
                print("Fuera de los margenes de la imagen")
            finally:
                if(self.selectArea!=None):
                    self.can.delete(self.selectArea)                
        else:
            try:
                nombre = tk.filedialog.asksaveasfilename()
                #nombre="/home/sersoker/Dropbox/Universidad/PTC/PracticaEvaluable2/pepe.gif"
                #nombre="C:/Users/Phoenix-Vento/Dropbox/Universidad/PTC/PracticaEvaluable2/pepe.gif"
                image = Image.open(self.filename)
                coord=[self.clicX,self.clicY, self.clicrX,self.clicrY]
                if coord[0] > coord[2]:
                    coord[0],coord[2] = coord[2],coord[0]
                if coord[1] > coord[3]:
                    coord[1],coord[3] = coord[3],coord[1]
                croped = image.crop(tuple(coord))
                #croped.show()
                croped.save(nombre)
                if(self.selectArea!=None):
                    self.can.delete(self.selectArea)
            except:
                showerror("Error guardando")
    
	#Función que procesa el recorte de la imagen o la cuadricula completa, añade los elementos a las estructuras internas que serán procesadas al darle al botón terminar.
    def processClicRelease(self):
        if self.gridMode:
            try:
                croped = self.gridimg.resize((8, 8), Image.ANTIALIAS)
                self.imagenes.append(PIL.ImageOps.invert(croped))
                #croped.show()
                pix = numpy.array(PIL.ImageOps.invert(croped))
                #print(pix)
                pix=pix.astype(float)
                self.normalize(pix)
                #print(pix)
                self.vectorProcessData.append(pix)
            except:
                print("Error de imagen")
            finally:
                if(self.selectArea!=None):
                    self.can.delete(self.selectArea)                
        else:
            try:
                image = Image.open(self.filename)
                coord=[self.clicX,self.clicY, self.clicrX,self.clicrY]
                if coord[0] > coord[2]:
                    coord[0],coord[2] = coord[2],coord[0]
                if coord[1] > coord[3]:
                    coord[1],coord[3] = coord[3],coord[1]
                try:
                    croped = image.crop(tuple(coord))
                    #croped=Image.open("C:/Users/Phoenix-Vento/Dropbox/Universidad/PTC/PracticaEvaluable2/pepe2.gif")
                    croped = croped.resize((8, 8), Image.ANTIALIAS)
                    #croped.show()
                    self.imagenes.append(croped)
                    pix = numpy.array(croped).reshape((8, 8))
                    #print(pix)
                    pix=pix.astype(float)
                    self.normalize(pix)
                    #print(pix)
                    self.vectorProcessData.append(pix)
                except:
                    print("Fuera de los margenes de la imagen")
                finally:
                    if(self.selectArea!=None):
                        self.can.delete(self.selectArea)                
            except:
                showerror("Error guardando")

    #Función auxiliar que crea los menús y submenús de la aplicación, se usa para simplificar código. 
    def createMenu(self):
        self.menu = Menu(self.master)
        self.filemenu = Menu(self.menu, tearoff=0)
        self.filemenu.add_command(label="Abrir imagen",command=self.openFile )
        self.filemenu.add_command(label="Abrir Grid",command=self.openGrid )
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit",command=self.closeAndExit)
        self.menu.add_cascade(label="Archivo", menu=self.filemenu)
        
        self.optionmenu = Menu(self.menu, tearoff=0)
        self.fullScreenString="FullScreen"
        self.optionmenu.add_command(label=self.fullScreenString, command=self.enableFullScreen )
        self.optionmenu.add_separator()
        self.optionmenu.add_command(label="Other", )
        self.optionmenu.add_separator()

        self.menu.add_cascade(label="File", menu=self.optionmenu)

    #Habilita y deshabilita el modo pantalla completa.        
    def enableFullScreen(self):
        self.fullScreenStatus=not self.fullScreenStatus
        self.master.attributes('-fullscreen', self.fullScreenStatus) 
    
	#Cierra y finaliza el programa    
    def closeAndExit(self):
        self.master.destroy() 
    
	#Función que genera el canvas de imágenes, muestra el selector dentro del sistema de ficheros y lo muestra.    
    def openFile(self):
        if(self.frameBotonesGrid!=None):
            self.frameBotonesGrid.destroy()
        if(self.frameInferior!=None):
            self.frameInferior.destroy()
        self.gridMode=False            
        self.__addCanvas__()
        self.filename=askopenfilename(filetypes=(("Imagenes", "*.gif"),("Todos", "*.*") ))
        #self.filename=askopenfilename(filetypes=(("Imagenes", "*.jpg;*.jpeg;*.png;*.gif"),("Todos", "*.*") ))
        self.displayFile()
	
	#Función que genera el canvas de cuadricula y lo muestra.
    def openGrid(self):
        if(self.frameInferior!=None):
            self.frameInferior.destroy()
        if(self.frameBotonesGrid!=None):
            self.frameBotonesGrid.destroy()  
        self.gridMode=True
        self.__addButtonGrid__()
      
    #Modifica la imagen que se muestra en el canvas de recorte.
    def displayFile(self):
        self.img = PhotoImage(file=self.filename)
        self.can.create_image(0, 0, image=self.img, anchor=tk.NW)
    
	#Función de normalización, el clasificador de dígitos trabaja con imágenes invertidas de valores 0-16, las imágenes son normales y con valores de 0-255 por lo que al pasar por aquí se modifican y adaptan al formato necesario.
    def normalize(self,array):
        for x in numpy.nditer(array, op_flags=['readwrite']):
            x[...] = 16-(x*16/numpy.amax(array))

    #Inicializa crea y enseña al clasificador utilizando la base de datos de dígitos, este clasificador queda disponible para clasificar en las funciones indicadas anteriormente.   
    def initClas(self):
        # El dataset de digitos
        self.digits = datasets.load_digits()
        # turn the data in a (samples, feature) matrix:
        self.n_samples = len(self.digits.images)
        self.data = self.digits.images.reshape((self.n_samples, -1))
        # Creando el clasificador con soporte para clasificación de vectores
        self.classifier = svm.LinearSVC()
        # Aprendemos con todo el dataset, usaremos como test lo introducido por pantalla
        self.classifier.fit(self.data, self.digits.target)
    
    #Dada una lista de rutas de imagen, las abre y las procesa ofreciendo su clasificación estimada como salida.
    def processImageList(self,imageList):  
        for name in imageList:
            image = Image.open(name).convert('L')
            croped = image.resize((8, 8), Image.ANTIALIAS)
            self.imagenes.append(croped)
            pix = numpy.array(croped)
            pix=pix.astype(float)
            self.normalize(pix)
            self.vectorProcessData.append(pix)
        self.processList()

            
            