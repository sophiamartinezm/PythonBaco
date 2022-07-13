#2) Un programa que imprima el siguiente patron
#*
#**
#***
#****
#*****
#******
#*******
#********
#*********
#**********

print("Patrón de tarea 1")
for i in range (0, 10): #RANGO QUE CUENTE LÍNEA POR LÍNEA
  for j in range (0, i+1): #DE 0 A i+1
   print("*", end = "") #PARA CADA ITERACIÓN VA UN ASTERISCO, LUEGO UN ESPACIO,Y UN SALTO. #END =: SE USA PARA QUE NO FINALICE LA LÍNEA PERO SI EL PRINT.
  print()

print("Patrón 2")
for i in range (0, 10):
  for j in range (0, 1):
   print("*", end = "")
  print()
