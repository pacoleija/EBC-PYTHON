import math
x=float(input("Ingresa x: "))
y= math.sqrt (x)

print('La raiz cuadrada de ', x, 'es igual a ', y)

first_number = int (input('Ingresa el primer número:'))
secod_number =int(input('Ingresa el segundo número: '))

try:
    print(first_number/secod_number)
except:
    print('Esa operación no puede ser realizada.')
print ('FIN.')
