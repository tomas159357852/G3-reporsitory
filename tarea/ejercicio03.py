#ejercicio03 en la tarea
def ejercicio03():
  print("Que regalo comprarle a tu ser querido")
  dineroX=int(input("ingrese la cantidad de dinero que tiene:"))
  if dineroX<=10 and dineroX>0:
    print("El regalo mas adecuado seria una Tarjeta")
  elif dineroX>10 and dineroX<=100:
    print("El regalo mas adecuado son chocolates")
  elif dineroX>=101 and dineroX<=251:
    print("El regalo adecuado son las flores")
  elif dineroX>251:
    print("El regalo mas adecuado es un anillo")
  else:
    print("Usted ah ingresado un dato incorrecto")
ejercicio03()