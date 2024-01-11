"""Este es un trabajo extra que hice para poder tener otro intento en la <Leccion01: Control de Flujo> que abrió el 30
de noviembre y cerró el 3 de diciembre
Este trabajo se me asignó el 5 de diciembre para entregar al dia siguiente en la mañana"""


#Ejercicio 1: Mini calculadora que solicita dos números y una operación (suma, resta, multiplicación, división) e 
#imprime el resultado.
"""
num1 = float(input("Ingrese un número: ")) #Pido al usuairo que ingrese dos numeros
num2 = float(input("Ingrese otro número: "))
operacion = input("Ingrese la operación que desea realizar (+, -, *, /): ") #Pido al usuario que ingrese la operacion

#Uso las condicionales if, elif y else para decirle que si el usuario tipea +, -, * o / realizará una suma, resta,
#multiplicacion o division respectivamente
if operacion == '+':
    resultado = num1 + num2
elif operacion == '-':
    resultado = num1 - num2
elif operacion == '*':
    resultado = num1 * num2
elif operacion == '/':
    resultado = num1 / num2
#En caso de que el usuario tipee cualquier cosa que no sea +, -, *, / imprimo un error
else:
    resultado = "Error, simbolo no reconocido"

print("Resultado:", resultado) #Imprimo el resultado de la operacion
"""

#Ejercicio 2: Pide al usuario ingresar cuatro números e imprime cuál es el mayor y cual es el menor.
"""
#Declaro las variables en donde iran los 4 numeros y con un input pido al usuario los valores 
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))
num4 = float(input("Ingresa el cuarto número: "))

#Sacar el numero mayor
maximo = max(num1, num2, num3, num4) #Uso la funcion "max" para sacar el elemento maximo de la lista con los numeros
print(f"El número mayor es: {maximo}") #Imprimo el numero mayor 

#Sacar el numero menor
minimo = min(num1, num2, num3, num4) #Uso la funcion "min" para sacar el elemento minimo de la lista con los numeros
print(f"El número menor es: {minimo}") #Imprimo el numero menor
"""

#Ejercicio 3: Le pide al usuario un número entero e imprime su tabla de multiplicar del 1 al 10

num = int(input("Ingresa un número entero: ")) #Pido al usuario un numero entero 

for i in range(1, 11): #Creo un rango del 1 al 11 para que llegue hasta el 10 
    print(f"{num} x {i} = {num * i}") #Imprimo que "num" x cada numero en el rango es igual a su multiplicacion


#Ejercicio 4: Imprimir una cuenta regresiva con un numero ingresado en pantalla

#Pido al usuario un numero entero
num = int(input("Ingresa un número entero para iniciar cuenta regresiva: ")) 

#Uso el bucle "for" y declaro un rango que irá desde el numero ingresado hasta 0 para que llegue a 1
for i in range(num, 0, -1): #Ademas, le pido que vaya restando los numeros de uno en uno
    print(i) #Imprimo el rango


#Ejercicio 5: Creo una lista de personas, el programa solicita al usuario ingresar un nombre e indica si el nombre 
#está en la lista.

lista = ["Miguel", "Sara", "Jorge", "Marcelo", "Lean" "Alicia"] #Creo la lista
buscar_nombre = input("Ingresa un nombre: ") #Almaceno en la variable "buscar_nombre" lo que tipee el usuario

if buscar_nombre in lista: #Uso la condicional "if" para pedirle que si lo ingresado por el usuario esta en lista... 
    print(f"{buscar_nombre} está en la lista.") #Imprime el nombre ingresado como parte de la lista
else:
    print(f"{buscar_nombre} no está en la lista.") #Caso contrario, nos dice que no está en la lista
