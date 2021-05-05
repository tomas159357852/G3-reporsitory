#ejercicio04 en la tarea
def ejercicio04():
  print("Cuanto cobrar por el estacionamiento")
  estacionamientoX=0
  mensaje=("")
  estacionamientoX=int(input("ingrese el tiempo de estacionamiento:"))
  if estacionamientoX>0 and estacionamientoX<=2:
    mensaje="El pago será de 5$ cada uno"
  elif estacionamientoX>2.01 and estacionamientoX<=5:
    mensaje="El pago será de 4$ cada uno"
  elif estacionamientoX>5.01 and estacionamientoX<=10:
    mensaje="El pago será de 3$ cada uno"
  elif estacionamientoX>10.01:
    mensaje="El pago será de 2 pesos cada uno"
  else:
    mensaje="Usted ah ingresado un dato incorrecto o negativo"
  print (mensaje)
ejercicio04()