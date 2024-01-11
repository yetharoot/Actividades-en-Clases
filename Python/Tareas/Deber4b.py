"""E) Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los 
números pares e impares desde 1 hasta ese número y la cantidad de números pares e impares que existe dentro del rango."""
"""
# Solicitar al usuario un número entero positivo
num = int(input("Ingrese un número entero positivo: "))

# Verificar si el número ingresado es positivo con el bucle if
if num <= 0:
    print("Ingrese un número entero positivo.")
else:
    # Inicializar contadores para números pares e impares
    cantidad_pares = 0
    cantidad_impares = 0
    # Mostrar números pares
    print(f"\nNúmeros pares desde 1 hasta {num}:")
    for i in range(2, num + 1, 2):
        cantidad_pares += 1
        print(i)
    # Mostrar la cantidad de números pares en el rango
    print(f"\nLa cantidad de números pares dentro del rango es {cantidad_pares}")

    # Mostrar números impares
    print(f"\nNúmeros impares desde 1 hasta {num}:")
    for i in range(1, num + 1, 2):
        cantidad_impares += 1
        print(i)
    # Mostrar la cantidad de números impares en el rango
    print(f"\nLa cantidad de números impares dentro del rango es {cantidad_impares}") """


"""F) Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde 
ese número hasta cero"""
"""
# Solicitar al usuario un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))

# Verificar si el número ingresado es positivo
if numero <= 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    # Mostrar la cuenta regresiva desde el número hasta cero
    print(f"\nCuenta regresiva desde {numero} hasta 0:")
    for i in range(numero, -1, -1): #Se irá restando de uno en uno, empezando en numero y terminando en -1, es decir en 0
        print(i)
"""

"""G) Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el 
de más abajo, de altura el número introducido.
*
**
***
****
"""
"""
# Solicitar al usuario un número entero
altura = int(input("Ingrese un número entero para la altura del triángulo: "))
# Verificar si el número ingresado es positivo
if altura <= 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    # Mostrar el triángulo rectángulo
    print("\nTriángulo rectángulo:")
    for i in range(1, altura + 1):
        print('*' * i) """

"""H) Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10."""
"""
#Uso el bucle for y creo un rango del 1 al 11 (que llegará hasta el 10) que será la tabla de cada numero del 1 al 10
for i in range(1, 11):
    print(f"\nTabla de multiplicar del {i}:") #Imprimo cada tabla que sera el total del rango

    for j in range(1, 11): #Realizo la multiplicacion entre el numero de la tabla y cada numero del rango
        resultado = i * j
        print(f"{i} x {j} = {resultado}") """


"""I) Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la 
palabra introducida empezando por la última."""
"""
# Solicitar al usuario una palabra
palabra = input("Ingrese una palabra: ")

#Mostrar las letras de la palabra desde la última
print("\nLetras de la palabra desde la última:")
#Uso la funcion reversed() para invertir el orden de las letras e imprimirlas en orden inverso
for letra in reversed(palabra): 
    print(letra) """

"""J) Escribir un programa que almacene las asignaturas de un curso (por ejemplo, Matemáticas, Física, Química, 
Historia y Lengua) en una lista y la muestre por pantalla."""
"""
# Almaceno las asignaturas en una lista
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Imprimo las asignaturas por pantalla
print("Asignaturas del curso:")
for asignatura in asignaturas:
    print(asignatura) """


"""K) Escribir un programa que almacene las asignaturas de un curso (por ejemplo, Matemáticas, Física, Química, 
Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es 
cada una de las asignaturas de la lista."""
"""
# Almaceno las asignaturas en una lista
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Muestro el mensaje "Yo estudio <asignatura>" por pantalla para cada asignatura
for asignatura in asignaturas:
    print(f"Yo estudio {asignatura}") """


"""L) Escribir un programa que almacene las asignaturas de un curso (por ejemplo, Matemáticas, Física, Química, Historia 
y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla 
con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una de las asignaturas de la lista y <nota> 
cada una de las correspondientes notas introducidas por el usuario."""
"""
# Almaceno las asignaturas en una lista
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# Crear un diccionario para almacenar las notas
notas = {}
# Pedir al usuario la nota para cada asignatura con el bucle for
for asignatura in asignaturas:
    nota = float(input(f"Ingrese la nota de {asignatura}: "))
    notas[asignatura] = nota
# Mostrar las notas por pantalla con bucle for
print("\nCalificaciones:")
for asignatura, nota in notas.items():
    print(f"En {asignatura} has sacado {nota}") """


"""M) Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso 
separados por comas."""

# Almacenar los números del 1 al 10 en una lista
numeros = list(range(1, 11))

# Mostrar los números en orden inverso separados por comas
print("Números en orden inverso:")
#utilizo map para aplicar la función str (que convierte a cadena de texto) a cada elemento de la lista numeros
print(", ".join(map(str, reversed(numeros)))) #Uso reversed para invertir el orden de los numeros

