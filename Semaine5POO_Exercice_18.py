from enum import Enum
from abc import ABC, abstractmethod


class couleur(Enum):
    VIDE = 0
    ROUGE = 1
    JAUNE = 2


class jeu(object):
    def __init__(self, taille=8):
        self.taille = taille
        self.grille = [[couleur.VIDE for x in range(self.taille)] for y in range(self.taille)]
        """
        self.grille = [[couleur.ROUGE, couleur.JAUNE, couleur.ROUGE, couleur.JAUNE, couleur.ROUGE,
                        couleur.JAUNE, couleur.ROUGE, couleur.JAUNE],
                       [couleur.ROUGE, couleur.JAUNE, couleur.ROUGE, couleur.JAUNE, couleur.ROUGE,
                        couleur.JAUNE, couleur.ROUGE, couleur.ROUGE],
                       [couleur.ROUGE, couleur.ROUGE, couleur.JAUNE, couleur.ROUGE, couleur.JAUNE,
                        couleur.ROUGE, couleur.JAUNE, couleur.ROUGE],
                       [couleur.JAUNE, couleur.JAUNE, couleur.ROUGE, couleur.ROUGE, couleur.ROUGE,
                        couleur.JAUNE, couleur.ROUGE, couleur.JAUNE],
                       [couleur.ROUGE, couleur.JAUNE, couleur.ROUGE, couleur.JAUNE, couleur.JAUNE,
                        couleur.JAUNE, couleur.ROUGE, couleur.JAUNE],
                       [couleur.ROUGE, couleur.JAUNE, couleur.ROUGE, couleur.ROUGE, couleur.ROUGE,
                        couleur.JAUNE, couleur.ROUGE, couleur.ROUGE],
                       [couleur.JAUNE, couleur.ROUGE, couleur.JAUNE, couleur.ROUGE, couleur.JAUNE,
                        couleur.ROUGE, couleur.JAUNE, couleur.ROUGE],
                       [couleur.JAUNE, couleur.JAUNE, couleur.ROUGE, couleur.JAUNE, couleur.ROUGE,
                        couleur.ROUGE, couleur.VIDE, couleur.VIDE]]
        """

        self.vainqueur = couleur.VIDE

    def get_taille(self):
        return len(self.grille)

    def jouer(self, i, c):
        if c == couleur.VIDE:
            return False
        if i >= self.get_taille():
            return False
        j = 0
        while j < self.get_taille() and self.grille[i][j] != couleur.VIDE:
            j += 1
        if j >= self.get_taille():
            return False
        self.grille[i][j] = c
        return True

    def compte(self, c, i, j, di, dj):
        n = 1
        if di != 0 or dj != 0:
            i += di
            j += dj
            while i < self.get_taille() and j < self.get_taille() and self.grille[i][j] == c:
                n += 1
                i += di
                j += dj
        return n

    def gagnant(self):
        for i in range(0, self.get_taille() - 1):
            for j in range(0, self.get_taille() - 1):
                if self.grille[i][j] != couleur.VIDE:
                    self.vainqueur = self.grille[i][j]
                    di = 0
                    while di <= 1:
                        dj = -1
                        while dj <= 1:
                            if self.compte(self.vainqueur, i, j, di, dj) >= 4:
                                #self.grille[i][j]="?"
                                return self.vainqueur
                            dj += 1
                        di += 1
        return couleur.VIDE

    def fini(self):
        resultat = self.gagnant()
        if resultat == couleur.VIDE:
            for ligne in range(0, self.get_taille()):
                for kase in range(0, len(self.grille[ligne])):
                    if self.grille[ligne][kase] == couleur.VIDE:
                        return False
            self.vainqueur = couleur.VIDE
        return True

    def afficher(self):
        if self.get_taille() > 0:
            j = self.get_taille()
            while j != 0:
                j -= 1
                result = ''
                for i in range(0, self.get_taille()):
                    if self.grille[i][j] == couleur.VIDE:
                        result += str(" ")
                    elif self.grille[i][j] == couleur.ROUGE:
                        result += "#"
                    elif self.grille[i][j] == couleur.JAUNE:
                        result += "O"
                    else:
                        result += self.grille[i][j]
                print(result)

            result_1 = ""
            result_2 = ""
            for i in range(0, self.get_taille()):
                result_1 += "-"
            print(result_1)
            for i in range(1, self.get_taille()+1):
                result_2 += str(i)
            print(result_2)
            print("\n")


class joueur(ABC):
    def __init__(self, un_nom, une_couleur=couleur.ROUGE):
        self.un_nom = un_nom
        self.une_couleur = une_couleur

    def get_nom(self):
        return self.un_nom

    def get_couleur(self):
        return self.une_couleur

    @abstractmethod
    def jouer(self, jeu_1):
        return 0

    def __del__(self):
        pass


class partie(object):
    def __init__(self, joueur_1, joueur_2):
        self.joeur_1 = joueur_1
        self.joeur_2 = joueur_2
        self.joueurs = [joueur_1, joueur_2]
        self.jeu_1 = jeu()

    def lancer(self):
        tour = 0
        while not self.jeu_1.fini():
            self.joueurs[tour].jouer(self.jeu_1)
            tour = 1 - tour
            self.jeu_1.afficher()
            #print("grille:\n", self.jeu_1.grille)
        print("La partie est finie.")
        self.jeu_1.afficher()
        if self.jeu_1.vainqueur == self.joueurs[0].get_couleur():
            print("Le vainqueur est " + self.joueurs[0].get_nom())
        elif self.jeu_1.vainqueur == self.joueurs[1].get_couleur():
            print("Le vainqueur est " + self.joueurs[1].get_nom())
        else:
            print("Match nul.")

    def vider(self):
        self.joueurs.clear()


class humain(joueur):
    def __init__(self, un_nom="quidam", une_couleur=couleur.JAUNE):
        joueur.__init__(self, un_nom, une_couleur)
        #self.un_nom = input("Entrez votre nom : ")
        self.un_nom = un_nom

    def jouer(self, jeu_1):
        #jeu_1.afficher()
        valide = False
        while not valide:
            print("Joueur " + self.un_nom + " , entrez un numéro de colonne\n" +
                  " (entre 1 et " + str(jeu_1.get_taille()) + ") : ")
            lu = int(input())
            lu -= 1
            valide = jeu_1.jouer(lu, self.une_couleur)
            if not valide:
                print("-> Coup NON valide.")


class ordi(joueur):
    def __init__(self, un_nom="Le programme", une_couleur=couleur.ROUGE):
        joueur.__init__(self, un_nom, une_couleur)

    def jouer(self, jeu_1):
        for i in range(0, jeu_1.get_taille()):
            if jeu_1.jouer(i, self.une_couleur):
                print(self.un_nom + " a joué en " + str(i + 1))
                return



#ordi_1 = ordi()
ordi_1 = humain("X", couleur.ROUGE)
humain_1 = humain()
partie_1 = partie(ordi_1, humain_1)
partie_1.lancer()
partie_1.vider()
