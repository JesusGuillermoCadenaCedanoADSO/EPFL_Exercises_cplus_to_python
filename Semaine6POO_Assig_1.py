class produit(object):
    def __init__(self, nom, unite=''):
        self.nom = nom
        self.unite = unite

    def get_nom(self):
        return self.nom

    def get_unite(self):
        return self.unite

    def adapter(self, n):
        return self

    def quantitetotale(self, nomproduit):
        if self.get_nom() == nomproduit:
            return 1
        else:
            return 0

    def tostring(self, n=1):
        return self.get_nom()


class ingredient(object):
    def __init__(self, new_produit, quantite=1):
        self.quantite = quantite
        self.new_produit = new_produit

    def product_representation(self, n):
        return self.get_produit().tostring(n)

    def get_quantite(self):
        return self.quantite

    def get_produit(self):
        return self.new_produit

    def quantitetotale(self, nomproduit):
        return self.get_quantite() * self.get_produit().quantitetotale(nomproduit)

    def descriptionadaptee(self):
        return str(self.quantite) + " " + \
               self.get_produit().get_unite() + " de " + \
               self.product_representation(self.quantite)


class recette(object):
    def __init__(self, nom, nbfois=1):
        self.nom = nom
        self.nbfois = nbfois
        self.ingredients = []

    def get_nom_recette(self):
        return self.nom

    def get_nbfois(self):

        return self.nbfois

    def ajouter(self, new_produit, new_quantite):
        new_ingredient = ingredient(new_produit, new_quantite * self.get_nbfois())
        self.ingredients.append(new_ingredient)

    def adapter(self, n):
        new_recette = recette(nom=self.get_nom_recette(), nbfois=n * self.nbfois)
        for i in self.ingredients:
            cantidad = i.get_quantite()
            new_recette.ajouter(i.get_produit(), cantidad / self.nbfois)
        return new_recette

    def quantitetotale(self, nomproduit):
        suma = 0
        for i in range(0, len(self.ingredients)):
            suma += self.ingredients[i].quantitetotale(nomproduit)
        return suma

    def tostring(self):
        result = ("  Recette " + self.get_nom_recette() + " x "
                  + str(self.get_nbfois()) + " :\n")
        for i in range(0, len(self.ingredients)):
            if i != len(self.ingredients) - 1:
                result += "  " + str(i + 1) + ". " + \
                          self.ingredients[i].descriptionadaptee() + '\n'
            else:
                result += "  " + str(i + 1) + ". " + \
                          self.ingredients[i].descriptionadaptee()
        return result


class ProduitCuisine(produit):
    def __init__(self, nom, unite="portion(s)"):
        produit.__init__(self, nom, unite)
        self.new_recette = recette(nom)

    def get_nom(self):
        return self.nom

    def get_unite(self):
        return self.unite

    def ajouterarecete(self, new_produit, new_quantite):
        self.new_recette.ajouter(new_produit, new_quantite)

    def adapter(self, n):
        new_produitcuisine = ProduitCuisine(nom=self.get_nom(), unite=self.get_unite())
        #adapter_recette = self.new_recette.adapter(1)
        new_produitcuisine.new_recette = self.new_recette
        new_produitcuisine.new_recette.nbfois = n
        #for i in self.new_recette.ingredients:
        #    new_produitcuisine.new_recette.ajouter(i.get_produit(), i.get_quantite() / 1)

        return new_produitcuisine

    def quantitetotale(self, nomproduit):
        if self.get_nom() == nomproduit:
            return 1
        else:
            return self.new_recette.quantitetotale(nomproduit)

    def tostring(self, n=1):
        adapter_recette = self.new_recette.adapter(n)
        return produit.tostring(self, n) + "\n" + \
               adapter_recette.tostring()


def afficherQuantiteTotale(intro_recette, cherche_ingredient):
    quantite_sum = intro_recette.quantitetotale(cherche_ingredient.get_nom())
    return "Cette recette contient " + str(quantite_sum) + " " \
           + cherche_ingredient.get_unite() + " de " \
           + cherche_ingredient.get_nom()


oeufs = produit("oeufs")
farine = produit("farine", "grammes")
beurre = produit("beurre", "grammes")
sucreGlace = produit("sucre glace", "grammes")
chocolatNoir = produit("chocolat noir", "grammes")
amandesMoulues = produit("amandes moulues", "grammes")
extraitAmandes = produit("extrait d'amandes", "gouttes")

glacage = ProduitCuisine("glaçage au chocolat")
glacage.ajouterarecete(chocolatNoir, 200)
glacage.ajouterarecete(beurre, 25)
glacage.ajouterarecete(sucreGlace, 100)
print(glacage.tostring())


glacageParfume = ProduitCuisine("glaçage au chocolat parfumé")
glacageParfume.ajouterarecete(extraitAmandes, 2)
glacageParfume.ajouterarecete(glacage, 1)
print(glacageParfume.tostring())

Recette = recette("tourte glacée au chocolat")
Recette.ajouter(oeufs, 5)
Recette.ajouter(farine, 150)
Recette.ajouter(beurre, 100)
Recette.ajouter(amandesMoulues, 50)
Recette.ajouter(glacageParfume, 2)

print("verificacion glacage\n", glacage.tostring())


print("===  Recette finale  =====")
print(Recette.tostring())
print(afficherQuantiteTotale(Recette, beurre))

print(afficherQuantiteTotale(Recette, sucreGlace))

doubleRecette = Recette.adapter(2)
print("===  Recette finale x 2 ===")
print(doubleRecette.tostring())
print(afficherQuantiteTotale(doubleRecette, beurre))
print(afficherQuantiteTotale(doubleRecette, oeufs))
print(afficherQuantiteTotale(doubleRecette, extraitAmandes))
print(afficherQuantiteTotale(doubleRecette, glacage))
print("===========================\n")
print("Vérification que le glaçage n'a pas été modifié :\n")
print(glacage.tostring())