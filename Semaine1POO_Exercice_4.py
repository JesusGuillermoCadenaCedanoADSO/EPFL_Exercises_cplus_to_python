class point3d(object):
    def __init__(self,c1=0.0,c2=0.0,c3=0.0):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3

    def init(self):
        print("Construction d'un nouveau point")
        self.c1 = float(input("Veuillez entrer x : "))
        self.c2 = float(input("Veuillez entrer y : "))
        self.c3 = float(input("Veuillez entrer z : "))

    def getc1(self):
        return self.c1

    def getc2(self):
        return self.c2

    def getc3(self):
        return self.c3

    def __str__(self):
        return "(" + str(self.c1) + ", " + str(+self.c2) + \
               ", " + str(self.c3) + ")"

def distance(punto1, punto2):
    return ((punto1.c1 - punto2.c1)**2 + (punto1.c2 - punto2.c2)**2 +
    (punto1.c3 - punto2.c3)**2)**0.5


class triangle(object):
    def __init__(self):
        self.p1 = point3d()
        self.p2 = point3d()
        self.p3 = point3d()

    def construir_puntos(self):
        self.p1.init()
        self.p2.init()
        self.p3.init()

    def perimetre(self):
        return "Périmètre : " + str(distance(self.p1, self.p2) + \
                distance(self.p1, self.p3) + distance(self.p3, self.p2))

    def isocele(self):
        if distance(self.p1, self.p2) == distance(self.p1, self.p3) or \
            distance(self.p1, self.p2) == distance(self.p2, self.p3) or \
            distance(self.p1, self.p3) == distance(self.p2, self.p3) :
            return "Ce triangle est isocèle !"
        else:
            return "Ce triange n'est isocèle !"


triangulo = triangle()
triangulo.construir_puntos()
print(triangulo.perimetre())
print(triangulo.isocele())
