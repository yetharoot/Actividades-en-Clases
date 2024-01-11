#---------------------------------COLECCIONES DE DATOS---------------------------------
#LISTAS***************************
#Crear lista. 
#Ejemplo 1:
"""
lista= [1,2,3,4,5,4,3,5]

#len() devule la longitud de la lista
longitud=len(lista)
print(F"La lista tiene {longitud} elementos")

#count() devuelve la cantidad de veces que un elemento aparece en la lista
totalNumero3=lista.count(3)
print("\nLa cantidad de veces que aparece el numero 3 es ",totalNumero3)

#index() devuelve el indice de un elemento en la lista
indice= lista.index(3)
print("\nEl indice del numero 3 es ",indice)"""

#Ejemplo 2:
"""
lista= [1,22,3,43,56,6]
ultimoNumero= lista[-1]
print("El ultimo numero de la lista es: ",ultimoNumero)
for i in range(len(lista)-1,1,-1):
    print(list[i])
#Crear sublista
#toma los 4 primeros elementos de la lista
rango1=lista[:4]
#toma desde el tercer elemento hasta el quinto
rango2=lista[2:5]
#toma desde el quinto elemento hasta el final
rango3= lista[4:]
print("rango3")
"""

#TUPLAS***************************
#Ejemplo:
"""
tupla=("mike",34,45,67)
print(tupla)
nombre = tupla.count("mike")
print("La cantidad de veces que aparece mike en la lista es ",nombre)
longitud=len(tupla)
print("El numero de elementos es ",longitud)
indice= tupla.index(34)
print("El indice de 34 es ",indice)
lista= list(tupla)
print("La lista es ",lista)
"""

#DICCIONARIOS***************************
#Ejemplo

#crear diccionario
diccionario={}
#llenar un diccionario
diccionario["blue"]="azul"
print(diccionario)

for i in range(2):
    nombre= input("Ingrese una palabra en ingles: ")
    traduccion = input("Ingrese el significado en español: ")
    diccionario[nombre]= traduccion
print(diccionario)

#acceder a un valor mediante su clave
azul= diccionario["blue"]
print("Se traduce como ",azul)

#elimina un elemento de la lista con del
del diccionario["blue"]
print(diccionario)
