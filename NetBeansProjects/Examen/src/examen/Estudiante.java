//Archivo "Estudiante.java"
package examen;

public class Estudiante {
    private String nombre;
    private int semestre;
    private double nota;

    // Constructor
    public Estudiante(String nombre, int semestre, double nota) {
        this.nombre = nombre;
        this.semestre = semestre;
        this.nota = nota;
    }

    public String getNombre() {
        return nombre;
    }

    public int getSemestre() {
        return semestre;
    }

    public double getNota() {
        return nota;
    }

    @Override
    public String toString() {
        return "Estudiante{" +
                "nombre='" + nombre + '\'' +
                ", semestre=" + semestre +
                ", nota=" + nota +
                '}';
    }
    
    //PERSONA
    public class Persona {
    private String nombre;
    private int edad;
    private String direccion;

    // Constructor
    public Persona(String nombre, int edad, String direccion) {
        this.nombre = nombre;
        this.edad = edad;
        this.direccion = direccion;
    }

    // Getters y setters

    public String getNombre() {
        return nombre;
    }

    public int getEdad() {
        return edad;
    }

    public String getDireccion() {
        return direccion;
    }

    // Métodos adicionales si es necesario
}
    //ESTUDIANTE-DS
    public class EstudianteDS extends Persona {
    private int semestre;
    private double nota;

    // Constructor
    public EstudianteDS(String nombre, int edad, String direccion, int semestre, double nota) {
        super(nombre, edad, direccion);
        this.semestre = semestre;
        this.nota = nota;
    }

    // Getters y setters específicos de EstudianteDS

    public int getSemestre() {
        return semestre;
    }

    public double getNota() {
        return nota;
    }

    // Métodos adicionales si es necesario
}


}
