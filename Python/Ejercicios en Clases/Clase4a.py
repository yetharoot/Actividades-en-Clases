#Practicas de la clase anterior:

#Ejercicio 1: Escribe un programa que pregunte una y otra vez si desea continuar con el programa, siempre que se 
#conteste si o SI (mayus o minus)
"""
salir= input("Desea continuar con el programa? escriba Si o No: ").lower()
while salir == "si":
    salir= input("Desea continuar con el programa? escriba Si o No: ").lower()

print("Gracias por utilizar") """
    
#Ejercicio 2: Escriba un programa que solicite una contraseña y la vuelva a solicitar hasta que las dos coincidan, con 
#un imite de tres peticiones
"""
pass1= input("Ingrese su contraseña: ")
pass2= input("Vuelva a ingresar su contraseña: ")
intentos= 3
contador= 0

while pass1 != pass2 and contador < intentos:
    print("La contraseña no coincide, por favor ingrese de nuevo: ")
    pass2= input("Confirme su contraseña: ")
    contador +=1 

    if pass1 == pass2:
       print("\nLas contraseñas coinciden")
    else:
       print("\nLas contraseñas no ha sido validada")
"""

#Ejercicio 3:
#Realizar un programa que lea un numero entero y determine si sus dos ultimos digitos son iguales

numero= int(input("Ingrese un numero entero: "))
ultimoNumero= numero % 10
segundoNumero= (numero %100)//10

if segundoNumero == ultimoNumero:
    print("\nLos ultimos dos digitos son iguales")
else:
    print("\nLos ultimos digitos no son iguales") 
