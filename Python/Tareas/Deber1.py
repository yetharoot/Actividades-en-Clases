#Ejercicio 1: Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
# Después debe mostrar por pantalla la paga que le corresponde. 
"""
jornada = float(input("¿Cuántas horas de trabajo realizas?: ")) #Le pedimos al usuario ingresar las horas que trabaja.
hora = float(input("¿Cuánto cobras por hora?: ")) #Luego, le pedimos la cantidad que cobra por hora.

paga = jornada * hora #Le decimos al programa que la paga será igual a las horas de trabajo multiplicadas por lo que
#cobra por hora

print("Tu pago total correspondiente es: ", paga) #Finalmente, inprimimos que su paga total es de "variable paga"
"""

#Ejercicio 2: Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa 
# corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde 
# <imc> es el índice de masa corporal.
"""
peso = input("¿Cuál es tu peso en kg?: ") #Pedimos al usuario que ingrese su peso para almacenarlo en una variable
estatura = input("¿Cuál es tu estatura en metros?: ") #Pedimos al usuairo su estatura para almacenar en otra variable

#Declaramos la variable "imc" cuyo valor es la division entre las variables "peso" y "estatura"
imc = float(peso)/float(estatura)

#Imprimimos en pantalla que el indice de masa corporal es... concatenamos con la variable "imc" y le pedimoms al 
#programa que cambie el tipo de dato (que es flotante) a un string
print("Tu índice de masa corporal es: " + str(imc)) 
"""

#Ejercicio 3: Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo 
# y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas 
#que saldrán en cada paquete a demanda. Cada payaso pesa 112g y cada muñeca 75g. Escribir un programa que lea el número 
# de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

peso_payaso = 112 #Declaro la variable para el peso del payaso y le doy el valor que le corresponde (112g)
peso_muñeca = 75 #Declaro la variable para el peso de la muñeca y le doy el valor que le corresponde (75g)

#Pido al usuario que ingrese el numero de payasos y muñecas que se vendieron en el ultimo pedido
payasos = int(input("Payasos vendidos en el ultimo pedido: ")) 
muñecas = int(input("Muñecas vendidas en el ultimo pedido: "))

#Defino la variable "peso_total" y le digo al programa que su valor será igual al peso del payaso multiplicado por los 
#payasos vendidos y eso se sumará al peso de la muñeca multiplicado por el numero de muñecas vendidas
peso_total = peso_payaso * payasos + peso_muñeca * muñecas

#Imprimo en pantalla que el peso del paquete es igual a la variable "peso_total" y cambio su tipo de dato a string
print("El peso total del paquete es " + str(peso_total))  





