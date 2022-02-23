class complexe(object):
    def __init__(self, re = 0.0, im = 0.0):
        self.re = re
        self.im = im

    def reel(self):
        return self.re

    def imag(self):
        return self.im

    def set_reel(self,x):
        self.re = x

    def set_imag(self,y):
        self.im = y

    def copy(self):
        return complexe(re = self.re, im = self.im)

    def __eq__(self, other):
        return other.reel() == self.re and other.imag() == self.im

    def __iadd__(self, other):
        if type(other) is complexe:
            self.set_reel(self.re + other.re)
            self.set_imag(self.im + other.im)
        else:
            self.set_reel(self.re + other)
        return self

    def __add__(self, other):
        return complexe(self.re, self.im).__iadd__(other)

    def __radd__(self, other):
        return complexe(self.re, self.im).__add__(other)

    def __sub__(self, other):
        if type(other) is complexe:
            return complexe(self.re - other.reel(), self.im - other.imag())
        else:
            return complexe(self.re - other, self.im)

    def __rsub__(self, other):
        if type(other) is complexe:
            return complexe(self.re - other.reel(), self.im - other.imag())
        else:
            return complexe(self.re - other, self.im)

    def __isub__(self, other):
        return complexe(re = self.re, im = self.im) - other

    def __mul__(self, other):
        if type(other) is complexe:
            return complexe(self.re * other.reel() - self.im * other.imag(),
                            self.re * other.imag() + self.im * other.reel())
        else:
            return complexe(self.re * other - self.im * 0,
                            self.re * 0 + self.im * other)

    def __rmul__(self, other):
        if type(other) is complexe:
            return complexe(self.re * other.reel() - self.im * other.imag(),
                            self.re * other.imag() + self.im * other.reel())
        else:
            return complexe(self.re * other - self.im * 0,
                            self.re * 0 + self.im * other)

    def __imul__(self, other):
        return complexe(re = self.re, im = self.im) * other

    def __truediv__(self, other):
        if type(other) is complexe:
            r = other.reel() * other.reel() + other.imag() * other.imag()
            return complexe(( self.re * other.reel() + self.im * other.imag() ) / r,
                            (( self.im * other.reel() - self.re * other.imag() ) / r))
        else:
            r = other * other
            return complexe(( self.re * other ) / r,
                            (( self.im * other ) / r))

    def __rtruediv__(self, other):
        if type(other) is complexe:
            r = other.reel()*other.reel() + other.imag()*other.imag()
            return complexe(( self.re * other.reel() + self.im * other.imag() ) / r,
                            (( self.im * other.reel() - self.re * other.imag() ) / r))
        else:
            r = other * other
            return complexe(( self.re * other ) / r,
                            (( self.im * other ) / r))

    def __itruediv__(self, other):
        return complexe(re = self.re,im = self.im)/other


    def __str__(self):
        return '(' + str(self.re) + ', ' + str(self.im) + ')'

defaut = complexe()
zero = complexe(0.0,0.0)
un = complexe(1.0,0.0)
i = complexe(0.0,1.0)
j = complexe()
print(zero, "==?" , defaut)
if zero == defaut:
    print("oui")
else:
    print("non")

print(zero, "==?" , i)
if zero == i:
    print("oui")
else:
    print("non")

j = un + i
print(un,"+",i,"=",j)

trois = un.copy()
trois += un
trois += 1.0
print(un)
print(un,"+",un,"+ 1.0 =",trois)

deux = complexe(trois.reel(), trois.imag())
deux -= un

print(trois,"-",un,"=",deux)

trois = 1.0 + deux
print("1.0 +",deux,"=",trois)

z = i*i
print(i,"*",i,"=",z)
print(z,"/",i,"=",z/i,"=")
z/=i
print(z)

k = complexe(2.0, -3.0)
z = k.copy()
z *= 2.0
z *= i
print(k,"* 2.0 *",i,"=",z)
z = 2.0 * k * i / 1.0
print("2.0 *",k,"*",i," / 1 =",z)

