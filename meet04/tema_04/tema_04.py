# #1
# print('\tEX_1')
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# print('\ta)')
#
# for elem in masini:
#     print(f'Masina mea preferata este {elem}')
#
# print('\tb)')
#
# for i in range(len(masini)):
#     print(f'Masina mea preferata este {masini[i]}')
#
# print('\tc)')
# l=len(masini)
# n=0
# while l>0:
#     print(f'Masina mea preferata este {masini[n]}')
#     n+=1
#     l-=1

#
# print('\tEX_2')
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
#
# for i in range(1,len(masini)-1):
#     masini[i]=masini[i].upper()
# else:
#     print(masini)
#
# print('\tEX_3')
#
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
#
# for elem in masini:
#     if elem=='Mercedes':
#         print('am gasit masina dorita de dumneavoastra')
#         break
#     else:
#         print(f'am gasit masina {elem} ,mai cautam')
#
# print('\tEX_4')
#
# for elem in masini:
#     if elem=='Trabant' or elem=='Lastun':
#         continue
#     else:
#         print(f's-ar putea sa va placa masina {elem}')
#
# print('\tEX_5')
#
# masini_vechi=[]
#
# for elem in masini:
#     if elem == 'Trabant' or elem == 'Lastun':
#         masini_vechi.append(elem)
#         masini[masini.index(elem)]='Tesla'
#
# print(masini_vechi)
# print(masini)
#
# print('\tEX_6')
# pret_masini = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
#
#
# buget=input('Bugetul clientului=')
#
# try:
#     buget=int(buget)
# except:
#     print('nu ati introdus o suma valida')
# else:
#     for elem in pret_masini:
#         if pret_masini[elem] < buget:
#             print(f"pentru un buget de {buget} puteti sa alegeti masina {elem}")
#
# #dict.items
#
# try:
#     buget=int(buget)
# except:
#     print('nu ati introdus o suma valida')
# else:
#     for elem in pret_masini.items():
#         if int(elem[1])< buget:
#             print(f"pentru un buget de {buget} puteti sa alegeti masina {elem[0]}")

# print('\tEX_7')
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
#
# nu_count_he_he=0
#
# for elem in numere:
#     if elem == 3:
#         nu_count_he_he+=1
# print(f'3 apare de {nu_count_he_he} ori')
#
# print('\tEX_8')
#
# nu_sum_he_he=0
# for elem in numere:
#     nu_sum_he_he+=elem
# print(f'suma numerelor este {nu_sum_he_he}')
#
# print('\tEX_9')
# nr_max=numere[0]
#
# for elem in numere:
#     if elem > nr_max:
#         nr_max=elem
#
# print(f'cel mai mare numar este {nr_max}')
#
# print('\tEX_10')
# for elem in numere:
#     if elem>0:
#         numere[numere.index(elem)]=-elem
#         print(elem)
# print(numere)

# print('\tEX_11')
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
#
#
# for elem in alte_numere:
#     if elem%2==0:
#         numere_pare.append(elem)
#     else:
#         numere_impare.append(elem)
#     if elem>=0:
#         numere_pozitive.append(elem)
#     else:
#         numere_negative.append(elem)
#
# print(f'nr pare={numere_pare}')
# print(f'nr impare={numere_impare}')
# print(f'nr pozitive={numere_pozitive}')
# print(f'nr negative={numere_negative}')
#
# print('\tEX_12')
#
# # for elem in alte_numere:
# #     print(f'elem curent comparat:{elem}')
# #     for i in range(alte_numere.index(elem)+1,len(alte_numere)):
# #         print(f'pozitie:{alte_numere.index(elem)+1}')
# #         if elem>alte_numere[alte_numere.index(i)]:
# #             (alte_numere[alte_numere.index(elem)],alte_numere[alte_numere.index(i)])=(alte_numere[alte_numere.index(i)],alte_numere[alte_numere.index(elem)])
#
#
# print(alte_numere)
#
# for i in range(len(alte_numere)):
#     for j in range(len(alte_numere)-1):
#         if alte_numere[j]>alte_numere[j+1]:
#             (alte_numere[j],alte_numere[j+1])=(alte_numere[j+1],alte_numere[j])
#
# print(alte_numere)
#
# print('\tEX_13')
# import random
# numar_secret=random.randrange(1,30)
# nr_inceput=1
# nr_final=30
# while True:
#     numar=input(f'Ghiceste un numar intre {nr_inceput} si {nr_final}:')
#     try:
#         numar=int(numar)
#     except:
#         print("Nu ati introdus un nr")
#     else:
#         if numar== numar_secret:
#             print('Felicitari,ai ghicit')
#             break
#         elif numar<numar_secret:
#             print('Nr secret e mai mare')
#             nr_inceput=numar
#         else:
#             print('Nr secret e mai mic')
#             nr_final=numar

# print('\tEX_14')
# numar=input("numar=")
# numar=int(numar)
# for i in range(numar+1):
#     print(i*str(i))

print('\tEX_15')
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]

for i in range(len(tastatura_telefon)):
    lista_curenta=tastatura_telefon[i].copy()
    for j in range(len(tastatura_telefon[i])):
        print(f'elementul curent este {lista_curenta[j]}')

fruits = ['apple', 'pear', 'cherry', 'mango']
for i, j in enumerate(fruits):
    print(i, j)
country = {'name': 'Romania' , 'population': '19.5mil', 'continent': 'Europe'}
for i, j in enumerate(country):
    print(i, j)

looping = True
while looping:
    nr = input('Please insert your natural number: ')
    try:
        nr = int(nr)
    except ValueError as e:
        print(f'Please input a valid number! You got an exception: {e}')
    else:
        looping = False
        for i in range(0, nr):
            print(i)