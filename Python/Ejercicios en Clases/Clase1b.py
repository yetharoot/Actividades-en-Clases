#Realizar cuatro variables... entero, caracter, booleano e imprimir texto en pantalla.
"""
numeroInpar = 27
precioTeclado = 45.999
letra = 'J'
esSabado = True
nombreDeEstudiante = "Mike"
#Todo en un solo print
print(f"El numero es: {numeroInpar} \nPrecio del teclado: ${precioTeclado} \nLa letra es: {letra} \nHoy es sabado?: {esSabado} \nEl estudiante se llama: {nombreDeEstudiante}\n")

#Cada una en un print aparte
print("El numero inpar es: "+str(numeroInpar))
print("El teclado cuesta: "+str(precioTeclado))
print("La letra es: "+(letra))
print("¿Hoy es sabado?: "+str(esSabado))
print("El estudiante se llama: "+(nombreDeEstudiante))"""


#La funcion type nos devuelve el tipo de dato que es una variable, asi:
#print(type(numeroInpar))

#La funcion input nos pide un texto y devuelve un texto, es decir una cadena
numeroInpar=input("Ingrese un numero inpar: ") 
print(numeroInpar)
print(type(numeroInpar)) #45 es un dato entero pero input me devuelve un string, nos dice que es tipo string

#Para convertir un dato tipo string a uno entero es:
numeroInpar=int(input("Ingrese un numero inpar: ")) #Pongo int antes de input y meto todo entre parentesis. Aplica igual para float...
print(numeroInpar)
print(type(numeroInpar)) #En este caso me pondrá que es de tipo entero (int)
