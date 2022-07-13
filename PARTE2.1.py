#Deberá de solicitar al usuario 10 números enteros. Debe mostrar la suma entre el primer y el último número de la lista y debe mostrar el resultado de la suma del segundo al noveno número de la lista.

#Se piden 10 número al usuario
a1=int(input("ingrese primer numero: "))
a2=int(input("ingrese segundo numero: "))
a3=int(input("ingrese tercer numero: "))
a4=int(input("ingrese cuarto numero: "))
a5=int(input("ingrese quinto numero: "))
a6=int(input("ingrese sexto numero: "))
a7=int(input("ingrese septimo numero: "))
a8=int(input("ingrese octavo numero: "))
a9=int(input("ingrese noveno numero: "))
a10=int(input("ingrese decimo numero: "))

#suma entre el primer y último númeroo
res=a1+a10
print("La suma del primer y último número es de: ",res)
#suma entre todos menos el primero y segundo
res=a2+a3+a4+a5+a6+a7+a8+a9
print("La suma de todos menos el primero y el segundo es de: ",res)


