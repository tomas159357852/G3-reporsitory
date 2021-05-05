def ejercicio10():
  print ("Cuanto costara el viaje de estudios por alumno")
  pasaje=int(input("Ingrese la cantidad de alumnos:"))
  mensaje=""
  if pasaje>100:
    mensaje="El costo por alumno será de 20 dolares"
  elif 50<=pasaje<=100:
    mensaje="El costo por alumno será de 35 dolares"
  elif 20<=pasaje<=49:
    mensaje="El costo por alumno será de 40 dolares"
  elif 1<=pasaje<20:
    mensaje="El costo por alumno será de 70 dolares "
  else:
    mensaje="Error: ah ingresado un dato negativo o incorrecto"
  print (mensaje)
ejercicio10()