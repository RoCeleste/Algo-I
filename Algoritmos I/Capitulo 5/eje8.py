suma=0
promedio=0
total_ingresados=0

numero = int(input("Ingresar Numero: "))
while numero != -1:
	suma += numero
	total_ingresados += 1
	numero = int(input("Ingresar Numero: "))
print(suma,"|", suma/total_ingresados,"|", total_ingresados)