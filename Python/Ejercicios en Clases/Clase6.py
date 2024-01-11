"""Ejercicio 1: Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matematicas, Fisica, Quimica, 
Historia y Lenguaje) en una lista y la muestre por pantalla el mensaje "Yo estudio <asignatura>, donde <asignatura> es 
cada una de las asignaturas de la lista"""
"""
cantidad= int(input("Ingrese la cantidad de materias: "))
lista_asignaturas = []

#[0,1] Rango
for i in range(cantidad):
    materia= input(f"Ingrese una materia en la posicion {i+1}: ")
    lista_asignaturas.append(materia)

for i in lista_asignaturas:
    print(f"Yo estudio la materia de {i}")
    
print(lista_asignaturas) 
"""

"""Ejercicio 2: Escribir un programa que pida al usuario un numero entero positivo y muestre por pantalla todos los 
numeros impares desde 1 hasta ese numero y la cantidad de numeros impares que existe dentro del rango"""
"""
num= int(input("Ingrese un numero entero positivo: "))

cantidad_impares= 0 
for i in range(1, num):
    if i % 2 != 0:
        cantidad_impares += 1
        print(f"Numeros impares desde 1 hasta {i}")
        
print(f"La cantidad de numeros impares dentro del rango es {cantidad_impares}")"""



"""Ejercicio 3: Imprimir la tabla de multiplicar de un numero ingresado por el usuario"""

numero =int(input("Ingrese un numero: "))
for i in range (1, 13):
    resultado=numero*i
    #5x1=5
    #5x2=10
    #5x3=15
    print(f"{numero} x {i} = {resultado}")


#Otra forma del ejercicio 3:
numero =int(input("Ingrese un numero: "))
inicio=int(input("ingrese un valor de inicio: "))
limite=int(input("ingrese un valor limite: "))

for i in range (inicio, limite+1):
    resultado=numero*i
    
    print(f"{numero} x {i} = {resultado}") 