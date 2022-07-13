#9. Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.

año = int(input("Ingresa un año para determinar si es bisiesto o no:  "))

if año % 4 == 0:
  print("Es un año bisiesto")

elif año % 100 == 0:
  print("No es bisiesto")

elif año % 400 == 0:
  print("Es un año bisiesto :)")

else:
  print("No es un año bisiesto :(")

  