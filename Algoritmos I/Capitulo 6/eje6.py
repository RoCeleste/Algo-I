def consonantes(cad):
	nueva_cad = ""
	vocales = [" ", "A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
	for i in cad:
		if i not in vocales:
			nueva_cad += i
	return nueva_cad
def vocales(cad):
	nueva_cad = ""
	vocales = [" ","A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
	for i in cad:
		if i in vocales:
			nueva_cad += i
	return nueva_cad

def siguiente_vocal(cad):
	nueva_cad = ""
	vocales = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
	for i in cad:
		if i == "a":
			nueva_cad += "e"
		elif i == "e":
			nueva_cad += "i"
		elif i == "i":
			nueva_cad += "o"
		elif i == "o":
			nueva_cad += "u"
		elif i == "u":
			nueva_cad += "a"
		else:
			nueva_cad += i
	return nueva_cad		


def palindromo(cad):
	return cad == cad[::-1]			
