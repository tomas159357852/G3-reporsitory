#ejercicio06 en la tarea
def ejercicio06():
  print ("Cual es el costo y descuento que tendrá un artículo")
  precioX=0
  precioP=int(input("Indique cual es el precio del artículo:"))
  if precioP >= 200:
    precioX=precioP-(precioP*0.15)
  elif precioP >= 100 and precioP < 200:
    precioX=precioP-(precioP*0.12)
  elif precioP < 100:
    precioX=precioP-(precioP*0.10)
  print ("El precio final del producto será:", precioX)
ejercicio06()