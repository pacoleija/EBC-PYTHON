from numpy import number


number1 =15
number2=22
print(bin(number1))
print(bin(number2))
print(number1 and number2)
if number1 and number2:
    print("Ok")
else:
    print("No ok")

print(not number1)
print(bin(number1))
print(~number1)
print(bin(~number1))

print('*******************')
#Mascara de bits
bit= number1&number2
print(bit) 

print('****************************')

numeroentero =17

print(numeroentero>>1)
print(bin(numeroentero))

print(numeroentero <<2)
