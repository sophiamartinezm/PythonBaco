#Escribir un programa en python que solicite un texto y lo devuelva de forma invertida.

x = str(input("Ingrese el texto: "))
j = "".join(reversed(x))
print(j)