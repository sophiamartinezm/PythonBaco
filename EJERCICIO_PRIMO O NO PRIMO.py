#solicitamos un numero
n = int(input("Ingrese un numero: "))
contador = 1
divisores = 0

#mientras el contador sea menor o igual que n el residuo debe ser igual a n modulo del contador
while contador <= n:
  residuo = n % contador
  print(residuo)
  
  #si el residuo es igual a 0, se tienen que hacer dos cosas, primero sumarle 1 al divisor y sumarle 1 al contador
  if residuo == 0:
    divisores = divisores + 1
  contador = contador + 1

#si el divisor es igual a 2 podemos confirmar que n si es primo y podemos decirle cuantos divisores tiene sino le tenemos que decir que no es primo pero aun le podemos mostrar los divisores que tenga
if divisores == 2:
  print("Sí es primo")
  print("Tiene ",divisores, " divisores")
else:
  print("no es primo")
  print("Tiene ",divisores, " divisores")