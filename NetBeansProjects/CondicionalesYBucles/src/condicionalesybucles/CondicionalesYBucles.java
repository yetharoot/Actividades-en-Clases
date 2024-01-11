package condicionalesybucles;

import java.util.Scanner;

//@autor michael

public class CondicionalesYBucles {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        System.out.println("Ingrese un dia de la semana");
        String dia = teclado.nextLine();
        
        switch (dia) {
           case "lunes":
                System.out.println("Es lunes");
                break;
            case "martes":
                System.out.println("Es martes");
                break;
            case "miercoles":
                System.out.println("Es miercoles");
                break;
            default:
                System.out.println("Error dia no valido");
        }
    }
}
