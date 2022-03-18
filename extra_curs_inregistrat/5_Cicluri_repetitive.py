
#masina merge cat timp are benzina
litri_benzina=10
while litri_benzina > 0:
    #acceleram
    print('Vrum Vrum')
    #scadem benzina
    litri_benzina=litri_benzina-1
    if litri_benzina<=3:
        print('beculetul rosu')
print('Stop!')

#dalmatieni din 2 in 2
for i in range(1,101,2):
    print(f'Dalmatianul cu nr {i} ')

numere = [3,7,10,20,30]
#parcurgere lista cu for prin interediul indexului
for i in range(0,len(numere)):
    print(numere[i])
