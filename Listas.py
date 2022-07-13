#Esto es una lista
alumnos5Baco=["Don Rolando","Scar", "Trejo", "Yusepe", "Triz","Sami", "Polanco", "Margarita", "Santi"]

print("Esta lista es" ,alumnos5Baco)
print("La lista tiene ",len(alumnos5Baco)," elementos")

#para acceder a un elemento podemos usar un index [ ]
print(alumnos5Baco[0])
#podemos acceder con un rango, donde incluye el primero pero no el ultimo
print(alumnos5Baco[2:7])

#Cambiar un elemento
alumnos5Baco[0]="Graviel"
print(alumnos5Baco)

#Agregar un elemento
alumnos5Baco.append("Javier")
print(alumnos5Baco)

#Quitar un elemento por su contenido
alumnos5Baco.remove("Triz")
print(alumnos5Baco)

#Quitar un elemento por su index
alumnos5Baco.pop(1)
print(alumnos5Baco)

#Ordenar lista
alumnos5Baco.sort()
print(alumnos5Baco)