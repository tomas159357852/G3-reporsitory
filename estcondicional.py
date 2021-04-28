def estcondicional01():
  #definiendo variables
  print("Ejemplo de estructura condicional en py")
  MontoP=0
  #datos de entrada
  cantidadX=int(input("ingrese la cantidad de lapices:"))
  #proceso
  if cantidadX>=1000:
    MontoP=cantidadX*0.80
  else:
    MontoP=cantidadX*0.90
  #Datos de salida
  print("El monto a pagar es:", MontoP)
estcondicional01()