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
