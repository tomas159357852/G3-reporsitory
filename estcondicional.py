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
def estcondicional02():
  #definir variables y otros
  print("Ejercicio 02 est. condicional")
  MontoP=0
  #datos de entrada
  cantidadX=int(input("ingrese la cantidad de personas invitadas:"))
  #proceso
  if cantidadX<200:
    MontoP=cantidadX*95
  elif cantidadX>200 and cantidadX<=300:
    MontoP=cantidadX*85
  else:
    MontoP=cantidadX*75
  #datos de salida
  print("La cantidad a pagar es:", MontoP)
#estcondicional01()
estcondicional02()