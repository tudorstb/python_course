#EX 1
print('\tEX 1')
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

#EX 2
print('\tEX 2')

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

#EX 3
print('\tEX 3')

class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume=nume
        self.prenume=prenume
        verify = -1
        while verify == -1:
            try:
                salariu = int(salariu)
            except:
                print("invalid option choose for 'salariu'")
                salariu = input('Select salariu:')
            else:
                verify = 1
                self.salariu = salariu
    def descrie(self):
        print(f'Numele angajatului:{self.nume}')
        print(f'Prenumele angajatului:{self.prenume}')
        print(f'Salariul angajatului:{self.salariu}')
    def nume_complet(self):
        return self.nume+" "+self.prenume
    def salariu_lunar(self):
        return self.salariu
    def salariu_anual(self):
        return self.salariu_lunar()*12
    def marire_salariu(self,procentaj):
        self.salariu=self.salariu+(self.salariu*procentaj/100)

new_employee=Angajat('Stanescu','Tudor',2000)
new_employee.descrie()
print(new_employee.salariu_lunar())
print(new_employee.salariu_anual())
new_employee.marire_salariu(30)
new_employee.descrie()

#EX 4
print('\tEX 4')
from tabulate import tabulate
import datetime
class Factura:
    def __init__(self,numar,nume_produs,cantitate,pret_buc):
        self.numar=numar
        self.nume=nume_produs
        self.cantitate=cantitate
        self.pret_buc=pret_buc

    serie = 'robell'
    def schimba_cantitatea(self,cantitiate):
        self.cantitate=cantitiate
    def schimpa_pret(self,pret):
        self.pret_buc=pret
    def prezent_time(self):
        now = datetime.datetime.now()
        return now.strftime("%d/%m/%Y %H:%M")

    def genereaza_factura(self):
        print(f'Factura seria {self.serie} numar {self.numar}')
        print(f'Data:{self.prezent_time()}')
        data=[[self.nume,self.cantitate,self.pret_buc,self.pret_buc*self.cantitate]]
        print(tabulate(data, headers=['Produs','Cantitate','Pret bucata','Total']))
new_factura=Factura(123,'Pulpe',2,10)
new_factura.genereaza_factura()

#EX 5
print('\tEX 5')

class Cont:
    def __init__(self,iban,titular_cont,sold):
        self.iban=iban
        self.titular_cont=titular_cont
        verify = -1
        while verify == -1:
            try:
                sold = int(sold)
            except:
                print("invalid option choose for 'sold'")
                salariu = input('Select sold:')
            else:
                verify = 1
                self.sold = sold
    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei')

# debitare_cont(suma)
# creditare_cont(suma)
#Habar nu am ce e de facut aici :))))))))))))))))))))))

new_account=Cont('ro1234','Tudor',20000)
new_account.afisare_sold()


#EX 6
print('\tEX 6')

class Masina:
    marca='asdasd'
    viteza_actuala=0
    culoare='gri'
    inmatriculata=False
    culori_disponibile = ('Gri', 'Verde', 'Albastru', 'Negru', 'Rosu')
    def __init__(self,model,viteza_maxima):
        self.model=model
        self.viteza_maxima=viteza_maxima
    def descriere(self):
        print(f'Marca={self.marca}')
        print(f'Viteza actuala={self.viteza_actuala}')
        print(f'culoare={self.culoare}')
        print(f'inmatriculata={self.inmatriculata}')
        print(f'model={self.model}')
        print(f'viteza maxima={self.viteza_maxima}')
    def inmatriculare(self):
        self.inmatriculata=True
    def vopseste(self,new_color):
        if new_color in self.culori_disponibile:
            self.culoare=new_color
        else:
            print("Error ,color not avalable")

    def accelereaza(self,speed):
        if speed<0:
            print('Error invalid speed')
        elif speed>self.viteza_maxima:
            self.viteza_actuala=self.viteza_maxima
        else:
            self.viteza_actuala=speed
    def franeaza(self):
        self.viteza_actuala=0

new_car=Masina("Dacia",90)
new_car.descriere()


#EX 7
print('\tEX 7')
class TodoList:
    todo={}
    def adauga_task(self,nume,descriere):
        self.todo[nume]=descriere
    def finalizeaza_task(self,nume):
        self.todo.pop(nume)
    def afiseaza_todo_list(self):
        for elem in self.todo:
            print(elem)
    def afiseaza_detalii_suplimentare(self,nume_task):
        if nume_task in self.todo:
            print(self.todo[nume_task])
        else:
            add=input("task not in list ,if you wish to add press (R):")
            if add=='R' or add=='r':
                detalii_task=input('Detalii task=')
                self.adauga_task(nume_task,detalii_task)

new_todo=TodoList()
new_todo.adauga_task('a','1')
new_todo.adauga_task('b','2')

new_todo.afiseaza_todo_list()
#new_todo.afiseaza_detalii_suplimentare("c")
new_todo.afiseaza_todo_list()
