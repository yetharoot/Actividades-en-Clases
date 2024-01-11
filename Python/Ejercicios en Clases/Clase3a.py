#----------------------------------CONTROL DE FLUJO----------------------------------

#-----------------------------------BUBLE IF-----------------------------------

#Ejercicio 1: 
#Realizar un programa que pida al usuario ingresar dos numeros, los sume y determine si es positivo o negativo
"""
n1= int(input("Ingrese un numero: "))
n2= int(input("Ingrese un numero: "))

suma=n1+n2
print(f"\nEl resultado de la suma es: {suma}")

if suma > 0:
    print("El resultado es positivo")
elif suma < 0:
    print("El resultado es negativo")
else:
    print("El resultado es cero") """


#Ejercicio 2: 
#Hacer un programa que pida al usuario ingresar un dia de la semana y nos diga cuantas letras tiene la palabra
"""
dia= input("\nIngrese un dia de la semana: ")

if dia.lower() == "lunes": 
    print(f"\nLa palabra {dia} tiene {len(dia)} letras")
elif dia.lower() == "martes":
    print(f"\nLa palabra {dia} tiene {len(dia)} letras")
elif dia.lower() == "miercoles":
    print(f"\nLa palabra {dia} tiene {len(dia)} letras")
elif dia.lower() == "jueves":
    print(f"\nLa palabra {dia} tiene {len(dia)} letras")
elif dia.lower() == "viernes":
    print(f"\nLa palabra {dia} tiene {len(dia)} letras")
elif dia.lower() == "sabado":
    print(f"\nLa palabra {dia} tiene {len(dia)} letras")
elif dia.lower() == "domingo":
    print(f"\nLa palabra {dia} tiene {len(dia)} letras")
else: 
    print("Opcion invalida, ingrese un dia correcto")"""


#Ejercicio 3: 
#Hacer que las variables cambian de valor la una con la otra

numeroA= 444
numeroB= 555

#Cambiar numeroA a 555 y numeroB a 444
aux=numeroA
numeroA=numeroB
numeroB=aux

print(numeroA, numeroB)