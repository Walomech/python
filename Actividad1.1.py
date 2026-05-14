#Actividad 1.1 SALUDO PERSONALIZADO
nombre =input("Ingresa tu nombre: ")
print("hola "+ nombre +" bienvenido al curso de python!")

#Actividad 1.2 FICHA DE ESTUDIANTE
nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
carrera = input("Ingresa tu carrera: ")
sede = input("Ingresa tu sede: ")
print("----------Ficha de estudiante----------")
print("Nombre: " + nombre)
print("Edad: " + edad)
print("Carrera: " + carrera)
print("Sede: " + sede)


#Actividad 1.3 CALCULADORA DE EDAD
nombre = input("Ingresa tu nombre: ")
año= int(input("Ingresa tu año de nacimiento: "))
año_actual = 2026
print ("nombre: " + nombre+ ", tienes: " + str(año_actual - año) + " Años")


#Actividad 1.4 Promedio de Notas
print("Calculadora de promedio de notas")
print("________________________________")
nota1 = float(input("Ingresa la primera nota: "))
nota2 = float(input("ingresa la segunda nota: "))
nota3 = float(input("Ingresa la tercera nota: "))
promedio = (nota1 + nota2 + nota3) / 3
import os
os.system("clear")
print("Calculadora de promedio de notas")
print("________________________________")
print("El promedio de las notas es: " + str(round(promedio, 1)))

# Actividad 1.5 CONVERSOR DE TEMPERATURA
print("Conversor de temperatura")
print("________________________")
celsius = float(input("Ingresa la temperatura en grados Celsius:"))
farenheit = (celsius * 9/5) + 32
print("Conversor de temperatura")
print("________________________")
print("La temperatura es de: " + str(round(celsius, 1)) + "°C")
print("La temperatura es de: " + str(round(farenheit, 1)) + "°F")

#Actividad 1.6 CALCULADORA DE PROPINA
print("Calculadora de propina")
print("_____________________")
total = float(input("Ingresa el monto de la cuenta: "))
propina = float(input("Ingresa el porcentaje de propina que deseas dejar: "))
print("La propina es de: $" + str(round(total * propina / 100, 1)) + " Pesos")
print("El total a pagar es: $" + str(round(total + (total * propina / 100), 1)) + " Pesos")

#Actividad 2.1 Identificado tipos 
texto_entero = input("Ingresa un número entero: ")
texto_decimal = input("Ingresa un número decimal: ")
palabra = input("Ingresa una palabra: ")    

entero= int(texto_entero)
decimal= float(texto_decimal)

print(f"{entero} es de tipo {type(entero)}")
print(f"{decimal} es de tipo {type(decimal)}")
print(f"{palabra} es de tipo {type(palabra)}")

#Actividad 2.2 Conversión de tipos
texto = input("Ingresa un numero decimal: ")
print("Como Float: "+ str(float(texto)))
print("Como Entero: "+ str(int(float(texto))))
print("Como String: "+ str(len(texto)))
print("Como Booleano: "+ str(bool(float(texto))))

#Actividad 2.3 Operaciones Aritméticas
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
print("Suma: " + str(num1 + num2))
print("Resta: " + str(num1 - num2))
print("Multiplicación: " + str(num1 * num2))
print("División: " + str(num1 / num2))
print("División entera: " + str(num1 // num2))
print("Potencia: " + str(num1 ** num2))
print("Módulo: " + str(num1 % num2))

#Actividad 2.4 Booleanos y Comparaciones
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
print(f"{num1} Igual que {num2}: {num1 == num2}") 
print(f"{num1} Mayor que {num2}: {num1 > num2}")
print(f"{num1} Mayor o Igual que  {num2}: {num1 >= num2}")
print(f"{num1} Distinto de {num2}: {num1 != num2}")
print(f"{num1} Menor que {num2}: {num1 < num2}")
print(f"{num1} Menor o Igual que {num2}: {num1 <= num2}")


#Actividad 2.5 Cajero automático

retiro = int(input("Ingresa el monto a retirar: "))
billetes_10000 = retiro // 10000
resto= retiro % 10000
billetes_5000 = resto // 5000
resto = resto % 5000
billetes_2000 = resto // 2000
resto = resto % 2000
billetes_1000 = resto // 1000
resto = resto % 1000
print("Monto a retirar: " + str(retiro) + " Pesos")
print("Billetes de 10000: " + "Cantidad de Billetes: " + str(billetes_10000))
print("Billetes de 5000: " + "Cantidad de Billetes: " + str(billetes_5000))
print("Billetes de 2000: " + "Cantidad de Billetes: " + str(billetes_2000))
print("Billetes de 1000: " + "Cantidad de Billetes: " + str(billetes_1000))


#Actividad 2.6 Desglose de tiempo
segundos = int(input("Ingresa el número de segundos: "))
horas = segundos // 3600
resto = segundos % 3600
minutos = resto // 60
resto = resto % 60
print("Desglose de tiempo")
print("________________")
print("Los segundos ingresados: " + str(segundos))
print ("Equivalen a: ")
print(str(horas) + " horas")
print(str(minutos) + " minutos "
"y")
print(str(resto) + " segundos")


#Ac