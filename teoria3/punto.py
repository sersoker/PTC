class Punto:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def __repr__(self):
        return str(self.x)+str(" ")+str(self.y)
        
    def __str__(self):
        return str(self.x)+str(" ")+str(self.y)
    
    def modify(self,x,y):
        self.x=x
        self.y=y
        
    