#----------------------------------------------PROGRAMACION ESTRUCTURADA----------------------------------------------
#----------------------------------------------/////////////////////////----------------------------------------------
"""
Realizar 15 ejercicios de programacion estructurada
•	5 funciones
•	5 bucles
•	5 sentencia if /switch 
"""

#*******************************************-5 EJERCICIOS CON FUNCIONES-*******************************************

#1 Calculadora que suma y resta todos los números naturales desde 1 hasta un límite X
"""
#Declaro la función suma para sumar los primeros X números naturales
def suma(x):
    suma = 0
    for s in range(1, x + 1): #s (suma) empieza en el rango desde 1 y a X se le va sumando 1 
        suma += s
    return suma

#Solicito al usuario ingresar el límite hasta donde se sumarán los numeros
limiteS = int(input("Ingrese el límite superior para la suma de números naturales: "))

#Declaro la función resta para restar los primeros X números naturales
def resta(y):
    resta = 0
    for r in range(1, y - 1): #r (resta) empieza en el rango desde 1 y a X se le va restando 1 
        resta -= r
    return resta

#Solicito al usuario ingresar el límite hasta donde se restarán los numeros
limiteR = int(input("Ingrese el límite superior para la resta de números naturales: "))

#Uso las funciones
resultado_suma = suma(limiteS)
print(f"\nLa suma de los primeros {limiteS} números naturales es {resultado_suma}")

resultado_resta = resta(limiteR)
print(f"La resta de los primeros {limiteR} números naturales es {resultado_resta}") """
#---------------------------------------------------------------------------------------------------------------------

#2. Programa para verificar si un número es o no primo.
"""
#Defino la función numPrimo para verificar si un número es primo
def numPrimo(num): #Tomará el parámetro num (nuemro que ingresará el usuario)
#Uso la condicional if para decirle que si num es menor que 2 la función es False porque los números primos son >= a 2
    if num < 2: 
        return False
#Uso el bucle for para recorrer los valores desde 2 hasta la raíz cuadrada de num más 1
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: #Verifico si num es divisible por i. 
        #Si es divisible, num tiene un factor aparte de 1 y num mismo, por ende no es primo.
            return False
    return True

#Solicito al usuario ingresar un número
num = int(input("Ingrese un número para determinar si es primo: "))

#Uso la función
if numPrimo(num):
    print(f"\n{num} es un número primo.")
else:
    print(f"\n{num} no es un número primo.") """
#---------------------------------------------------------------------------------------------------------------------

#3. Calcular el factorial de un número
"""
#Defino la función para calcular el factorial de un número, su parámetro será "n"
def factorial(n):
    if n == 0 or n == 1: #Si n es igual a 0 o 1, la función devuelve 1 ya que el factorial de 0 y 1 es siempre 1.
        return 1
    else:
        #Multiplica n por el resultado de la llamada recursiva con n - 1 y se repite hasta que n sea 0 o 1,
        return n * factorial(n - 1) 

#Solicito al usuario ingresar un número
numero = int(input("\nIngrese un número: "))

#Uso la función
resultado_factorial = factorial(numero)
print(f"\nEl factorial de {numero} es {resultado_factorial}") """
#---------------------------------------------------------------------------------------------------------------------


#4.	Calculadora básica que realiza las 4 principales operaciones aritméticas. 
"""
#Defino las funciones para realizar las 4 operaciones básicas
def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def mult(a, b):
    return a * b
def div(a, b):
    if b != 0: #Mientras b sea diferente a 0 regresa la division, sino, con else devuelve un mensaje de error 
        return a / b
    else:
        return "Error: No se puede dividir por cero."

#Solicito al usuario ingresar dos números
num1 = float(input("\nIngrese el primer número: "))
num2 = float(input("\nIngrese el segundo número: "))

#Uso las funciones. Declaro las variables "resOperacion" (res de Respuesta) con cada operacion 
resSuma = suma(num1, num2)
print(f"\nSuma: {resSuma}")

resResta = resta(num1, num2)
print(f"\nResta: {resResta}")

resMult = mult(num1, num2)
print(f"\nMultiplicación: {resMult}")

resDiv = div(num1, num2)
print(f"\nDivisión: {resDiv}") """
#---------------------------------------------------------------------------------------------------------------------

