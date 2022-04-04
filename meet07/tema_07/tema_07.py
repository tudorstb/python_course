from abc import ABC, abstractmethod
class FormaGeometrica(ABC):
    _PI = 3.14
    def descriere(self):
        print("cel mai probabil am colturi")
    @abstractmethod
    def aria(self):
        pass

class Patrat(FormaGeometrica):
    def __init__(self,latura):
        self.__latura = latura
    def descriere(self):
        print("Eu am coluturi")
    @property
    def latura(self):
        return self.__latura

    @latura.setter
    def latura(self,latura):
        if latura>0:
            self.__latura
        else:
            print("Latura must be greater than 0")

    @latura.deleter
    def latura(self):
        del self.__latura


    def aria(self):
        return self.__latura*self.__latura
class Cerc(FormaGeometrica):
    def __init__(self,raza):
        self.__raza=raza
    def descriere(self):
        print("forma nu are colturi")

    @property
    def raza(self):
        return self.__raza

    @raza.setter
    def raza(self, raza):
        if raza > 0:
            self.__raza
        else:
            print("Raza must be greater than 0")

    @raza.deleter
    def raza(self):
        del self.__raza
    def aria(self):
        return self._PI*self.__raza*self.__raza
new_square=Patrat(3)
print(new_square.aria())

new_circle=Cerc(3)
print(new_circle.aria())

def colturi_test(forma):
    forma.descriere()

colturi_test(new_circle)
colturi_test(new_square)

#github link
#TODO https://github.com/tudorstb/python_course