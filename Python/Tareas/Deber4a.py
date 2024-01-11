"""A) Escriba un programa que simule una cuenta de banco. El programa solicitará primero una cantidad, que será la cantidad de dinero que 
queremos ahorrar (validar la cantidad ingresada)."""
"""
# Solicito al usuario la cantidad que quiere ahorrar
objetivo_ahorro = float(input("Ingrese la cantidad que desea ahorrar: "))

# Inicializar el total ahorrado
total_ahorrado = 0

# Bucle para ingresar las cantidades que se van ahorrando
while total_ahorrado < objetivo_ahorro: #Mientras el total sea menor que el objetivo
    # Continua ingresando la cantidad a ahorrar
    cantidad_ahorro = float(input("Ingrese la cantidad a ahorrar (positiva): "))

    # Validar que la cantidad ingresada sea positiva y mayor a 0
    while cantidad_ahorro <= 0:
        print("Por favor, ingrese una cantidad positiva.")
        cantidad_ahorro = float(input("Ingrese la cantidad a ahorrar (positiva): "))

# Incrementa el total ahorrado con la cantidad ingresada por el usuario
    total_ahorrado += cantidad_ahorro
    print(f"Total ahorrado hasta ahora: {total_ahorrado}") #Imprimo el total ahorrado# 

    # Una vez que el bucle ha terminado (se alcanzó o superó el objetivo de ahorro),
    #imprime un mensaje de felicitaciones indicando el objetivo de ahorro alcanzado
print(f"¡Felicidades! Has alcanzado tu objetivo de ahorro de {objetivo_ahorro}.") 
"""

"""B) Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante) y la vuelva a solicitar hasta que las dos 
contraseñas coincidan, con un límite de tres peticiones."""
"""
# Ingresar la contraseña principal
contraseña = input("Ingrese la contraseña principal: ") #Pido la contraseña al usuario

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


"""C) Realizar un menú de opciones:
Escriba un programa que pregunte una y otra vez si desea terminar el programa, siempre que conteste:
1. Si contesta exactamente "N" en mayúsculas       2. Si contesta exactamente "sí" en minúsculas.
3. Si contesta exactamente "SI" en mayúsculas      4. Si contesta exactamente "no" en minúsculas
5. Salir
"""
"""
while True:
    print("Menú de opciones:") #Creo el menu con mis opciones dentro de un bucle while que correrá mientras la respuesta sea True
    print('1. Si contesta exactamente "N" en mayúsculas')
    print('2. Si contesta exactamente "sí" en minúsculas.')
    print('3. Si contesta exactamente "SI" en mayúsculas')
    print('4. Si contesta exactamente "no" en minúsculas')
    print('5. Salir')

    opcion = input("Ingrese el número de la opción deseada: ") #Pido al usuario una opcion
#Uso el bucle if para decirle que se hará según la opcion que tipee el usuario, si se equivoca vuelve al menu pero si tipea lo correcto
#pregunta si desea continuar
    if opcion == "1":
        respuesta = input('Ingrese "N" en mayúsculas para confirmar: ')
        if respuesta == "N":
            print("Opción 1 seleccionada. Continuando...")
        else:
            print("Respuesta incorrecta. Volviendo al menú.")
    elif opcion == "2":
        respuesta = input('Ingrese "sí" en minúsculas para confirmar: ')
        if respuesta == "sí":
            print("Opción 2 seleccionada. Continuando...")
        else:
            print("Respuesta incorrecta. Volviendo al menú.")
    elif opcion == "3":
        respuesta = input('Ingrese "SI" en mayúsculas para confirmar: ')
        if respuesta == "SI":
            print("Opción 3 seleccionada. Continuando...")
        else:
            print("Respuesta incorrecta. Volviendo al menú.")
    elif opcion == "4":
        respuesta = input('Ingrese "no" en minúsculas para confirmar: ')
        if respuesta == "no":
            print("Opción 4 seleccionada. Continuando...")
        else:
            print("Respuesta incorrecta. Volviendo al menú.")
    elif opcion == "5":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else: #Ademas, si ingresa cualquier otra opcion le decimos que no es valida
        print("Opción no válida. Por favor, ingrese un número del 1 al 5.")
#Si al hacer la pregunta el usuario responde que si, termina el programa
    terminar = input("¿Desea terminar el programa? (Ingrese 'sí' para salir): ")
    if terminar.lower() == "sí":
        print("Saliendo del programa. ¡Hasta luego!")
        break
"""

"""D) realizar un menú de opciones:
Leer números enteros de teclado, hasta que el usuario ingrese el 0.
1. Mostrar la sumatoria de todos los números ingresados.
2. Mostrar la sumatoria de todos los números positivos ingresados.
3. Mostrar cuál fue el mayor número ingresado.
4. La cantidad de números negativos ingresados
"""

#Creo una lista para almacenar los números ingresados
numeros = []
#Uso el bucle while para leer números hasta que se ingrese 0
while True:
    numero = int(input("Ingrese números enteros (ingrese 0 para dejar de ingresar): "))
    numeros.append(numero)
#Verificar si se ingresó 0 para finalizar el ingreso de números
    if numero == 0:
        numeros.pop()  # Eliminar el último 0 de la lista
        break
#----------------------------Menú de opciones----------------------------
while True:
    print("\nMenú de opciones:")
    print("1. Mostrar la sumatoria de todos los números ingresados.")
    print("2. Mostrar la sumatoria de todos los números positivos ingresados.")
    print("3. Mostrar cuál fue el mayor número ingresado.")
    print("4. La cantidad de números negativos ingresados.")
    print("5. Salir")
#-------------------------------------------------------------------------
    opcion = int(input("Ingrese el número de la opción deseada: ")) #Pido la opcion de las que hay en el menú
#Defino con el bucle if lo que hará cada opcion del menú
    if opcion == 1:
        sumatoria = sum(numeros)
        print(f"Sumatoria de todos los números ingresados: {sumatoria}")
    elif opcion == 2:
        sumatoria_positivos = sum(num for num in numeros if num > 0)
        print(f"Sumatoria de todos los números positivos ingresados: {sumatoria_positivos}")
    elif opcion == 3:
        if numeros:
            mayor_numero = max(numeros)
            print(f"El mayor número ingresado fue: {mayor_numero}")
        else:
            print("No se ingresaron números.")
    elif opcion == 4:
        cantidad_negativos = len([num for num in numeros if num < 0])
        print(f"Cantidad de números negativos ingresados: {cantidad_negativos}")
    elif opcion == 5:
        print("Saliendo del programa. ¡Hasta luego!") #La opcion 5 será para slair
        break
    else: #Si no imprime ninguna de las opciones imprimo un mensaje que diga lo siguiente
        print("Opción no válida. Por favor, ingrese un número del 1 al 5.")

