# #1
# print("\tEX_1")
# note_muzicale=['do','re','mi','fa','sol','la','si','do']
#
# #a)
# print(note_muzicale)
#
# #b)
# #V1
# note_muzicale=note_muzicale[::-1]
# # note_muzicale.reverse()
# #V2
# #nu inteleg de ce nu merge pana la ultimul element
# '''note_muzicale_inversa=[]
# note_muzicale_f=note_muzicale
# for elem in note_muzicale:
#     note_muzicale_inversa.append(note_muzicale_f.pop(-1))
# print(note_muzicale_inversa)'''
#
# #c)
# print(f"lista inversata:{note_muzicale}")
# #d)
# note_muzicale.reverse()
# #e)
# print(f"lista initiala:{note_muzicale}")
#
# #2
# print("\tEX_2")
# print(f"do apare de {note_muzicale.count('do')} ori")
#
# #3
# print("\tEX_3")
# l_1=[3, 1, 0, 2]
# l_2= [6, 5,0, 4]
#
# # print("V1")
# # l_1=l_1+l_2
# # print(l_1)
#
# print('V2')
# l_1.extend(l_2)
# print(l_1)
#
# #4
# print("\tEX_4")
#
# l_1.sort()
# print(f"lista sortata este:{l_1}")
#
# while 0 in l_1:
#     l_1.pop(l_1.index(0))
# print(f"lista fara 0 este :{l_1}")
# #TODO
# ''' nici aici nu prea inteleg de ce forul nu vrea sa citeasca index cu index sau noh elem cu elem
# l_1_fara_0=l_1
#
# for elem in l_1:
#     if elem==0:
#         l_1_fara_0.pop(l_1.index(elem))
# '''
#
# #5
# print("\tEX_5")
# #7
# print("\tEX_7")
#
# l_1.clear()
#
# if l_1==[]:
#     print('lista este goala')
# else:
#     print("lista nu este goala")
#
# #6
# print("\tEX_6")
# l_1.clear()
#
# #8
# print("\tEX_8")
#
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5 , 'Marcel':6,'Daniel':9}
#
# print(f'Elevi din dict1 sunt:{dict1.keys()}')
#
# #print(type(dict1.keys()))
#
# #9
# print("\tEX_9")
#
# dict1_cpy=dict1
# print(dict1_cpy)
#
# #am observat ca functia '.popitem' ne returneaza un touple ,un tip de date indexat ceea ce ne ajuta sa afisam indesx cu index pe parcurs ce scoatem cate o grupa din dict
# while dict1!={}:
#     pop=dict1.popitem()
#     print(f'{pop[0]} a luat nota {pop[1]}')
#     print(dict1_cpy)
# #
# dict1=dict1_cpy
# #todo am observat ca nu putem sa copiem un dictionar ,sau cel putin nu in mocul clasic ,sau il ca pointer?
#
# #10
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5 , 'Marcel':6,'Daniel':9}
# print("\tEX_10")
# dict1['Dorel']=6
# print(f'Dorel a primit nota {dict1["Dorel"]} dupa contestatie')
#
# #11
#
# print("\tEX_11")
# dict1.pop('Dorel')
# dict1['Ionica']=9
# print(dict1)
#
# #12
# print("\tEX_12")
#
# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'a', 'miercuri'}
#
# zile_sapt.add('luni')
# print(zile_sapt)
# #observam ca in set nu se repeta elem
#
# #13
# print("\tEX_13")
# adevar=0
# for elem in weekend:
#     if elem not in zile_sapt:
#         adevar=adevar+1
# if adevar==0:
#     print('da')
# else:
#     print('nu')

# #14
# print("\tEX_14")
#
# print(f"Diferentele dintre cele 2 seturi:{zile_sapt}-{weekend}={zile_sapt - weekend}")
# print(f'                                 {weekend}-{zile_sapt}={weekend - zile_sapt}')
#
# #15
# print("\tEx15")
# print(f"Intersectia dintre cele 2 seturi este:{zile_sapt & weekend}")
#
# #16
# print("\tEx16")
#
# jucatori=['Alin','Teo','Stasiuc','Mihaita','Dodo']
# schimbari_max = 3
#
# while schimbari_max!=0:
#     alege_jucator=input("alege jucator pentru a iesi de pe teren:")
#     if alege_jucator in jucatori:
#         jucator_nou = input('alege jucator pentru a intra pe teren:')
#         jucatori.pop(jucatori.index(alege_jucator))
#         jucatori.append(jucator_nou)
#         schimbari_max=schimbari_max-1
#         print(f"a intrat {jucator_nou} si a iesit {alege_jucator} si mai aveti {schimbari_max} schimbari" )
#     else:
#         print(f'nu se poate efectua schimbarea deoarece jucatorul {alege_jucator} nu e in teren')
#         print(f'mai aveti {schimbari_max} schimbari')
# print(f"echipa finala este:{jucatori}")
#
# #17
# print("\tEx17")
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# fructe_cu_e=[]
# fructe_6_litere=[]
# for elem in fruits:
#     if 'e' in elem:
#         fructe_cu_e.append(elem)
#     if len(elem)==6:
#         fructe_6_litere.append(elem)
#
# if fructe_cu_e==[]:
#     print("nu avem fructe ce contin litera \"e\"")
# else:
#     print(f'fructele ce contin litera \"e\" sunt:{fructe_cu_e}')
#
# #18
# print("\tEx18")
# if fructe_6_litere==[]:
#      print('nu avem fructe din 6 litere')
# else:
#     print(f'fructele formate din 6 litere sunt:{fructe_6_litere}')

# #EX_9_V2
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
#
# for elem in dict1:
#     print(f'{elem} a luat nota {dict1[elem]}')

#copiere lista
l1=[1,2,3,4]


# l2=list(l1)
# print(l2)
# print(l1)
#
# l2.pop()
#
# print(l2)
# print(l1)

l2=l1.copy()

print(l2)
print(l1)

l2.pop()

print(l2)
print(l1)
