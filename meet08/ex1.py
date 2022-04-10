import csv
# #importuri in python
# from datetime import datetime
# from math import sqrt
# from math import factorial
# data=datetime.now()
# print(data)
#
# print(sqrt(14))
#
# #Import libraries
# #v1:from library import func
#
#
# from math import *
# #"*" inseamna ca importam totul
#
# print(prod([2,3,4,5]))
#
# #v2
# import math
# math.factorial(16)
#
# #v3
# import math as mathematisc
# mathematisc.factorial(16)
#
# import os
# print(os.listdir())
#
# import sys
# print(sys.path)
#
# with open('file.txt','r') as f:
#     file_content=f.read()
#
# with open('file.txt','w') as f:
#     f.write('bla bla')
# print(file_content)


# Given the csv file student_grades.csv:
# 1. List the contents of the file as a list of dicts, a row being a dict of form:
# {"student_name": <name_of_student>, "subject": <name_of_subject>, "grade": <grade>}
# 2. Sort the contents of the file based on student`s name and saved it back like that
# 3. List the student that has the most grades and how many it has
# 4. Write a function that returns the overall grade average for every student in a dict of form {student_name1: grade_avg1,..}
rows=[]
list_of_stud=[]
with open ("student_grades.csv",'r') as csv_file:
    csv_reader=csv.reader(csv_file)
    for row in csv_reader:
        #v1
        student_dict={}
        student_dict["student_name"]=row[0]
        student_dict["name_of_subj"]=row[1]
        student_dict["grade"]=row[2]
       #v2
        student_dict={
                'student_name':row[0],
                'name_of_subj':row[1],
                'grade':row[2]
        }
        list_of_stud.append(student_dict)


print(list_of_stud)
rows=[]
with open("student_grades.csv",'r') as csv_file:
    reader=csv.reader(csv_file)
    for row in reader:
        rows.append(row)

print(sorted(rows))
sorted_rows=sorted(rows)
#v2
#rows.sort()
with open("student_grades_sorted.csv",'w',newline='') as csv_file:
    writer=csv.writer(csv_file)
    writer.writerows(sorted_rows)

dict_count={}

#name:count
#Andrew:1
#Eveline:1
#Celine:3
#Matthew:2
for elem in sorted_rows:
    if elem[0] in dict_count:
        dict_count[elem[0]]+=1
    else:
        dict_count[elem[0]]=1
print(dict_count)
#v1
max=-1
max_key=""
for key in dict_count:
    if dict_count[key]>max:
        max=dict_count[key]
        max_key=key

print(max_key,dict_count[max_key])
dict_medie={}
for elem in sorted_rows:
    if elem[0] in dict_medie:
        dict_medie[elem[0]].extend([elem[2]])
    else:
        dict_medie[elem[0]]=[elem[2]]
print(dict_medie)

for key in dict_medie:
    medie=0
    for elem in dict_medie[key]:
        medie+=int(elem)

    medie=medie/len(dict_medie[key])

    dict_medie[key]=medie
print(dict_medie)
