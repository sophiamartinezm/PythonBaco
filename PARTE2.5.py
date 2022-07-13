#Un programa que solicite una palabra y muestre si inicia con vocal o con consonantes.


#Comenzamos pidiendo una palabra
palabra = str(input("Ingrese una palabra:"))
#Aquí vamos a buscar la inicial de la palabra
ini= palabra[0]
#Esto indica que si comienza con alguna de estas vocales pues inicia con vocal"
if ini =="a" or ini == "e" or ini == "i" or ini == "o" or ini == "u" or ini == "A" or ini == "E" or ini =="I" or ini == "O" or ini == "U":
  print("Inicia con vocal")
  #Esto indica que si comienza con alguna otra que no sea vocal pues comienza con consonante
else:
   print("Inicia con consonante")