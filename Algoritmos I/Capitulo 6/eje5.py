def siglas(cad):
	palabras = cad.split(" ")
	nueva_cad = ""
	for i in palabras:
		nueva_cad += i[0].upper()
	return nueva_cad

def mayuscula(cad):
	nueva_cad = ""
	palabras = cad.split(" ")
	for i in palabras:
		nueva_cad += i.capitalize()
		nueva_cad += " "
	return nueva_cad[:-1]

def palabras_con_a(cad):
	nueva_cad = ""
	palabras = cad.split(" ")
	for i in palabras:
		if i[0] == "a" or i[0] == "A":
			nueva_cad += i
	return nueva_cad		
