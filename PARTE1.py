#la listas se crearon para guardar la información adquirida con cada pregunta

lista = [] #esta es la lista de los ingredientes
acompañamientos = [] #esta es la lista de los acompañamientos
bebidas = [] #esta es la lista de las bebidas

#esto imprime la información basica del menú, como el nombre del establecimiento
print("Menú HamburCat")
#esto especifica las opciones que el usuario tiene para adquirir los ingredientes, acompañamientos o bebidas
print("Indica Si o No, si quieres los siguientes ingredientes, acompañamientos o bebidas para tu hamburguesa (su hamburguesa ya trae carne xd) : ")

#todos los siguientes ejercicios esta hechos de la misma forma, lo unico que varian son las variables y la lista a la que se agregan
print("")
#carne extra
aa = str(input("¿Desea torta de carne extra?: "))
a1 ="si"
a2 ="no"
if aa == "si":
  print("Usted agregó carne extra a su hamburguesa")
  lista.append("si carne")
else:
  print("No va a tener carne")
  lista.append("no carne")

  
print("")
#tocino
ab = str(input("¿Desea tocino?: "))
a3 ="si"
a4 ="no"
if ab == "si":
  print("Usted agregó tocino a su hamburguesa")
  lista.append("si tocino")
else:
  print("No va a tener tocino")
  lista.append("no tocino")

print("")
#lechuga
ac = str(input("¿Desea lechuga?: "))
a5 ="si"
a6 ="no"
if ac == "si":
  print("Usted agregó lechuga a su hamburguesa")
  lista.append("si lechuga")
else:
  print("No va a tener lechuga")
  lista.append("no lechuga")

print("")
#tomate
ad = str(input("¿Desea tomate?: "))
a7 ="si"
a8 ="no"
if ad == "si":
  print("Usted agregó tomate a su hamburguesa")
  lista.append("si tomate")
else:
  print("No va a tener tomate")
  lista.append("no tomate")

print("")
#cebolla
ae = str(input("¿Desea cebolla?: "))
a9 ="si"
a10 ="no"
if ae == "si":
  print("Usted agregó cebolla a su hamburguesa")
  lista.append("si cebolla")
else:
  print("No va a tener cebolla")
  lista.append("no cebolla")

print("")
#mayonesa
af = str(input("¿Desea mayonesa?: "))
a11 ="si"
a12 ="no"
if af == "si":
  print("Usted agregó mayonesa a su hamburguesa")
  lista.append("si mayonesa")
else:
  print("No va a tener mayonesa")
  lista.append("no mayonesa")

print("")
#mostaza
ag = str(input("¿Desea mostaza?: "))
a13 ="si"
a14 ="no"
if ag == "si":
  print("Usted agregó mostaza a su hamburguesa")
  lista.append("si mostaza")
else:
  print("No va a tener mostaza")
  lista.append("no mostaza")

print("")
#ketchup
ah = str(input("¿Desea ketchup?: "))
a15 ="si"
a16 ="no"
if ag == "si":
  print("Usted agregó ketchup a su hamburguesa")
  lista.append("si ketchup")
else:
  print("No va a tener ketchup")
  lista.append("no ketchup")

print("")
print("--------ACOMPAÑAMIENTOS--------")
print("")
#papas
ai = str(input("¿Desea papas?: "))
a17 ="si"
a18 ="no"
if ai == "si":
  print("Usted agregó papas a su pedido")
  acompañamientos.append("si papas")
else:
  print("No va a tener papas")
  acompañamientos.append("no papas")

print("")
#aros de cebolla
aj = str(input("¿Desea aros de cebolla?: "))
a17 ="si"
a18 ="no"
if aj == "si":
  print("Usted agregó aros de cebolla a su pedido")
  acompañamientos.append("si aros de cebolla")
else:
  print("No va a tener aros de cebolla")
  acompañamientos.append("no aros de cebolla")

print("")
print("-----------BEBIDAS-----------")
print("")
#coca
ak = str(input("¿Desea coca cola?: "))
a19 ="si"
a20 ="no"
if ak == "si":
  print("Usted agregó coca cola a su pedido")
  bebidas.append("si aros de cebolla")
else:
  print("No va a tener coca cola")
  bebidas.append("no coca cola")

print("")
#sprite
al = str(input("¿Desea sprite?: "))
a21 ="si"
a22 ="no"
if al == "si":
  print("Usted agregó sprite a su pedido")
  bebidas.append("si sprite")
else:
  print("No va a tener sprite")
  bebidas.append("no sprite")

print("")
#7up
am = str(input("¿Desea 7up?: "))
a23 ="si"
a24 ="no"
if al == "si":
  print("Usted agregó 7up a su pedido")
  bebidas.append("si 7up")
else:
  print("No va a tener 7up")
  bebidas.append("no 7up")

print("")
print("----------- GRACIAS, VUELVA PRONTO ------------")
