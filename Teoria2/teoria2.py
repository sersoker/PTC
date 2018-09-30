import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from matplotlib.path import Path
import matplotlib.patches as patches
from scipy import special


def t2f2():
    x=range(100)
    y=[sqrt(i)for i in x]
    plt.plot(x,y,color='k',lw=2)
    plt.fill_between(x,y,0,color='0.8')
    plt.show()
    
def t2f3():
    x=np.arange(0,4,0.2)
    y=np.exp(-x)
    el=0.1*np.abs(np.random.randn(len(y)))
    plt.errorbar(x,y,yerr=el,fmt='.-')
    plt.show()    
        
def t2f4():
    plt.figure(figsize=(3,3))
    x=[45,20,35]   
    labels=['Perros','Gatos','Peces']
    plt.pie(x,labels=labels)
    plt.show()
    
       
def t2f5():
    plt.figure(figsize=(3,3))
    x=[4,9,21,55,30,19]   
    labels=['Sioza','Austria','Espana','Italia','Francia','Benelux']
    explode=[0.2,0.1,0,0,0.1,0]
    plt.pie(x,labels=labels,explode=explode)
    plt.show()

def t2f6():
    plt.figure(figsize=(3,3))
    x=[13,21,55,30,19]   
    labels=['Sioza','Austria','Espana','Italia','Francia']
    explode=[0.2,0.1,0,0.1,0]
    colors=['yellowgreen','gold','lightskyblue','lightcoral','brown']
    plt.pie(x,labels=labels,explode=explode,colors=colors,shadow=True)
    plt.axis('equal')    
    plt.show()

def f(x,y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)  
    
def t2f7():
    n=256
    x=np.linspace(-3,3,n)
    y=np.linspace(-3,3,n)
    X,Y=np.meshgrid(x,y)
    plt.contourf(X,Y,f(X,Y),25,alpha=.75,cmap='jet')
    C=plt.contour(X,Y,f(X,Y),25,linewidth=0.5,colors='black')
    plt.clabel(C,fmt='%1.1f%%')
    plt.show()

def t2f8():
    verts=[(0.,0.),(0.,1.),(1.,1.),(1.,0.),(0.,0.)]
    
    codes=[Path.MOVETO,Path.LINETO,Path.LINETO,Path.LINETO,Path.CLOSEPOLY]  
    
    path=Path(verts,codes)
    fig=plt.figure()
    ax=fig.add_subplot(111)
    patch=patches.PathPatch(path,facecolor='orange',lw=2)
    ax.add_patch(patch)
    ax.set_xlim(-2,2)
    ax.set_ylim(-2,2)
    plt.show()

def t2f9():
    x,y=np.mgrid[-25:25:100j,-25:25:100j]
    r=np.sqrt(x**2+y**2)
    s=special.j0(r)*25
    
    plt.imshow(s,extent=[-25,25,-25,25])
    plt.colorbar()    
    
def t2f9():
    x,y=np.mgrid[-25:25:100j,-25:25:100j]
    r=np.sqrt(x**2+y**2)
    s=special.j0(r)*25
    
    plt.imshow(s,extent=[-25,25,-25,25])
    plt.colorbar()        
    
if __name__=="__main__":
    """        
    t2f2()
    t2f3()
    t2f4()
    t2f5()
    t2f7()
    t2f8()
    t2f9()
    t2f10()
    """    
    t2f9()

    