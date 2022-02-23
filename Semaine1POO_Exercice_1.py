import math

class cercle(object):

    def __init__(self, rayon=0, punto=[0, 0]):
        self.rayon = rayon
        self.punto = punto

    def getpunto(self):
        return self.punto

    def setpunto(self, newpunto):
        self.punto = newpunto

    def getrayon(self):
        return self.rayon

    def setrayon(self, newrayon):
        if newrayon < 0:
            newrayon = 0
        self.rayon = newrayon

    def surface(self):
        return (math.pi * (self.rayon)**2)

    def estinterieur(self,newpunto):
        return (self.punto[0] - newpunto[0])**2 + (self.punto[1] - newpunto[1])**2 <= self.rayon**2

def dans(oui):
    if oui:
        return " dans "
    else:
        return " hors de "

def test(punto_prueba, circulo, segundo_circulo):
    return "position du point " + '({0}'.format(punto_prueba[0]) + "," +\
           ' {0})'.format(punto_prueba[1]) + ":" +  dans(circulo.estinterieur(punto_prueba)) + \
           "C1 et" + dans(segundo_circulo.estinterieur(punto_prueba)) +   " C2."

circulo_1 = cercle()
circulo_2 = cercle()
point_1 = [1, 2]
point_2 = [-2, 1]

circulo_1.setpunto(point_1)
circulo_1.setrayon(math.sqrt(5))

circulo_2.setpunto(point_2)
circulo_2.setrayon(2.25)

area_circulo_1 = circulo_1.surface()
area_circulo_2 = circulo_2.surface()

print("Surface de C1 : " + "{0:.3f}".format((area_circulo_1)))
print("Surface de C2 : " + "{0:.4f}".format((area_circulo_2)))

test_point_1 = [0, 0]
test_point_2 = [1, 1]

print(test(test_point_1,circulo_1,circulo_2))
print(test(test_point_2,circulo_1,circulo_2))
