class Animal:
    def __init__(self,name,age):
        self._name=name #scruiem cu _ si inswamna ca atributul este protected
        self._age=age

my_dog=Animal('Rex',2)
print(my_dog._name)

# class Bird:
#     def __init__(self):
#         print('Bird created')
#     def who_am_i(self):

class Student:
    def __init__(self,nume,nota):
        self.nume=nume
        self.nota=nota
    def get_grade(self):
        return self.nota
    def set_grade(self,nota_noua):
        verify = True
        while verify:
            try:
                nota_noua = int(nota_noua)
                assert nota_noua>=0 and nota_noua<=10
            except:
                print("invalid option choose")
                nota_noua = input('Selectati noua nota nota:')
            else:
                verify=False
                self.nota = nota_noua
    def student_profile(self):
        print(f'Students name is {self.nume} and has graade {self.nota}')

list_of_stud=[]
while True:

    student_name=input("Student name=")
    if student_name=="Stop":
        break
    student_nota=int(input('Student grade='))
    student1=Student(student_name,student_nota)
    list_of_stud.append(student1)
    # print(type(student1))
# student2=Student('Bogdan',7)
# print(type(student2))
# student3=Student('Liviu',9)
# list_of_stud.append(student1)
# list_of_stud.append(student2)
# list_of_stud.append(student3)

for elem in list_of_stud:
    elem.student_profile()
# d) Filtrati lista de studenti (sau construiti una noua) astfel incat sa ramana doar acei studenti care au o nota de trecere:
# de preferat determinati daca studentul are nota de trecere sau nu folosindu`va de o alta functie a clasei Student

pass_students=[]
print('EX D')
for elem in list_of_stud:
    if elem.get_grade()>=5:
        pass_students.append(elem)
for elem in pass_students:
    elem.student_profile()

#V2
print('V2')
def is_passing_grade(stud):
    return stud.get_grade()>=5
# list_of_stud=list(filter(lambda x:x.get_grade()>=5,list_of_stud))
list_of_stud=list(filter(is_passing_grade,list_of_stud))
for elem in list_of_stud:
    elem.student_profile()

