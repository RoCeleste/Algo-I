num_notas = 0
total = 0
mas_notas = True
while mas_notas == True:
	nota = int(input("Ingresar nota: "))
	total = total + nota
	num_notas = num_notas + 1
	salir = input("Queres ingresar mas notas? y/n: ")
	if salir == "n":
		break
print("El promedio de notas es:", total/num_notas)