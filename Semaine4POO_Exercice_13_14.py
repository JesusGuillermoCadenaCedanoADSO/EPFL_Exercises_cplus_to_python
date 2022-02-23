import math
import copy

class point3d(object):
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def __eq__(self, newpoint):
        return self.x == newpoint.x and self.y == newpoint.y and \
                self.z == newpoint.z

    def __str__(self):
        return "(" + str(self.get_x()) + ", " \
               + str(self.get_y()) + ", " + str(self.get_z()) + ")"


class vecteur(point3d):
    def __init__(self, x=0.0, y=0.0, z=0.0):
        point3d.__init__(self, x, y, z)


    def __str__(self):
        return point3d.__str__(self)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    def __imul__(self, other):
        if type(other) is not vecteur:
            self.x *= other
            self.y *= other
            self.z *= other
            return self

    def __itruediv__(self, other):
        if type(other) is not vecteur:
            self.x /= other
            self.y /= other
            self.z /= other
            return self

    def __add__(self, other):
        return vecteur(self.x, self.y, self.z).__iadd__(other)

    def __sub__(self, other):
        return vecteur(self.x, self.y, self.z).__isub__(other)

    def __neg__(self):
        return vecteur(-self.x, -self.y, -self.z)

    def __mul__(self, other):
        if type(other) is vecteur:
            return self.get_x() * other.get_x() + \
            self.get_y() * other.get_y() + \
            self.get_z() * other.get_z()
        else:
            return vecteur(self.x, self.y, self.z).__imul__(other)

    def __truediv__(self, other):
        if type(other) is vecteur:
            return self.get_x() / other.get_x() + \
            self.get_y() / other.get_y() + \
            self.get_z() / other.get_z()
        else:
            return vecteur(self.x, self.y, self.z).__itruediv__(other)

    def __rmul__(self, other):
        return vecteur(self.x, self.y, self.z).__mul__(other)

    def norme(self):
        v = vecteur(self.x, self.y, self.z)
        return math.sqrt(v*v)


def angle_version_1(self, other):
    return math.acos((self*other)/(self.norme()*other.norme()))

class vecteurunitaire(vecteur):
    def __init__(self, x=1, y=0, z=0):
        vecteur.__init__(self, x, y, z)
        self.normalise()

    def __str__(self):
        return vecteur.__str__(self)

    def __copy__(self):
        v = vecteur(x=self.x, y=self.y, z=self.z)
        return v.normalise()

    def __iadd__(self, other):
        vecteur.__iadd__(self, other)
        self.normalise()
        return self

    #def __add__(self, other):
    #    return vecteurunitaire(self.x, self.y, self.z).__iadd__(other)


    def __imul__(self, other):
        vecteur.__imul__(self, other)
        self.normalise()
        return self

    def norme(self):
        return 1

    def normalise(self):
        n =vecteur.norme(self)
        if n==0:
            return vecteurunitaire()
        else:
            self.x/=n
            self.y/=n
            self.z/=n
            return vecteur(self.x, self.y, self.z)


def angle_version_2(self, other):
    resx = self.normalise() * other.normalise()
    return math.acos(resx)


"""
#test 13
v1 = vecteur(1.0, 2.0, -0.1)
v2 = vecteur(2.6, 3.5, 4.1)

print("vecteur v1 : ", v1)
print("vecteur v2 : ", v2)

print("v1 + v2 : ", v1 + v2)
print("v1 - v2 : ", v1 - v2)
print("-v1 : ", -v1)
print("3.2 * v1 : ", 3.2 * v1)
print("v1 * 3.2 : ", v1 * 3.2)
print("v1 * v2  : ", v1 * v2)
print("norme de v1 : ", v1.norme())
print("norme de v2 : ", v2.norme())
print("norme de v1+v2 : ", (v1 + v2).norme())
print("angle de v1 et v2 : ", angle_version_1(v1, v2))
print("angle de v2 et v1 : ", angle_version_1(v2, v1))
"""

#test 14
v1 = vecteurunitaire(1.0, 2.0, -0.1)
v2 = vecteurunitaire(2.6, 3.5, 4.1)

print("Vecteur V1 : ", v1)
print("Vecteur V2 : ", v2)
print("norme de V1 : ", v1.norme())
print("norme de V2 : ", v2.norme())

print("V1 + V2 : ", v1 + v2)

v3 = vecteurunitaire((v1+v2).get_x(), (v1+v2).get_y(), (v1+v2).get_z())
print("V3 = V1 + V2 : ", v3)

print("norme de V1+V2 : ", (v1 + v2).norme())

print("norme de V3 : ", v3.norme())

v3 = vecteurunitaire(1, 2, 3)
print("V3 = (1,2,3) : ", v3)

print("norme de V3 : ", v3.norme())
v3 += v1
print("V3 += V1 : ", v3)

print("norme de V3 : ", v3.norme())
print("angle de V1 et V2 : ", angle_version_2(v1, v2))

