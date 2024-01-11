"""A) Escriba un programa que lea un número entero del usuario y luego imprima el siguiente mensaje:
1.	"El número es positivo" si el número es mayor que cero.
2.	"El número es negativo" si el número es menor que cero.
3.	"El número es cero" si el número es igual a cero."""
"""
#Solicito al usuario que ingrese un número entero
numero = int(input("Ingrese un número entero: "))
#Verifico si el número es positivo, negativo o cero con bucle if
if numero > 0:
    print ("El número es positivo")
elif numero < 0:
    print ("El número es negativo")
else:
    print ("El número es cero") """
    


"""B) Escriba un programa que solicite una contraseña y la vuelva a solicitar hasta que las dos contraseñas coincidan, 
con un límite de tres peticiones."""
"""
#Configuro el número máximo de intentos
intentos_maximos = 3
#Inicializar el contador de intentos
intentos = 0

contraseña = input("Ingrese su contraseña: ") #Pido la contraseña al usuario

intentos_maximos = 3 #Inicio los contadores para intentos (0) e intentos maximos (3)
intentos = 0
#Uso el bucle while para decirle que se ejecute mientras intentos sea menor que intentos maximos
while intentos < intentos_maximos: 
    # Solicito la validación de la contraseña con un mensaje diferente
    validacion_contraseña = input("Ingrese nuevamente la contraseña para validar: ")

    # Verificar si la contraseña de validación coincide con la principal
    if validacion_contraseña == contraseña:
        print("Contraseña validada. ¡Acceso permitido!")
        exit()  # Terminar del programa si la contraseña de validación es correcta
    #Sumo los intentos de uno en uno y si intentos es menor que intentos maximos le digo que es incorrecta y pido que vuelva a validar
    else:
        intentos += 1 
        if intentos < intentos_maximos:
            print("Contraseña incorrecta. Inténtelo de nuevo.")

# Mensaje si se supera el límite de intentos
if intentos == intentos_maximos:
    print("Se ha alcanzado el límite de intentos. Acceso denegado.") """



"""C) Mostrar la serie de Fibonacci hasta el numero ingresado por el usuario """
"""
print (("Generar serie de Fibonacci: "))

# Solicito al usuario que ingrese un número
limite = int(input("Ingrese un número: "))

#Inicializo las variables a y b con los primeros dos términos de la serie de Fibonacci.
a, b = 0, 1

#Genero la serie con un bucle while que continuará mientras el valor actual (a) sea menor/igual al limite
while a <= limite: 
    print(a, end=", ") #Imprime el valor actual de la serie sin pasar a una nueva línea. Agrega una coma y espacio al final.
    a, b = b, a + b #a, b = b, a + b actualiza los valores de a y b para obtener el siguiente par de términos en la serie de Fibonacci.
"""


"""D) Leer un numero por teclado, contar el número total de dígitos de un número y sumar sus dígitos. Por ejemplo, el 
número es 12345, por lo que la salida debería ser 5. La suma de sus dígitos es 15."""

#Solicito al usuario que ingrese un número
numero = int(input("Ingrese un número: "))

#Convierto el número a una cadena de texto (string) para contar los dígitos
numero_str = str(numero)

#Uso la funcion "len" que me devuelve la longitud, en este caso del número total de dígitos
conDigitos = len(numero_str)

#Inicializo la suma de dígitos
sumDigitos = 0

#Sumo los dígitos individualmente 
for digito in numero_str:
    sumDigitos += int(digito)

#Muestro los resultados
print(f"El total de dígitos es: {conDigitos}")
print(f"La suma de los dígitos es: {sumDigitos}")

