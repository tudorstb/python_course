#telefon din tema
# for rand in tastatura_telefon:
#     for buton in rand:
#         print(buton)

#functii
def greeting():
    print('Hello!')

greeting()

#parametrii optionali
def greeting_2(name='World'):
    print(f'Hello {name}')

greeting_2()
greeting_2("john")

#parametrii optionali se pun ultimii sau dau eroare

#vrem sa adunam 4


#args
def sum(*args):
    s=0
    for arg in args:
        s+=arg
    return s

print(sum(1,2,3,4,5,6,7,7))

def sum_of_pop(**kwargs):
    print(type(kwargs))
    s=0
    for key in kwargs:
        s+=kwargs[key]
    return s



print(sum_of_pop(**{"Romania":19000000,'moldova':12222222}))

def greeting_and_sum_of_n_numbers(name, *args):
    print(f'salut,{name}')
    s =0
    for arg in args:
        s +=arg
    return s

print(greeting_and_sum_of_n_numbers('ioan',3,4,5))

def get_population(**kwargs):
    s=0
    for key in kwargs:
        s+= kwargs[key]
    print(s)
get_population(Bucuresti=1,Cluj=2,Aiud=3)

print("""""""""""""""""""")

# nr=int(input("nr="))
# def to_number(nr):
#     for elem in range(1,nr):
#         print elem
# to_number(nr)

# y=int(input('y='))
# x=int(input('x='))
#
# def power(x,y=2):
#     print(x**y)
#
# print(f'The result of x={x} to the power of y={y} is:{power(x,y)}')

def s(name):
    name_2=name[0]+name[len(name)//2]+name[len(name)-1]
    print(name_2)

s('Tudore')

def append_middle(s1,s2):
    s1=s1[:len(s1)//2]+s2+s1[len(s1)//2:len(s1)]
    print(s1)
append_middle('Legendary', 'wait')

def coma_separated(*args):
    string=''
    for elem in args:
        string+=elem+'-'
    return string[:-1]

print(coma_separated('one', 'two', 'three', 'four', 'five'))