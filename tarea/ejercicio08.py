def ejercicio08():
  print ("Sueldo y bono para el empleado")
  sueldo=int(input("Ingrese el sueldo actual que recibe:"))
  tiempo=int(input("Ingrese el tiempo que lleva trabajando en la empresa:"))
   #Proceso
  sueldot=0.0
  sueldo1=0.0
  sueldo2=0.0
  if tiempo>2 and tiempo<5:
    sueldo1=(sueldo*0.2)
  else:
    sueldo1=(sueldo*0.3)

  if sueldo<1000:
    sueldo2=(sueldo*0.25)
  elif sueldo>1000 and sueldo<=3500:
    sueldo2=(sueldo*0.15)
  elif sueldo>3500:
    sueldo2=(sueldo*0.1)
  
  if sueldo1>sueldo2:
    sueldot=sueldo1
  elif sueldo2>sueldo1:
    sueldot=sueldo2
    
  
  print("El bono que tendrá será de:", sueldot)
ejercicio08()
