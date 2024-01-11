# 1: Ejemplo de métodos y propiedades de las listas
"""
#Creo mi lista
lista = [1, 2, 3, 4, 5]

# Acceder y modificar elementos por índice
primer_elemento = lista[0]   #Usmos la propiedad "index" para acceder a un elemento por índice
lista[2] = 10               #Modificamos un elemento por índice

# Agregar un elemento al final de la lista
lista.append(6)             #Usamos el método append para agregar un elemento al final de la lista

# Imprimir la lista y algunos resultados
print("Lista actualizada:", lista)
print("Primer elemento:", primer_elemento)
print("Longitud de la lista:", len(lista))  # Propiedad: Obtener la longitud de la lista """


# 2: Ejemplo de métodos y propiedades de las tuplas
"""
# Creo mi tupla
tupla = (1, 2, 3, 4, 2, 5, 2)

# Para acceder a elementos por índice usamos la propiedad de indexacion y asi obtenemos el primer elemento
primer_elemento = tupla[0]

# Métodos "index" y "count"
indice_del_dos = tupla.index(2)  # Para que devuelva el índice de la primera aparición de 2
conteo_del_dos = tupla.count(2)  # Para que devuelva la cantidad de veces que aparece 2 en la tupla

# Imprimo la tupla y los resultados que quiero
print("Tupla actual:", tupla)
print("Primer elemento:", primer_elemento)
print("Índice de la primera aparición de 2:", indice_del_dos)
print("Cantidad de veces que aparece 2:", conteo_del_dos) """


# 3: Ejemplo de métodos y propiedades del set
"""
# Crear un conjunto
conjunto = {1, 2, 3, 3, 4}

#Usamos los métodos add y remove

# Agregar un elemento al conjunto con el método "add"
conjunto.add(5) 

# Eliminar un elemento del conjunto con el método "remove"
conjunto.remove(3)  

# Imprimir el conjunto y los resultados que queremos 
print("Conjunto actualizado:", conjunto)
print("Número de elementos:", len(conjunto))  # Agregamos la propiedad "len" para tener la longitud
print("¿El número 2 está en el conjunto?", 2 in conjunto)  """


# 4: Ejemplo de métodos y propiedades de los diccionarios 

# Crear un diccionario
diccionario = {"nombre": "Sara", "edad": 21, "ciudad": "Cuzco"}

# Para obtener un valor mediante una clave
nombre = diccionario["nombre"]  #Uso la propiedad acceso mediante clave
edad = diccionario.get("edad")  #Uso el método "get" para obtener un vaor mediante una clave

#Uso el método "key" para tener una vista de todas las claves en el diccionario
claves = diccionario.keys()  #

# Imprimir el diccionario con los resultados deseados
print("Diccionario:", diccionario)
print("Valor de 'nombre':", nombre)
print("Claves en el diccionario:", claves)
