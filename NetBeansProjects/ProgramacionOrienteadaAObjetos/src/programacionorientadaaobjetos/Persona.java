



package programacionorientadaaobjetos;

/*
Una clase es una plantilla que define la estructura y comportamiento de un 
objeto. tiene dos partes principales que son atributos y metodos 
fundamentos de la POO herencia polimorfismo
*/
//Clase padre
public class Persona {
    
    /*
    la encapsulacion garantiza la integridad de los datos y protege la informacion
    contra modificaciones inesperadas
    */
        protected int edad;
        protected String nombre;
     
        
        public Persona() {
             edad = 24;
             nombre = "Michael";
        }
        
        //Valores proporcionados por el usuario
        public Persona(int edad, String nombre){
            this.nombre=nombre;
            this.edad=edad;
        }
        
        public static void metodoStatic(int numero){
            System.out.println("El numero es "+numero);
        }
                              
     
        public void imprimirDatos () {
             System.out.println (
             "Nombre: "+nombre +" edad: "+edad);
        }
               
    public void verificarEdad(int numero){
        if (numero % 2==0) {
            System.out.println("Es un numero par");
        }else {
            System.out.println("Es un numero impar");
        }
    }
    
    public void verificarEdad(int numero, String nombre){
        System.out.println("Mi nombre es: "+nombre);
        if (numero % 2==0) {
            System.out.println("Es un numero par");
        }else {
            System.out.println("Es un numero impar");
        }
    }
}
