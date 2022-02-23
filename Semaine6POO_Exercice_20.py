class animal(object):
    def __init__(self, nom, continent):
        self.__nom = nom
        self.__continent = continent
        print("Nouvel animal protégé")

    @property
    def get_nom(self):
        return self.__nom

    @property
    def get_continent(self):
        return self.__continent

    def affiche(self):
        return "Je suis un " + self.get_nom + \
               " et je vis en " + self.get_continent + "."

    def __del__(self):
        print("Je ne suis plus protégé")


class endanger(object):
    def __init__(self, nombre):
        self.__nombre = nombre
        print("Nouvel animal en danger")

    @property
    def get_nombre(self):
        return self.__nombre

    def affiche(self):
        return "Il ne reste que " + str(self.get_nombre) + \
               " de mes congénères sur terre."

    def __del__(self):
        print("ouf! je ne suis plus en danger")


class gadget(object):
    def __init__(self, nom_gadget, prix):
        self.__nom_gadget = nom_gadget
        self.__prix = prix
        print("Nouveau gadget")

    @property
    def get_nom_gadget(self):
        return self.__nom_gadget

    @property
    def get_prix(self):
        return self.__prix

    def affiche(self):
        return "Mon nom est " + self.get_nom_gadget + "."

    def affiche_prix(self):
        return "Achetez-moi pour " + "{0:1.0f}".format(self.get_prix) + \
                " francs et vous contribuerez à me sauver !"

    def __del__(self):
        print("Je ne suis plus un gadget")


class peluche(animal, endanger, gadget):
    def __init__(self, nom, nom_gadget, continent, nombre, prix):
        animal.__init__(self, nom, continent)
        endanger.__init__(self, nombre)
        gadget.__init__(self, nom_gadget, prix)
        print("Nouvelle peluche")

    def __del__(self):
        print("Je ne suis plus une peluche")
        gadget.__del__(self)
        endanger.__del__(self)
        animal.__del__(self)

    def etiquette(self):
        return "Hello,\n" + gadget.affiche(self) + "\n" + \
                animal.affiche(self) + "\n" + endanger.affiche(self) + "\n" + \
                gadget.affiche_prix(self)


animals = ['' for i in range(3)]

animals[0] = peluche("Panda", "Ming", "Asie", 200, 20.0)
animals[1] = peluche("Cobra", "ssss", "Asie", 500, 10.0)
animals[2] = peluche("Toucan", "Bello", "Amérique du Sud", 1000, 15.0)

for i in animals:
    print(i.etiquette(), "\n")

