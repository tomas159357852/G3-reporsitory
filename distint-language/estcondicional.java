import java.util.Scanner;
class estcondicional{
  static Scanner teclado=new Scanner(System.in);
  static void ejercicio01(){
    //Definir variables y otros
    System.out.println("Ejemplo estructura Condicional en Java");
    int cantidadX=0;
    double montoP=0;
    try{
    //Datos de Entrada
    System.out.println("Ingrese la cantidad de lapices:");
    cantidadX=teclado.nextInt();
    //Proceso
    if(cantidadX>=1000){
    montoP=cantidadX*0.80;
    }else{
    montoP=cantidadX*0.90;
    }
    //Datos de salida
    System.out.println("El monto a pagar es:"+montoP);
    }catch(Exception e){
      System.out.println("Error en el ingreso de datos, vuelva a ejecutar");
    }
  }

  static void ejercicio02(){
    //declarar variables
    int cantidadX;
    double montoP;
    //Datos de Entrada
    System.out.println("Ingrese la cantidad de personas invitadas:");
    cantidadX=teclado.nextInt();
    //Proceso
    if(cantidadX<=200){
      montoP=cantidadX*95;
    }else if(cantidadX>200 && cantidadX<=300){
      montoP=cantidadX*85;
    }else{
      montoP=cantidadX*75;
    }
    //datos de salida
    System.out.println("El monto a pagar es:"+montoP);
  }
  public static void main(String[] arg){
  //ejercicio01();
  ejercicio02();
  }
}