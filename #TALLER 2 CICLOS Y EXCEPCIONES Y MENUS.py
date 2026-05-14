#TALLER 2 CICLOS Y EXCEPCIONES Y MENUS


#CICLO FOR: Se utiliza para iterar sobre una secuencia 
# (como una lista, tupla, diccionario, conjunto o cadena) o un rango de números. 
# La sintaxis básica es:
#for variable in secuencia:
    # bloque de código a ejecutar

#Ejercicio 1 TABLA DE MULTIPLICAR

numero=int(input("Ingrese el numero que desea multiplicar: "))
for i in range(1,11):
    print(numero,"X",i,"=",numero*i)

#Ejercicio 2 Suma de los primeros N Numeros 
numero=int(input("Ingrese el numero hasta el cual desea sumar: "))
suma=0
for i in range(1,numero+1):
    suma+=i
print("La suma de los primeros",numero,"numeros es:",suma)

#Ejercicio 3 CONTADOR DE PARES E IMPARES
numero=int(input("Ingrese el numero hasta el cual desea contar: "))
pares=0
impares=0
for i in range(1,numero+1):
    if i%2==0:
        pares+=1
    else:
        impares+=1
print("Cantidad de numeros pares:",pares)
print("Cantidad de numeros impares:",impares)

#Ejercicio 4 CUENTA REGRESIVA
import time 
numero=int(input("Ingrese el numero desde el cual desea hacer la cuenta regresiva: "))
for i in range(numero,0,-1):
    time.sleep(1) # Pausa de 1 segundo entre cada número
    print(i)
print("¡Despegue!") 

#Ejercicio 5 PROMEDIO DE NOTAS
cantidad=int(input("Ingrese la cantidad de notas que desea promediar: "))
suma=0
for i in range(cantidad):
    nota=float(input("Ingrese la nota "+str(i+1)+": "))
    suma+=nota
promedio=suma/cantidad
print("El promedio de las notas es:",round(promedio,1))

#Ejercicio 6 FACTORIAL
numero=int(input("Ingrese el numero a factorizar: "))
factorial=1
for i in range(1,numero+1):
    factorial*=i
print("El factorial de",numero,"es:",factorial)

#Ejercicio 7 Triangulo con asteriscos
altura=int(input("Ingrese la altura del triangulo: "))
for i in range(1,altura+1):
    print("*"*i)









#CICLO WHILE: 
# Se utiliza para ejecutar un bloque de código mientras una condición sea verdadera.
# La sintaxis básica es:
# while condicion:
#   bloque de código a ejecutar

# Ejercicio 8 Adivina el numero   
numero_secreto=7
intento=0
contador=0
while intento!=numero_secreto:
    intento=int(input("Adivina el numero secreto (entre 1 y 10): "))    
    contador=contador+1
    if intento<numero_secreto:
        print("Demasiado bajo, intenta de nuevo.")
    elif intento>numero_secreto:
        print("Demasiado alto, intenta de nuevo.")
print("¡Felicidades! Adivinaste el numero secreto en",contador,"intentos.")    


#Ejercicio 9 suma hasta que ingrese 0
suma=0
contador=0
while True:
    numero=int(input("Ingrese un numero (0 para terminar): "))
    if numero==0:
        break
    suma+=numero
    contador+=1
print("La suma total es:",suma)
print("cantidad de numeros ingresados:",contador)

#Ejercicio 10 Mayor de una lista de numeros
Cant=int(input("Ingrese cantidad de numeros a comparar: "))
mayor=0
while Cant>0:
    numero=int(input("Ingrese un numero: "))
    if numero>mayor:
        mayor=numero
    Cant-=1
print("El numero mayor es:",mayor)



#Ejercicio 11 VALIDACION DE NOTA
nota=-1
while nota<1 or nota>7:
    nota=float(input("Ingrese una nota entre 1 y 7: "))
    if nota<1 or nota>7:
        print("Nota invalida, intente de nuevo.")



#Ejercicio 12 Contraseña con intentos limitados
contraseña="python123"
intentos=3
while intentos>0:
    ingreso=input("Ingrese la contraseña: ")
    if ingreso==contraseña:
        print("Acceso concedido.")
        break
    else:
        intentos-=1
        print("Contraseña incorrecta. Intentos restantes:",intentos)
if intentos==0:
    print("Acceso denegado. Se han agotado los intentos.")

#Ejercicio 13 Suma de digitos de un numero
numero=int(input("Ingrese un numero para sumar sus digitos: "))
suma=0
while numero>0:
    digito=numero%10
    suma+=digito
    numero//=10
print("La suma de los digitos es:",suma)










#MANEJO DE EXCEPCIONES:
# Se utiliza para manejar errores que pueden ocurrir durante la ejecución de un programa.
# La sintaxis básica es:
# try:
#   bloque de código que puede generar una excepción
# except TipoDeExcepcion:
#   bloque de código para manejar la excepción

#EJERCICIO 3.1 DIVISION SEGURA

try:
    numero1=float(input("Ingrese el primer numero: "))
    numero2=float(input("Ingrese el segundo numero: "))
    resultado=numero1/numero2
except ValueError:
    print("Error: Entrada no valida. Por favor ingrese numeros.")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
else:
    print(f"Resultado: {numero1} / {numero2} = {resultado}")
finally:
    print("Gracias por usar el programa de division segura.")

#EJERCICIO 3.2 CONVERTIR A ENTERO CON VALIDACION
while True:
    try:
        entero=int(input("Ingrese un numero entero: "))
        break
    except ValueError:
        print("Error: Entrada no valida. Por favor ingrese un numero entero.")
print("El doble de",entero,"es:",entero*2)


#Ejercicio 3.3 EDAD CON RAISE 
try:
    edad=int(input("Ingrese su edad: "))
    if edad<0 or edad>150:
        raise ValueError("La edad no puede ser negativa.")
    else:
        print("Su edad es:",edad)
except ValueError as e:
    print("Error:", e)

#Ejercicio 3.4 CALCULADURA CON MULTIPLES EXCEPCIONES
try:
    num1=float(input("Ingrese el primer numero: "))
    num2=float(input("Ingrese el segundo numero: "))   
    operacion=input("Ingrese la operacion (+, -, *, /): ")
    if operacion=='+':
        resultado=num1+num2
    elif operacion=='-':
        resultado=num1-num2
    elif operacion=='*':
        resultado=num1*num2
    elif operacion=='/':
        resultado=num1/num2
    else:
        raise ValueError("Operacion no valida.")
except ValueError as e:
    print("Error:", e)
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
else:
    print(f"Resultado: {num1} {operacion} {num2} = {resultado}")

#Ejercicio 3.5 VALIDAR ENTRADA CON WHILE Y TRY
while True:
    try:
        numero=int(input("Ingrese un numero entero positivo: "))
        if numero<0 or numero>120:
            raise ValueError("El numero no puede ser negativo o mayor que 120.")
        if numero=="":
            raise ValueError("El numero no puede ser texto.")
        else:
            print("Numero valido.")
        break
    except ValueError as e:
        print("Error:", e)
print("El numero ingresado es:",numero)



