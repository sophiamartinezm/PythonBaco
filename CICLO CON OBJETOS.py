#1) Ciclo que reciba objetos y que los ponga en una lista. Debe dejar de recibir objetos cuando identifique la palabra clave "FIN". Luego imprimir la lista

objeto = str(input("Ingrese un objeto: "))
objetos = []

clave = "Fin"
while clave != objeto:
  objetos.append(objeto)
  objeto = str(input("Ingrese el objeto: "))
 

print(objetos)
  