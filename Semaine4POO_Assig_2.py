def distance(x, y):
    return abs(x - y)


class creature(object):
    def __init__(self, nom, niveau, points_de_vie, force, position=0):
        self.nom = nom
        self.niveau = niveau
        self.points_de_vie = points_de_vie
        self.force = force
        self.position = position

    def vivant(self):
        if self.points_de_vie > 0:
            return True
        else:
            return False

    def points_attaque(self):
        if self.vivant():
            return self.niveau * self.force
        else:
            return 0

    def deplacer(self, steps):
        if self.vivant():
            self.position += steps

    def adieux(self):
        return self.nom + " n'est plus!"

    def faiblir(self, points):
        if self.vivant():
            self.points_de_vie -= points
        if not self.vivant():
            self.points_de_vie = 0
            print(self.adieux())

    def afficher(self):
        return self.nom + ", niveau: " + str(self.niveau) + ", points de vie: " + \
               str(self.points_de_vie) + ", force: " + str(self.force) + \
               ", points d'attaque: " + str(self.points_attaque()) + ", position: " + \
               str(self.position)


class dragon(creature):
    def __init__(self, nom, niveau, points_de_vie, force, portee_flame, position=0):
        creature.__init__(self, nom, niveau, points_de_vie, force, position)
        self.portee_flame = portee_flame

    def voler(self, pos):
        if self.vivant():
            self.position = pos

    def souffle_sur(self, other_creature):
        if self.vivant() and other_creature.vivant() and \
                distance(other_creature.position, self.position) <= self.portee_flame:
            other_creature.faiblir(self.points_attaque())
            self.faiblir(distance(other_creature.position, self.position))
            if self.vivant() and other_creature.vivant() == False:
                self.niveau += 1


class hydre(creature):
    def __init__(self, nom, niveau, points_de_vie, force, longueur_cou, dose_poison, position=0):
        creature.__init__(self, nom, niveau, points_de_vie, force, position)
        self.longueur_cou = longueur_cou
        self.dose_poison = dose_poison

    def empoisonne(self, other_creature):
        if self.vivant() and other_creature.vivant() and \
               distance(other_creature.position, self.position) <= self.longueur_cou:
            other_creature.faiblir(self.points_attaque() + self.dose_poison)
            if self.vivant and not other_creature.vivant():
                self.niveau += 1


def combat(a_dragon, a_hydra):
    a_hydra.empoisonne(a_dragon)
    a_dragon.souffle_sur(a_hydra)


dragon_1 = dragon("Dragon rouge", 2, 10, 3, 20)
hydre_1 = hydre("Hydre maléfique", 2, 10, 1, 10, 1, 42)

print(dragon_1.afficher())
print("se prépare au combat avec :")
print(hydre_1.afficher())
print("\n1er combat :")
print("     les créatures ne sont pas à portée, donc ne peuvent pas s'attaquer.")
combat(dragon_1, hydre_1)
print("Après le combat :")
print(dragon_1.afficher())
print(hydre_1.afficher())
print("\nLe dragon vole à proximité de l'hydre :")
dragon_1.voler(hydre_1.position - 1)
print(dragon_1.afficher())
print("\nL'hydre recule d'un pas :")
hydre_1.deplacer(1)
print(hydre_1.afficher())
print("\n2e combat :")
print("\
  + l'hydre inflige au dragon une attaque de 3 points\n\
      [ niveau (2) * force (1) + poison (1) = 3 ] ;\n\
  + le dragon inflige à l'hydre une attaque de 6 points\n\
      [ niveau (2) * force (3) = 6 ] ;\n\
  + pendant son attaque, le dragon perd 2 points de vie supplémentaires\n\
       [ correspondant à la distance entre le dragon et l'hydre : 43 - 41 = 2 ].\
")
combat(dragon_1, hydre_1)
print("Après le combat :")
print(dragon_1.afficher())
print(hydre_1.afficher())
print("\nLe dragon avance d'un pas :")
dragon_1.deplacer(1)
print(dragon_1.afficher())
print("\n3e combat :")
print("\
  + l'hydre inflige au dragon une attaque de 3 points\n\
      [ niveau (2) * force (1) + poison (1) = 3 ] ;\n\
  + le dragon inflige à l'hydre une attaque de 6 points\n\
      [ niveau (2) * force (3) = 6 ] ;\n\
  + pendant son attaque, le dragon perd 1 point de vie supplémentaire\n\
       [ correspondant à la distance entre le dragon et l'hydre : 43 - 42 = 1 ] ;\n\
  + l'hydre est vaincue et le dragon monte au niveau 3.\
")
combat(dragon_1, hydre_1)
print("Après le combat :")
print(dragon_1.afficher())
print(hydre_1.afficher())
print("\n4e combat :")
print("    quand une créature est vaincue, rien ne se passe.")
combat(dragon_1, hydre_1)
print("Après le combat :")
print(dragon_1.afficher())
print(hydre_1.afficher())

