menu = int(input('''Elige uno de los tres:
1. ¿SON O NO TOCAYOS?
2. POTENCIAS
3. SALUDAR CON TU EDAD 
'''))

if menu == 1 :
  print("¿SON O NO TOCAYOS?")

  print("Ingrese el primer nombre")
  x = str(input())

  print("Ingrese el segundo nombre")
  y = str(input())
  if (x == y) :
    print("¡Son tocayos! :)")
  else :
    print("No son tocayos :(")
  
  
if menu == 2 :
  print("POTENCIAS")

  print("Ingrese el primer número")
  x1 = float(input())

  print("Ingrese el segundo número")
  y1 = float(input())

  res1 = (x1 ** y1)
  print(res1)


if menu == 3 :
  print("SALUDAR CON TU EDAD")

  print("Ingresa tú nombre")
  x2 = str(input())

  print("Ingresa tú año nacimiento")
  y2 = int(input())

  print("¿En que año estás?")
  z2 = int(input())

  res = (z2 - y2)
  print("¡Holaaa",x2,"felicidades ya tienes",res,":)!")




