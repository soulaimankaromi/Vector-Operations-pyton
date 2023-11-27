class Vecteur2D :
    _count = 0
    def __init__(self, X = 1, Y = 2):
        self.__abscisse = X
        self.__ordonne = Y
        self._count += 1
    def GetX(self):
        return self.__abscisse
    def GetY(self):
        return self.__ordonne
    def Getcount(self):
        return self._count
    def SetX(self, X1):
        self.__abscisse = X1
    def SetY(self, Y1):
        self.__ordonne = Y1
    def ToString(self):
        return "X = " + str(self.GetX()) + " Y = " + str(self.GetY())
    def Equals(self, vecteur1) :
        if vecteur1.GetX() == self.GetX() and vecteur1.GetY() == self.GetY() :
            return True
        else : 
            return False 
    def Norme (self) :
        return (self.GetX()**2 + self.GetY()**2)**0.5

class Vecteur3D (Vecteur2D) :
    def __init__(self, X = 1, Y = 2, Z = 3) :
        super().__init__(X, Y)
        self.__propriete = Z
        self._count += 1
    def GetZ(self):
        return self.__propriete
    def SetZ(self, Z1):
        self.__propriete = Z1
    def ToString(self):
        return "X = " + str(self.GetX()) + " Y = " + str(self.GetY()) + " Z = " + str(self.GetZ())
    def Equals(self, vecteur1) :
        if vecteur1.GetX() == self.GetX() and vecteur1.GetY() == self.GetY() and vecteur1.GetZ() == self.GetZ() :
            return True
        else : 
            return False 
    def Norme (self) :
        return (self.GetX()**2 + self.GetY()**2 + self.GetZ()**2)**0.5
    
    