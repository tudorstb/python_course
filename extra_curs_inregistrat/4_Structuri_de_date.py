#listele in pyton pot sa cuprinda elem de tipuri diferite
#au dimensiune dinamica
#accesam elemente prin index,care incepe cu 0


fructe=['mar', 'banana', 'portocala',3,True,3]


#afisare lista
print(fructe)

#accesam un elem in functie de index
print(fructe[1])

#adaugam un elem
fructe.append('Galbene')
print(fructe)

#suprascriere
fructe[0]="para"
print(fructe)

#dimensiune
print(len(fructe))

#scoate si ne returneaza ultiumul element
last=fructe.pop()
print(last)
print(fructe)

print(fructe.count(3))
#extindem lista
fructe_exotice=['ananas','kiwi']
fructe.extend(fructe_exotice)
print(fructe)

#dict = reprezentare de date in sisteme cheie valoare
#declaram si initializam un dict
note_elevi={'Gigel':10, 'Costel':9, 'Dani':7}
