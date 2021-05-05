import java.util.Scanner;
class ejercicio08{
static Scanner teclado=new Scanner(System.in);
static void ejercicio08(){
  //definir variables
  int anhoant;
  double sueldo, bonoant=0, bonosueld=0, bonoreal=0;
  //datos de entrada
  System.out.print("Ingrese los años de antiguedad:");
  anhoant=teclado.nextInt();
  System.out.print("Ingrese el sueldo del trabajador:");
  sueldo=teclado.nextDouble();
  //proceso
  if(anhoant>2 && anhoant<5){
    bonoant=sueldo*0.20;
  }else if(anhoant<=5){
    bonoant=sueldo*0.30;
  }
  if(sueldo<1000){
    bonosueld=sueldo*0.25;
  }else if(sueldo<=1000 && sueldo<=3500){
    bonosueld=sueldo*0.15;
  }else{
    bonosueld=sueldo*0.10;
  }
  if(bonoant>=bonosueld){
    bonoreal=bonoant;
  }else{
    bonoreal=bonosueld;
  }
  //datos de salida
  System.out.println("El trabajador tendrá un bono de:" +bonoreal+ "\nSin embargo su bono por antiguedad es: "+bonoant+ "\n y el bono sueldo es:"+bonosueld);
  
  }
  public static void main(String[] arg){
  ejercicio08();
}
}