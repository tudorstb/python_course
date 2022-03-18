#V1 folosind if - else -if -else
populatie=input('populatie=')

if populatie.find("mil")>=0:
    populatie = float(populatie.strip('mil')) * 1000000
    populatie = int(populatie)
    print(populatie)
else:
    if populatie.find("bil")>=0:
        populatie = float(populatie.strip('bil')) * 1000000000
        populatie=int(populatie)
        print(populatie)
    else:
        populatie=int(populatie)
        print(populatie)

#V2 folosint elif in loc de if else

populatie=input('populatie=')

if populatie.find("mil")>=0:
    populatie = float(populatie.strip('mil')) * 1000000
    populatie = int(populatie)
    print(populatie)
elif populatie.find("bil")>=0:
    populatie = float(populatie.strip('bil')) * 1000000000
    populatie=int(populatie)
    print(populatie)
else:
    populatie=int(populatie)
    print(populatie)
