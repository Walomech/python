
acceso= False
motivo= ""
nombre_completo = input("Ingrese su nombre completo: ")
edad = int(input("Ingrese su edad: "))
code=input("Ingrese codigo de invitacion: (EJ_2026-AB) ")
vip= input("Es socio VIP (S/N): ").lower()

partes= nombre_completo.split()
nombre=partes[0]
if len(partes) >=3:
    apellido=partes[-2]
else:
    apellido=partes[-1]
id_invitado= ((nombre[0]+apellido).upper()+str(edad))
codigo_limpio= code.replace("-","") 
if (edad>=18 and code.startswith("2026")):
    acceso= True
    motivo= "Acceso permitido por ser mayor de edad y tener un código válido."

elif (vip=="s" and edad>=16):
    acceso= True
    motivo= "Acceso permitido por ser socio VIP y tener la edad requerida."
else:
    acceso= False
    motivo= "Acceso denegado por no cumplir con los requisitos de edad o código de invitación."


print("")
print("________________________________________")
print("__________VALIDACION DE ACCESO__________")
print("________________________________________")
print(f"ID de invitado: {id_invitado}")
print(f"Codigo limpio: {codigo_limpio}")
if acceso:
    print("Estado: Acceso Permitido")
    print(f"Motivo: {motivo}")
else:
    print("Estado: Acceso Denegado")
    print(f"Motivo: {motivo}")