class employe(object):
    def __init__(self, prenom, nom, age, date_entree):
        self.__prenom = prenom
        self.__nom = nom
        self.__age = age
        self.__date_entree = date_entree

    @property
    def get_nom(self):
        return self.__nom

    @property
    def get_prenom(self):
        return self.__prenom

    @property
    def get_age(self):
        return self.__age

    @property
    def get_date_entree(self):
        return self.__date_entree

    def calculer_salaire(self):
        pass

    def get_employe(self):
        return "L'employé " + self.get_prenom + " " + self.get_nom

    def __del__(self):
        pass


class commercial(employe):
    def __init__(self, prenom, nom, age, date_entree, chiffre_affaire):
        employe.__init__(self, prenom, nom, age, date_entree)
        self.__chiffre_affaire = chiffre_affaire

    @property
    def get_chiffre(self):
        return self.__chiffre_affaire

    def __del__(self):
        pass


class vendeur(commercial):

    def calculer_salaire(self):
        return self.get_chiffre * 0.2 + 400

    def __del__(self):
        pass

    def get_employe(self):
        return "Le vendeur " + self.get_prenom + " " + self.get_nom


class representant(commercial):

    def calculer_salaire(self):
        return self.get_chiffre * 0.2 + 800

    def __del__(self):
        pass

    def get_employe(self):
        return "Le représentant " + self.get_prenom + " " + self.get_nom


class technicien(employe):
    def __init__(self, prenom, nom, age, date_entree, unites):
        employe.__init__(self, prenom, nom, age, date_entree)
        self.__unites = unites

    @property
    def get_unites(self):
        return self.__unites

    def calculer_salaire(self):
        return self.get_unites * 5

    def get_employe(self):
        return "Le technicien " + self.get_prenom + " " + self.get_nom


class manutentionnaire(employe):
    def __init__(self, prenom, nom, age, date_entree, heures):
        employe.__init__(self, prenom, nom, age, date_entree)
        self.__heures = heures

    @property
    def get_heures(self):
        return self.__heures

    def calculer_salaire(self):
        return self.get_heures * 65

    def get_employe(self):
        return "Le manut. " + self.get_prenom + " " + self.get_nom


class arisque(object):
    def __init__(self, prime=100):
        self.__prime = prime

    @property
    def getprime(self):
        return self.__prime

    def __del__(self):
        pass


class technarisque(technicien, arisque):
    def __init__(self, prenom, nom, age, date_entree, unites, prime):
        technicien.__init__(self, prenom, nom, age, date_entree, unites)
        arisque.__init__(self, prime)

    def calculer_salaire(self):
        return technicien.calculer_salaire(self) + self.getprime


class manutarisque(manutentionnaire, arisque):
    def __init__(self, prenom, nom, age, date_entree, heures, prime):
        manutentionnaire.__init__(self, prenom, nom, age, date_entree, heures)
        arisque.__init__(self, prime)

    def calculer_salaire(self):
        return manutentionnaire.calculer_salaire(self) + self.getprime


class personel(object):
    def __init__(self):
        self.employes = []

    def ajouter_employe(self, new_employe):
        self.employes.append(new_employe)

    def afficher_salaires(self):
        for i in self.employes:
            print(i.get_employe() + " gagne " +
                  "{0:0.0f}".format(i.calculer_salaire()) + " francs.")

    def salaire_moyen(self):
        sum_salaire = 0
        for i in self.employes:
            sum_salaire += i.calculer_salaire()
        if len(self.employes):
            return sum_salaire/len(self.employes)

    def licencie(self):
        for i in self.employes:
            i.__del__
        self.employes.clear()


p = personel()

employes = ['' for x in range(6)]

employes[0] = vendeur("Pierre", "Business", 45, "1995", 30000)
employes[1] = representant("Léon", "Vendtout", 25, "2001", 20000)
employes[2] = technicien("Yves", "Bosseur", 28, "1998", 1000)
employes[3] = manutentionnaire("Jeanne", "Stocketout", 32, "1998", 45)
employes[4] = technarisque("Jean", "Flippe", 28, "2000", 1000, 200)
employes[5] = manutarisque("Al", "Abordage", 30, "2001", 45, 120)

for i in employes:
    p.ajouter_employe(i)

p.afficher_salaires()
print("Le salaire moyen dans l'entreprise est de "
      + "{0:0.2f}".format(p.salaire_moyen()) + " francs.")

p.licencie()
