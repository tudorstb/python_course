# Recapitulare

pi=3.142123

print(round(pi,2))

#OOP
    #clase

class Car:
    #fields(atribute)
    make='Dacia'
    model="1211"
    year=2022
    def __init__(self,imput_brand,i_model,i_year):
        self.imput_brand

#methods
    def accelerate(self):
        print('Vrum Vrum')
    def show_year(self):
        print(self.year)


    def stop(self):
        print("stop")


#initializam instanta
my_car=Car()
my_car.accelerate()
my_car.show_year()

class Rectangle:
    lenght=4
    width=2

    def get_area(self):
        return self.lenght*self.width
    def desen(self,outline='*'):
        print()

