#Ejercicio 6: Solicita al usuario ingresar una frase y una vocal para contar cuántas veces aparece la vocal en su frase.

frase = input("Ingresa una frase: ") #Le pido al usuario una frase y una vocal
vocal = input("Ingresa una vocal: ")

#Declaro la variable "contar_vocales" cuyo resultado será el conteo de cada letra que encuentre dentro de la frase
contar_vocales = frase.lower().count(vocal)

print(f"La letra {vocal} aparece {contar_vocales} veces en la frase.") #Imprimo el resultado concatenando las variables


#Ejercicio 7: Solicita al usuario ingresar una cantidad en dólares y realiza la conversión a euros utilizando un tipo 
#de cambio fijo y teniendo en cuenta que 1 dolar equivale a 93 centimos al momento de hacer el ejercicio 6/12/2023

#Declaro mi variable para hacer el tipo de cambio considerando que 1 dólar = 0.93 centimos de euro 
tipo_cambio = 0.93  

dolares = float(input("Ingresa la cantidad en dólares: ")) #Pido al usuario ingresar cantidad en dolares
euros = dolares * tipo_cambio #Declaro que "euros" es igual a "dolares" multiplicado por "tipo_cambio" ó 0.93

print(f"{dolares} dólares equivalen a {euros:.2f} euros.") #Imprimo el resultado agregandole dos decimales a euros


#Ejercicio 8: Pide al usuario ingresar una palabra y muestra la palabra al revés.

palabra = input("Ingresa una palabra: ") #Pido al usuario que ingrese una palabra

#Declaro la variable para la palabra al revés 
#Para ponerla al revés utilizo este slice [::-1] que me devuelve los elementos de mi iterable desde el ultimo al primero
palabra_al_reves = palabra[::-1] 

print(f"Palabra al revés: {palabra_al_reves}") #Imprimo la palabra al revés con un texto


#Ejercicio 9: Pide al usuario ingresar su edad y determina si es mayor de edad o no.

edad = int(input("Ingresa tu edad: ")) #Pido al usuario que ingrese su edad

#Uso la condicional if-else para decirle que si "edad" es mayor o igual a 18 entonces es mayor de edad.
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.") #Caso contrario, imprimirá que la persona es menor de edad


#Ejercicio 10: Pide al usuario un número e imprime su tabla de multiplicar del 1 al 10, pero solo para los primeros 
#5 términos.

numero = int(input("Ingresa un número entero: ")) #Pido al usuario un numero entero

#Uso el bucle for para crear un rango del 1 al 6 para que llegue hasta 5
for i in range(1, 6):
    #Imprimo que el numero ingresado por cada numero del rango es igual a su multiplicacion
    print(f"{numero} x {i} = {numero * i}")
