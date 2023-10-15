
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coords(self):
        return(self.x, self.y)
    
    def izq(self, p):
        res = False
        if self.x < p.x:
            res = True
        return res
    

centro = Punto(0, 0)
p1= Punto(-1, -1)
print(centro.izq(p1))


class Linea:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def puntos(self):
        return((self.p1.x, self.p1.y), (self.p2.x, self.p2.y))

lin = Linea(centro, p1)
print(lin.puntos())