def ejercicio01():
  print ("Como saber si puedes votar por tu edad")
  montoP=0
  cantidadX=int(input("ingrese la edad que tiene:"))
  if cantidadX>=18:
    print ("Usted tiene la edad necesaria para votar")
  else:
    print ("Usted no cumple con la edad minima para votar")
ejercicio01()

#def votoElecciones2():
  print ("Como saber si puedes votar por tu edad")
  mensaje=""
  edadP=int(input("ingrese la edad que tiene:"))
  if edadP>=18:
    mensaje="Usted tiene la edad necesaria para votar"
  else:
    mensaje="Usted no cumple con la edad minima para votar"
  print (mensaje)