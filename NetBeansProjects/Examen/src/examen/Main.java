//Archivo "Main.java" modificado para este ejercicio
package examen;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Crear una lista de objetos de tipo Estudiante
        List<Estudiante> listaEstudiantes = new ArrayList<>();

        // Leer por teclado el nombre del estudiante
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese el nombre del estudiante: ");
        String nombreEstudiante = scanner.nextLine();

        // Llenar dinámicamente un arreglo de notas
        System.out.print("Ingrese la cantidad de notas a registrar: ");
        int cantidadNotas = scanner.nextInt();

        double[] notas = new double[cantidadNotas];
        for (int i = 0; i < cantidadNotas; i++) {
            System.out.print("Ingrese la nota " + (i + 1) + ": ");
            notas[i] = scanner.nextDouble();
        }

        // Calcular el promedio del estudiante
        double promedio = calcularPromedio(notas);

        // Determinar si el estudiante aprobó el semestre
        String estadoAprobacion = determinarEstadoAprobacion(promedio);

        // Mostrar por mensaje el estado del estudiante
        System.out.println("El estudiante " + nombreEstudiante + " " + estadoAprobacion +
                " el semestre con un promedio de " + promedio);

    }

    private static double calcularPromedio(double[] notas) {
        if (notas.length == 0) {
            return 0.0;
        }

        double suma = 0.0;
        for (double nota : notas) {
            suma += nota;
        }

        return suma / notas.length;
    }

    private static String determinarEstadoAprobacion(double promedio) {
        if (promedio >= 7.0) {
            return "aprobó";
        } else if (promedio >= 4.0) {
            return "supletorio";
        } else {
            return "reprobó";
        }
    }
}

