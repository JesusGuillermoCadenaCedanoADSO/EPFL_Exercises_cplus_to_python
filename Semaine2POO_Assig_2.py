class auteur(object):
    def __init__(self,name='',awarded=False):
        self.name = name
        self.awarded = awarded

    def getnom(self):
        return self.name

    def getprix(self):
        return self.awarded

class oeuvre(object):
    def __init__(self,title='',autor = auteur(),language=''):
        self.title = title
        if not type(autor) is auteur:
            raise TypeError('A object auteur is required')
        else:
            self.auteur = autor
        self.language = language

    def getTitre(self):
        return self.title

    def getAuteur(self):
        return self.auteur

    def getLangue(self):
        return self.language

    def __str__(self):
        return self.title + ", " + self.auteur.getnom() + ", en " + self.language

    def __del__(self):
        print("L´oeuvre " + self.title + ", " + self.auteur.getnom() + \
               " en " + self.language + " n´est plus disponible")


class exemplaire(object):
    def __init__(self,obra):
        self.obra = obra
        print("Nouvel exemplaire de : " + self.obra.getTitre() +
              ", " + self.obra.auteur.getnom() + ", en " + self.obra.getLangue() )

    def copy(self):
        print("Copie d’un exemplaire de : " + self.obra.getTitre() +
              ", " + self.obra.getAuteur().getnom() + " en " + self.obra.getLangue())
        return exemplaire(oeuvre=self.obra)

    def getOeuvre(self):
        return self.obra

    def __str__(self):
        return "Exemplaire de : " + self.obra.getTitre() + \
                ", " + self.obra.getAuteur().getnom() + ", en " + self.obra.getLangue()

    def __del__(self):
        print("Un exemplaire de : " + self.obra.getTitre() + \
              ", " + self.obra.getAuteur().getnom() + ", en " + self.obra.getLangue() + \
              " a été jeté !")

class bibliotheque(object):
    def __init__(self, name='', exemplaires=[]):
        self.name = name
        self.exemplaires = exemplaires
        print("La bibliothèque " + name + " est ouverte !")

    def getNom(self):
        return self.name

    def stocker(self, ejemplares,n=1):
        for i in range(0, n):
            self.exemplaires.append(exemplaire(ejemplares))

    def lister_exemplaires(self,givenlanguage=''):
        if givenlanguage == '':
            for i in self.exemplaires:
                print(i)
        else:
            for i in self.exemplaires:
                if i.getOeuvre().getLangue() == givenlanguage:
                    print(i)

    def compter_exemplaires(self,givenbook):
        if not type(givenbook) is oeuvre:
            raise TypeError('A object oeuvre is required')
        else:
            cuenta = 0
            for i in self.exemplaires:
                if i.getOeuvre().getTitre() == givenbook.getTitre():
                    cuenta += 1
            return cuenta

    def afficher_Auteur(self, withprize = False):
        lista_ordenada = ''
        if withprize:
            count = 0
            for i in self.exemplaires:
                if i.getOeuvre().getAuteur().getprix():
                    count += 1
                    if count != len(self.exemplaires) and count !=1:
                        lista_ordenada += "{0:1s}\n".format(i.getOeuvre().getAuteur().getnom())
                    else:
                        lista_ordenada += "{0:1s}".format(i.getOeuvre().getAuteur().getnom())
        else:
            count = 0
            for i in self.exemplaires:
                count += 1
                if count != len(self.exemplaires) and count !=1:
                    lista_ordenada += "{0:1s}\n".format(i.getOeuvre().getAuteur().getnom())
                else:
                    lista_ordenada += "{0:1s}".format(i.getOeuvre().getAuteur().getnom())
        return lista_ordenada

    def __del__(self):
        print ("La bibliothèque " + self.name + " ferme se portes, et " + \
                "détruit ses exemplaires:")


a1 = auteur("Victor Hugo")
a2 = auteur("Alexandre Dumas")
a3 = auteur("Raymond Queneau", True)

o1 = oeuvre("Les Misérables", a1, "français")
o2 = oeuvre("L'Homme qui rit"          , a1, "français" )
o3 = oeuvre("Le Comte de Monte-Cristo" , a2, "français" )
o4 = oeuvre("Zazie dans le métro"      , a3, "français" )
o5 = oeuvre("The Count of Monte-Cristo", a2, "anglais" )

biblio = bibliotheque("municipale")
biblio.stocker(o1,2)
biblio.stocker(o2)
biblio.stocker(o3, 3)
biblio.stocker(o4)
biblio.stocker(o5)

print("La bibliothèque " + biblio.getNom() + " offre les exemplaires suivants :")
biblio.lister_exemplaires()
langue = "anglais"
print(" Les exemplaires en " + langue + " sont :")
biblio.lister_exemplaires(langue)

print(" Les auteurs à succès sont :")
print(biblio.afficher_Auteur(True))
print(" Il y a " + str(biblio.compter_exemplaires(o3)) + " exemplaires de " + o3.getTitre())

