#Un programa que solicite un número N y un número R y luego calcule la raíz R del número N y lo muestre en pantalla.

#En ambos se deben ingresar números, el primero es la base y el segundo a lo que se quiere elevar la raiz
primer =int(input("Ingrese un número: "))
segundo = int(input("Ingrese un número para elevar: "))

#Esto ** ayuda a calcular la raíz cuadrada de un número
raiz = primer**(1/segundo)

#Esto imprime el resultado
print("La raíz es de: ",raiz)

