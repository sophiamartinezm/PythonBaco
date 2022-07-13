#Ingrese usuario
u = str(input("Ingrese su usuario: "))
#Ingrese contrseña
c = str(input("Ingrese su contraseña: "))
#Esta variable nos ayuda a encontrar los últimos 3 digitos del usuario
y=u[-3:]
#Esta nos permite identificar que esos ultimos 3 digitos sean números
p=y.isdigit()
pv=str(p)
#Con esta variable contamos los espacios en blanco
r = c.count(str(" "))
#Este If contiene 3 condiciones, la primera dice que el usuario tiene que tener 10 caracteres y la segunda valida que eso sea así con un true, luego el true se convierte en un string para luego imprimir si es válido o no, en general  válidan o desválidan el usuario
if (len(u))<=10 and pv=="True" and r<=0:
 print("Usuario válido")
else:
  print("Usuario inválido")

#contraseña
count=0
may=0
min=0
while count < len(c):
  letra = c[count]
  if letra.isupper() == True:
    may +=1
  else:
    min +=1
  count += 1
#En esta variable, ponemos el máximo de caracteres y contamos los caracteres que contiene la contrasena
if  (len(c))>= 5 and may>=1 and min>=1:
  print("Contraseña valida")
else:
  print("Constraseña invalida")
#Se evalluan las condiciones
