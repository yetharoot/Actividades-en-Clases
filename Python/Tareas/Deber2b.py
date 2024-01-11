#Ejercicio 6: Imprime los números pares e impares del 1 al 50
"""
print("Números Pares:") #Muestro un texto en pantalla para numeros pares
#Utilizo el bucle for y le digo que la variable "num" tiene un rango de 1 a 51. Pongo 51 porque range no toma en cuenta 
#el ultimo valor, entonces llegará a 50

for num in range(1, 51): 
    if num % 2 == 0: #Le digo que si "num" al ser dividido para 2 da como resto 0 entonces imprime el numero en Pares
        print(num)

print("\nNúmeros Impares:") #Muestro un texto en pantalla para numeros impares
#Utilizo el mismo bucle de arriba con el mismo rango

for num in range(1, 51):
    #Ahora le digo que si al ser dividido "num" para 2 da como resto un numero diferente a 0 lo imprime en Impares 
    if num % 2 != 0: 
        print(num) """


#Ejercicio 7: Imprime los números divisibles por 5 del 1 al 100
"""
print("Números Divisibles para 5:")
#Uso el bucle for y le digo que la variable "num" tiene un rango de 1 a 101 para que llegue al 100
for num in range(1, 101): 
    if num % 5 == 0:      #Le digo que si el resto entre dividir "num" para 5 es igual a 0 entonces imprime el num
        print(num)        #ya que eso significa que es dividible para 5
"""

#Ejercicio 8: Solicita al usuario un número y un límite e imprime los números desde el número hasta el límite:
"""
numero = int(input("Ingrese un número: ")) #Solicitar al usuario ingresar un número
limite = int(input("Ingrese un límite: ")) #Solicitar al usuario ingresar un límite

#Imprimo un texto que ponga que mostrará los números desde el número ingresado hasta el límite ingresado
print(f"Números desde {numero} hasta {limite}:")
#Con el bucle for le digo que el rango será desde el numero hasta el limite ingresados... 
for i in range(numero, limite + 1): #...tambien le pido que me incremente de uno en uno los numeros
    print(i) #Imprimo el bucle
"""

#Ejercicio 9: Escribe un programa que solicite al usuario un número y calcule su factorial:
# Solicito al usuario ingresar un número
"""
numero = int(input("Ingrese un número: "))

# Inicializo la variable "factorial" a 1
factorial = 1

#Para calcular el factorial del número uso el bucle for, inicio un rango desde 1 que irá aumentando de uno en uno
for i in range(1, numero + 1): 
    factorial *= i #factorial se multiplica por los números del 1 al número ingresado 

print(f"El factorial de {numero} es {factorial}") #Imprimo el resultado concatenando las variables  """


#Ejercicio 10: Escribe un programa que imprima los números primos del 1 al 100

# Defino la función "num_primo" que tendrá el nombre de "numero" y con ella verificaré si un numero es primo
def num_primo(numero):
    #Uso el condicional "if" para decirle que si "numero" es menor que 2 será falso ya que el numero 1 no es primo
    if numero < 2: 
        return False
    #Inicio un bucle for con un rango que empieza en dos, calculamos la potencia de "numero" con 0.5 y vamos sumando 1 
    for i in range(2, int(numero**0.5) + 1): 
        if numero % i == 0:  #Si el resto entre "numero" y cada elemento del rango es igual a cero será falso
            return False     #Caso contrario será verdadero
    return True

# Imprimo los números primos del 1 al 100
print("Números primos del 1 al 100:")
for num in range(1, 101): #Determino que el rango será de 1 a 101 para que llegue a 100 y que no vaya al infinito
    if num_primo(num): 
        print(num)
