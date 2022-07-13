#1) Un programa en Python que reciba un numero entero N y que muestre una escalera de # con N escalones. Ejemplo: a. Entrada: 5, b. Salida: 
#
##
###
####
#####

x = int(input("Ingrese un número: ")) #Se pide ungresar un número
for i in range (0, x): #RANGO QUE CUENTE LÍNEA POR LÍNEA
  for j in range (0, i+1): #DE 0 A i+1
   print("#", end = "") #PARA CADA ITERACIÓN VA UN HASHTAG, LUEGO UN ESPACIO,Y UN SALTO. #END =: SE USA PARA QUE NO FINALICE LA LÍNEA PERO SI EL PRINT.
  print()
