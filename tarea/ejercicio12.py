def ejercicio12():
  print ("\t::Dias numericos a dias normales::")
  dia=int(input("Ingrese con el numero correspondiente el día de la semana:"))
  if dia==1:
    mensaje="El día de hoy es Lunes"
  elif dia==2:
    mensaje="El día de hoy es martes"
  elif dia==3:
    mensaje="El día de hoy es miércoles"
  elif dia==4:
    mensaje="El día de hoy es jueves"
  elif dia==5:
    mensaje="El día de hoy es viernes"
  elif dia==6:
    mensaje="El día de hoy es sabado"
  elif dia==7:
    mensaje="El día de hoy es domingo"
  else:
    mensaje="Error: ah ingresado un numero supeior a 7 o un número negativo"
  print (mensaje)
ejercicio12()