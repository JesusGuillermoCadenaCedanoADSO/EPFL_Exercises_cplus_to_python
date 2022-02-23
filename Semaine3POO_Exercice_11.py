class monome(object):
    #Atributo de clase
    letra = 'X'
    def __init__(self, coef = 1, degre = 1):
        #Atributos de instancia
        self.coef = coef
        self.degre = degre
        self.diccionario = {}
        if coef < 0:
            self.signe = True
        else:
            self.signe = False
        self.diccionario[self.degre] = self.coef

    @classmethod
    #metodo de clase no puede acceder a atributos de instancia
    #puede modificar los atributos de clase
    def cambiarletra(cls, nueva_letra):
        cls.letra = nueva_letra
    @classmethod
    def getletra(cls):
        return cls.letra
    @staticmethod
    #no puede modificar el estado ni de la clase ni de la instancia
    #puede aceptar parametros de entrada
    def metodoestatico(letra=''):
        return "La letra actual es : " + letra

    def getcoef(self):
        return self.coef

    def getdegre(self):
        return self.degre

    def setcoef(self, newcoef):
        self.coef = newcoef
        self.diccionario[self.degre] = self.coef

    def setdegre(self, newdegre):
        self.degre = newdegre
        self.diccionario[self.degre] = self.coef

    def getsigne(self):
        return self.signe

    def setsigne(self, newsigne):
        self.signe = newsigne

    def copy(self):
        new_monome = monome(coef = self.coef, degre = self.degre)
        new_monome.diccionario = self.diccionario.copy()
        return new_monome

    def simplifie_dict(self,diccionario):
        lista_claves = list(diccionario.keys())
        for i in range(0, len(lista_claves)):
            if not diccionario[lista_claves[i]]:
                diccionario.pop(lista_claves[i])
        return diccionario

    def affiche_monome(self, m):
        resultado = ''
        if m.coef == 1:
            resultado +=  self.letra
        elif m.coef == -1:
            resultado += "-" + self.letra
        else:
            resultado += str(m.coef) + "*" + self.letra
        if m.degre > 0:
            if m.degre > 1:
                resultado += "^" + str(m.degre)
        elif m.degre == 0:
            resultado = str(m.coef)
        else:
            return ''
        return resultado

    def affiche_list(self):
        resultado2 = ''
        lista_claves = sorted(list(self.diccionario.keys()))
        lista_claves.reverse()
        if len(lista_claves) > 1:
            for i in range(0, len(lista_claves)):
                valor = round(self.diccionario[lista_claves[i]], 3)
                if i:
                    if valor > 0:
                        sep = "+"
                    else:
                        valor *= -1
                        sep = "-"
                else:
                    sep = ''
                resultado2 += sep + self.affiche_monome(monome(valor, lista_claves[i]))
        elif len(lista_claves) == 1:
            resultado2 = self.affiche_monome(monome(round(self.diccionario[lista_claves[0]], 3),
                                                    lista_claves[0]))
        return resultado2

    def __str__(self):
        return self.affiche_list()

    def __iadd__(self, m2):
        if type(m2) is monome:
            for i in m2.diccionario:
                if i not in self.diccionario:
                    self.diccionario[i] = m2.diccionario[i]
                else:
                    self.diccionario[i] += m2.diccionario[i]
        elif type(m2) != str:
            if list(self.diccionario.keys()).count(0):
                self.diccionario[0] += m2
            else:
                self.diccionario[0] = m2
        self.diccionario = self.simplifie_dict(self.diccionario)
        return self

    def __add__(self, m2):
        new_monome = monome()
        new_monome.diccionario = self.diccionario.copy()
        return new_monome.__iadd__(m2)

    def __radd__(self, m2):
        new_monome = monome()
        new_monome.diccionario = self.diccionario.copy()
        return new_monome.__add__(m2)

    def __isub__(self, m2):
        if type(m2) is monome:
            for i in m2.diccionario:
                if i not in self.diccionario:
                    self.diccionario[i] = -m2.diccionario[i]
                else:
                    self.diccionario[i] -= m2.diccionario[i]
        elif type(m2) != str:
            if list(self.diccionario.keys()).count(0):
                self.diccionario[0] -= m2
            else:
                self.diccionario[0] = -m2
        self.diccionario = self.simplifie_dict(self.diccionario)
        return self

    def __sub__(self, m2):
        new_monome = monome()
        new_monome.diccionario = self.diccionario.copy()
        return new_monome.__isub__(m2)

    def __rsub__(self, m2):
        new_monome = monome()
        new_monome.diccionario = self.diccionario.copy()
        return new_monome.__sub__(m2)

    def __mul__(self, m2):
        new_monome = monome()
        new_monome.diccionario.clear()
        lista_claves = sorted(list(self.diccionario.keys()))
        if type(m2) is monome:
            lista_claves_m2 = sorted(list(m2.diccionario.keys()))
            for i in range(0, len(lista_claves)):
                for j in range(0, len(lista_claves_m2)):
                    if not new_monome.diccionario.get(lista_claves[i] + lista_claves_m2[j]):
                        new_monome.diccionario[lista_claves[i] + lista_claves_m2[j]] = \
                        self.diccionario[lista_claves[i]]*m2.diccionario[lista_claves_m2[j]]
                    else:
                        new_monome.diccionario[lista_claves[i] + lista_claves_m2[j]] += \
                            self.diccionario[lista_claves[i]] * m2.diccionario[lista_claves_m2[j]]
        elif type(m2) != str:
            for i in range(0, len(lista_claves)):
                new_monome.diccionario[lista_claves[i]] = \
                    self.diccionario[lista_claves[i]] * m2
        new_monome.diccionario = new_monome.simplifie_dict(new_monome.diccionario)
        return new_monome

    def __rmul__(self, m2):
        new_monome = monome(self.coef,self.degre)
        new_monome.diccionario = self.diccionario.copy()
        return new_monome.__mul__(m2)

    def __imul__(self, m2):
        new_monome = monome(coef=self.coef,degre=self.degre)
        new_monome.diccionario = self.diccionario.copy()
        return new_monome * m2

    def divise(self, denominateur, cociente, reste):
        cociente.diccionario.clear()
        grado_reste = max(reste.diccionario)
        grado_denominateur = max(denominateur.diccionario)
        dq = grado_reste - grado_denominateur
        while dq >= 0 and len(reste.diccionario):
            grado_reste = max(reste.diccionario)
            dq = grado_reste - grado_denominateur
            if dq >= 0:
                division = reste.diccionario[grado_reste]/denominateur.diccionario[grado_denominateur]
                cociente.diccionario[dq] = division
                grado_quotient = max(cociente.diccionario)
                new_monome = monome(min(cociente.diccionario), dq)
                new_monome.diccionario[dq] = cociente.diccionario[min(cociente.diccionario)]
                reste -= new_monome * denominateur
        return reste

    def __truediv__(self, m2):
        r = monome()
        s = self.copy()
        if type(m2) is monome:
            self.divise(m2, r, s)
            return r
        elif type(m2) != str:
            return s.__mul__(1/m2)
        else:
            return s

    def __itruediv__(self, m2):
        return self / m2

    def __mod__(self, m2):
        r = monome()
        s = self.copy()
        if type(m2) is monome:
            self.divise(m2, r, s)
        return s

    def __eq__(self, m2):
        return self.diccionario == m2.diccionario

    def __ne__(self, m2):
        return self.diccionario != m2.diccionario

    def print_divise(self,q):
        r = self / q
        s = self % q
        print("La division de :",self,"\npar :",q,
              "\napour quotient :", r, "\net pour reste :", s)

