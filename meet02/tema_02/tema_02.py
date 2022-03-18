# #1
# #Un if else este folosit in programe pentru a lua decizii
#
# #2
# print("\tEX_2")
# x=input('x=')
# try:
#     x=int(x)
# except:
#     print("Nu ati introdus un numar")
# else:
#     if x>=0:
#         print(f'{x} este pozitiv')
#     else:
#         print(f'{x} este negativ')
# #3
#     print("\tEX_3")
#     if x>0:
#        print(f'{x} este pozitiv')
#     elif x<0:
#         print(f'{x} este negativ')
#     else:
#         print(f'{x} este neutru')
# #4
#     print("\tEX_4")
#     if x>=-2 and x<=13:
#         print(f'{x} este intre -2 si 13')
#     else:
#         print(f'{x} nu este intre -2 si 13')
# #5
#     print("\tEX_5")
#     y=input("y=")
#     try:
#         y=int(y)
#     except:
#         print('nu ati introdus un nr')
#     else:
#         if y>=x:
#             if y-x>5:
#                 print(f'diferenta {y}-{x} este mai mare decat 5')
#             elif y-x==5:
#                 print(f'diferenta {y}-{x} este 5')
#             else:
#                 print(f'diferenta {y}-{x} este mai mica decat 5')
#         else:
#             if x-y>5:
#                 print(f'diferenta {x}-{y} este mai mare decat 5')
#             elif x-y==5:
#                 print(f'diferenta {x}-{y} este 5')
#             else:
#                 print(f'diferenta {x}-{y} este mai mica decat 5')
# #6
#         print("\tEX_6")
#         if not(x<5 or x>27):
#             print(f'{x} este intre 5 si 27')
#         else:
#             print(f'{x} nu este intre 5 si 27')
#
# #7
#         print("\tEX_7")
#         if x==y:
#             print(f"x=y")
#         elif x>y:
#             print('x este mai mare')
#         else:
#             print('y este mai mare')
# #8
#         print("\tEX_8")
#         z=input('z=')
#         try:
#             z=int(z)
#         except:
#             print('nu ati introdus un nr')
#         else:
#             if x==y and x==z:
#                 print(f"Triunghiul format din laturile {x},{y},{z} este echilateral")
#             elif x==y or x==z or y==z:
#                 print(f"Triunghiul format din laturile {x},{y},{z} este isoscel")
#             else:
#                 print(f"Triunghiul format din laturile {x},{y},{z} este unul oarecare")
#
#
#
#
# #9
# print("\tEX_9")
# vocale="aeiou"
#
# litera=input('litera=')
#
# if vocale.find(litera)>=0:
#     print(f'{litera} este vocala')
# else:
#     print(f"{litera} nu este vocala")

# #10
# print('\tEX_10')
# nota=input('nota primita este=')
#
# try:
#     try:
#         nota=int(nota)
#     except:
#         try:
#             nota=float(nota)
#         except:
#             nota=int(nota)
# except:
#     print(f"nu a fost introdusa o nota valida")
# else:
#
#     if nota>=0 and nota<=10 :
#         if nota >= 9:
#             nota='A'
#         elif nota >= 8:
#             nota='B'
#         elif nota >=7:
#             nota='C'
#         elif nota >=6:
#             nota='D'
#         elif nota >=5:
#             nota='E'
#         else:
#             nota='F'
#         print(f"nota primita este {nota}")
#     else:
#         print(f"nu a fost introdusa o nota valida")
#
# # #11
# print('\tEX_11')
# x=input('x=')
# try:
#     x==int(x)
# except:
#     print('nu ati introdus un numar')
# else:
#     x=str(x)
#     if len(x)==4:
#         print(f"{x} are 4 cifre")
#     else:
#         print(f'{x} nu are 4 cifre')
#     print('EX_12')
# #12
#     if len(x)==6:
#         print(f'{x} are exact 6 cifre')
#     else:
#         print(f'{x} nu are exact 6 cifre')
# #13
#     print('EX_13')
#     x=int(x)
#     if x%2==0:
#         print(f'{x} este par')
#     else:
#         print(f'{x} este impar')
#14
# x=input('x=')
# try:
#     x==int(x)
# except:
#     print(f'{x} nu este un numar')
# else:
#     y=input('y=')
#     try:
#         y==int(y)
#     except:
#         print(f'{y} nu este un numar')
#     else:
#         z=input('z=')
#         try:
#             z==int(z)
#         except:
#             print(f'{z} nu este un numar')
#         else:
#             print(max(x,y,z))
#             print("EX_15")
# #15
#             suma=x+y+z
#             if suma==180:
#                 print('triunghiul este valid')
# #TODO la 16 nu prea am inteles ce e de facut (daca chiar e ceva de facut) :)))))
