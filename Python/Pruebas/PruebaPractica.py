#---------------------------------EVALUACION PRACTICA PYTHON---------------------------------
#1
"""
def numeroEnt(): #Defino la funcion para mi numero entero
    #Uso el bucle while 
    while True:
        try:
            numero = int(input("Ingrese un número entero positivo: ")) #Pido el numero al usuario
            if numero > 0: #Uso el bucle if para decirle que si es mayor a 0 regrese el valor de numerok
                return numero
            else:
                print("Por favor, ingrese un número entero positivo.") #Si es menor que 0 pedrá al usuario corregir
        except ValueError:
            print("Error, ingrese un número entero válido.") #Si tipea cualqueir caracter que no sea un numero
                                                                 #dirá que es invalido
#Para imprimir impares:
def numerosImp(n):
    impares = [i for i in range(1, n+1) if i % 2 != 0]
    return impares

def main():
    numero = numeroEnt()
    impares = numerosImp(numero)

    print(f"\nNúmeros impares desde 1 hasta {numero}:")
    for impar in impares:
        print(impar, end=" ")
#Para imprimir cuantos impares hay:
    print(f"\n\nCantidad de números impares: {len(impares)}")

if __name__ == "__main__":
    main() """


#2
"""
def longitud_cadenas(lista_cadenas): #Defino la funcion para tener la longitud de cada string
    for cadena in lista_cadenas:
        #Imprimo la longitud de cada cadena y muestro un mensaje
        print(f"{cadena} tiene {len(cadena)} letras")

def main():
    #Creo la lista con las cadenas
    lista_cadenas = ["Yo", "Soy", "Estudiante", "De", "Ciberseguridad"]

    #Llamo a la función para imprimir la longitud de cada string
    longitud_cadenas(lista_cadenas)

if __name__ == "__main__":
    main() """


#3
"""
def numeroEntero(): #Defino la funcon para mi numero entero
    while True: #Uso el bucle while para ejecutar el programa
        try:
            #Pido al usuario un número entero
            numero = int(input("Ingrese un número entero positivo: "))
            
            #Verifico si el número es positivo diciendo que debe ser mayor a 0 con bucle if
            if numero > 0:
                return numero
            else:
                print("Por favor, ingrese un número entero positivo.") #Si no es mayor a 0 dirá esto
        except ValueError:
            print("Error: ingrese un número entero válido.") #Si no ingresa un numero saldrá mensaje de ERROR

def tablaMult(numero): #Defino la funcion para imprimir la tabla de multiplicar del numero ingresado por usuario
    print(f"\nTabla de multiplicar del {numero}:\n") #Concateno el mensaje con la variable numero
    for i in range(1, 11): #Creo el rango del 1 al 11 para que llegue hasta el 10
        resultado = numero * i #El resultado será el numero por (x) cada elemento del rango
        print(f"{numero} x {i} = {resultado}") #Imprimo que "numero por (x) i (cada elemento del rango) es resultado" 

def main():
    #Obtengo el número entero positivo del usuario
    numero = numeroEntero()
    #Imprimo la tabla de multiplicar del número ingresado
    tablaMult(numero)
if __name__ == "__main__": 
    main() """

"""
#4
#Funciones para cada operacion
def sumar(num1, num2):                      
    return num1 + num2                      
def restar(num1, num2):                      
    return num1 - num2
def multiplicar(num1, num2):
    return num1 * num2
def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        print("Error: No se puede dividir por cero.")
        return None
    
#---------------------MENU---------------------
def menu(): #Deino la funcion para el menu
    print("\nMenu de opciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
#-------------------FIN MENU-------------------

def obtener_opcion(): #Declaro la funcion para tener la opcion que se ingrese
    while True: #Uso bucle while para ejecutar el programa y... 
        try:
            opcion = int(input("\nIngrese la opcion que desea realizar: "))
            if 1 <= opcion <= 5: #...si la opcion está entre 1 y 5 entonces regresa lo que corresponda a cada opcion
                return opcion
            else:                #Si esta fuera de este limite imprime un mensaje de error
                print("ERROR: Ingrese una opción válida (1-5).")
        except ValueError:       #Si no ingresa un numero, le imprimo otro ERROR
            print("ERROR: Ingrese un número entero.")

def main(): #Llamo la funcion para iniciar el bucle y mostraré el menu
    while True:
        menu()

        opcion = obtener_opcion()

        if opcion == 5: #si la opcion es 5 saldra
            print("Saliendo del programa. ¡Hasta luego!")
            break

        num1 = float(input("Ingrese el primer número: ")) #Si la opcion es cualquier otra pedirá dos numeros
        num2 = float(input("Ingrese el segundo número: "))
#------------Se define lo que hará en base a cada opcion, es decir, la operacion que va a realizar------------------
        if opcion == 1:
            resultado = sumar(num1, num2)
            print(f"\nLa suma es: {resultado}")
        elif opcion == 2:
            resultado = restar(num1, num2)
            print(f"\nLa resta es: {resultado}")
        elif opcion == 3:
            resultado = multiplicar(num1, num2)
            print(f"\nLa multiplicación es: {resultado}")
        elif opcion == 4:
            resultado = dividir(num1, num2)
            if resultado is not None:
                print(f"\nLa división es: {resultado}")
if __name__ == "__main__":
    main() """



#5

def main(): 
    while True: #Uso el bucle while para iniciar el programa con la pregunta
        respuesta = input("¿Desea terminar el programa? (Ingrese 'SALIR' para salir): ") #Sin upper o lower porque debe ser mayus
        #Con bucle if le digo que si se tipea SALIR entonces termina el programa (break)
        if respuesta == 'SALIR': 
            print("Terminando el programa. ¡Hasta luego!")
            break
        else: #De lo contrario, me regresará la pregunta infinitamente. 
            print("Respuesta no válida. Por favor, ingrese 'SALIR' para terminar el programa.")

if __name__ == "__main__":
    main()
