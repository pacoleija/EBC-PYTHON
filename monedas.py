pesos = input("¿Cuantos pesos tienes?:  ")
pesos = float(pesos)
valor_bitcoin = 774340
bitcoins = pesos / valor_bitcoin
bitcoins = round(bitcoins, 2)
bitcoins = str(bitcoins)
print("tienes $" + bitcoins + "bitcoins")
