from enum import Enum, auto

class couleur(Enum):
    VIDE = 0
    ROUGE = 1
    JAUNE = 2

lista = [[0,1,2],[3,4,5],[6,7,8]]

grille_1 = [[couleur.VIDE for x in range(8)] for y in range(8)]
grille_2 = [[couleur.ROUGE for x in range(8)] for y in range(8)]
grille_3 = [[couleur.JAUNE for x in range(8)] for y in range(8)]

print("grille1:\n",grille_1)
print("grille2:\n",grille_2)
print("grille3:\n",grille_3)

j = len(lista)
variable = False
#while j != 0:
while not variable:
    if j==0:
        variable=True
    j -=1
    result = ''
    for i in range(0, len(lista)):
        result += str(lista[i][j])
    print(result)
print("variable ", variable)

for i in range(0, len(lista)):
    for j in range(0, len(lista[i])):
        print(str(lista[i][j]))