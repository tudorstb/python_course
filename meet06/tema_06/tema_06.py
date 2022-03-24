# class Cerc:
#     def __init__(self,raza,culoare):
#         verify=-1
#         while verify == -1:
#             try:
#                 raza = int(raza)
#             except:
#                 print("invalid option choose")
#                 raza = input('Select raza:')
#             else:
#                 verify=1
#                 self.raza = raza
#
#         self.culoare=culoare
#     def descire_cerc(self):
#         print(f'culoarea cercului este {self.culoare} iar raza este {self.raza} ')
#     def aria(self):
#         return 3.14*self.raza*self.raza
#     def diametru(self):
#         return self.raza*2
#     def circumferinta(self):
#         #help putin aici
#         #return diametru()*3,14
#         return self.diametru()*3.14
#
# new_circle = Cerc('a','rosu')
#
# new_circle.descire_cerc()
# print(new_circle.aria())
# print(new_circle.diametru())
# print(new_circle.circumferinta())

class Dreptunghi:

    def __init__(self,lungime,latime,culoare):
        if latime>lungime:
            (latime,lungime)=(lungime,latime)
        verify = -1
        while verify == -1:
            try:
                lungime = int(lungime)
            except:
                print("invalid option choose")
                lungime = input('Select raza:')
            else:
                verify = 1
                self.lungime = lungime

        verify = -1
        while verify == -1:
            try:
                latime = int(latime)
            except:
                print("invalid option choose")
                latime = input('Select raza:')
            else:
                verify = 1
                self.latime = latime
        self.culoare=culoare
    def descrie(self):
        print(f'Lungimea este {self.lungime} , latimea este {self.latime} iar culoarea este {self.culoare}')
    def aria(self):
        print(f'aria este {self.latime*self.lungime}')
    def perimetru(self):
        print(f'perimetrul este {self.latime*2+self.lungime*2}')
    def schimba_culoarea(self,noua_culoare):
        self.culoare=noua_culoare

new_rectangle=Dreptunghi(2,6,'rosu')
new_rectangle.descrie()
new_rectangle.aria()
new_rectangle.perimetru()
new_rectangle.schimba_culoarea('albastra')
new_rectangle.descrie()
