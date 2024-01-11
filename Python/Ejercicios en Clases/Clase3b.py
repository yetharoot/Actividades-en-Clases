#Ejercicio 4: 
#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
# Después debe mostrar por pantalla la paga que le corresponde. 
"""
jornada = float(input("\n¿Cuántas horas de trabajo realizas?: ")) #Le pedimos al usuario ingresar las horas que trabaja.
hora = float(input("\n¿Cuánto cobras por hora?: ")) #Luego, le pedimos la cantidad que cobra por hora.

paga = jornada * hora #Le decimos al programa que la paga será igual a las horas de trabajo multiplicadas por lo que
#cobra por hora

print("\nTu pago total correspondiente es: ", paga) #Finalmente, inprimimos que su paga total es de "variable paga"
"""

#-----------------------------------BUBLE WHILE-----------------------------------
#Ejemplo 1: 
"""
while True:
    condicion= int(input("Ingrese un numero entero: "))
    if condicion > 0:
       print("\nEl número es positivo")
    elif condicion < 0:
       print("\nEl número es negativo")
    else:
       print("\nEl número es cero") 
    salir=input("Presiona cualquier tecla para continuar o escribe ('no') para salir: ")

    if (salir == "no"): break

print("\nGRACIAS POR UTILIZAR EL PROGRAMA") """
"""
#Ejemplo 2:
numero = 1
while numero <= 10:
    print("Michael Suarez ",numero)
    numero += 1
    if numero == 5: continue
   
print("Gracias por utilizar el programa") """


#-----------------------------------BUBLE FOR-----------------------------------
#Ejemplo 1:
print("Ejemplo 1")
for i in range (1, 6): #Mi rango va del 1 al 5 ya que range no toma en cuenta el ultimo valor
    print(i)
#Ejemplo 2:
print("Ejemplo 1")
for i in range (10, 0, -4):
    print(i)                   
#---range y len---
print("Ejemplo 3")
for i in range (4, 12): 
    if i % 2 == 0:
        print(i)
