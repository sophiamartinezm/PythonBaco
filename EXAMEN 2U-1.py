#2) Un programa en Python que reciba la altura y el radio de un cilindro y devuelva el volumen del mismo. 

print("VOLUMEN DEL CILINDRO")
altura = int(input("Ingrese la altura del cilindro: ")) #aquí se pide la altura
radio = int(input("Ingrese el radio del cilindro: ")) #aquí se pide el radio
pi = 3.14 #determinamos pi
ra = radio * radio #aquí determinamos es el radio al cuadrado
vol = ((pi * ra) * altura) #aquí multiplicamos todo, adjuntando la altura
print("El cilindro tiene un volumen de: ", vol) #y esto adjunta el resultado a un print

print("Adiós ¯\_(ツ)_/¯")