#Ejercicio 1: Elaborar un programa que lea un número entero y determine si sus dos últimos dígitos son iguales

# Solicito al usuario que ingresar un número entero
numero_entero = int(input("Ingrese un número entero: ")) #Determino la variable "numero_entero" que será de tipo int

# Obtengo los dos últimos dígitos del número, para ello determino la variable "ultimos_dos_digitos" que será igual 
# al resto entre "numero_entero" y 100... 
ultimos_dos_digitos = numero_entero % 100 

# Determino si los dos últimos dígitos son iguales, para ello utilizo la funcion if y le digo que si la division entre 
# "ultimos_dos_digitos" y 10 es igual a el resto entre "ultimos_dos_digitos" y 10 entonces los ultimos dos digitos 
# del numero serán iguales
if ultimos_dos_digitos // 10 == ultimos_dos_digitos % 10: 
    print(f"Los dos últimos dígitos de {numero_entero} son iguales.")
    
# De lo contrario, los ultimos dos digitos no son iguales
else:
    print(f"Los dos últimos dígitos de {numero_entero} no son iguales.") 


#Ejercicio 2: Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
# Después debe mostrar por pantalla la paga que le corresponde

jornada = float(input("¿Cuántas horas de trabajo realizas?: ")) #Le pedimos al usuario ingresar las horas que trabaja.
hora = float(input("¿Cuánto cobras por hora?: ")) #Luego, le pedimos la cantidad que cobra por hora.

paga = jornada * hora #Le decimos al programa que la paga será igual a las horas de trabajo multiplicadas por lo que
#cobra por hora

print("Tu pago total correspondiente es: ", paga) #Finalmente, inprimimos que su paga total es de "variable paga"


#Ejercicio 3: Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de 
#masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> 
#donde <imc> es el índice de masa corporal

peso = input("¿Cuál es tu peso en kg?: ") #Pedimos al usuario que ingrese su peso para almacenarlo en una variable
estatura = input("¿Cuál es tu estatura en metros?: ") #Pedimos al usuairo su estatura para almacenar en otra variable

#Declaramos la variable "imc" cuyo valor es la division entre las variables "peso" y "estatura"
imc = float(peso)/float(estatura)

#Imprimimos en pantalla que el indice de masa corporal es... concatenamos con la variable "imc" y le pedimoms al 
#programa que cambie el tipo de dato (que es flotante) a un string
print("Tu índice de masa corporal es: " + str(imc)) 


#Ejercicio 4: Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por 
#correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y 
#muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que 
#lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado

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


#Ejercicio 5: Imprime los números del 1 al 10. en orden descendente:10,9,8,7,6,5,4,3,2,1 y ascendente:1,2,3,4,5,6,7,8,9,10

#-------------------Orden descendente-------------------
print("Orden descendente:") 
#Utilizo el bucle for para imprimir en orden descendente, para ello determino que mi rango empieza en 10 y acaba en cero
#para que termine en 1 ya que no range toma el último valor del rango. Además, le pido que vaya restando de uno en uno
for i in range(10, 0, -1): 
    print(i)

#-------------------Orden ascendente-------------------
print("\nOrden ascendente:") #A este string agrego un salto de linea 
#Utilizo el bucle for para imprimir en orden ascendente, para ello determino que mi rango empieza en 1 y acaba en 11
#para que termine en 10 ya que range no toma el último valor del rango.
for i in range(1, 11):
    print(i)
    