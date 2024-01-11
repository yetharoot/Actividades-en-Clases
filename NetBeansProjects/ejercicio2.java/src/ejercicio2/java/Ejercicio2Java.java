package ejercicio2.java;
import java.util.Scanner;

/*
   @author michael
 */

public class Ejercicio2Java {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in); 

        int numeros[] = new int[5];
        for (int i = 0; i < 5; i++) {
            System.out.print((i + 1) + " Ingrese un numero entero: ");
            int entrada = teclado.nextInt();
            numeros[i] = entrada; // Corregir la asignación al array 'numeros'
        }
        int suma = 0;
        for (int i : numeros) {
            suma += i;
        }
        System.out.println("El promedio es " + (suma / numeros.length));
    }
}
