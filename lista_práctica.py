#Tarea 1: Comprobar que todas las listas tienen el mismo largo
#Tarea 2: Sumar el primer y el ultimo numero de cada variable
#Ejemplo: 20
#Tarea 3: Sumar todos los numeros que esten en la lista que no sean el primero y el último. 
#Ejemplo: 26
#Tarea 4: Restar los resultados obtenidos de las tareas 2 y 3 
#Ejemplo: 20-26
#Tarea 5: Mostrar el resultado.
#Ejemplo: -6

f1 = [1,3,2,1,2]
f2 = [3,2,5,4,4]
f3 = [6,7,7,5,6]

a = len(f1)
b = len(f2)
c = len(f3) 
#Para acceder al ultimo, utilizamos f1[len-1]
if len(f1) == len(f2) == len(f3):
  d = f1[0]+f1[-1]
  e = f2[0]+f2[-1]
  f = f3[0]+f3[-1]
  suma = (d+e+f)
  print("Como sí tienen el mismo largo :), entonces:")
  print("1.) Suma entre 1er y último número:",suma)

#1.(f1[1]+f1[lf1-1])+(f2[1]+f2[lf2-1])+(f3[1]+f3[lf3-1])
#2.(f1[1]+f1[1])+(f2[1]+f2[1])+(f3[1]+f3[1])
  g = (sum(f1+f2+f3))
  h = (g-d-e-f)
  print("2.) Suma entre todos menos el 1er y último número:",h)

#((f1[0]+f1[3])+(f2[0]+f2[3])+(f3[0]+f3[3]))-((f1[1]+f1[2])+(f2[1]+f2[2])+(f3[1]+f3[2])))
  
  print("3.) Resta entre el 1er y 2do ejercicio:", (suma-h))
else:
  print("No tienen el mismo largo :(")
    