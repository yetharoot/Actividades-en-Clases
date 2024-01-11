#----------------------------------------1: VARIABLES---------------------------------------- 
"""
numero = 4
nombre = "Michael"
letra = 'S'
print("El numero es: ",numero, "\nEl nombe es: ",nombre, "\nLa letra es: ",letra) """


#----------------------------------------2: FORMAS DE IMPRIMIR----------------------------------------
"""#Utilizar la función print()
#Cada una por separado con un salto de linea
nombre="Mike"
materia="Programacion"
horas=2
print(nombre)
print(materia)
print(horas)

#Imprimir separando argumentos
nombre="Mike"
materia="Programacion"
horas=2
print(nombre,materia,horas)"""


#----------------------------------------3: CONCATENAR CADENAS----------------------------------------
"""nombre="Mike"
print("Mi nombre es "+ nombre +" y me gusta codificar")"""

#Nos saldra ERROR porque solo podemos concatenar un str (no int) con str. 
#Solo se puede concatenar tipo de dato string.
"""numero=24
print("El numero ingresado es: "+numero)"""


#----------------------------------------4: FUNCION STR()----------------------------------------
#Convierte cualquier tipo de dato a una cadena. Tambien permite formatear el texto que se imprime

"""numero = 145.134

print("El numero ingresado es: "+str(numero)) #Sale el numero completo

print(f"El numero ingresado es {numero:.2f}") #Sale el numero redondeado"""


#----------------------------------------5: ENTRADA DE TEXTO----------------------------------------

#La funcion input pide al usuario que ingrese texto y devuelve el texto (string) ingresado como una cadena
#Muestro un mensaje por pantalla 

print("Cual es tu nombre:\n")

#Asigna el valor ingresado a la variable nombre

nombre = input() #Mike
print(f"Mi nombre es {nombre}")
