from abc import ABC, abstractmethod


class figure(ABC):
    @abstractmethod
    def affiche(self):
        pass

    @abstractmethod
    def copie(self):
        pass

    @abstractmethod
    def __del__(self):
        print("Une figure de moins.")


class cercle(figure):
    def __init__(self, rayon=0):
        self.rayon = rayon
        print("Construction d'un cercle de rayon " + str(self.rayon))

    def copie(self):
        print("Copie d'un cercle de rayon " + str(self.rayon))
        return cercle(rayon=self.rayon)

    def __del__(self):
        print("Destruction d'un cercle")

    def affiche(self):
        return "Un cercle de rayon " + str(self.rayon)


class carre(figure):
    def __init__(self, cote=0):
        self.cote = cote
        print("Construction d'un carré de coté " + str(self.cote))

    def copie(self):
        print("Copie d'un carré de coté " + str(self.cote))
        return carre(cote=self.cote)

    def __del__(self):
        print("Destruction d'un carré")

    def affiche(self):
        return "Un carré de coté " + str(self.cote)


class triangle(figure):
    def __init__(self, b=0, h=0):
        self.b = b
        self.h = h
        print("Construction d'un triangle " + str(self.b) + " x " + str(self.h))

    def copie(self):
        print("Copie d'un triangle " + str(self.b) + " x " + str(self.h))
        return triangle(b=self.b, h=self.h)

    def __del__(self):
        print("Destruction d'un triangle")

    def affiche(self):
        return "Un triangle " + str(self.b) + " x " + str(self.h)


class dessin(object):
    def __init__(self):
        self.figures = []

    def ajoutefigure(self, new_figure):
        self.figures.append(new_figure)

    def affiche(self):
        print("Je contiens :")
        for i in range(0, len(self.figures)):
            print(self.figures[i].affiche())

    def __del__(self):
        print("\nLe dessins s'efface...")
        self.figures.clear()


def uncercledeplus(dessin_new):
    dessin_new.ajoutefigure(cercle(1))
    print("\nAffichage de new_dessin: \n")
    dessin_new.affiche()


dessin_1 = dessin()
dessin_1.ajoutefigure(triangle(3, 4))
dessin_1.ajoutefigure(carre(2))
dessin_1.ajoutefigure(triangle(6, 1))
dessin_1.ajoutefigure(cercle(12))

print("\nAffichage du dessin : ")
dessin_1.affiche()

uncercledeplus(dessin_1)
