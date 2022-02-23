# Exercice 1 Jeux de nombres
def operaciones(a):
    cuenta = 0
    numero = a
    while numero:
        if numero % 3 == 0:
            numero = numero + 4
        elif numero % 4 == 0:
            numero = numero / 2
        else:
            numero = numero - 1
        cuenta += 1
    return (a, cuenta)


def jeux(number):
    diccionario = {}
    for i in range(1, number + 1):
        resultado = operaciones(i)
        diccionario[resultado[0]] = resultado[1]
    return diccionario


numero = 7
print(jeux(numero))