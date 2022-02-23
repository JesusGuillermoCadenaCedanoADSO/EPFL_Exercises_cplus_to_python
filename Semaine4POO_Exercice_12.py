from datetime import date


class Vehicule(object):

    def __init__(self, marque, date_achat, prix_achat, prix_courant=0):
        self.marque = marque
        self.date_achat = date_achat
        self.prix_achat = prix_achat
        self.prix_courant = prix_courant

    def calculer_prix(self, pourcentage=0.01, date=date.today().year):
        decote = pourcentage * (date - self.date_achat)
        self.prix_courant = max((1 - decote) * self.prix_achat, 0)

    def __str__(self):
        return "marque : " + self.marque + ", " + "data d'achat : " + \
               str(self.date_achat) + ", " + " prix d'achat : " + str(self.prix_achat) + \
               ", " + "prix actuel : " + str(self.prix_courant) + "\n"


class voiture(Vehicule):
    def __init__(self, marque, date_achat, prix_achat, cylindree, portes,
                 puissance, kilometrage):
        Vehicule.__init__(self, marque, date_achat, prix_achat)
        self.cylindree = cylindree
        self.portes = portes
        self.puissance = puissance
        self.kilometrage = kilometrage

    def calculer_prix(self, pourcentage, date):
        decote = pourcentage * (date - self.date_achat)
        decote += 0.05 * (self.kilometrage / 10000)
        if self.marque == "Fiat" or self.marque == "Renault":
            decote += 0.1
        elif self.marque == "Ferrari" or self.marque == "Porsche":
            decote -= 0.2
        self.prix_courant = max((1 - decote) * self.prix_achat, 0)

    def __str__(self):
        return "----Voiture----\n" + Vehicule.__str__(self) + str(self.cylindree) + \
               " litres, " + str(self.portes) + " portes, " + str(self.puissance) + \
               " CV, " + str(self.kilometrage) + " km."


class avion(Vehicule):
    def __init__(self, marque, date_achat, prix_achat, motor, heures_vol):
        Vehicule.__init__(self, marque, date_achat, prix_achat)
        self.motor = motor
        self.heures_vol = heures_vol

    def calculer_prix(self):
        if self.motor == "HELICES":
            tranche = 100
        elif self.motor == "REACTION":
            tranche = 1000
        prix = self.prix_achat * (1 - 0.1 * self.heures_vol / tranche)
        self.prix_courant = max(prix, 0)

    def __str__(self):
        if self.motor == "HELICES":
            motor = "hélices"
        else:
            motor = "réaction"
        return "----Avion à " + motor + " ----" + "\n" + \
               Vehicule.__str__(self) + str(self.heures_vol) + " heures de vol. "


voitures = []
avions = []
anee = 2015

voitures.insert(0, voiture("Peugeot", 1998, 147325.79, 2.5, 5, 180.0, 12000))
voitures.insert(1, voiture("Porsche", 1985, 250000.00, 6.5, 2, 280.0, 81320))
voitures.insert(2, voiture("Fiat", 2001, 7327.30, 1.6, 3, 65.0, 3000))

avions.insert(0, avion("Cessna", 1972, 1230673.90, "HELICES", 250))
avions.insert(1, avion("Nain Connu", 1992, 4321098.00, "REACTION", 1300))

for i in range(0, len(voitures)):
    voitures[i].calculer_prix(0.02, anee)
    print(voitures[i])

for i in range(0, len(avions)):
    avions[i].calculer_prix()
    print(avions[i])
