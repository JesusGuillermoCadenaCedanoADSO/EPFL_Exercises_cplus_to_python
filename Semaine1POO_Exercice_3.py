class point3d(object):
    def __init__(self,pointname='',c1=0.0,c2=0.0,c3=0.0):
        self.pointname = pointname
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3

    def init(self,nombre,newc1,newc2,newc3):
        self.pointname = nombre
        self.c1 = newc1
        self.c2 = newc2
        self.c3 = newc3

    def compare(self,newpoint):
        resultado = "Le point " + self.pointname + " est "
        if self.c1==newpoint.c1 and self.c2==newpoint.c2 and \
                self.c3==newpoint.c3:
            resultado += "identique au"
        else:
            resultado += "différent du "
        resultado += newpoint.pointname + "."
        return resultado

    def __str__(self):
        return str(self.pointname) + ": (" + str(self.c1) + ", " \
               + str(+self.c2) + ", " + str(self.c3) + ")"

point1 = point3d()
point2 = point3d()
point3 = point3d()

point1.init("punto 1,",1.0,2.0,-0.1)
point2.init("punto 2",2.6,3.5,4.1)

point3.init("punto 3",point1.c1,point1.c2,point1.c3)

print(point1)
print(point2)


print(point1)
print(point3)
#point3.init("punto 3",1,2,2)
print(point1)
print(point3)
print(point1.compare(point3))
