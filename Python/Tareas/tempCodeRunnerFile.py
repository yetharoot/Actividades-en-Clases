while intentos < intentos_maximos:
    # Solicitar la contraseña al usuario
    pass1 = input("Ingrese la contraseña: ")
    pass2 = input("Ingrese de nuevo contraseña: ")
    
    # Verificar si la contraseña es correcta
    if pass1 == pass2:
        print("¡Contraseña correcta! Acceso concedido.")
        break  # Salir del bucle si la contraseña es correcta
    else:
        print("Contraseña incorrecta. Inténtelo nuevamente.")
        intentos += 1

# Verificar si se alcanzó el límite de intentos
if intentos == intentos_maximos:
    print("Se ha alcanzado el límite de intentos. Acceso denegado.")
