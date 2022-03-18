print('hello world')
# asa se face un comentariu
# cltl + ? -> comm mai multe linii

'''pyton este un limbaj interpretat
interpretat = codul este citit linie cu linie
compilat = codul este transformat in bytecode ,care apoi este rulat in intregime
'''
#
# """
#
# comm mai multe linii
#
# """
#
# a='''abcdefg'''
# b='merge si asa'
#
# print(a)
# print(b)
#
# """
# Variabile
# are o valoare ,un nume ,o locaite unde se pune
# """
# #conventii de naming
# #snake_case = cel mai folosit in Py
# #camLcase
# #nu poate sa inceapa cu nr,caracteer speciale
#
#
# #pyton este tipizat dinamic (dinamically typed)
# var_a = 10
# var_a = 'un string'
# print(var_a)
#
# var1 , var2 , var3=1,2,3
#
# print(var2)
# print(var1,var2,var3)
# nr=10 #int
# nr2= -1# int
# nr3= 1.5#float
# #nr4= 1+2j complex
# nume='Vlad' #char
# adevar=True #bool
# nume2="Andrei"
#
# #verificam tipul de variabila
# print(type(nume))
#
# #argumente
# # argumente=10
# # print(argument)#functia primita acepta un argument
#
# #type casting
# var1="1"#e str
# #vrem sa fie int
# var1 = int(var1)
# print(type(var1))
#
# """
# eroare dearece "a" nu este int
# nr="123a"
# nr=int(nr)
#
# """
# nume_familie='Stanescu'
# prenume='Tudor'
# print('NUmele meu este :'+nume_familie +' '+ prenume)
# print(f'Numele meu este :{nume_familie}{prenume}')
# print(f'suma dintre 1 si 2 este {1+2}')
#
# varsta = 20
# print("Ma numesc" + prenume + 'si am '+ str(varsta) +" ani!")#type casting
# pi=3.14564574
# print(pi)
# ##TODO: Cum Fac sa afisex pi doar cu 2 zecimal?
# # practic vreau sa afisez 3.14
#
#
# #testare cod
# #conditie assert de adevar
# a=1
# assert a==1 #stii la ce rez sa te astepti ,iar cu assert in verifici
#
# #cand se scrie cu un = inseamna atribuire
# #cand scriem == inseamna is_equal(verificare a egalitatii dintre 2 valori)
#
# #input()-> functie care permite input de la tastatura
# tastatura=input()
#
# print(tastatura)
# print(tastatura)
#
# print(type(tastatura))
# #functia input() returneaza un string
# nr=input("Introduceti nr=")
# #TODO: Se da var pass='12345asd'
# #
# # Creati o bucla care sa accepte parole pana cand introducem cea corecta
# #
# # Tip va puteti ajuta de assert si de mecanismul handling ca sa va asigurati ca parola e cea corecta
# #
# my_name = input('introduce numele:')
# print(my_name)
# nr= input('Introducem un nr:')
# nr=int(nr)
# print(nr)
# print(type(nr))
# '''
# try:
#
#
# '''

# propozitie = "Aceasta este o propozitie"
# ##############0123456789...............
#
# print(propozitie[0])
# print(len(propozitie))
#
# #ultimul caracter
# print(propozitie[len(propozitie)-1])
#
#
# #slicing string[start:stop:step] start = index de inceput , stop =index de orpire (exclude indexul ), step = pas cu care sa mearga
#
# alta_prop='o prop scurta'
# print(alta_prop[0:6])
# print(alta_prop[::2])
# print(alta_prop[:5:2])
# print(alta_prop[-6:])#cand punem - luam  de la capt
#
# populatie='20mil'
# # vreau sa astez populatia la int si sa adaug 0-urile aferente =>2000000
# print(populatie[:2] + "00000")
#
# #caz 2 populatie= '7bil'
# populatie= '7bil'
# populatie=int(populatie.strip('bil')) * 1_000_000_000
# print(populatie)
# #TODO:indiferent ce val primim sa ret int corect
# #test cu populatie='20mil' sau 7bil sau 2000000
#
# # in jupiter n >>>>> s1.replace?