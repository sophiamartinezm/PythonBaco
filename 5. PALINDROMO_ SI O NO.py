a = str(input("Ingrese una palabra: ")) 
b = "".join(reversed(a))
print(" ")

if a == b:
  print("Si es un palindromo :)")
else:
  print("No es un palindromo :(")