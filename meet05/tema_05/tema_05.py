#1
print("\tEX_1")
def sum(nr_1,nr_2):
    return nr_1+nr_2

print(sum(1,2))
print(sum(3,2))

#2
print("\tEX_2")
def nr_odd_even(nr):
    if nr%2==0:
        return True
    else:
        return False

print(nr_odd_even(3))
print(nr_odd_even(32))

#3
print("\tEX_3")

#middle name may not exist so we make it optional
def name_len(f_name,l_name,middle_name=('')):
    return len(f_name)+len(l_name)+len(middle_name)

print(name_len('Tudor','Stanescu','Bogdan'))
print(name_len('Tudor','Stanescu'))

#4
print("\tEX_4")



def rectangle_area(L,l):
    try:
        l=float(l)
        L=float(L)
    except:
        if type(L)!=type(1.2) and type(l)!=type(1.2):
            print(f'{L} and {l} values is not accepted for lenght of rectangle')
        elif type(L)!=type(1.2):
            print(f'{L} value is not accepted for lenght of rectangle')
        else:
            print(f'{l} value is not accepted for lenght of rectangle')
    else:
        return l*L

print(rectangle_area(6,2))
print(rectangle_area(10,2))


#5
print("\tEX_5")

def circle_area(r):
    try:
        r=float(r)
    except:
        print(f'{r} value is not accepted ,try entering a number')
    else:
        return round(3.14159265359*r*r,2)

print(circle_area(3))
print(circle_area(4))


#6
print("\tEX_6")

def ch_in_string(ch,string):
    if ch in string:
        return True
    else:
        return False

print(ch_in_string('c','acadea'))
print(ch_in_string('x','acadea'))

#7
print("\tEX_7")

def nr_lower_upper(string):
    lower=0
    upper=0

    for elem in string:
        if elem==elem.upper():
            upper+=1
        elif elem==elem.lower():
            lower+=1
    print(f'{string} has {lower} ch on lower case and {upper} on upper ')


nr_lower_upper('AcAcS')
nr_lower_upper('AcAcooooo')

#8
print("\tEX_8")

def poz_nr(*args):
    list_poz=[]
    for arg in args:
        if arg>0:
            list_poz.append(arg)
    return list_poz

print(poz_nr(*[1,-2,4,-6,8,-5]))

#tot nu prea am inteles care era faza cu * din apelarea functiei :)))

#9
print("\tEX_9")

def compare_2_nr(x,y):
    if x==y:
        print('The 2 numbers are equal')
    elif x>y:
        print(f'{x} is greater then {y}')
    else:
        print(f'{y} is greater then {x}')

compare_2_nr(2,3)
compare_2_nr(3,2)
compare_2_nr(2,2)

#10
print("\tEX_10")

def nr_in_set(nr,*numbers):
    if nr in numbers:
        print('Elem already in set')
        return False
    else:
        print('Elem added to set')
        return True

val=nr_in_set(3,*(3,5,'t','4'))
print(val)
val=nr_in_set(3,*('t'))
print(val)

#11
print("\tEX_11")

months={'january':31,
        'february':28,
        'march':31,
        'april':30,
        'may':31,
        'june':30,
        'july':31,
        'august':31,
        'september':30,
        'october':31,
        'november':30,
        'december':31
        }
def len_month(month):
    return months[month]

print(len_month('february'))
print(len_month('december'))

#12
print("\tEX_12")
#
# def calculator(option,nr_1,nr_2):
#     if option=='Suma':
#         return nr_1+nr_2
#     elif option=='Diferenta':
#         return nr_1-nr_2
#     elif option=='Inmultirea':
#         return nr_1*nr_2
#     elif option=='Impartirea':
#         return nr_1/nr_2
#     else:
#         return "invalid option"

def calculator(nr1,nr2):
    return nr1+nr2,nr1-nr2,nr1*nr2,nr1/nr2

a,b,c,d=calculator(3,4)

print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)

#13
print("\tEX_13")
dict_nr={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
def count_nr(*args):
    for arg in args:
        dict_nr[arg]+=1
    return dict_nr

print(count_nr(*[1, 3, 1, 5, 9, 7, 7, 5, 5]))


#14
print("\tEX_14")

def max_3_nr(nr_1,nr_2,nr_3):
    return max(nr_3,nr_2,nr_1)

print(max_3_nr(1,2,3))
print(max_3_nr(1,3,2))
print(max_3_nr(3,1,2))

#15
print("\tEX_15")

def sum_to_nr(nr):
    sum=0
    for i in range(nr+1):
        sum+=i
    return sum

print(sum_to_nr(4))
print(sum_to_nr(3))

#16
print("\tEX_16")


#17
print("\tEX_17")

def repeat_list(list1,list2):
    list1=set(list1)
    list2=set(list2)
    return(list1 & list2)


print(repeat_list([1, 1, 2, 3],[2, 2, 3, 4]))


#18
print("\tEX_18")

def discount(discount,sum):
    if discount>0 and discount<=100:
        sum_copy=sum
        sum_copy=(sum_copy*discount)/100
        sum-=sum_copy
    else:
        return f"O reducere de {discount}% este invalida"


print(discount(-10,400))
print(discount(10,400))
print(discount(20,400))
print(discount(100,400))
print(discount(101,400))

#19
print("\tEX_19")
from datetime import datetime
def current_time():
    now=datetime.now()
    return now.strftime("%d"),now.strftime("%H")

date,time=current_time()

print(f"current day is {date} and current is {time} ")

#20
print("\tEX_20")
from datetime import date
b_day=date(1,8,16)
def time_to_bday():
    now = datetime.now()
    present=date(1,int(now.strftime("%m")),int(now.strftime("%d")))

    return b_day-present

days_till_bd=time_to_bday()
print(days_till_bd.days)

#21
print("\tEX_21")

def is_prime(nr):
    prim=True
    for i in range(2,nr):
        if nr%i==0:
            prim=False
    return prim

print(is_prime(17))
print(is_prime(8))

#22
print("\tEX_22")

