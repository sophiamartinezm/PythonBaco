#8 Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”. Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, informarle que no se puede procesar el dato.

letra = str(input("Ingrese una letra: "))

if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U" or letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
  print("¡Es una vocal! :)")

else:
  print("No es una vocal :(")

