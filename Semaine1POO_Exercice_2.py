class papier(object):
    def __init__(self,age=0,argent=0):
        self.age = age
        self.argent = argent
    def ecrire(self,un_age,de_l_argent):
        self.age = un_age
        self.argent = de_l_argent
    def lire_age(self):
        return self.age
    def lire_somme(self):
        return self.argent

class Assistant(object):
    def __init__(self, age_lu=0, argent_lu=0,resultat=0):
        self.age_lu=age_lu
        self.argent_lu=argent_lu
        self.resultat=resultat

    def lire(self,billet):
        print("[Assistant] (je lis le papier)")
        self.age_lu = billet.lire_age()
        self.argent_lu = billet.lire_somme()
        
    def calculer(self):
        print("[Assistant] (je calcule mentalement)")
        self.resultat = self.age_lu * 2
        self.resultat += 5
        self.resultat *= 50
        self.resultat += self.argent_lu
        self.resultat -= 365

    def annoncer(self):
        print("[Assistant] J'annonce : " + str(self.resultat) + " !")
        return self.resultat
    
class spectateur(object):
    def __init__(self,age_s=0,argent_s=0):
        self.age_s = age_s
        self.argent_s = argent_s
        self.paquet_cigarettes = papier()

    def arriver(self):
        self.age_s = int(input("[Spectateur] (j'entre en scène)\nQuel âge ai-je ? "))
        while self.argent_s >=100 or self.argent_s == 0:
            self.argent_s = int(input("Combien d'argent ai-je en poche (<100) ? "))
        print("[Spectateur] (je suis là)")

    def ecrire(self):
        print("[Spectateur] (j'écris le papier)")
        self.paquet_cigarettes.ecrire(self.age_s,self.argent_s)

    def montrer(self):
        print("[Spectateur] (je montre le papier)")
        return self.paquet_cigarettes

class magicien(object):
    def __init__(self, age_devine=0,argent_devine=0):
        self.age_devine=age_devine
        self.argent_devine=argent_devine

    def tourDeMagie(self,asistente,espectador):
        print("[Magicien] un petit tour de magie...")
        espectador.ecrire()
        asistente.lire(espectador.montrer())
        asistente.calculer()
        self.calculer(asistente.annoncer())
        return self.annoncer()


    def calculer(self,resultat_recu):
        resultat_recu +=115
        self.age_devine = int(resultat_recu / 100);
        self.argent_devine = resultat_recu % 100;

    def annoncer(self):
        return( "[magicien] \n" +\
        " - hum... je vois que vous êtes agé de " + str(self.age_devine) + " ans\n" +\
        " et que vous avez " + str(self.argent_devine) + " francs en poche !")

thorin = spectateur()
thorin.arriver()
gandalf = magicien()
bilbo =  Assistant()
print(gandalf.tourDeMagie(bilbo,thorin))
