
#TODO am lasat totul in comentarii pentru ca deja ma ametea de cap sa tot completez pentru fiecare ex :)))
# #b
# #1
#
# #variabila este o dimensiune vitruala ce tine valori
#
# #2
# nume = 'Tudor'
# varsta=18
# inaltime=1.83
# admis=True
#
# #3
# print(type(nume))
# print(type(varsta))
# print(type(inaltime))
# print(type(admis))
#
# #4
# inaltime=round(inaltime)
# print(f'inaltime rotunjita:{inaltime}')
# print(f'tipul variabilei este:{type(inaltime)}')
#
# #5
#
# print(f'{nume} are {varsta} de ani si are inaltimea de {varsta} si a fost {admis}')
#
# #6
#
# nume=input('Introduceti nume:')
# inaltime=input('Introduceti inaltime:')
#
# print(f'Numele complet are {len(nume)} caractere')
#
# #7
#
# lungimea= input('Introduceti lungimea:')
# latimea= input('Introduceti latimea:')
# aria=int(latimea)*int(lungimea)
#
# print(f'Aria dreptunghiului este {aria}')
#
# #8
# propozitie='Coral is either the stupidest animal or the smartest rock'
#
# x=input('cate litere sa se ignore de la capat:')
# print(propozitie[:-int(x)])
#
# #9
#marime=len(propozitie)
# ex9=propozitie[:5] + propozitie[marime-5]
# print(ex9)
#
# #10
#
# print(f'de cate ori apare the in propozitia data:{propozitie.count("the")}')
#
# #TODO print(f'de cate ori apare the in propozitia data:{propozitie.count('the')}')
# #de ce nu merge cand pun ' ' iar cand folosesc " " functioneaza
#
# print("de cate ori apare the in propozitia data:" + str(propozitie.count('the')))
#
# #11
#
# print(propozitie.replace('the', 'THE'))
#
# #12
#
# cuvant=input("cuvant scos:")
# """
# Vartiata I
#
# propozitie=propozitie[:-int(len(cuvant))]
# print(f'indexul cuvantului {cuvant} este {len(propozitie)}')
# print(propozitie)
#
#
# """
# #Varianta II
# print(f'indexul cuvantului {cuvant} este {propozitie.find(cuvant)}')
# index=propozitie.find(cuvant)
# print(propozitie[:index])
#
# #13
#
# propozitie=nume + " "+ str(inaltime) +" "+str(varsta) +" "+ str(admis)
# print(propozitie)

# #14
#
# ##daca pun 0 in fata numarului primesc eroare ,ce e de facut?
# stringul=str("0123456789")
# print(stringul[1::2])
# print(stringul[::2])
#
# #15
#
# lungime=input("lungime=")
# latime=input("latime=")
# aria=int(lungime)*int(latime)
# print(f'aria dreptunghiului este {aria}')

# #16
#
# string_impar=input("string impar=")
#
# print(string_impar[int((len(string_impar))/2):int((len(string_impar))/2)+1])
#
# #17
#
# string_17=input("alege cuvant:")+" "#am adaugat un spatiu la final pentru a lasa programul sa mearga pana la capatul ultimului cuvant
#
# while len(string_17)>0:#cat timp lungimea este mai mare ca 0 cautam cubinte
#     print(string_17[:int(string_17.find(" "))])#cautam primul spatiu intre cuvinte si afisam ce apare pana acolo
#     string_17=string_17[int(string_17.find(" "))+1:]#transformam stringul dat intr-un string fara cuvantul afisat

# #18
#
# string_18=input("alege string:")
# primul_caracter=string_18[0]
# ultimul_caracter=string_18[-1]
# #salvam primul si ultimul caracter pentru a putea sa le adaugam la final ,dupa ce am modificat stringul fata acestea
#
# string_18=string_18[1:len(string_18)-1].replace(primul_caracter,primul_caracter.upper())
#
# print(primul_caracter + string_18 + ultimul_caracter)

#19
user=input('user=')
parola=input('parola=')
dim_parola=len(parola)#salvam dim parolei pentru a putea sa o afisam in str ul final
numarare_stelute=len(parola)#salvam  lungimea parolei intr o valoare pentru a putea sa numaram literele din care este formata ,astfel pentru fiecare litera vom scadea 1

stelute="*"#initializam stelute
while numarare_stelute>1:#fiind alocata o steluta de la inceput este necesar sa ne oprim la 1 nu la 0
    stelute=stelute+"*"
    numarare_stelute=numarare_stelute-1
print(f'Parola pt user {user} este {stelute} si are {dim_parola} caractere')

# #Tema din timpul cursului
# #problema cu pi
# pi = 3.1467123
# print(f"Valoarea lui pi este: {pi}")
#
# print(f"Pi cu doar 2 zecimale este:{str(pi)[:4]}")
#
# #problema cu populatia
#
populatie=input('populatie=')

if populatie.find("mil")>=0:
    populatie = int(populatie.strip('mil')) * 1000000
    print(populatie)
else:
    if populatie.find("bil")>=0:
        populatie = int(populatie.strip('bil')) * 1000000000
        print(populatie)
    else:
        print(populatie)





