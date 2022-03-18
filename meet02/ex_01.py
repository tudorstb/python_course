# #tema de la cursul_01
# print("asdas \"asdasdasdad\"")
# #\ este escape character
#
# print(3//2)#partea intreaga ->int
# print(3/2)#->float
# print(3%2)#->rest
#
# #merge sa inmultim un str cu un int
# s="yes"
# print(s*3)
#
# ##Cursul_02
# #paritate
# x=3
# print(x%2==0)
# #
# print(x**3)
# print(pow(x,3))#fct echivalenta cu op **
#
# #comparare
#
# s1='abcd'
# s2='bcd'
# print(s1>s2) #compararea se face alfanumeric
# #merge pe fiecare pozitie si compara caracterele
# #compara carecter cu caracter
#
# x=10
# y=8
# z=9
# #verific daca x este mai mare ca y si daca este mai mare z
#
# print(x > y and x > z)
# #not
# adev=True
# print(not adev)
#
# #TODO and are prioritate
# print(True or False and False)
# #=> True or (False and False)
#
# a,b=10,10
# c=a
#
# #
# a is b
# #id-ul
# id(c)
#
# #liste
# x=3
# a_list = [1,23,4,5]
# print(x in a_list)
#
# text = '1,23,4'
# print('1,23' in text)
#
# # 1)IF
#
# if conditie:
#     #do something when cond is True
# elif alt_cond:
#     #do something when alt_cond is True after cond was False
# else
#     #do something when niether cond nor alt_cond is true
#
# #elif si else pot sa nu apara (obtionale)







# #2)bucla for
# lst=[1,2,3]
# for elem in lst:
#     print(elem)
# print('Gata forul\n')
#
# #3)bucla while

string="fox, cat, cow, horse"
string="dog, fox, cat, cow, horse"
if string.find("monkey")>=0:#find returneaza primul indx la care gaseste stringul cautat
    print("You found your dog")
else:
    print("horse")
print(string.find("monkey"))

# #exception handeling
# try:
#     #aici avem cod care functioneaza fara erori
# except:
#     #aici intram cand apar erori ,pe care le solutionam intr-un fel sau altul
#     #daca sunt exceptii /erori ,,try nu se va ma execurta
# else:
#     #se executa in cazul fara erori ,in continuarea lui try
# finally:
#     #se executa mereu
# #else si finally nu e musai sa apara

print(ord('a'))

a=12
b=12
c=a

print(id(a))
print(id(b))
print(id(c))

print(a is b)

a = [1, 2]
b = [1, 2]
c = a

print(id(a))
print(id(b))
print(id(c))

print(a is b)

#
x = 5
a_list = [1,23,4,5]
print(x in a_list)
#TODO cautare

animals = 'dog, foxy, cat, horse'
a = 'fox'

print(f" animale_1:{a in animals}")

#
animals = 'dog, foxy, cat, horse'
a = 'fox'
list_of_animals = animals.split(", ")
print(list_of_animals)

print(a in list_of_animals)

text = '1,23,4'
print('1,23' in text)

# 2) bucla for
lst = [1, 2, 3]
for elem in lst:
    print(elem)
print('Gata forul\n')

# 3) bucla while
n = 3
while n > 0:
    print(n)
    n -= 1  # n = n - 1
#     print('Gata while\n')   # daca aveam print aici, ne afisa dupa fiecare print(n)

print('Gata while\n')
