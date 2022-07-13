#7 Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul. Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje “Usted ha votado por el partido [color que corresponda al candidato elegido]”. Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”.

menu = int(input('''Elige por quien votar:
1. Candidato A: Partido rojo
2. Candidato B: Partido verde
3. Candidato C: Partido azul 
'''))

if menu == 1:
  print("Usted ha votado por el partido rojo.")

if menu == 2:
  print("Usted ha votado por el partido verde")
  
if menu == 3:
  print("Usted ha votado por el partido azul")

else:
  print("Opción errónea amigo, eliga de nuevo :)")