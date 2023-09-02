import fact
cant_valores = int(input("Cuantos valores queres ingresar?: "))

for x in range(1, cant_valores + 1):
	num = int(input("Ingresa numero: "))
	print(num, "-", fact.factorial(num))