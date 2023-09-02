dic = {}
nombre = input("Ingresa un nombre(* para terminar): ")
while nombre != "*":
	if nombre in dic:
		print(f"{nombre} : {dic[nombre]}")
		cambiar = input("Queres cambiar el numero?(y/n): ")
		if cambiar == "y":
			dic[nombre] = int(input("Nuevo numero: "))
	else:
		dic[nombre] = int(input("Ingresa el numero: "))
	nombre = input("Ingresa otro nombre: ")
print(dic)	
	