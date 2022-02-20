from sre_constants import RANGE


Edad =25
Nombre = "Abril"
EdadLegal = 30
if Edad >= EdadLegal:
    print(f"Felicidades {Nombre} por tus {Edad} años")
else:
    print(f"Hola {Nombre} aun eres menor de edad")
    print("Chale")

Steps =10
for i in range(Steps):
    print(f"Paso número #{i}")

i=0
while (i< Steps):
    i=i+1
    print("runnig")

print('\n*****************************')

while(i<Steps):
  i+=1
  print('runnig')
