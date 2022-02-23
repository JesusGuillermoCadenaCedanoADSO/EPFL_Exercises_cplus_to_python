class couleur(object):
    def __init__(self, c):
        self.__c = c
        self.choix = {'ROUGE': 'rouge', 'VERT': 'vert',
                      'BLEU': 'bleu', 'BLANC': 'blanc',
                      'NOIR': 'noir'}

    @property
    def get_c(self):
        return self.__c

    def affiche(self, feminin=False):
        color = self.choix[self.get_c]
        if feminin:
            if color == "rouge":
                return color
            if color == "blanc":
                return color + 'he'
            return color + 'e'
        else:
            return color

    def __del__(self):
        pass


class carte(object):
    def __init__(self, cost=0):
        self.__cost = cost

    @property
    def get_cost(self):
        return self.__cost

    def afficher(self, arg):
        return arg + " de coût " + str(self.get_cost)

    def __del__(self):
        pass


class terrain(carte):
    def __init__(self, cx):
        self.__couleur_terrain = couleur(cx)
        print("Un nouveau terrain.")

    @property
    def get_couleur_terrain(self):
        return self.__couleur_terrain

    def afficher(self):
        return "Un terrain " + self.get_couleur_terrain.affiche() + "."

    def __del__(self):
        pass


class creature(carte):
    def __init__(self, cost, nom, attaque, defense):
        carte.__init__(self, cost)
        self.__nom = nom
        self.__attaque = attaque
        self.__defense = defense
        print("Une nouvelle créature.")

    @property
    def get_nom(self):
        return self.__nom

    @property
    def get_attaque(self):
        return self.__attaque

    @property
    def get_defense(self):
        return self.__defense

    def __del__(self):
        pass

    def afficher(self):
        texte = "Une créature " + self.get_nom + " " + str(self.get_attaque) + \
                "/" + str(self.get_defense) + " "
        return carte.afficher(self, texte)


class sortilege(carte):
    def __init__(self, cost, nom, description):
        carte.__init__(self, cost)
        self.__nom = nom
        self.__description = description
        print("Un sortilège de plus.")

    @property
    def get_nom(self):
        return self.__nom

    @property
    def get_description(self):
        return self.__description

    def __del__(self):
        pass

    def afficher(self):
        texte = "Un sortilège " + self.get_nom + " "
        return carte.afficher(self, texte)


class creatureterrain(creature, terrain):
    def __init__(self, cost, nom, attaque, defense, couleurx):
        carte.__init__(self, cost)
        creature.__init__(self, cost, nom, attaque, defense)
        terrain.__init__(self, couleurx)
        print("Houla, une créature/terrain.")

    def __del__(self):
        pass

    def afficher(self):
        texte = "Une créature/terrain " + self.get_couleur_terrain.affiche(True) + " " + \
                self.get_nom + " " + str(self.get_attaque) + \
                "/" + str(self.get_defense) + " "
        return carte.afficher(self, texte)


class jeu(object):
    def __init__(self):
        self.contenu = []
        print("On change de main")

    def ajoute(self, new_carte):
        self.contenu.append(new_carte)

    def jette(self):
        print("Je jette ma main.")
        for i in self.contenu:
            i.__del__
        self.contenu.clear()

    def __str__(self):
        reponse = ''
        for i in range(0, len(self.contenu)):
            if i != len(self.contenu)-1:
                reponse += '+ ' + self.contenu[i].afficher() + "\n"
            else:
                reponse += '+ ' + self.contenu[i].afficher()
        return reponse


mamain = jeu()
new_terrain = terrain("BLEU")
new_creature = creature(6, "Golem", 4, 6)
new_sortilege = sortilege(1, "Croissance Gigantesque",
                          "La créature ciblée gagne +3/+3 jusqu'à  la fin du tour")
new_creatureterrain = creatureterrain(2, "Ondine", 1, 1, "BLEU")


mamain.ajoute(new_terrain)
mamain.ajoute(new_creature)
mamain.ajoute(new_sortilege)
mamain.ajoute(new_creatureterrain)
print("LC , j'ai en stock : ")
print(mamain)
mamain.jette()

print(new_sortilege.get_description)

