# # atribute protected: sunt accesibile doar din interiorul clasei si din interiorul claselor care o mostenesc
# class Animal:
#
#     def __init__(self, name, age):
#         self._name = name  # scriem cu _ si inseamna atribut protected
#         self._age = age
#
#
# my_dog = Animal('Rex', 2)
# print(my_dog._name)
#
# my_dog._name = 'Tobi'
# print(my_dog._name)
#
#
# # atribute private: nu sunt accesibile decat din interiorul clasei
# # daca incercam sa le accesam de altundeva, o sa primim eroare
# #nu le putem accesa direct dar le putem folosii daca sunt in functii in clase
# class Animal:
#
#     def __init__(self, name, age):
#         self.__name = name  # scriem cu __ si inseamna atribut private
#         self.__age = age
#
#     def print_name(self):
#         print(self.__name)
#
#     def set_name(self, new_name):
#         self.__name = new_name
#
#
# my_dog = Animal('Rex', 2)
# # my_dog.__name = 'Tobi'
# # print(my_dog.__name)  # eroare fiindca e private
#
# my_dog.print_name()
#
# my_dog.set_name("Tobi")
# my_dog.print_name()

class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property # getter - get field value
    def age(self):
        return self.__age

    @age.setter # setter - sets a new field value
    def age(self,age):
        if age> 0:
            self.__age = age
        else:
            print("Age must be greater than 0.")

    @age.deleter # deleter - delete the field
    def age(self):
        del self.__age

my_dog = Animal('Sara', 11)
my_dog.age = 5
print(my_dog.age)

del my_dog.age
print(my_dog.age)