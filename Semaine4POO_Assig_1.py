class timbre(object):
    def __init__(self, code, annee, pays="Suisse", valeur_faciale=1.0):
        self.code = code
        self.annee = annee
        self.pays = pays
        self.valeur_faciale = valeur_faciale
        self.anee_courante = 2016

    def get_nom(self):
        return self.code

    def get_annee(self):
        return self.annee

    def get_pays(self):
        return self.pays

    def get_valeur_faciale(self):
        return self.valeur_faciale

    def vente(self):
        if self.age() < 5:
            return self.valeur_faciale
        else:
            return self.valeur_faciale * 2.5 * self.age()

    def age(self):
        return self.anee_courante - self.annee

    def afficher(self):
        return " de nom " + self.get_nom() + " datant de " + str(self.get_annee()) \
               + " (provenance " + self.get_pays() + ")" + \
               " ayant pour valeur faciale " + str(self.get_valeur_faciale()) + " francs"

    def __str__(self):
        return "Timbre de nom " + self.get_nom() + " datant de " + str(self.get_annee()) + \
            " (provenance " + self.get_pays() + ")" + " ayant pour valeur faciale " + \
            str(self.get_valeur_faciale()) + " francs"


class rare(timbre):
    def __init__(self, code, annee, pays="Suisse", valeur_faciale=1.0, copies=100):
        timbre.__init__(self, code, annee, pays, valeur_faciale)
        self.copies = copies
        self.prix_base_tres_rare = 600
        self.prix_base_rare = 400
        self.prix_base_peu_rare = 50

    def get_exemplaires(self):
        return self.copies

    def vente(self):
        if self.get_exemplaires() < 100:
            return self.prix_base_tres_rare * (self.age()/10)
        elif 100 < self.get_exemplaires() < 1000:
            return self.prix_base_rare * (self.age()/10)
        else:
            return self.prix_base_peu_rare * (self.age()/10)

    def __str__(self):
        return "Timbre rare " + "(" + str(self.get_exemplaires()) + " ex.)" \
               + timbre.afficher(self)


class commemoratif(timbre):
    def __init__(self, code, annee, pays="Suisse", valeur_faciale=1.0):
        timbre.__init__(self, code, annee, pays, valeur_faciale)

    def vente(self):
        return timbre.vente(self) * 2

    def __str__(self):
        return "Timbre commémoratif" + timbre.afficher(self)


t1 = rare("Guarana-4574", 1960, "Mexique", 0.2, 98)
t2 = rare("Yoddle-201", 1916, "Suisse", 0.8,  3)
t3 = commemoratif("700eme-501", 2002, "Suisse", 1.5)
t4 = timbre("Setchuan-302", 2004, "Chine", 0.2)

print(t1)
print("Prix vente : ", "{:.0f}".format(t1.vente()), " francs")
print(t2)
print("Prix vente : ", "{:n}".format(t2.vente()), " francs")
print(t3)
print("Prix vente : ", "{:n}".format(t3.vente()), " francs")
print(t4)
print("Prix vente : ", "{:.0f}".format(t4.vente()), " francs")



