class patient(object):
    def __init__(self, masa=0, altura=0):
        self.masa = masa
        self.altura = altura

    def init(self,newmasa,newaltura):
        if newmasa > 0 and newaltura> 0:
            self.masa = newmasa
            self.altura = newaltura
        else:
            self.masa = 0
            self.altura = 0

    def getmasa(self):
        return self.masa

    def getaltura(self):
        return self.altura

    def imc(self):
        if self.altura ==0:
            return 0
        else:
            return self.masa/(self.altura)**2

    def __str__(self):
        return "Patient : " + str(self.masa) + " kg pour " + str(self.altura) + " m\n"


quidam = patient()
poids = float(input("Entrez un poids (kg)"))
taille = float(input("et une taille (m)"))

quidam.init(poids, taille)

print(quidam)

print("IMC : " + str(quidam.imc()))

