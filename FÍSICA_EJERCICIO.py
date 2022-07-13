menu = int(input('''¿Qué quiere encontrar?: 
      1. Velocidad 
      2. Distancia 
      3. Tiempo
      '''))

if menu == 1:
  print("Velocidad")

  print("Ingrese la distancia ")
  d = int(input())

  print("Ingrese el tiempo")
  t = int(input())
  
  r = (d / t)
  print("La velocidad es de:" ,r, "(^o^)丿")


if menu == 2:
  print("Distancia")

  print("Ingrese velocidad ")
  v = int(input())

  print("Ingrese el tiempo")
  t = int(input())
  
  r = (v * t)
  print("La distancia es de:" ,r, ":)")

  
if menu == 3:
   print("Tiempo")

   print("Ingrese distancia")
   d = int(input())

   print("Ingrese la velocidad")
   t = int(input())
  
   r = (d / t)
   print("El tiempo es de:" ,r, "♪┏(･o･)┛♪")
  
