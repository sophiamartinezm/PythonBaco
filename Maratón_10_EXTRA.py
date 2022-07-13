print("Numeros de mayor a menor :)")

x = int(input("Ingrese el primer numero: "))

y = int(input("Ingrese el segundo numero: "))

z = int(input("Ingrese el tercer numero: "))

a = min(x, y, z)
m = max(x, y, z)
s = (x + y + z) - a - m

print("Los numeros ordenados son: {}, {} y {} :)".format(m, s, a))

#Vi un vídeo en youtube para lograr hacerlo, sólo que en el vídeo era de menor a mayor y lo cambié para que fuera de mayor a menor. https://www.youtube.com/watch?v=w2RTWQzbDIc