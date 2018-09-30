
from numpy import *
from matplotlib.pylab import *

def t1f1():
#GRAFICA NORMAL
    t=arange(0.0,7.0,0.01)
    s=sin(2*pi*t)
    s2=cos(2*pi*t)
    fig=figure()
    plot(t,s,'b-o',linewidth=1.0,label="sin(x)")
    plot(t,s2,'r-^',linewidth=1.0,label="cos(x)")
    annotate('Maximo',xy=(2,1),xytext=(math.pi/2,1.5),arrowprops=dict(facecolor='black'))
    axis([0,7,-2,2])
    legend()
    show()
    fig.savefig("prueba.png")
    show()



def t1f2():
#NUBE DE PUNTOS
    x=rand(200)
    y=rand(200)
    size=rand(200)*30
    color=rand(200)
    scatter(x,y,size,color)
    colorbar()
    show()


def t1f3():
    x=arange(0,8,0.1)
    bar(x,sin(x),width=(x[1]-x[0]))
    show()
    barh(x,sin(x),height=(x[1]-x[0]))
    show()

  
        
if __name__=="__main__":
            
    t1f1()
    t1f2()
    t1f3()
    