#EJERCICIO 1
print("CONTADORA DE PARTICIPANTES")
print("__________________________")

cant = int(input("Ingrese cantidad de participantes: "))

nombres = []

for i in range(cant):
    nombre = input("Ingrese nombre del participante: ")
    nombres.append(nombre)

print(f"La cantidad de participantes es: {cant}")
print("Los participantes son:")

for nombre in nombres:
    print(nombre)

  
