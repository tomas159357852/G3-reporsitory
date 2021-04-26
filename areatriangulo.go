  
import java.util.Scanner;
class AreaTriangulo{
static Scanner teclado=new Scanner(System.in);
public static void main(String [] arg ){
 //definir Variables y otros
  System.out.println("hola mundo");
  int b, h, area;
  //Datos de Entrada
  System.out.println("Ingrese la base:");
  b=teclado.nextInt();
  System.out.println("ingrese altura:");
  h=teclado.nextInt();
  //proceso
  area=(b+h)/2;
  //datos de salida
  System.out.println("El area es:"+area);
}
}