#5.	Programa que realiza la conversión de temperatura entre Celsius y Fahrenheit.
"""
#Defino las funciones para convertir entre Celsius y Fahrenheit
def celsius_a_fahrenheit(celsius):
    #Fórmula para convertir de C a F: F = (9/5)C + 32
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    #Fórmula para convertir de F a C: C = (5/9)(F - 32)
    return (fahrenheit - 32) * 5/9

#Menú de opciones para que el usuario elija la conversion que quiere hacer.
print("\nSeleccione la conversión:")
print("1. Celsius a Fahrenheit")
print("2. Fahrenheit a Celsius")
opcion = int(input("\n¿Qué conversión desea realizar?: "))

#Solicito al usuario ingresar la temperatura
temperatura = float(input("\nIngrese la temperatura a convertir: "))

# Realizamos la conversión según la opción seleccionada
if opcion == 1:
    resultado = celsius_a_fahrenheit(temperatura)
    print(f"\n{temperatura} grados Celsius equivalen a {resultado:.2f} grados Fahrenheit.")
elif opcion == 2:
    resultado = fahrenheit_a_celsius(temperatura)
    print(f"\n{temperatura} grados Fahrenheit equivalen a {resultado:.2f} grados Celsius.")
else:
    print("Opción no válida. Por favor, seleccione 1 o 2.") """
#---------------------------------------------------------------------------------------------------------------------


#*******************************************-5 EJERCICIOS CON BUCLES-*******************************************
#1.	Programa que muestra la tabla de multiplicar de un numero ingresado por el usuario. 
"""
numero = int(input("Ingrese un numero entero: "))

#Uso el bucle for para crear el rango que tendrá mi tabla de multiplicar (1 - 10)
for i in range(1, 11): #Pongo el rango hasta 11 para que llegue hasta 10
    resultado = numero * i #El resultado será el número ingresado por el usuario multiplicado por cada número del rango
    #Imprimo el resultado
    print(f"{numero} x {i} = {resultado}") """
#---------------------------------------------------------------------------------------------------------------------
"""
#2.	Programa que imprime los números en una secuencia dada por el usuario hasta un límite también ingresado por el usuario. 

#Pido al usuario que ingrese la secuencia y el limite deseados
secuencia = int(input("Ingrese la secuencia deseada: "))
limite = int(input("Ingrese el límite: "))

print(f"Números en la secuencia de {secuencia} en {secuencia} hasta {limite}:")

#Uso el bucle for para determinar el rango al que irán sus elementos que inicia en 0, va al limite y aumenta segun
#la secuencia ingresada
for i in range(0, limite + 1, secuencia):
    print(i)"""
#---------------------------------------------------------------------------------------------------------------------

#3. Programa que realiza un conteo regresivo desde un número ingresado por el usuario hasta el 0
"""
#Pido al usuario un numero que será el valor de "inicio"
inicio = int(input("Ingrese el número de inicio para el conteo regresivo: "))

#Uso el bucle for para crear mi rango que irá desde el número ingresado, llegará hasta 0 (-1) e irá restando de 1 en 1
for i in range(inicio, -1, -1):
    print(i) #Imprimo la cuenta regresiva  
"""
#---------------------------------------------------------------------------------------------------------------------

#4.	Programa que solicita al usuario ingresar un número infinitamente y no termina hasta que se ingrese cero.
"""
#Uso el bucle while para ejecutar mi programa
while True:
    numero = int(input("Ingrese un número (o 0 para salir): ")) #Pido un numero al usuario
    print(f"Usted ingresó: {numero}") #Imprimo el numero que ingresó el usuario
#Con la condicional if le digo que si numero es igual a 0 se cierra el programa con break
    if numero == 0:
        print("Fin del programa")
        break
"""
#---------------------------------------------------------------------------------------------------------------------

# 5. Programa que cuenta la cantidad de dígitos de un número ingresado por el usuario. 
"""
numero = int(input("\nIngrese un número: ")) #Pido al usuario un numero 
digitos = 0
#Uso el blucle while que se ejecutará mientras el numero no sea 0
while numero != 0:
    #Primero eliminamos el último dígito dividiendo el número por 10
    numero //= 10
    #Luego, incrementamos el contador de dígitos en 1
    digitos += 1
    
#Y al salir del bucle, mostramos la cantidad de dígitos
print(f"\nEl número ingresado tiene {digitos} dígitos.") """
#---------------------------------------------------------------------------------------------------------------------


