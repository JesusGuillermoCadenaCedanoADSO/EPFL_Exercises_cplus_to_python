class souris(object):
    def __init__(self, poids = 0.0, couleur = 'no one', age = 0,
                 esperance_vie = 36, clonee = False):
        self.poids = poids
        self.couleur = couleur
        self.age = age
        self.clonee = clonee
        self.esperance_vie = esperance_vie

        if self.clonee:
            print("Clonage d’une souris !")
        else:
            print("Une nouvelle souris !")

    def copy(self):
        return souris(poids=self.poids, couleur=self.couleur, age=self.age,
                      esperance_vie=self.esperance_vie*4/5, clonee=True)

    def __del__(self):
        print('Fin d’une souris...')

    def __str__(self):
        if self.clonee:
            return "Une souris " + self.couleur + ", clonee, de " \
                   + str(int(self.age) )+ " mois et pesant " + str(int(self.poids)) + " grammes" +\
                    " et une esperance_vie " + str(self.esperance_vie)
        else:
            return "Une souris " + self.couleur + " de " \
                   + str(int(self.age)) + " mois et pesant " + str(int(self.poids)) + " grammes" +\
                    " et une esperance_vie " + str(self.esperance_vie)

    def vieillir(self,y = 0):
        self.age += 1 - y
        if self.clonee:
            if self.age > self.esperance_vie/2:
                self.couleur = 'verte'

    def evolue(self):
        self.age = self.esperance_vie
        self.vieillir(1)



s1 = souris(50.0, "blanche", 2)
s2 = souris(45.0, "grise")
s3 = s2.copy()
print(s1)
print(s2)
print(s3)

s1.evolue()
s2.evolue()
s3.evolue()
s3.vieillir()
print(s1)
print(s2)
print(s3)
print(s2)

