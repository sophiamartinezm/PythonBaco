n = int(input("Ingrese un numero: "))
contador = 1
divisores = 0

while contador <= n:
  residuo = n % contador
 
  
  if residuo == 0:
    divisores = divisores + 1
  contador = contador + 1

if divisores == 2:
  print("Sí es primo :)")
else:
  print("No es primo :(")
