#6. Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos variables. A continuación, imprimir “coincidencia” si los nombres de ambas personas comienzan con la misma letra ó si terminan con la misma letra. Si no es así, imprimir “no hay coincidencia”. 

print("¿Hay coincidencias en los nombres?")

x = str(input("Ingrese el primer nombre: "))

y = str(input("Ingrese el segundo nombre: "))      

if x[-1] == y[-1] or x[0] == y[0]:
  print("¡Si hay coincidencias! :)")
else:
  print("No hay coincidncias :(")