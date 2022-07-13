#Debe solicitar el nombre completo de una persona y generar un correo electrónico con su nombre basándose en las iniciales y el apellido del mismo para mostrarlo en pantalla.

#Ejemplo: Sebastián Alejandro Juárez Cantoral = sa.juarezcantoral@baco.com

#Ingresar el nombre
nombre = str(input("Ingrese su nombre: "))
nombre1 = str(input("Ingrese su segundo nombre: "))
nombre2 = str(input("Ingrese sus apellidos: "))
b = nombre2.replace(" ","")

#cpn este len podemos ver cuantos caracteres hay en el nombre
#print(len(nombre))

#Esto muestra las primeras dos letras
a = nombre[0]+nombre1[0]
#Esto une el nombre y los apellidos al correo
print(a+"."+b+"@baco.com")

