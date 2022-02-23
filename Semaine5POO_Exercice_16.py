from abc import ABC, abstractmethod
class forme(ABC):
    @abstractmethod
    def aire(self):
        pass

    @abstractmethod
    def description(self):
        return "Ceci est une forme !"


class cercle(forme):
    def __init__(self, rayon=0):
        self.rayon = rayon

    def description(self):
        print(super().description())
        return "Ceci est un cercle !"

    def aire(self):
        return 3.1416 * self.rayon * self.rayon


class triangle(forme):
    def __init__(self, h=0, b=0):
        self.h = h
        self.b = b

    def description(self):
        print(super().description())
        return "Ceci est un triangle !"

    def aire(self):
        return 0.5 * self.b * self.h

def affichagedesc(forme):
    print(forme.description())
    return " son aire est " + str(forme.aire())


c = cercle(5)
t = triangle(10, 2)
print(affichagedesc(t))
print(affichagedesc(c))



