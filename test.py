class arisque(object):
    def __init__(self, prime=100):
        self.__prime = prime

    @property
    def getprime(self):
        return self.__prime

    def __del__(self):
        pass


class prueba(arisque):
    def __init__(self, prime=100, valor=100):
        arisque.__init__(self, prime)
        self.valor = valor

    def calcul(self):
        #return arisque.prime + self.valor
        return self.getprime + self.valor


clase = prueba(50, 120)

print(clase.calcul())

print(type(clase))