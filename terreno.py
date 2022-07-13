#Escribir un programa que solicite largo y ancho de un terreno y muestre los metros cuadrados del mismo. Es importante que al terminar de solicitar la primera información lo haga de forma infinita hasta que el usuario escriba "FIN"
#El objetivo de este programa es que reutilicen la función del ejercicio anterior. while y def.

def terreno():
  alto = int(input("Ingrese el alto del terreno: "))
  ancho = int(input("Ingrese el ancho del terreno: "))
  res = alto * ancho
  print("El terreno tiene", res, "metros cuadrados")
terreno()

x = str(input("¿Desea continuar? "))

while x == "si":
  terreno()
  x = str(input("¿Desea continuar (＾ｕ＾)?"))

else:
  print("Adiós ¯\_(ツ)_/¯")