/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package herencia;

import programacionorientadaaobjetos.Persona;

//Clase Hija
public class Estudiantes extends Persona {
    private int notas[];
    private int numeroCreditos;
    
    public Estudiantes (int notas[], int numeroCreditos, int edad, String nombre) {
        super(edad,nombre);
        this.notas = notas;
        this.numeroCreditos = numeroCreditos;
        
    }
    
    public int promedio() {
        int contador=0;
        for (int i=0;i<notas.length;i++) {
            contador += notas[i];
        }
        return contador/notas.length;
    }
    
    @Override
     public void imprimirDatos () {
             System.out.println (
                    "Nombre: "+nombre +" edad: "+edad +"Numero de Creditos: "+numeroCreditos);
             
             System.out.println("Mostrando notas");
             for (int i:notas){
                 System.out.println(i);
             }
        }
     
    
}
