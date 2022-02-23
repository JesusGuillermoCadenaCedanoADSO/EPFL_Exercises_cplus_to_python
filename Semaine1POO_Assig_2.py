class tirelire(object):
    def __init__(self,montant=0):
        self.montant = montant

    def getmontant(self):
        return self.montant

    def __str__(self):
        if self.montant == 0:
            return "Vous etes sans le sou"
        else:
            return "Vous avez :" + str(self.montant) + " euros dans votre tirelire."

    def secouer(self):
        if self.montant:
            return "Bing bing"

    def remplir(self, newadd):
        if newadd>0:
            self.montant += newadd

    def vider(self):
        self.montant = 0

    def puiser(self, newremove):
        if self.montant > 0:
            if newremove > self.montant:
                self.montant = 0
            else:
                self.montant -= newremove

    def montant_suffisant(self, budget):
        if budget >= 0:
            if self.montant >= budget:
                return self.montant - budget
            else:
                return budget - self.montant
        else:
            return self.montant

piggy = tirelire()
piggy.vider()
if piggy.secouer():
    print(piggy.secouer())
print(piggy)
piggy.puiser(20)
if piggy.secouer():
    print(piggy.secouer())
print(piggy)

piggy.remplir(550.0)
if piggy.secouer():
    print(piggy.secouer())
print(piggy)

piggy.puiser(10.0)
piggy.puiser(5.0)
print(piggy)

donnerbudget =  1000
print("\nDonnez le budget de vos vacances : " + str(donnerbudget))


if piggy.getmontant() >= donnerbudget or donnerbudget < 0:
    print("Vous êtes assez riche pour partir en vacances !")
    print("Il vous restera " + str(piggy.montant_suffisant(donnerbudget)) +
          " euros à la rentrée.")
    piggy.puiser(donnerbudget)

elif piggy.getmontant() < donnerbudget:
    print("Il vous manque " + str(piggy.montant_suffisant(donnerbudget)) +
          " pour partir en vacances !")

