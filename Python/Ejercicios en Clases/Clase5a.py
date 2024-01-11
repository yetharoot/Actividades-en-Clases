#Ejercicio 1: 
#Imprime los numeros del 1 al 10 en orden descendente "10,9,8,7,6,5,4,3,2,1" y ascendente 1,2,3,4,5,6,7,8,9,1,0
"""
num = 10
print("Orden desdcendente: ")

while(num>0):
   print(num)
   num-=1

num = 1
print("Orden ascendente: ")

while(num<=10):
   print(num)
   num+=1 
"""

#Ejercicio 2: 
"""Leer numeros enteros de teclado, hasta que el usuario ingrese el 0. Fianlmente mostrar la sumatoria de todos los 
nuemros ingresados"""
"""
# Inicializar la variable de sumatoria
sumatoria = 0
# Bucle para leer números hasta que se ingrese 0
while True:
    try:
        # Leer un número entero desde el teclado
        numero = int(input("Ingrese un número (ingrese 0 para terminar): "))
        # Verificar si el número ingresado es 0
        if numero == 0:
            break  # Salir del bucle si el número es 0
        # Sumar el número a la sumatoria
        sumatoria += numero

    except ValueError:
        print("Por favor, ingrese un número entero válido.")
# Mostrar la sumatoria de los números ingresados
print("\nLa sumatoria de los números ingresados es:", sumatoria)"""


#Ejercicio 3:
"""Leer numeros enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cual fue el mayor numero
ingresado"""
"""
numero = int(input("Ingrese un numero entero positivo: "))

aux= 0

while numero !=0:

     if numero > aux:
         aux = numero

     numero = int(input("Ingrese un numero entero positivo: "))
print("El numero mayor es ",aux) 
"""
"""OTRA FORMA
# Inicializar la variable para almacenar el mayor número
mayor_numero = None

# Bucle para leer números hasta que se ingrese 0
while True:
    try:
        # Leer un número entero desde el teclado
        numero = int(input("Ingrese un número entero positivo (ingrese 0 para terminar): "))

        # Verificar si el número ingresado es 0
        if numero == 0:
            break  # Salir del bucle si el número es 0

        # Verificar si el número ingresado es positivo
        if numero < 0:
            print("Por favor, ingrese un número entero positivo.")
            continue  # Volver al inicio del bucle

        # Actualizar el mayor número si es necesario
        if mayor_numero is None or numero > mayor_numero:
            mayor_numero = numero

    except ValueError:
        print("Por favor, ingrese un número entero válido.")

# Mostrar el mayor número ingresado
if mayor_numero is not None:
    print("El mayor número ingresado es:", mayor_numero)
else:
    print("No se ingresaron números positivos.") """

#Ejercicio 4: -----------------Menu de opciones con while True-----------------
#Hacer menu de opciones para que al ingresar 1 haga una suma, con 2 una resta y con 3 salga del programa
#Agregar multiplicacion, division, potencia, raiz cuadrada:

import math

estado = True
while estado:
    print("\n==>Menu de opciones<==\n"
        +"1..Para Sumar\n"
        +"2..Para Restar\n"
        +"3..Para Multiplicar\n"
        +"4..Para Dividir\n"
        +"5..Para Sacar potencia\n"
        +"6..Para Sacar raiz cuadrada\n"
        +"7..Para Salir")

    opcion = int(input("\nIngrese la opción deseada: ")) 
   
    if opcion == 7:
        break
    else:
        num1 = float(input("\nIngrese el primer número: "))

        if opcion in [1, 2, 3, 4] and opcion != 6:
            num2 = float(input("Ingrese el segundo número: "))

            if opcion == 1:
                print("\nEl resultado de la suma es: ", num1 + num2)
            elif opcion == 2:
                print("\nEl resultado de la resta es: ", num1 - num2)
            elif opcion == 3:
                print("\nEl resultado de la multiplicación es: ", num1 * num2)
            elif opcion == 4:
                if num2 != 0:
                    print("\nEl resultado de la división es: ", num1 / num2)
                else:
                    print("\nError: No se puede dividir por cero.")
        elif opcion == 5:
            num2 = float(input("Ingrese el exponente: "))
            print(f"\nLa potencia de {num1} elevado al exponente {num2} es: ", num1 ** num2)
        elif opcion == 6:
            if num1 >= 0:
                print(f"\nLa raíz cuadrada de {num1} es: ", math.sqrt(num1))
            else:
                print("\nERROR: No se puede clcular la raíz cuadrada de un número negativo. Ingresa un número válido.")
        else:
            print("ERROR: opción no válida.") 

#TEMAS: Diccionario, Coleccion de Datos 