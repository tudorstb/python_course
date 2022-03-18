#liste
#este ordonata
#lista este mutabila
my_list=[1,23,True,'stringul_meu',3.5,('a','c',1),{'key':'val'}]

print(my_list)
my_list.append('capat')
print(my_list)

v='adad'

my_list=[1,2,4,5,6,6]
my_list.insert(2, 'q')
print(my_list)
#merge sa + o lista cu o alta valoare o data ce valoarea o facem intr-o lista => adaug=[valoarea_introdusa]

lst=['a','b','c']
lst.append('d')
print(lst)

#index
print(lst.index('b'))


#Todo tuple
#imutabile
#ordonate si indexate

t=(12,True,'qwerq',[1,2,3])

#nu merge append deoarece este imutabil
#adaugare tupla
t=(t,100)

# print(t.count('a'))
# print(t.index('a'))

#tuple unpaking,se foloseste la functii cand se ret mai multe valori
x=4
y=5
x,y=y,x

def my_func():
    return 1,2
func_returned_value=my_func()
print(func_returned_value)
print(type(func_returned_value))

a,b=my_func()
print(a)
print(b)
print(type(a))

#dict
#key - porecla pt input
#e neindexat (nu il accesam prin numere 0,1,2,3, )il accesam prin key
my_dict={'key':'value'}#construieste ca un dictionar {termen;definitia_termenului}
#print(my_dict[1]) nu merge
print(my_dict['key'])
#este neordonat in comparare => '==' verifica continutul
#TODO dict este ordonat / in pyton 2 nu era
my_dict_1={'key':'value','key2':'value2'}
my_dict_2={'key2':'value2','key':'value'}

print(my_dict_1== my_dict_2)

#dictionarul este mutabil
my_dict_1={'a':1,'b':2}
#vrem sa adaugam 'c' cu valoarea 3
my_dict_1['c']=3
print(my_dict_1)

#ce putem pune in dict ca key si value
d={'un_string':'value_string','tot_string':102,10:'value_str2','lista?':[1,2,3]}
print(d)
#merge sa adaugam orice strc de date ,pana si un alt dict
#d={[1,2,3]:"o valoare random ,nu conteaza ca verificam cheia"} #dict are constructia key:value
#prit(d) #nu poti avea o lista drept key intr-un dict ,pt ca lista e mutabila

#pyton nu poate risca sa i se modifice key-ul,deoarece nu accepta chei mutabile


#TODO de ce exista tuple =>deoarece poate fi folosita drept cheie in dict deoarece este imutabila


#Set => similare liste
#nu sunt ordonate
#nu sunt indexate,nu sunt ordonate

s={'alb','rosu','negru','albastru'}
#constructor=
s=set()
#merge si la liste l=lst[....
#se poate transforma lista in set
s=set(['alb','rosu','negru','albastru'])
s2=set(['z','rosu','negru','y'])

print(s==s2)

#setul e mutabil
s.add("verde")
print(s)
s1=set(['c','rosu','negru','d'])
#Union_elemente distincte
print(s1|s2)

#setul nu contine elem multiplicate /este luat mai mult ca o multime
s3={1,2,3,1,2}
print(s3)

#intersectie
print(s1 & s2)

#difference-elem unice din primul set
print(s1-s2)

#diferenta simetrica - elem fara cele comune
print(s1 ^ s2)

animals1 = {"wolf", "cheetah", "elephant", "crocodile"}
st1 = ["horse", "chimpanzee"]


for elem in st1:
    animals1.add(elem)
print(animals1)