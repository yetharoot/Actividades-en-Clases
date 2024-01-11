
package programacionorientadaaobjetos;

import herencia.Estudiantes;
import herencia.EstudianteDS;
import java.util.ArrayList;
import java.util.Scanner;






public class ProgramacionOrienteadaAObjetos {

    public static void main(String[] args) {
        
        Scanner teclado = new Scanner(System.in);
        //Crear un nuevo objeto de la clase persona
        int notas[] = new int[] {5,6,8,7};
        String materias[]=new String[] {"uno","dos"}; 
        
        Persona [] persona = new Persona[3];
        /*
        
        
        
        
        */
        Persona[0]= new Persona(32,"Michae");
        Persona[1]= new EstudianteDS(notas, 20, 2, "Miguel");
        Persona[2]= new Estudiantes (materias, 20, 20, "Sara");
         
        for (Persona i :persona); {
            i.imprimirDatos();
            System.out.println(""); 
        }
    }
    
    
}
