from tkinter import Variable


lista1=[1,2,5,8,23,52]
for i in lista1:
    print(i)

print('***********************')

for number in lista1:
    print(number)

lista1.append(24)
print(lista1)

for number in lista1:
    print(number)

lista1.remove (5)
print(lista1)

lista1.insert (1,86)
print(lista1)

lista1.pop ()
print(lista1)

lista1.reverse()
print(lista1)

lista1.sort()
print(lista1)

lista1.clear()
print(lista1)

print('***************************')


lista2_=[1,5,3,[8,78,4]]
for x in lista2_:
    print(x)

lista2_=[1,5,3,[8,78,4]]
for x in range(len(lista2_)):
    print(x)

print(lista2_,x)

if x ==3:
    for y in range(len(lista2_[x])):
     print(lista2_[x][y])
else:
    print(lista2_[x])

persona =['Francisco', 'Leija', 10, ['licenciatura1', 'licenciatura2']]
print(persona)

for value in persona:
    print (value)
print('***************')

persona1 =['Francisco', 'Leija', 10, ['licenciatura1', 'licenciatura2']]
persona2 =['Missael', 'Leija', 23, ['licenciatura1']]
persona3 =['Abril', 'Gamino', 10, ['licenciatura', 'Programacion']]

listadeusuarios=[]
def registar_usuarios(usuario):
    listadeusuarios.append(usuario)
registar_usuarios(persona1)
registar_usuarios(persona2)
registar_usuarios(persona3)
print(listadeusuarios)

print('******************')

for usuario in listadeusuarios:
    print(usuario)
