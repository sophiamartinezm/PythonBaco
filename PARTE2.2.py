#Solicite al usuario un texto y muestre si es un palíndromo o no. Recuerde que un palíndromo funciona con o sin espacios.

#Ingresar una palabras
a = str(input("Ingrese un texto: ")) 
#Aquí se quitan los espacios que la frase puede llegar a tener
b = a.replace(" ","")
#Aquí se une y se da vuelta a la palabra
c = "".join(reversed(b))
print(c)
#Esto dice que si la frase es igual 
if b == c:
 print("Si es un palindromo :)")
else:
 print("No es un palindromo :(")