"""1. Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!."""
"""
def saludo(nombre):
    
    #Esta función recibe un nombre y muestra un saludo por pantalla.
    
    #Imprimo el saludo personalizado concatenando la variable nombre
    print(f"¡Hola {nombre}!")

# Solicito al usuario que ingrese su nombre
nombre_usuario = input("Ingrese su nombre: ")

# Llamar a la función saludar con el nombre ingresado
saludo(nombre_usuario) """


"""2. Escribir una función que reciba un número entero positivo y devuelva su factorial."""
"""
def factorial(numero): #Declaro la función para calcular el factorial de un número entero positivo.
    #Verifico que el número sea positivo con el bucle if
    if numero < 0:
        return "El factorial no está definido para números negativos"
    #Inicializar el resultado a 1
    resultado = 1
    #Para calcular el factorial
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

#Pido un numero al usuario
numero_ingresado = int(input("Ingrese un número entero positivo: "))

# Llamo a la función factorial e imprimo el resultado
resultado_factorial = factorial(numero_ingresado)
print(f"El factorial de {numero_ingresado} es {resultado_factorial}") """


"""3. Escribir una función que calcule el área de un círculo."""
"""
import math #Llamo a la libreria math
 #Declaro la función para calcular el área de un círculo dado su radio.
def calcular_area_circulo(radio):
    
    #Uso el bucle if para verificar que el radio sea positivo
    if radio < 0:
        return "El radio no puede ser negativo"
    
    #Paa calcular el área debemos usar la fórmula Area = πr²
    area = math.pi * radio**2
    return area

#Pido al usuario ingresar el radio de un circulo
radio_ingresado = float(input("Ingrese el radio del círculo: "))

#Llamo a la función calcular_area_circulo e imprimo el resultado
resultado_area = calcular_area_circulo(radio_ingresado)
print(f"El área del círculo con radio {radio_ingresado} es {resultado_area}") """


"""4. Escribir una función que reciba una muestra de números en una lista y devuelva el promedio."""
"""
def calcular_promedio(muestra): #Declaro la función para calcular el promedio de una muestra de números.
    #Verifico que la muestra no esté vacía
    if not muestra:
        return "La muestra está vacía, no se puede calcular el promedio"
    
    #Calculo el promedio sumando los números y dividiendo por la cantidad
    promedio = sum(muestra) / len(muestra)
    return promedio

#Pido al usuario que ingrese una lista de números separados por espacios
muestra_ingresada = input("Ingrese una muestra de números separados por espacios: ")
#Convierto la entrada a una lista de números
numeros = [float(numero) for numero in muestra_ingresada.split()]
#Llamo a la función calcular_promedio e imprimo el resultado
resultado_promedio = calcular_promedio(numeros)
print(f"El promedio de la muestra es: {resultado_promedio}") """


"""5. Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados."""
"""
def calcular_cuadrados(muestra): #Defino la función para calcular los cuadrados de una muestra de números.

    # Utilizar list comprehension para obtener la lista de cuadrados
    cuadrados = [numero**2 for numero in muestra]
    return cuadrados

#Pido al usuario ingresar una lista de números separados por espacios
muestra_ingresada = input("Ingrese una muestra de números separados por espacios: ")

#Convierto la entrada a una lista de números
numeros = [float(numero) for numero in muestra_ingresada.split()]

#Se llama a la función calcular_cuadrados y se imprime el resultado
resultado_cuadrados = calcular_cuadrados(numeros)
print(f"Los cuadrados de la muestra son: {resultado_cuadrados}") """


"""6. Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos 
(utilizando una función que realice dicha suma)."""
"""
def suma_digitos(numero): #definir variable
    #Convertir el número a una cadena para iterar sobre sus dígitos
    str_numero = str(numero)
    
    #Utilizar la función sum junto con int para sumar los dígitos
    suma = sum(int(digito) for digito in str_numero)  
    return suma
#Inicializar la variable para la entrada del usuario
numero_ingresado = 1  # Iniciar con un valor diferente de cero

#Pedir números hasta que se ingrese cero
while numero_ingresado != 0:
    numero_ingresado = int(input("Ingrese un número (ingrese 0 para salir): "))
    
    #Si el número ingresado es diferente de cero, calcular y mostrar la suma de los dígitos
    if numero_ingresado != 0:
        resultado_suma = suma_digitos(numero_ingresado)
        print(f"La suma de los dígitos de {numero_ingresado} es: {resultado_suma}") """


"""7. Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos. Al 
finalizar, mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos."""

def suma_digitos(numero):
    # Convertir el número a una cadena para iterar sobre sus dígitos
    str_numero = str(numero)
    # Utilizar la función sum junto con int para sumar los dígitos
    suma = sum(int(digito) for digito in str_numero)
    return suma
# Inicializar variables para la sumatoria de números y sumatoria de dígitos
sumatoria_numeros = 0
sumatoria_digitos = 0
# Solicitar números hasta que se ingrese cero
while True:
    numero_ingresado = int(input("Ingrese un número (ingrese 0 para realizar la sumatoria): "))
    
    if numero_ingresado == 0:
        break
    
    # Calcular y mostrar la suma de dígitos para cada número
    resultado_suma_digitos = suma_digitos(numero_ingresado)
    print(f"La suma de los dígitos de {numero_ingresado} es: {resultado_suma_digitos}")
    
    # Actualizar la sumatoria de números y sumatoria de dígitos
    sumatoria_numeros += numero_ingresado
    sumatoria_digitos += resultado_suma_digitos

# Mostrar la sumatoria de todos los números y la sumatoria de dígitos al finalizar
print(f"La sumatoria de todos los números ingresados es: {sumatoria_numeros}")
print(f"La sumatoria de los dígitos de todos los números ingresados es: {sumatoria_digitos}")
