print("Productos La Torre")


print("Ingrese el producto")
var = str(input())

print("Ingrese la cantidad")
c1 = int(input())

print("Ingrese el precio unitario")
p = int(input())

if (c1 >= 5):
  print("OBTUVO UN DESCUENTO DEL 25%")

  print("Precio total sin descuento")
  ds = c1*p
  print(ds)

  print("Precio total con descuento")
  d = (100-25)
  d1 = (ds*d/100)
  print(d1)

  print("Se descuenta y se ahorra")
  tp = (25*ds/100)
  print(tp)
else:
  print("Vuelva pronto")
