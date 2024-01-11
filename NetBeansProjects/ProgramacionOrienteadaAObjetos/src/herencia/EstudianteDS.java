/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package herencia;

import programacionorientadaaobjetos.Persona;

// Clase hija
public class EstudianteDS extends Persona {
    private int notas[];
    private int numeroCreditos;

    public Estudiantes (int notas[], int numeroCreditos,int edad, String nombre) {
        super(edad,nombre);
        this.notas = notas;
        this.numeroCreditos = numeroCreditos;
        
    }
    
}