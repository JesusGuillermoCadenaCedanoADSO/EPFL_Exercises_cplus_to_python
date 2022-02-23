import math
class flacon(object):
    def __init__(self, nom, volume, ph):
        self.nom = nom
        self.volume = volume
        self.ph = ph

    def etiquette(self):
        return self.nom + " : " + str(self.volume) + " ml, " + "ph " + str(self.ph)

    def __add__(self, other):
        new_nom = self.nom + " + " + other.nom
        new_volume = self.volume + other.volume
        new_ph = round(-math.log(((self.volume*10**(-self.ph) +
                             other.volume*10**(-other.ph))/new_volume), 10), 3)
        new_flacon = flacon(new_nom, new_volume, new_ph)

        return new_flacon

    def __iadd__(self, other):
        return flacon(nom=self.nom,volume=self.volume,ph=self.ph) + other

    @staticmethod
    def afficher_melange(f1, f2):
        print("Si je mélange\n",'"', f1.__str__, '"', "\navec\n", '"', f2.__str__, '"',
              "\nj'obtiens :\n",'"', f1.__add__(f2),'"\n', end='', sep='')

    def __str__(self):
        return self.etiquette()

flacon1 = flacon("Eau", 600, 7)
flacon2 = flacon("Acide chlorhydrique", 500.0, 2.0)
flacon3 = flacon("Acide perchlorique",  800.0, 1.5)

flacon.afficher_melange(flacon1,flacon2)
flacon.afficher_melange(flacon2,flacon3)

flacon1 += flacon1

print(flacon1)