x = monome(1, 1)
x2 = monome(1, 2)
x3 = monome(1, 3)
x4 = monome(1, 4)
x5 = monome(1, 5)

monome.cambiarletra("W")
z = monome.metodoestatico(monome.getletra())
w = monome(-2,2)

y = - 2 * x + 3 + 5 * x3 + 4 * x2
z = 2 * x - 2 * x2 +  1

yy = 15 * x3 + 8 * x2 - 2 * x + 3
zz = 6 * x4 + 5 * x3 + 4 * x2 - 2 * x + 3
zzz = 3*x3

y/= z

print(z == y)
print(y)
#print(y/z)
yy.print_divise(zzz)
#print("resto: ", y%z)



x.setcoef(1)
print(x)
print(x2)
x+=x2
print(x.diccionario)
print(x)

x2.setcoef(-2)
print(x2)
x+=x2
print(x)
print(x.diccionario)

x+=x
print(x.diccionario)
print(x)

x+=x2
print(x)
print(x.diccionario)

x+=x3
print(x)

x+=x4
print(x.diccionario)
print(x)
x2.setcoef(2)
x+=x2
print(x)
s = x

#verificacion de operador suma

x = monome(1, 1)
x2 = monome(1, 2)
y = x4 + x2 + x3 + x + x + w +  x2 + w


print("y = ", y,"\n","s = ",s,sep='')



