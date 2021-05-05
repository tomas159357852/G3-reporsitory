def ejercicio11():
  print ("\t.::Calificación de examén::.")
  nota=int(input("Ingrese la nota númerica que obtuvo en el examén:"))
  if nota==10:
    mensaje="La nota en letra que obutvo es una A"
  elif nota==9:
    mensaje="La nota en letra que obutvo es una B"
  elif nota==8:
    mensaje="La nota en letra que obutvo es una C"
  elif nota==7 or nota==6:
    mensaje="La nota en letra que obutvo es una D"
  elif 1<=nota<=5:
    mensaje="La nota en letra que obutvo es una F"
  else:
    mensaje="Error: la nota que ingreso es errónea o superior a 10"
  print (mensaje)
ejercicio11()
  
