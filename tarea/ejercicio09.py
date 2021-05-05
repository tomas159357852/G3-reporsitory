def ejercicio09():
  #ingreso de datos1
  print ("\t .::Bienvenido a la compañia de seguros::.")
  print ("1. Cobertura amplia")
  print ("2. Cobertura de daños a terceros")
  tipo=int(input("Escriba la opción correspondiente al tipo de poliza que desde adquirir:"))
  cuota=1200
  cuotaB=950
  primerC=0
  segundoC=0
  tercerC=0
  cuartoC=0
  #Proceso
  if tipo==1:
    print("Conteste con un si y un no las preguntas:")
    pregunta1=input("¿Tiene el hábito de beber alcohol?:").lower()
    if pregunta1=="si":
      primerC=cuota+(cuota*0.10)
    elif pregunta1=="no":
      primerC=cuota
    else:
      print("Respuesta incorrecta")
    pregunta2=input("¿Usted utiliza lentes?:").lower()
    if pregunta2=="si":
      segundoC=primerC+(cuota*0.05)
    elif pregunta2=="no":
      segundoC=primerC
    else:
      print("Respuesta incorrecta")
    pregunta3=input("¿Usted padece algúna enfermedad?:").lower()
    if pregunta3=="si":
      tercerC=segundoC+(cuota*0.05)
    elif pregunta3=="no":
      tercerC=segundoC
    else:
      print("Respuesta incorrecta")
    pregunta4=input("¿Usted tiene mas de 40 años?:").lower()
    if pregunta3=="si":
      cuartoC=tercerC+(cuota*0.20)
    elif pregunta3=="no":
      cuartoC=tercerC+(cuota*0.10)
    else:
      print("Respuesta incorrecta")
  elif tipo==2:
    print("Conteste con un si y un no las preguntas:")
    pregunta1=input("¿Tiene el hábito de beber alcohol?:").lower()
    if pregunta1=="si":
      primerC=cuotaB+(cuotaB*0.10)
    elif pregunta1=="no":
      primerC=cuotaB
    else:
      print("Respuesta incorrecta")
    pregunta2=input("¿Usted utiliza lentes?:").lower()
    if pregunta2=="si":
      segundoC=primerC+(cuotaB*0.05)
    elif pregunta2=="no":
      segundoC=primerC
    else:
      print("Respuesta incorrecta")
    pregunta3=input("¿Usted padece algúna enfermedad?:").lower()
    if pregunta3=="si":
      tercerC=segundoC+(cuotaB*0.05)
    elif pregunta3=="no":
      tercerC=segundoC
    else:
      print("Respuesta incorrecta")
    pregunta4=input("¿Usted tiene mas de 40 años?:").lower()
    if pregunta4=="si":
      cuartoC=tercerC+(cuotaB*0.20)
    elif pregunta4=="no":
      cuartoC=tercerC+(cuotaB*0.10)
    else:
      print("Respuesta incorrecta")
  else:
    print("Error, ingrese la opción 1 o la opción 2")
  #salida de datos
  print(f"El costo total de la póliza será {cuartoC}")     
ejercicio09()