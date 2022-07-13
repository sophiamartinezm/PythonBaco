#Escribir un programa en python que solicite un texto y devuelva el mismo texto sin espacios y todo en minúsculas.

v = str(input("Ingrese un texto en mayuscula: ")) 
x = v.replace(' ', '')
print(x.lower())


