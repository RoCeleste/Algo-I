def numero_con_sep(num):
	num = str(num)
	nuevo_num = ""
	cont = 0
	for i in num[::-1]:
		if cont == 3:
			cont = 1
			nuevo_num += "."
			nuevo_num += i
		else:
			nuevo_num += i
			cont += 1
	return nuevo_num[::-1]
print(numero_con_sep(12678))