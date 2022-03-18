#transformare
#merge
x='14'
x=int(x)

y='1.2'
y=float(y)

#nu merge
#x='14'
#x=float(x)

#y='1,2'
#y=int(y)

#range
#TODO MERGE DOAR CU INT
if x in range(-2,14):
    print('da')
else :
    print('nu')

#swap pyton
y=5
x=1
if y >x:
    x,y=y,x
print(x)
print(y)

#abs = modul
print(abs(5-9))

#vocale
vocale='aeiou'
litera='a'
if litera.lower() in vocale:
    print('l e v')
else:
    print('l nu e v')

#ex 12
#il facem in float ,sa nu inceapa cu 0
#si grija la punct


#ex14 cu max
x=1002
y=2
z=4

print(max(x,y,z))
print(max([1,23,6,100,5]))
print(max('qwerty'))