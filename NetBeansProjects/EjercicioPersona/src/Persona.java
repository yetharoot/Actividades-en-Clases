public class Persona {
    private String nombre;
    private int edad;
    private double promedio;
    // Constructor
    public Persona(String nombre, int edad, double[] calificaciones) {
        this.nombre = nombre;
        this.edad = edad;
        this.promedio = calcularPromedio(calificaciones);
    }
    private double calcularPromedio(double[] calificaciones) { // Método para calcular el promedio
        if (calificaciones.length == 0) {
            return 0.0;
        }
        double suma = 0.0;
        for (double calificacion : calificaciones) {
            suma += calificacion;
        }
        return suma / calificaciones.length;
    }
    public void verificarPasoSemestre() { // Método para verificar si el estudiante pasa el semestre
        if (promedio >= 6.0) {
            System.out.println(nombre + " ha pasado el semestre con un promedio de " + promedio);
        } else {
            System.out.println(nombre + " no ha pasado el semestre con un promedio de " + promedio);
        }
    }
    public double getPromedio() { // Método getter para obtener el promedio
        return promedio;
    }
    public static void main(String[] args) { // Método main para probar la clase Persona
        double[] calificacionesEstudiante1 = {7.5, 8.0, 6.5};
        Persona estudiante1 = new Persona("Carlos", 26, calificacionesEstudiante1);
        estudiante1.verificarPasoSemestre();

        double[] calificacionesEstudiante2 = {5.0, 4.5, 6.0};
        Persona estudiante2 = new Persona("Sara", 19, calificacionesEstudiante2);
        estudiante2.verificarPasoSemestre();
    }
}

