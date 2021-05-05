#ejercicio 3.17
def ejercicio13():
  print ("\tDetermina que paquete de te puedes comprar con tu dinero")
  #ingreso de datos
  dinero=int(input("Ingrese la cantidad de dinero que tiene:"))
  paquete1="una televisión, un modular, tres pares de zapatos, cinco camisas y cinco pantalones"
  paquete2="una grabadora, tres pares de zapatos, cinco camisas y cinco pantalones"
  paquete3="dos pares de zapatos, tres camisas y tres pantalones"
  paquete4="un par de zapatos, dos camisas y dos pantalones"
  mensaje=""
  #proceso
  if dinero>=50000:
    mensaje=f"Usted podrá comprarse el paquete A que consta de: {paquete1}."
  elif 20000<=dinero<50000:
    mensaje=f"Usted podrá comprarse el paquete B que consta de: {paquete2}."
  elif 10000<=dinero<20000:
    mensaje=f"Usted podrá comprarse el paquete C que consta de: {paquete3}."
  elif dinero<10000:
    mensaje=f"Usted podrá comprarse el paquete D que consta de: {paquete4}."
  print (mensaje)
ejercicio13()