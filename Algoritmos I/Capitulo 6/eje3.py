def intercalar(cad, c, l):
	nueva_cad = ""
	for i in cad:
		nueva_cad += i + c
	return nueva_cad[:-1]

def reemplazar(cad, c, l):
	nueva_cad = ""
	for i in cad:
		if i == " ":
			nueva_cad += c
		else:
			nueva_cad += i
	return nueva_cad

def reemplazar_dig(cad, c, l):
	nueva_cad = ""
	for i in cad:
		if i.isdigit() == True:
			nueva_cad += c
		else:
			nueva_cad += i
	return nueva_cad

def insertar_cada_3(cad, c, l):
	nueva_cad = ""
	cont = 0
	for i in cad:
		if cont == 3:
			cont = 1
			nueva_cad += c
			nueva_cad += i
			
		else:
			nueva_cad += i
			cont += 1
	return nueva_cad

