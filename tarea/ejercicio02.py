def ejercicio02():
  print ("El sueldo semanal de un trabajador")
  sueldoP=0
  cantidadX=int(input("ingrese las horas trabajadas:"))
  cantidad2X=int(input("ingrese el sueldo por hora:"))
  if cantidadX>40:
    sueldoP=cantidadX*cantidad2X
  else:
    sueldoP=cantidadX*cantidad2X
  print("El sueldo que recibe es:", sueldoP)
ejercicio02()


#def pagoSemanaBase40horas():
  print ("Pago semanal del trabajador")
  sueldoPagarSem=0.0
  #Datos de entrada
  horasTra=int(input("Ingrese horas trabajadas a la semana:"))
  horasPago=int(input("Ingrese el pago por hora:")) 
  #Proceso 
  if horasTra>40:
    sueldoPagarSem=40*horasPago+(horasTra-40)*2*horasPago
  else:
    sueldoPagarSem=horasTra*horasPago
  #Datos de salida
  print("El sueldo a pagar al trabajador es:", sueldoPagarSem)