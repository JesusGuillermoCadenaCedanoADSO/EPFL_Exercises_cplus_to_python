class livre(object):
    def __init__(self, titre, auteur, nombre_de_pages, bestseller=False):
        self.titre = titre
        self.auteur = auteur
        self.nombre_de_pages = nombre_de_pages
        self.bestseller = bestseller

    def calculer_prix(self):
        if self.bestseller:
            return self.nombre_de_pages * 0.3 + 50
        else:
            return self.nombre_de_pages * 0.3

    def is_bestseller(self):
        if self.bestseller:
            return "oui"
        else:
            return "non"

    def __del__(self):
        pass

    def affiche(self):
        return "titre : " + self.titre + "\nauteur : " + self.auteur + \
               "\nnombre de pages : " + str(self.nombre_de_pages) + \
               "\nbestseller : " + self.is_bestseller() + "\nprix : " + \
               "{0:1.1f}".format((self.calculer_prix())) + "\n"


class roman(livre):
    def __init__(self, titre, auteur, nombre_de_pages,
                 bestseller=False, biographie=False):
        livre.__init__(self, titre, auteur, nombre_de_pages, bestseller)
        self.biographie = biographie

    def is_biographie(self):
        if self.biographie:
            return "Ce roman est une biographie"
        else:
            return "Ce roman n'est pas une biographie"

    def __del__(self):
        pass

    def affiche(self):
        return livre.affiche(self) + roman.is_biographie(self) + "\n"


class policier(roman):
    def __init__(self, titre, auteur, nombre_de_pages, bestseller=False, biographie=False):
        roman.__init__(self, titre, auteur, nombre_de_pages, bestseller, biographie)

    def __del__(self):
        pass

    def calculer_prix(self):
        prix = livre.calculer_prix(self) - 10
        if prix < 0:
            return 1
        return prix

    #def affiche(self):
    #    return roman.affiche(self)


class beaulivre(livre):
    #def __init__(self, titre, auteur, nombre_de_pages, bestseller=False):
    #    livre.__init__(self, titre, auteur, nombre_de_pages, bestseller)

    def __del__(self):
        pass

    def calculer_prix(self):
        return livre.calculer_prix(self) + 30

    #def affiche(self):
    #    return livre.affiche(self) +\
    #           "\nprix : " + "{0:1.1f}".format((self.calculer_prix()))


class librairie(object):
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, new_livre):
        self.livres.append(new_livre)

    def afficher(self):
        for i in self.livres:
            print(i.affiche())

    def vider_stock(self):
        for i in self.livres:
            i.__del__
        self.livres.clear()


libros = ['' for x in range(5)]
libros[0] = policier("Le chien des Baskerville", "A.C.Doyle", 221, False, False)
libros[1] = policier("Le Parrain ", "A.Cuso", 367, True, False)
libros[2] = roman("Le baron perche", "I. Calvino", 283, False, False)
libros[3] = roman("Memoires de Geronimo", "S.M. Barrett", 173, False, True)
libros[4] = beaulivre("Fleuves d'Europe", "C. Osborne", 150, False)

new_librairie = librairie()

for i in range(0, len(libros)):
    new_librairie.ajouter_livre(libros[i])

new_librairie.afficher()
new_librairie.vider_stock()


"""
__mro__ :Esta función nos devuelve una tupla con el orden de búsqueda de los métodos.
Como era de esperar se empieza en la propia clase
y se va subiendo hasta la clase padre, de izquierda a derecha.
"""
print(policier.__mro__)

#libro = beaulivre("Fleuves d'Europe", "C. Osborne",
#150, False)

#print(libro.affiche())
