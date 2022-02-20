from numpy import outer


numero1 = 2
numero2 =4

mul = numero1 *numero2
sum = numero1 + numero2
sub = numero2 - numero1
div = numero2 / numero1


print(mul)
print(sum)
print(sub)
print(div)

print('\n *********************')
numero1 += numero2

mul = numero1 *numero2
sum = numero1 + numero2
sub = numero2 - numero1
div = numero2 / numero1
div2 = numero2 // numero1

print(mul)
print(sum)
print(sub)
print(div)
print(div2)

Edad = 25
EdadLegal = 18
Resultado = "Eres mayor de edad" if Edad >= EdadLegal else "Eres menor de edad"
print(Resultado)
