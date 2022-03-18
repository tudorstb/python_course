
ture_alergate = 0
#vrem sa alergam atata timp cat avem "suflu"(presupunem ca nu mai avem suflu)
while ture_alergate <15:
    ture_alergate+=1
    print('ai alergat o tura')
else:
    print('ai obosit')

#sintaxa for
for elem in range(5):
    print('ai alergat o tura')

t=('a','v')

for elem in t:
    print(elem)

country={'name':'Romania','population':'19.5','continent':'Europa'}
for key in country:
    print(key,country[key])

fr=['a','b','c']

for idx,elem in enumerate(fr):
    print(idx,elem)

prop="asdawdasdassf asdasda da sd asda sd"

for ch in prop:
    print(ch)

#Break opreste for/while
print('\t bla bla')
for n in range(10):
    if n==5:
        break
    print(n)

#contiune // nu se afiseaza 5// conditia

for nr in range(10):
    if nr==5:
        continue
    print(nr)

#pass
print('inaite de for')
for nr in range(10):
    pass #pass e folosit doar ca sa nu dea eroare in anumite situatii
print('dupa for')

lst1 = ["Black", "White", "Red"]
lst2 = ["Red", "Green"]

print(set(lst1) - set(lst2))

for elem in lst1:
    if elem not in lst2:
        print(elem)



lst = [1,2,3,3,1,1,4,5,5]
lst_v2=[]
for elem in lst:
    if elem not in lst_v2:
        lst_v2.append(elem)
print(lst_v2)

#v2 set nu printeaza duplicate
print(list(set(lst)))


names_list = ["Valentina", "Raluca"," Cristian", "Arthur", "Vlad", "Florina", "Dan", "Tudor", "Gabi"]

#v1

for elem in names_list:
    if elem[0]=='V':
        pass
    else:
        print(f' {elem} este pe pozitia {names_list.index(elem)}')

#v2
for idx,elem in enumerate(names_list):
    if elem[0]=='V':
        pass
    else:
        print(elem,idx)

print('                 ')
print('                 ')
print('                 ')
print('                 ')

# a=input('a=')
# b=input('b=')
#
# if a>b:
#     (a,b)=(b,a)
# lista=[]
# for i in range(int(a),int(b)):
#     if (i % 3 == 0 or i % 7 == 0) :
#         if i % 3 == 0 and i % 7 == 0:
#             pass
#         else:
#             lista.append(i)
# print(lista)

print('                 ')
print('                 ')
print('                 ')
print('                 ')

n=15

while n>0:
    print(n)
    if n%5==0:
        n-=2
    elif n%2==0:
        n-=3
    else:
        n-=1


print('                 ')
print('                 ')
print('                 ')
print('                 ')
while True:
    n=input('n=')
    if n=='stop':
        break
    try:
        n=float(n)
    except:
        print('nu ati introdus un nr ')
    else:
        n=int(n)
        while n>=0:
            print(n)
            n-=1
