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
import numpy

# Standard scientific Python imports
import matplotlib.pyplot as plt
# Import datasets, classifiers and performance metrics
from sklearn import datasets, svm, metrics

class Clasificador:
    
    def __init__(self,master):
        #Inicializar y entrenar clasificador
        self.initClas()

        #Init de variables y pantalla principal
        self.fullScreenStatus=False
        self.master=master
        self.selectArea=None
        self.vectorProcessData=[]
        self.imagenes=[]

#        self.master.grid()
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
        
        #Añadiendo canvas
        self.frameInferior=Frame(self.master)
        self.frameInferior.pack(side=TOP,fill=BOTH)
        self.can = Canvas(self.frameInferior)
        self.can.pack(side=TOP,fill=BOTH)


        #Controladores de teclado
        self.master.bind('<Escape>',self.enableFullScreen)
        
        #Manejadores de raton
        self.can.bind("<Motion>",self.mouseEntered)
        self.can.bind("<Button-1>",self.clicImage)
        self.can.bind("<ButtonRelease-1>",self.releaseImage)
        self.can.bind("<B1-Motion>",self.motionImage)
        
    def mouseEntered(self,event):
        st="["+str(event.x)+"]["+str(event.y)+"]"
        self.position.config(text=st)
        
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

    
    def releaseImage(self,event):
        if(event.x>self.img.width()):
            self.clicrX=self.img.width()
        else:
            self.clicrX=event.x

        if(event.x>self.img.height()):
            self.clicrY=self.img.height()
        else:
            self.clicrY=event.y   

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

        
    def processClicReleaseSave(self):        
        #Guardamos la región en el archivo indicado
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
            
    def processClicRelease(self):
        #Guardamos la región en formato vector.
#        try:
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
#        except:
#            showerror("Error guardando")

            
    def createMenu(self):
        self.menu = Menu(self.master)
        self.filemenu = Menu(self.menu, tearoff=0)
        self.filemenu.add_command(label="Abrir imagen",command=self.openFile )
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

            
            
    def enableFullScreen(self):
        self.fullScreenStatus=not self.fullScreenStatus
        self.master.attributes('-fullscreen', self.fullScreenStatus) 
        
    def closeAndExit(self):
        self.master.destroy() 
        
    def openFile(self):
        self.filename=askopenfilename(filetypes=(("Imagenes", "*.gif"),("Todos", "*.*") ))
        #self.filename=askopenfilename(filetypes=(("Imagenes", "*.jpg;*.jpeg;*.png;*.gif"),("Todos", "*.*") ))
        self.displayFile()
        
    def displayFile(self):
        self.img = PhotoImage(file=self.filename)
        self.can.create_image(0, 0, image=self.img, anchor=tk.NW)
    
    def normalize(self,array):
        for x in numpy.nditer(array, op_flags=['readwrite']):
            x[...] = 16-(x*16/numpy.amax(array))
        
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
        