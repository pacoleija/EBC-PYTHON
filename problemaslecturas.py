from cmath import e
from ntpath import join


cadena1="arbol"
telefono="4445470200"

#print(cadena1)
#print(cadena1[1])
#for letra in cadena1:
#   print(letra)

#print(len(cadena1))

numero=55
#print(str(numero))

#for index in range(len(telefono)):
#    print(telefono[index], end='-')
#print()
#for letra in telefono:
#    print(telefono, end='_')

ABC='abcdefg'

print(ABC[0:1])
print(ABC[0:2])
print(ABC[0:3])

print(ABC[1:1])
print(ABC[1:2])
print(ABC[1:3])

t=[0,1,2]
print(min(t))   

correo='michelle2909@live.com'
""" print(correo)
print (list(correo)) """



reverseMail=list(correo)
reverseMail.pop()
print(reverseMail)

print('amkajamasko'.count('a'))

print(correo.capitalize())

print(correo.upper())

print('['+ correo.center(50) +']')

print(f'[{correo.center(50, "*")}]')

print(correo.endswith('.com'))

print(correo.find ('che')) #Solo sirve con cadenas

print(correo.index('e'))

nobreCompleto = ['Abril', 'Michelle' ,'Gamiño']

my_name=' '.join (nobreCompleto) 

print(my_name.replace('Abril', 'Mayo').lstrip().lower())

paises = ['México', 'Honduras', 'Agerntina', 'Chile', 'Peru','Brasil']

print(sorted(paises))