#***************************************-5 EJERCICIOS CON SENTENCIA IF/SWITCH-***************************************
"""
#1. Programa que determina el día de la semana en base a un numero ingresado del 1 al 7
numeroDia = int(input("Ingrese un número del 1 al 7: ")) #Pido al usuario el numero
#Uso las condicionales if-elif-else para determinar que va a imprimir en cada caso
if numeroDia == 1:
#imprimo un mensaje concatenando la var numeroDia con el dia que corresponde en cada caso
    print(f"\nEl dia {numeroDia} correspode al Lunes") 
elif numeroDia == 2:
    print(f"\nEl dia {numeroDia} correspode al Martes")
elif numeroDia == 3:
    print(f"\nEl dia {numeroDia} correspode al Miércoles")
elif numeroDia == 4:
    print(f"\nEl dia {numeroDia} correspode al Jueves")
elif numeroDia == 5:
    print(f"\nEl dia {numeroDia} correspode al Viernes")
elif numeroDia == 6:
    print(f"\nEl dia {numeroDia} correspode al Sábado")
elif numeroDia == 7:
    print(f"\nEl dia {numeroDia} correspode al Domingo")
else:
    print("\nNúmero inválido, ingrese un número del 1 al 7.") #Si el numero no está en el rango de 1 a 7 mostramos error
"""
#---------------------------------------------------------------------------------------------------------------------


#2.	Calculadora que realiza operaciones básicas (suma, resta, multiplicación, división) utilizando if-elif-else.
"""
operacion = input("Ingrese la operación (suma, resta, mult, div): ") #Pido la operacion al usuario
#Con if-elif-else determino la operacion que corresponde en cada caso
if operacion in ('suma', 'resta', 'mult', 'div'):
    numero1 = float(input("\nIngrese el primer número: ")) #Pido los numeros al usuario para la operacion
    numero2 = float(input("\nIngrese el segundo número: "))

    if operacion == 'suma':
        resultado = numero1 + numero2
    elif operacion == 'resta':
        resultado = numero1 - numero2
    elif operacion == 'mult':
        resultado = numero1 * numero2
    elif operacion == 'div':
        resultado = numero1 / numero2
#Imprimo el resultado concatenando las respectivas variables
    print(f"\nEl resultado de {numero1} {operacion} {numero2} es: {resultado}") 
#En caso de no ingresar ninguna de las opciones correctas imprimo mensaje de error
else:
    print("\nERROR: Ingrese una opcion entre suma, resta, mult, div") """
#---------------------------------------------------------------------------------------------------------------------


#3.	Programa que pide al usuario un número y dice si es positivo/negativo y entero/decimal.
"""
numero = float(input("\nIngrese un número: ")) #Pido al usuario el numero

#Uso if-elif-else para verificar si el número es positivo, negativo o cero
if numero > 0:
    print(f"\nEl número {numero} es positivo.")
elif numero < 0:
    print(f"\nEl número {numero} es negativo.")
else:
    print(f"\nEl número {numero} es cero.")
#Nuevamente uso if para verificar si el número es entero o decimal e imprimo las respuestas 
#concatenadas a las variables
if numero == int(numero):
    print(f"\nEl número {numero} es un entero.")
else:
    print(f"\nEl número {numero} es decimal.") """
#---------------------------------------------------------------------------------------------------------------------


#4.	Programa que categoriza una edad ingresada por el usuario. 
"""
edad = int(input("\nIngrese su edad: ")) #Pido la edad al usuario
#Uso if-elif-else para determinar si es menor, adulto o adulto mayor

if edad < 18: 
    print("\nEres menor de edad.")
elif 18 <= edad < 65:
    print("\nEres adulto.")
else:
    print("\nEres un adulto mayor.") """
#---------------------------------------------------------------------------------------------------------------------


#5.	Programa para validar una contraseña con un máximo de 3 intentos. 

realPass = "MypAss123" #declaro la variable con la contraseña correcta
intentos_maximos = 3 #Defino la var con el limite de intentos en 3
intentos = 0 #intentos será igual a 0

#Uso el bucle while para que corra el programa mientras intentos sea menor a intentos_maximos
while intentos < intentos_maximos:
    userPass = input("\nIngrese su contraseña: ")
    
#Uso if-else para determinar lo que hará si se ingresa la contraseña correcta/incorrecta
    if userPass == realPass:
        print("\nContraseña correcta. Acceso permitido.")
        break  #Sale del bucle y cierra el programa si la contraseña es correcta
    else:
        intentos += 1 #Si la contraseña es incorrecta se suma 1 a "intentos"
        print(f"\nContraseña incorrecta. Intentos restantes: {intentos_maximos - intentos}")

if intentos == intentos_maximos: #Si "intentos" llega al maximo se termina el programa
    print("\nSe agotaron los intentos. Acceso denegado.")
