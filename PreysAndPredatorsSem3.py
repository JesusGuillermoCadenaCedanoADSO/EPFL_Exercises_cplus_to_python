taux_croissance_lapins = 0.3
taux_attaque = 0.01
taux_croissance_renards = 0.008
taux_mortalite = 0.1
duree = 50
renards_i = 0.0
lapins_i = 0.0
#part 1

while renards_i < 2:
    renards_i = float(input("enter number of renards (>=2)"))

while lapins_i < 2:
    lapins_i = float(input("enter number of lapins (>=5)"))

renards = renards_i
lapins = lapins_i

#part 2
for i in (range(1, duree + 1)):
    nb_lapins = lapins
    nb_renards = renards
    lapins = nb_lapins * (1.0 + taux_croissance_lapins - taux_attaque * nb_renards)

    renards = nb_renards * (1.0 + taux_attaque * nb_lapins * taux_croissance_renards
              - taux_mortalite)

    if lapins < 0:
        lapins = 0
    if renards < 0:
        renards = 0

    if lapins == 0 and renards == 0:
        break
    """
    print("Après " + str((i)) + " mois, il y a " + "{:.1f}".format(lapins) +
          " lapins et " + "{:.2f}".format(renards) + " renards")
    """
#part 3

initial_attack_rate = 0.0
while not 0.5 <= initial_attack_rate <= 6:
    initial_attack_rate = float(input('enter initial attack rate between 0.5 and 6'))
final_attack_rate = 0
while not initial_attack_rate <= final_attack_rate <= 6:
    final_attack_rate = int(input('enter initial attack rate between initial attack rate and 6'))

rate_attack = initial_attack_rate
while rate_attack < final_attack_rate:
    renards = renards_i
    lapins = lapins_i

    peligro_lapins = False
    peligro_renards = False

    taux_attaque = rate_attack/100
    for i in (range(1, duree + 1)):
        nb_lapins = lapins
        nb_renards = renards
        lapins = nb_lapins * (1.0 + taux_croissance_lapins - taux_attaque * nb_renards)

        renards = nb_renards * (1.0 + taux_attaque * nb_lapins * taux_croissance_renards
                  - taux_mortalite)
        if renards < 5:
            peligro_renards = True
        if lapins < 5:
            peligro_lapins = True
        if lapins < 2:
            lapins = 0
        if renards < 2:
            renards = 0
        if lapins < 0:
            lapins = 0
        if renards < 0:
            renards = 0
        if lapins == 0 and renards == 0:
            break
    normal_situation = True
    print('\n***** Le taux d’attaque vaut ' + str(rate_attack) + '%\n')
    print("Après " + str((i)) + " mois, il y a " + "{:.1f}".format(lapins) +
          " lapins et " + "{:.2f}".format(renards) + " renards")
    if peligro_lapins:
        print("Les lapins ont été en voie d'extinction")
        normal_situation = False
        if lapins > 5:
            print("mais la population est remontée ! Ouf !")
    if not lapins:
        print("et les lapins ont disparu :-(")
        normal_situation = False
    if peligro_renards:
        print("Les renards ont été en voie d'extinction")
        normal_situation = False
        if renards > 5:
            print("mais la population est remontée ! Ouf !")
    if not renards:
        print("et les renards ont disparu :-(")
        normal_situation = False
        if lapins == 0:
            break
    if normal_situation:
        print("Les lapins et les renards ont des populations stables.")
    rate_attack += 1

