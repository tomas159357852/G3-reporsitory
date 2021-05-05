#ejercicio05 en la tarea
def ejercicio05():
  print ("Cual es la edad del menor de las personas")
  nombreA=input("ingrese el nombre de la primera persona:")
  edadA=int(input("ingrese la edad de la primera persona:"))
  nombreB=input("ingrese el nombre de la segunda persona:")
  edadB=int(input("ingrese la edad de la segunda persona:"))
  nombreC=input("ingrese el nombre de la tercera persona:")
  edadC=int(input("ingrese la edad de la tercera persona:"))
  if edadA < edadB and edadA < edadC and edadA<110:
    print ('La persona con menor edad es', nombreA + ' con la edad de', edadA)
  elif edadB < edadA and edadB < edadC and edadB<110:
    print ('La persona con menor edad es', nombreB + ' con la edad de', edadB)
  elif edadC < edadA and edadC < edadB and edadC<110:
    print ('La persona con menor edad es', nombreC + ' con la edad de', edadC)
  elif edadA == edadB or edadB ==edadC or edadA == edadC or edadA == edadB == edadC:
    print ('Hay mas de una persona con la menor edad')
  else:
    print("La edad o nombre es incorrecto")
ejercicio05()
  