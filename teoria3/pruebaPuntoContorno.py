import punto as p
import contorno as c


if __name__=="__main__":
    p1=p.Punto(10,20)
    p2=p.Punto(30,40)
    p3=p.Punto(50,60)
    p4=p.Punto(80,90)
    
    l=[]
    l.append(p1)
    l.append(p2)
    
    print(str(p3))
    contorno = c.Contorno(l)
    print("Contorno Inicial: "+str(contorno))
    contorno.addPoint(p3)
    print("Contorno punto extra: "+str(contorno))
    
    print("Numero de puntos:"len(contorno))

